from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("LLM_API_KEY")

if not api_key:
    print("API key not found!")
    exit()

client = Groq(api_key=api_key)

PROMPT = "Explain Machine Learning in simple terms."

experiments = [
    {
        "name": "Low Temperature",
        "temperature": 0.2,
        "max_tokens": 100,
        "system": "You are a professional AI tutor."
    },
    {
        "name": "Medium Temperature",
        "temperature": 0.7,
        "max_tokens": 100,
        "system": "You are a professional AI tutor."
    },
    {
        "name": "High Temperature",
        "temperature": 1.2,
        "max_tokens": 100,
        "system": "You are a professional AI tutor."
    },
    {
        "name": "Long Response",
        "temperature": 0.7,
        "max_tokens": 300,
        "system": "You are a professional AI tutor."
    },
    {
        "name": "Friendly Assistant",
        "temperature": 0.7,
        "max_tokens": 150,
        "system": "You are a friendly teacher who explains concepts with examples."
    }
]

for exp in experiments:

    print("\n" + "=" * 70)
    print("Experiment:", exp["name"])
    print("=" * 70)

    try:

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            temperature=exp["temperature"],
            max_tokens=exp["max_tokens"],
            messages=[
                {
                    "role": "system",
                    "content": exp["system"]
                },
                {
                    "role": "user",
                    "content": PROMPT
                }
            ]
        )

        print(response.choices[0].message.content)

    except Exception as e:
        print("Error:", e)