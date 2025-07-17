from openai import OpenAI
import json

with open("config.json", encoding="utf-8") as f:
    key = json.load(f)["openai_api_key"]

client = OpenAI(api_key=key)

models = client.models.list()
print("✅ API работает. Доступные модели:")
print([m.id for m in models.data])
