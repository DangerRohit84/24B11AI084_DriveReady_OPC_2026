# Agentic AI Learning Challenge

A daily learning repository for practical LLM chatbots and AI agents. Each day's work is kept in its own folder.

## Current project — AutoMate AI 🚗

**AutoMate AI — Your Journey. Your Intelligent Co-Pilot.**

An English-only automotive assistant built with Python, LangChain, Groq, and Google Colab. It is the individual project used to apply the concepts from the daily classes.

### Day 1 — Basic LLM chatbot

- Connect to a Groq-hosted model using LangChain's `ChatGroq`.
- Define the assistant's role, domain facts, rules, and response format.
- Load the API key securely from Colab Secrets.
- Run a conversational chatbot with a maximum of eight question-and-answer turns in its in-memory history.

### Day 2 — Prompt engineering and Python foundations

- System messages: role, facts, rules, and response format.
- Few-shot prompting for automotive request classification.
- Structured JSON extraction and Python parsing.
- Dictionary lookup with safe defaults using `.get()`.
- Type hints and docstrings.
- Decorators for function-call logging and a LangChain `@tool` definition example.
- Manual conversation memory capped at eight question-and-answer turns.
- `try/except` error handling for invalid input and API failures.

## Submission task

The class recording on **24 November 2026** instructed students to post both Day 1 and Day 2 code to their GitHub repository by **25 November 2026, 11:00 AM IST**. The GitHub profile is to be submitted once through the mentor's Google Form.

Before submitting:
- Run both notebooks in Google Colab.
- Add `GROQ_API_KEY` using Colab Secrets; never hard-code or commit the key.
- Test the chatbot, few-shot classification, JSON parsing, memory limit, reset, and exit flow.
- Confirm both notebooks are present in `Day-01` and `Day-02`.
- Submit your GitHub profile through the mentor's Google Form.

## Repository structure

```text
agentic/
├── Day-01/
│   ├── AutoMate_AI_Day_01.ipynb
│   └── README.md
├── Day-02/
│   ├── AutoMate_AI_Day_02.ipynb
│   └── README.md
├── Day-03/
├── ...
└── Day-12/
```

## Run the notebooks

1. Open the relevant `.ipynb` file in Google Colab.
2. Create a Groq API key at <https://console.groq.com/keys>.
3. In Colab, open **Secrets** (key icon), add `GROQ_API_KEY`, paste the key as its value, and enable notebook access.
4. Run the cells in order.
5. Never paste API keys into notebook code or commit them to GitHub.

The notebooks currently use `openai/gpt-oss-120b` through LangChain-Groq. Check the current model catalogue at <https://console.groq.com/docs/models> if the model becomes unavailable.

## Important limitations

AutoMate AI is a learning prototype, not a live vehicle database. It does not verify current prices, on-road costs, variants, availability, mileage, safety ratings, recalls, or manufacturer specifications. Confirm important details with official sources before making a vehicle decision.

## Technology

- Python
- LangChain
- `langchain-groq`
- Groq API
- Google Colab

## Security

Never commit API keys, `.env` files, access tokens, or other credentials. Use Colab Secrets to supply the API key.
