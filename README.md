# 🤖 Telegram GPT-4 Bot for Persona, Audience & Competitor Analysis

**AI Developer & Prompt Engineer**  
I built this Telegram bot to help users explore their personal brand, target audience, or competitors — step by step.  
It uses **GPT-4** to generate structured, warm, and strategic text directly in the chat.

The bot works with custom prompts, asks questions, supports link parsing (Instagram, YouTube), and limits access to authorized users only.

---

## 🚀 What It Can Do

- 🧠 Asks tailored questions based on selected topic
- 💬 Works as a dialog – block by block
- 🔐 Access limited to approved Telegram users (ALLOWED_USERS)
- 🤖 Uses OpenAI (GPT-4) for full text generation
- 🔗 Can read and extract info from links (Instagram, YouTube)
- 🌐 Works with VPN (for non-accessible links)

---

## 🧰 Technologies Used

- `Python 3.11+`
- `python-telegram-bot`
- `OpenAI GPT-4 API`
- `BeautifulSoup4` + `requests`
- `Regex`, `JSON`, `asyncio`

---

## 📂 Project Structure
📁 telegram-ai-bot/
├── bot.py # Main bot logic
├── gpt_api.py # GPT response logic
├── user_state.py # Manages questions & answers
├── link_parser.py # Parses and extracts metadata from links
├── prompts/
│ ├── unpacking.txt # Prompt for persona
│ ├── audience.txt # Prompt for audience
│ └── competitors.txt # Prompt for competitors
├── config.json.example # Template config file
├── test_openai_key.py # For testing OpenAI key
└── *.png # Screenshots for README

---

## ⚙️ Configuration

Create a `config.json` file like this:

```json
{
  "TELEGRAM_TOKEN": "your-bot-token",
  "ALLOWED_USERS": [12345678],
  "openai_api_key": "your-gpt4-api-key"
}

---

##  💡 Prompt Style Example
GPT prompt uses this system message:

---

You are a strategist and coach. Your job is to write a structured, helpful, 12-block analysis.
Each block must be clear, readable, and separated with two line breaks (\n\n).
Write like a warm coach from 2025 – with examples, ideas, and practical insights.

| Start Menu                                                                                               | Question Flow                                                                                            | Access Control                                                                                           |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| <img src="https://github.com/user-attachments/assets/2063f521-f594-4a15-a9f9-11b3a4243a71" width="300"/> | <img src="https://github.com/user-attachments/assets/312a269c-959b-453f-a7ee-cc51ded1fdf1" width="300"/> | <img src="https://github.com/user-attachments/assets/536a5d4b-f8f7-4c3f-9efd-a6be76e9a0e2" width="300"/> |

---

##  ▶️ How to Run
Clone the repo

Install packages:

pip install -r requirements.txt
Add your credentials to config.json

Run the bot:
python bot.py

---

##  📜 License
MIT License

---

##  🧑‍💻 Author
KalinNika
AI Developer & Prompt Engineer
Focused on building useful AI tools with GPT, automation, and smart prompts.
