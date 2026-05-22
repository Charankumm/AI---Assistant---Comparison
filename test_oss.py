from assistants.oss_assistant import OSSAssistant

assistant = OSSAssistant()

messages = [
    {
        "role": "user",
        "content": "Hello, who are you?"
    }
]

response = assistant.generate_response(messages)

print(response)