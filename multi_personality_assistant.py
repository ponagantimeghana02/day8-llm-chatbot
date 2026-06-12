from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("LLM_API_KEY")

if not API_KEY:
    print("Error: API key not found in .env file")
    exit()

client = Groq(api_key=API_KEY)

MODES = {
    "1": {
        "name": "Teacher Mode",
        "prompt": """
You are an expert teacher.
Explain concepts in a beginner-friendly manner.
Provide step-by-step explanations.
Include examples whenever possible.
"""
    },

    "2": {
        "name": "Software Engineer Mode",
        "prompt": """
You are a senior software engineer.
Provide technical explanations.
Suggest best practices.
Review code and recommend improvements.
Focus on correctness and performance.
"""
    },

    "3": {
        "name": "HR Manager Mode",
        "prompt": """
You are an experienced HR Manager.
Help with resumes, interviews, career guidance,
professional communication, and workplace advice.
Maintain a professional tone.
"""
    },

    "4": {
        "name": "Business Analyst Mode",
        "prompt": """
You are a Senior Business Analyst.
Analyze business ideas.
Provide requirements, user stories,
features, risks, and recommendations.
Use a structured format.
"""
    },

    "5": {
        "name": "Translator Mode",
        "prompt": """
You are a professional translator.
Translate text accurately.
Preserve meaning, context, and tone.
Keep names and proper nouns unchanged unless requested.
"""
    }
}

print("=" * 60)
print("MULTI-PERSONALITY AI ASSISTANT")
print("=" * 60)

while True:

    print("\nAvailable Modes:")
    print("1. Teacher Mode")
    print("2. Software Engineer Mode")
    print("3. HR Manager Mode")
    print("4. Business Analyst Mode")
    print("5. Translator Mode")
    print("0. Exit")

    mode = input("\nSelect Mode: ")

    if mode == "0":
        print("\nGoodbye!")
        break

    if mode not in MODES:
        print("\nInvalid choice. Try again.")
        continue

    selected_mode = MODES[mode]

    print(f"\n{selected_mode['name']} Activated")
    print("Type 'back' to return to mode selection.")

    while True:

        user_input = input("\nYou: ")

        if user_input.lower() == "back":
            break

        try:

            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "system",
                        "content": selected_mode["prompt"]
                    },
                    {
                        "role": "user",
                        "content": user_input
                    }
                ],
                temperature=0.7
            )

            print("\nAI:")
            print(response.choices[0].message.content)

        except Exception as e:

            error_message = str(e).lower()

            if "401" in error_message:
                print("\nError: Invalid API Key")

            elif "429" in error_message:
                print("\nError: Rate Limit Exceeded")

            elif "timeout" in error_message:
                print("\nError: Request Timed Out")

            else:
                print(f"\nError: {e}") 