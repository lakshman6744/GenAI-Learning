from config import client, MODEL
from chat_history import messages

print("=" * 50)
print("     WELCOME TO AI CHATBOT.")
print("=" * 50)
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages
    )

    assistant_reply = response.choices[0].message.content

    print("AI:", assistant_reply)

    messages.append(
        {
            "role": "assistant",
            "content": assistant_reply
        }
    )