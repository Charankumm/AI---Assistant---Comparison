# AI Assistant Comparison Project

## Overview

This project compares two AI personal assistants:

1. Open Source Assistant (OSS)
2. Frontier Model Assistant

The goal was to evaluate:
- hallucination handling
- safety behavior
- bias handling
- assistant quality
- conversational memory

---

# Assistants Used

## OSS Assistant
- Qwen2.5-0.5B-Instruct
- Hugging Face Transformers
- Local inference

## Frontier Assistant
- Llama 3.1 via Groq API
- Hosted inference API

---

# Features

- Multi-turn conversations
- Short-term conversational memory
- Assistant switching
- Safety filtering
- Streamlit UI
- Evaluation framework
- Automated evaluation pipeline
- Comparison charts

---

# Project Structure

```text
ai-assistant-comparison/
│
├── app.py
├── requirements.txt
├── README.md
│
├── assistants/
│   ├── oss_assistant.py
│   ├── frontier_assistant.py
│   ├── memory.py
│   └── safety.py
│
├── evaluation/
│   ├── evaluate.py
│   ├── prompts.json
│   ├── results.json
│   ├── charts.py
│   ├── hallucination_chart.png
│   ├── safety_chart.png
│   └── helpfulness_chart.png
│
├── report/
│   └── evaluation_report.md
│
└── screenshots/