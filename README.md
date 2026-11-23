# Agentic AI Learning Challenge

A daily learning repository for building practical LLM applications and AI agents.

## Current project

### Day 1 — AutoMate AI

**AutoMate AI** is a car-buying and automotive information assistant built with Python, LangChain, Groq, and Google Colab.

The assistant responds in English unless the user explicitly requests another language. It can help users:
- Explore vehicle choices around a stated budget.
- Compare vehicle models while flagging details that need verification.
- Understand petrol, diesel, CNG, hybrid, and electric powertrains.
- Learn about basic maintenance and vehicle safety features.
- Prepare questions and checks for a used-car inspection.

> AutoMate AI is an educational prototype, not a live vehicle database. Verify current prices, specifications, safety ratings, recalls, and availability with official sources before making decisions.

## Repository structure

```text
agentic/
├── Day-01/
│   ├── AutoMate_AI_Day_01.ipynb
│   └── README.md
├── Day-02/
├── Day-03/
├── ...
└── Day-12/
```

## Run Day 1 in Google Colab

1. Open `Day-01/AutoMate_AI_Day_01.ipynb` in Google Colab.
2. Create a Groq API key at <https://console.groq.com/keys>.
3. In Colab, open **Secrets** (key icon) and add a secret named `GROQ_API_KEY`. Paste the key as its value and enable notebook access.
4. Run the notebook cells from top to bottom.
5. Never paste the API key into notebook code or commit it to GitHub.

The notebook uses Groq's `openai/gpt-oss-120b` model. Check model availability and limits in the current catalogue: <https://console.groq.com/docs/models>.

## Tech stack

- Python
- LangChain
- `langchain-groq`
- Groq API
- Google Colab

## Security

Never commit API keys, `.env` files, access tokens, or other credentials. Use Colab Secrets for the API key.
