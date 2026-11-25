# Agentic AI Learning Challenge

A daily learning repository for building practical LLM chatbots and AI agents. Each day's work is kept in its own folder.

## Individual project — AutoMate AI 🚗

**AutoMate AI — Your Journey. Your Intelligent Co-Pilot.**

An English-only automotive assistant built with Python, LangChain, and Google Colab. This individual project applies the concepts introduced in the Agentic AI classes.

### Day 1 — Basic LLM chatbot

Required OPC source: `Day-01/task.py` (the `.ipynb` file is an optional Colab notebook).

- Connect to a Groq-hosted model using LangChain's `ChatGroq`.
- Define the assistant's role, facts, rules, and response format.
- Load the API key securely from Colab Secrets.
- Run a conversational chatbot with a maximum of eight question-and-answer turns in its in-memory history.

### Day 2 — Prompt engineering and Python foundations

Required OPC source: `Day-02/task.py` (the `.ipynb` file is an optional Colab notebook).

- System messages: role, facts, rules, and response format.
- Few-shot prompting for automotive request classification.
- Structured JSON extraction and Python parsing.
- Dictionary lookup with safe defaults using `.get()`.
- Type hints and docstrings.
- Decorators for function-call logging and a LangChain `@tool` definition example.
- Manual conversation memory capped at eight question-and-answer turns.
- `try/except` error handling for invalid input and API failures.

### Day 3 — First basic LangChain agent

Required OPC source: `Day-03/task.py`; test data: `Day-03/test.csv` (the `.ipynb` file is an optional Colab notebook).

- Create a basic agent using LangChain's `create_agent`.
- Switch between Google Gemini and OpenAI models.
- Understand the four agent components: brain, instructions, tools, and memory.
- Understand the ReAct loop: reason, act, observe, and repeat.
- Test the agent with ten questions from `Day-03/test.csv`.
- Inspect failed answers, improve instructions, and rerun all tests.

**Day 3 scope:** this first agent has no external tools connected yet. Google Sheets and Telegram tool integrations are for the following class.

## Current class follow-ups

The 25 November class asked students to:
- Upload Days 1, 2, and 3 into this same GitHub repository.
- Submit the repository link through the mentor's Google Form (the profile/repository form is submitted once).
- Register for the Google Gemini for Bharat hackathon and complete the separate college verification form shared by the mentors.
- Run the Day 3 agent using an OpenAI or Google Gemini API key.
- Test at least ten cases, inspect failures, improve the instructions, and test again.
- Identify an individual real-world problem to develop further in the next phase.

## Repository structure

```text
agentic/
├── Day-01/
│   ├── task.py
│   ├── AutoMate_AI_Day_01.ipynb
│   └── README.md
├── Day-02/
│   ├── task.py
│   ├── AutoMate_AI_Day_02.ipynb
│   └── README.md
├── Day-03/
│   ├── task.py
│   ├── AutoMate_AI_Day_03.ipynb
│   ├── README.md
│   └── test.csv
├── Day-04/
├── ...
└── Day-12/
```

## OPC submission format

Each completed day has a `task.py` source file and a `README.md` describing its implementation. The Colab notebooks are included as optional interactive companions.

## Run the notebooks and source files

1. Open the relevant `.ipynb` file in Google Colab.
2. Add the required provider API key in Colab Secrets and enable notebook access:
   - Day 1 and Day 2: `GROQ_API_KEY`
   - Day 3 with Gemini: `GOOGLE_API_KEY`
   - Day 3 with OpenAI: `OPENAI_API_KEY`
3. Run the notebook cells in order.
4. Never paste API keys into notebook code or commit them to GitHub.

Day 1 and Day 2 currently use Groq's `openai/gpt-oss-120b` model. Day 3 defaults to `gemini-3.8-flash` and also offers `gpt-6.2-sol`. Model access, pricing, free-tier eligibility, rate limits, and availability depend on each provider account and can change; check the current provider catalogue before running.

## Important limitations

AutoMate AI is a learning prototype, not a live vehicle database. It does not verify current prices, on-road costs, variants, availability, mileage, safety ratings, recalls, or manufacturer specifications. Confirm important vehicle details with official sources before making a purchase decision.

## Security

Never commit API keys, `.env` files, access tokens, or other credentials. Use Google Colab Secrets to supply API keys.
