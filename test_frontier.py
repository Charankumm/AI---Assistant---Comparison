from assistants.frontier_assistant import FrontierAssistant

assistant = FrontierAssistant()

messages = [
    {
        "role": "user",
        "content": "Hello, who are you?"
    }
]

response = assistant.generate_response(messages)

print(response)