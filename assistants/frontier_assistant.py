from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

SYSTEM_PROMPT = """
You are a helpful AI assistant.
Be concise, friendly, and conversational.
Refuse harmful requests politely.
"""


class FrontierAssistant:

    def generate_response(self, messages):

        formatted_messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            }
        ]

        formatted_messages.extend(messages)

        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=formatted_messages,
            temperature=0.5,
            max_tokens=80
        )

        return completion.choices[0].message.content