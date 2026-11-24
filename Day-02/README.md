# Day 2 — AutoMate AI: Prompting and Python Foundations

Day 2 applies the concepts from the second Agentic AI class to the automotive assistant.

## Topics covered

1. **System messages:** define AutoMate AI's role, project facts, behavioural rules, and response format.
2. **Few-shot prompting:** provide examples to guide automotive request classification. Examples are prompt context, not model training.
3. **JSON output:** extract a vehicle enquiry into consistent key-value fields and validate it with Python's `json.loads()`.
4. **Python dictionaries:** use `.get()` to provide a safe fallback for missing keys.
5. **Type hints and docstrings:** document function inputs, outputs, and purpose.
6. **Decorators:** add function-call logging without changing the wrapped function's core behaviour.
7. **Manual conversation memory:** append the latest user/assistant messages and cap history at eight question-and-answer turns.
8. **Exception handling:** catch input, JSON, and API failures and return useful messages rather than abruptly stopping the chatbot.

## Run in Google Colab

1. Open `AutoMate_AI_Day_02.ipynb` in Google Colab.
2. Add the `GROQ_API_KEY` secret in Colab Secrets and enable notebook access.
3. Run the cells from top to bottom.
4. Complete the Day 2 checklist at the end of the notebook.

## Language

AutoMate AI's system prompt requires English responses. The notebook, explanations, and documentation are in English.

## Limitations

The chatbot does not access live vehicle listings, prices, specifications, recalls, or dealer inventory. Treat its answers as general guidance and verify current vehicle details with official sources.

## Stack

Python · LangChain · LangChain-Groq · Groq API · Google Colab
