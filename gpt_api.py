import json
from openai import OpenAI

# Загружаем API-ключ
with open('config.json', encoding='utf-8') as f:
    config = json.load(f)

client = OpenAI(api_key=config["openai_api_key"])

def generate_response(prompt):
    try:
        print("📤 Запрос в GPT-4o с температурой 0.9, стиль: коуч")
        response = client.chat.completions.create(
            model="gpt-4o",  # 🔁 Можешь сменить на "gpt-4-1106-preview" или "gpt-4"
            messages=[
                {
                    "role": "system",
                    "content": "Ты — стратег и коуч. Твоя задача: написать подробный, структурированный анализ в 12 логических блоках. "
                               "Каждый блок должен быть отделён двойным переносом строки (\\n\\n), без вступлений и заключений. "
                               "Пиши как для Telegram-чата: тёплым тоном, с примерами, списками и блоками, как коуч-друг в 2025 году."
                },
                {"role": "user", "content": prompt}
            ],
            temperature=0.9,
            max_tokens=3000
        )

        content = response.choices[0].message.content.strip()

        if not content:
            return None  # Явная проверка

        return content

    except Exception as e:
        print(f"❌ Ошибка GPT: {e}")
        return None
