# Day 3 — AutoMate AI: First Basic Agent

Day 3 turns the Day 1–2 chatbot into a basic goal-oriented LangChain agent. It follows the class demonstration using `create_agent` with a language model, a clear system prompt, and **no external tools yet**. Google Sheets and Telegram tools belong to the next lesson.

## What this notebook demonstrates

- The difference between a question-answering chatbot and a goal-oriented agent.
- The four parts of an agent: brain (LLM), instructions, tools, and memory.
- A basic agent loop: reason, act, observe, and repeat (ReAct).
- LangChain's standard `create_agent` structure.
- A model provider switch between Google Gemini and OpenAI.
- A ten-case CSV evaluation using expected keyword groups.
- Reviewing failures and improving facts/rules, then rerunning the full test set.
- Conversation history capped at eight question-and-answer turns.

## Model provider

The notebook defaults to Google Gemini. You can switch `MODEL_PROVIDER` to `"openai"` and use an OpenAI API key instead.

- Google Gemini API key: <https://aistudio.google.com/app/apikey>
- OpenAI API key: <https://platform.openai.com/api-keys>

Save the selected key in Google Colab Secrets as `GOOGLE_API_KEY` or `OPENAI_API_KEY`. Enable notebook access. Never write a key directly in the notebook or commit it to GitHub.

The default Gemini model configured in the notebook is `gemini-3.8-flash`; the OpenAI option is `gpt-6.2-sol`. Model names, access, pricing, and quotas can change. Confirm the current provider catalogue before running.

## Run the notebook

1. Open `AutoMate_AI_Day_03.ipynb` in Google Colab.
2. Choose `google` or `openai` in the provider configuration cell.
3. Add the matching API key in Colab Secrets.
4. Run the notebook cells in order.
5. Download `test.csv` from this folder and upload it when the notebook requests the file.
6. Review all ten outputs, the PASS/FAIL results, and the failed cases.
7. Improve the instructions where a response failed, then run the complete evaluation again.

## Evaluation notes

The supplied `test.csv` contains ten AutoMate AI car-advisor questions. The notebook uses expected keyword groups as a quick screening check; it is not a complete semantic evaluation. Read each generated answer and manually confirm that it is accurate, safe, and consistent with the project instructions. Do not mark a response correct only because it contains a matching word.

## Scope and limitations

This Day 3 agent has no external tools. It cannot check live vehicle prices, dealer inventory, current specifications, recalls, safety ratings, or place orders. Do not claim it can take those actions. External tools will be added in a later lesson.

## Stack

Python · LangChain `create_agent` · Google Gemini or OpenAI · Google Colab


## OPC submission files

The required Python source file for this task is `task.py`. The Colab notebook is retained as an optional interactive version, and `test.csv` supplies the ten evaluation questions. Run the task in Google Colab, install `langchain`, `langchain-openai`, `langchain-google-genai`, and `pandas`, then add either `GOOGLE_API_KEY` or `OPENAI_API_KEY` in Colab Secrets. Upload `test.csv` when the notebook or script requests it.
