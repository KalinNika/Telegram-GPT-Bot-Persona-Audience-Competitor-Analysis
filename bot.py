from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application, CommandHandler, MessageHandler,
    filters, ConversationHandler, ContextTypes
)
import json
from user_state import get_questions, save_answer, get_full_prompt
from gpt_api import generate_response
from link_parser import parse_links_in_text  # ✅ добавлено

with open("config.json") as f:
    config = json.load(f)

ALLOWED_USERS = config["ALLOWED_USERS"]
SELECT, QUESTION, NEXT = range(3)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id not in ALLOWED_USERS:
        await update.message.reply_text("🚫 Доступ разрешён только подписчикам клуба.")
        return ConversationHandler.END

    await update.message.reply_text(
        "👋 Привет! Я помогу тебе распаковать личность, проанализировать ЦА или конкурентов.\n\n"
        "Выбери, с чего начнём 👇",
        reply_markup=ReplyKeyboardMarkup(
            [["Распаковка личности", "Анализ ЦА", "Анализ конкурентов"]],
            resize_keyboard=True,
            one_time_keyboard=True
        )
    )
    return SELECT

async def reset(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔁 Всё очищено. Давай начнём заново. Напиши /start")
    return ConversationHandler.END

async def select_mode(update: Update, context: ContextTypes.DEFAULT_TYPE):
    choice = update.message.text.lower()
    if "личност" in choice:
        mode = 'unpacking'
    elif "ц" in choice:
        mode = 'audience'
    elif "конкурент" in choice:
        mode = 'competitors'
    else:
        await update.message.reply_text("Пожалуйста, выбери один из вариантов.")
        return SELECT

    context.user_data['mode'] = mode
    context.user_data['answers'] = []
    context.user_data['q_index'] = 0
    context.user_data['block_index'] = 0

    questions = get_questions(mode)
    await update.message.reply_text(f"📝 Отлично, начнём!\n{questions[0]}")
    return QUESTION

async def handle_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    answer = update.message.text
    save_answer(context.user_data, answer)

    questions = get_questions(context.user_data['mode'])
    q_index = context.user_data['q_index']

    if q_index < len(questions):
        await update.message.reply_text(questions[q_index])
        return QUESTION
    else:
        await update.message.reply_text("✨ Спасибо за ответы! Генерирую персональный анализ… 🧠")
        prompt = get_full_prompt(context.user_data)

        # ✅ Добавим ссылки в конец промпта, если они есть
        link_meta = parse_links_in_text("\n".join(context.user_data['answers']))
        if link_meta:
            prompt += f"\n\nДополнительно по ссылкам:\n{link_meta}"

        try:
            gpt_result = generate_response(prompt)
            if not gpt_result:
                await update.message.reply_text("⚠️ Ошибка: GPT не вернул текст.")
                return ConversationHandler.END

            if isinstance(gpt_result, list):
                blocks = gpt_result
            else:
                blocks = gpt_result.split("\n\n")

            context.user_data["gpt_blocks"] = blocks
            context.user_data["block_index"] = 0

            await update.message.reply_text("✅ GPT ответ получен. Отправляю первый блок 👇")
            await update.message.reply_text(blocks[0])
            return NEXT

        except Exception as e:
            await update.message.reply_text(f"❌ Произошла ошибка при генерации: {e}")
            return ConversationHandler.END

async def next_block(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["block_index"] += 1
    blocks = context.user_data["gpt_blocks"]
    i = context.user_data["block_index"]

    if i < len(blocks):
        await update.message.reply_text(blocks[i])
        return NEXT
    else:
        await update.message.reply_text("✅ Всё готово! Хочешь пройти другой анализ — напиши /start")
        return ConversationHandler.END

def main():
    app = Application.builder().token(config["TELEGRAM_TOKEN"]).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            SELECT: [MessageHandler(filters.TEXT & ~filters.COMMAND, select_mode)],
            QUESTION: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_answer)],
            NEXT: [MessageHandler(filters.TEXT & ~filters.COMMAND, next_block)],
        },
        fallbacks=[
            CommandHandler("reset", reset),
            CommandHandler("start", start),
        ],
        allow_reentry=True
    )

    app.add_handler(conv_handler)
    app.run_polling()

if __name__ == "__main__":
    main()
