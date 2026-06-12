from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("LLM_API_KEY")

if not API_KEY:
    print("Error: API key not found in .env file")
    exit()

client = Groq(api_key=API_KEY)

SYSTEM_PROMPT = """
You are a Professional Technical Support Assistant.

Responsibilities:
- Help users troubleshoot technical issues.
- Explain solutions clearly and professionally.
- Provide step-by-step instructions.
- Use simple language when possible.
- Be polite and concise.
- If information is unknown, say so honestly.

Response Style:
- Professional
- Helpful
- Structured
- Easy to understand
"""

print("=" * 60)
print("TECHNICAL SUPPORT ASSISTANT")
print("Type 'exit' to quit.")
print("=" * 60)

while True:

    try:
        user_query = input("\nUser: ")

        if user_query.lower() == "exit":
            print("\nAssistant: Thank you for using Technical Support Assistant.")
            break

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": user_query
                }
            ]
        )

        print("\nAssistant:")
        print(response.choices[0].message.content)

    except KeyboardInterrupt:
        print("\n\nAssistant: Session terminated.")
        break

    except Exception as e:

        error_message = str(e).lower()

        if "401" in error_message:
            print("\nError: Invalid API Key")

        elif "429" in error_message:
            print("\nError: API Rate Limit Exceeded")

        elif "timeout" in error_message:
            print("\nError: Request Timed Out")

        else:
            print(f"\nUnexpected Error: {e}")