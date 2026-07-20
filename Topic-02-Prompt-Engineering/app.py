from config import client, MODEL
from prompts import (
    ZERO_SHOT_PROMPT,
    ONE_SHOT_PROMPT,
    FEW_SHOT_PROMPT,
    PYTHON_TEACHER_PROMPT,
    HR_PROMPT,
    SHOPPING_PROMPT,
    JSON_PROMPT
)


print("=" * 50)
print("      AI Prompt Playground")
print("=" * 50)

print("1. Zero-Shot Prompt")
print("2. One-Shot Prompt")
print("3. Few-Shot Prompt")
print("4. Python Teacher")
print("5. HR Interviewer")
print("6. Shopping Assistant")
print("7. JSON Output")

choice = input("\nEnter your choice (1-7): ")

question = input("Enter your question: ")
# Select Prompt

if choice == "1":
    prompt = ZERO_SHOT_PROMPT.format(question)

elif choice == "2":
    prompt = ONE_SHOT_PROMPT.format(question)

elif choice == "3":
    prompt = FEW_SHOT_PROMPT.format(question)

elif choice == "4":
    prompt = PYTHON_TEACHER_PROMPT.format(question)

elif choice == "5":
    prompt = HR_PROMPT.format(question)

elif choice == "6":
    prompt = SHOPPING_PROMPT.format(question)

elif choice == "7":
    prompt = JSON_PROMPT.format(question)

else:
    print("Invalid Choice")
    exit()
response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

print("\nAI Response:\n")
print(response.choices[0].message.content)