# 🤖 Telegram GPT Bot for Persona, Audience & Competitor Analysis

A GPT-powered Telegram bot that guides users through strategic self-discovery, audience profiling, and competitor research.

> **Built by KalinNika** — AI Developer & Prompt Engineer. Developed a full Telegram bot with integrated GPT-4 flow and warm, coach-style prompts. Clean UX, structured logic, and answer generation in a mini-book format.

---

## 📁 Project Structure

* `bot.py` – main Telegram bot logic
* `gpt_api.py` – sends structured prompt to GPT and returns response
* `user_state.py` – manages question flow, answers, prompt assembly
* `link_parser.py` – parses metadata from Instagram/YouTube links
* `prompts/`

  * `unpacking.txt` – for personal analysis
  * `audience.txt` – for audience research
  * `competitors.txt` – for competitive analysis
* `config.json.example` – example configuration with allowed users
* `test_openai_key.py` – test your OpenAI key availability
* `*.png` – screenshots for demo (in `/prompts` folder)

---

## ⚙️ Configuration

Create a `config.json` file like this:

```json
{
  "TELEGRAM_TOKEN": "your-bot-token",
  "ALLOWED_USERS": [123456789],
  "openai_api_key": "your-openai-api-key"
}
```

---

## 🧠 Prompt Style

GPT uses this system message to generate answers:

> You are a strategist and coach. Your job is to write a structured, helpful, 12-block analysis.
> Each block must be clean, readable, and separated with two line breaks (`\n\n`).
> Write like a warm coach from 2025 — with examples, lists, and practical ideas.

---

## ▶️ How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Add your credentials in `config.json`

Start the bot:

```bash
python bot.py
```

---

## 📸 Screenshots

| Start Menu                                                                                               | Question Flow                                                                                            | Access Control                                                                                           |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| <img src="https://github.com/user-attachments/assets/2063f521-f594-4a15-a9f9-11b3a4243a71" width="250"/> | <img src="https://github.com/user-attachments/assets/312a269c-959b-453f-a7ee-cc51ded1fdf1" width="250"/> | <img src="https://github.com/user-attachments/assets/536a5d4b-f8f7-4c3f-9efd-a6be76e9a0e2" width="250"/> |

---

## 📄 License

[MIT License](LICENSE)

---

## 🧑‍💻 Author

**KalinNika**
AI Developer & Prompt Engineer
[https://github.com/KalinNika](https://github.com/KalinNika)

Focused on building useful AI tools with GPT, automation, and smart prompts.
