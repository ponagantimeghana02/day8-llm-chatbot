from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("LLM_API_KEY")

if not API_KEY:
    print("Error: API key not found in .env")
    exit()

client = Groq(api_key=API_KEY)


conversation_history = [
    {
        "role": "system",
        "content": "You are a helpful AI assistant."
    }
]

print("=" * 60)
print("MEMORY CHATBOT")
print("Commands:")
print("  exit  -> Quit chatbot")
print("  reset -> Clear conversation history")
print("=" * 60)

while True:

    try:
        user_input = input("\nYou: ")

        if user_input.lower() == "exit":
            print("\nAI: Goodbye!")
            break

        if user_input.lower() == "reset":
            conversation_history = [
                {
                    "role": "system",
                    "content": "You are a helpful AI assistant."
                }
            ]

            print("\nAI: Conversation history cleared.")
            continue

        conversation_history.append(
            {
                "role": "user",
                "content": user_input
            }
        )

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=conversation_history
        )

        ai_response = response.choices[0].message.content

        conversation_history.append(
            {
                "role": "assistant",
                "content": ai_response
            }
        )

        print("\nAI:")
        print(ai_response)

    except KeyboardInterrupt:
        print("\n\nAI: Chat ended.")
        break

    except Exception as e:
        print(f"\nError: {e}")