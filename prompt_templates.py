# ============================================
# Prompt Templates for Different Use Cases
# ============================================

class PromptTemplates:

    # ----------------------------------------
    # AI Teacher Template
    # ----------------------------------------
    @staticmethod
    def ai_teacher(topic):
        return f"""
You are an expert AI Teacher.

Task:
Explain the following topic in a beginner-friendly way.

Topic:
{topic}

Instructions:
1. Use simple language.
2. Assume the learner is a beginner.
3. Explain step-by-step.
4. Include real-world examples.
5. Provide sample code if applicable.
6. Summarize key points at the end.

Output Format:
- Introduction
- Step-by-Step Explanation
- Example
- Key Takeaways
"""

    # ----------------------------------------
    # Code Reviewer Template
    # ----------------------------------------
    @staticmethod
    def code_reviewer(code):
        return f"""
You are an experienced Python Code Reviewer.

Review the following code:

{code}

Analyze:

1. Bugs
   - Identify logical or syntax errors.

2. Performance Issues
   - Suggest optimizations.

3. Security Issues
   - Highlight vulnerabilities.

4. Code Quality
   - Readability
   - Maintainability

5. Suggestions
   - Best practices
   - Improvements

Output Format:

## Bugs
## Performance Issues
## Security Issues
## Suggestions
"""

    # ----------------------------------------
    # Business Analyst Template
    # ----------------------------------------
    @staticmethod
    def business_analyst(product_idea):
        return f"""
You are a Senior Business Analyst.

Product Idea:
{product_idea}

Analyze the idea and provide:

1. Requirements
2. User Stories
3. Key Features
4. Risks and Challenges
5. Recommendations

Output Format:

## Requirements

## User Stories

## Features

## Risks

## Recommendations
"""

    # ----------------------------------------
    # Translator Template
    # ----------------------------------------
    @staticmethod
    def translator(sentence, target_language):
        return f"""
You are a professional translator.

Translate the following sentence into {target_language}.

Sentence:
"{sentence}"

Instructions:
1. Preserve the original meaning.
2. Preserve tone and intent.
3. Use natural language.
4. Avoid literal word-for-word translation.
5. Keep names and proper nouns unchanged.

Output Format:

Translated Text:
"""
        

# ============================================
# Example Usage
# ============================================

if __name__ == "__main__":

    print("=" * 60)
    print("AI TEACHER TEMPLATE")
    print("=" * 60)

    print(
        PromptTemplates.ai_teacher(
            "Explain Python decorators."
        )
    )

    print("\n" + "=" * 60)
    print("CODE REVIEWER TEMPLATE")
    print("=" * 60)

    sample_code = """
password = "admin123"
print(password)
"""

    print(
        PromptTemplates.code_reviewer(
            sample_code
        )
    )

    print("\n" + "=" * 60)
    print("BUSINESS ANALYST TEMPLATE")
    print("=" * 60)

    print(
        PromptTemplates.business_analyst(
            "AI-powered Resume Screening Platform"
        )
    )

    print("\n" + "=" * 60)
    print("TRANSLATOR TEMPLATE")
    print("=" * 60)

    print(
        PromptTemplates.translator(
            "Artificial Intelligence is transforming the world.",
            "French"
        )
    )