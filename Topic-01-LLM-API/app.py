import os
from dotenv import load_dotenv
from groq import Groq

# Load .env
load_dotenv()

# Read API key
api_key = os.getenv("GROQ_API_KEY")

# Create client
client = Groq(api_key=api_key)

# Ask the user for input
question = input("Ask AI: ")

# Send request
response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": question
        }
    ]
)

# Print response
print("\nAI Response:\n")
print(response.choices[0].message.content)