from transformers import pipeline

SYSTEM_PROMPT = """
You are a helpful AI assistant.
Be concise, friendly, and conversational.
Avoid repetition.
Refuse harmful requests politely.
"""


class OSSAssistant:

    def __init__(self):

        self.pipe = pipeline(
            "text-generation",
            model="Qwen/Qwen2.5-0.5B-Instruct"
        )

    def generate_response(self, messages):

        prompt = SYSTEM_PROMPT + "\n\n"

        for msg in messages:
            role = msg["role"]
            content = msg["content"]

            prompt += f"{role}: {content}\n"

        prompt += "assistant: "

        output = self.pipe(
            prompt,
            max_new_tokens=40,
            temperature=0.4,
            do_sample=True,
            repetition_penalty=1.3,
            truncation=True
        )

        generated_text = output[0]["generated_text"]

        response = generated_text[len(prompt):]

        response = response.split("user:")[0]
        response = response.split("assistant:")[0]

        return response.strip()