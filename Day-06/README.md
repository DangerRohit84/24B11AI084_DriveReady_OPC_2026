# Day 6 — AutoMate AI: Multi-Agent Orchestration with LangGraph

This is our dealership-focused adaptation of the 28 November class. It demonstrates an intent classifier, specialist nodes, conditional edges, and shared graph state.

## Graph design

- Classifier node: LLM returns one of three structured intents: inventory, faq, or other.
- Inventory specialist: searches the local inventory CSV using deterministic Python filters.
- FAQ specialist: answers from the approved reference facts included in the source.
- General specialist: handles greetings and general automotive questions.
- Shared state: passes message, intent, reply, source list, and inventory matches.
- Conditional edges: choose the correct specialist node and finish at END.

The graph uses one model with separate specialist responsibilities. It is a foundational routed multi-specialist graph, not a fully autonomous multi-agent company.

## Run in VS Code

1. Install Python 3.10 or newer and open this repository in VS Code.
2. Create and activate a virtual environment.
3. Run `pip install -r requirements.txt`.
4. Set the GROQ_API_KEY environment variable. Never commit the key.
5. Keep inventory_template.csv in the same folder as task.py.
6. Run `python task.py`.

## Inventory data

Add only authorised dealership records to inventory_template.csv. Only rows with status AVAILABLE are returned. The supplied file contains headers only, not fake stock.

## Test

Use test.csv to check routing, stock filtering, policy answers, and fallback behaviour. Check both the intent and the content of each answer.

## Limitations

- Inventory comes from a local CSV, not Google Sheets or a live dealer system.
- FAQ facts are demonstration references, not an official dealership policy.
- No payment, messaging, booking, or persistent customer memory is connected.
- All stock, price, warranty, legal, and vehicle-condition details require authorised verification.

## OPC submission files

- task.py — Python source.
- README.md — implementation guide.
- inventory_template.csv — inventory input template.
- test.csv — routing test prompts.
