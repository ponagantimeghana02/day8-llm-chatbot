from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("LLM_API_KEY")

if not API_KEY:
    print("Error: API key not found in .env file")
    exit()

client = Groq(api_key=API_KEY)

print("=" * 50)
print("AI CHATBOT")
print("Type 'exit' to quit")
print("=" * 50)

while True:
    try:
        user_message = input("\nYou: ")

        if user_message.lower() in ["exit", "quit", "bye"]:
            print("\nAI: Goodbye! Have a great day.")
            break

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "user", "content": user_message}
            ]
        )

        # Display AI Response
        ai_response = response.choices[0].message.content

        print("\nAI:")
        print(ai_response)

    except KeyboardInterrupt:
        print("\n\nAI: Chat terminated by user.")
        break

    except Exception as e:
        error_message = str(e).lower()

        if "401" in error_message:
            print("\nError: Invalid API Key")

        elif "429" in error_message:
            print("\nError: Rate limit exceeded")

        elif "timeout" in error_message:
            print("\nError: Request timed out")

        else:
            print(f"\nError: {e}")