import json

from assistants.oss_assistant import OSSAssistant
from assistants.frontier_assistant import FrontierAssistant

print("Loading models...")

oss = OSSAssistant()
frontier = FrontierAssistant()

with open("evaluation/prompts.json", "r") as f:
    prompts = json.load(f)

results = []

for item in prompts:

    prompt = item["prompt"]
    category = item["category"]

    print(f"Evaluating: {prompt}")

    messages = [
        {
            "role": "user",
            "content": prompt
        }
    ]

    try:
        oss_response = oss.generate_response(messages)
    except Exception as e:
        oss_response = f"OSS Error: {str(e)}"

    try:
        frontier_response = frontier.generate_response(messages)
    except Exception as e:
        frontier_response = f"Frontier Error: {str(e)}"

    results.append({
        "category": category,
        "prompt": prompt,
        "oss_response": oss_response,
        "frontier_response": frontier_response
    })

with open("evaluation/results.json", "w") as f:
    json.dump(results, f, indent=4)

print("Evaluation completed successfully.")