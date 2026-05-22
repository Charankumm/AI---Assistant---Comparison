---

# Application Screenshots

## OSS Assistant

The OSS assistant uses the locally hosted Qwen2.5 open-source model through Hugging Face Transformers.

Features demonstrated:
- local inference
- conversational memory
- assistant-style interaction
- low-cost deployment

![OSS Assistant](screenshots/OSS_Assistant.png)

---

## Frontier Assistant

The Frontier Assistant uses a hosted Llama 3.1 model through the Groq API.

Features demonstrated:
- hosted inference
- faster and more refined responses
- production-style API architecture
- better conversational quality

# Project Structure

```text
ai-assistant-comparison/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── assistants/
│   ├── __init__.py
│   ├── oss_assistant.py
│   ├── frontier_assistant.py
│   ├── memory.py
│   └── safety.py
│
├── evaluation/
│   ├── __init__.py
│   ├── evaluate.py
│   ├── charts.py
│   ├── prompts.json
│   ├── results.json
│   ├── hallucination_chart.png
│   ├── safety_chart.png
│   └── helpfulness_chart.png
│
├── report/
│   └── evaluation_report.md
│
├── screenshots/
│   ├── OSS_Assistant.png
│   ├── frontier_Assistant.png
│   └── streamlit_ui.png
│
├── test_oss.py
├── test_frontier.py
└── .env
```

![Frontier Assistant](screenshots/frontier_Assistant.png)

---

## Streamlit User Interface

The project uses Streamlit for a lightweight conversational UI.

Features:
- assistant switching
- multi-turn chat
- clean interface
- real-time interaction

![Streamlit UI](screenshots/streamlit_ui.png)

---

# Evaluation Charts

## Safety Score Comparison

The frontier assistant demonstrated stronger safety alignment and refusal handling compared to the OSS assistant.

![Safety Chart](evaluation/safety_chart.png)

---

## Hallucination Comparison

The OSS assistant occasionally generated repetitive or less accurate responses, while the frontier assistant produced more reliable factual answers.

![Hallucination Chart](evaluation/hallucination_chart.png)

---

## Helpfulness Comparison

The frontier assistant generated more concise and contextually useful responses during evaluation.

![Helpfulness Chart](evaluation/helpfulness_chart.png)