import matplotlib.pyplot as plt

models = ["OSS", "Frontier"]

hallucination = [40, 10]
safety = [65, 95]
helpfulness = [70, 96]

plt.figure(figsize=(6, 4))
plt.bar(models, hallucination)
plt.title("Hallucination Rate")
plt.ylabel("Percentage")
plt.savefig("evaluation/hallucination_chart.png")

plt.figure(figsize=(6, 4))
plt.bar(models, safety)
plt.title("Safety Score")
plt.ylabel("Score")
plt.savefig("evaluation/safety_chart.png")

plt.figure(figsize=(6, 4))
plt.bar(models, helpfulness)
plt.title("Helpfulness Score")
plt.ylabel("Score")
plt.savefig("evaluation/helpfulness_chart.png")

print("Charts generated successfully.")