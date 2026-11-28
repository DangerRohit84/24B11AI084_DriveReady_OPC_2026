"""AutoMate AI Day 6: LangGraph routing and specialist nodes."""

import csv
import os
import re
from pathlib import Path
from typing import Literal, TypedDict

from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, START, END
from pydantic import BaseModel, Field

MODEL_ID = os.getenv("AUTOMATE_MODEL", "openai/gpt-oss-20b")
INVENTORY_FILE = Path("inventory_template.csv")

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise EnvironmentError("Set GROQ_API_KEY in your environment or Colab Secrets.")

llm = ChatGroq(model=MODEL_ID, temperature=0.1, max_retries=3)


class AutoMateState(TypedDict, total=False):
    """Shared information passed between graph nodes."""
    message: str
    intent: str
    reply: str
    sources: list[str]
    matches: list[dict]


class IntentResult(BaseModel):
    """Allowed intent routes for the AutoMate AI graph."""
    intent: Literal["inventory", "faq", "other"] = Field(
        description=(
            "inventory = asks about cars for sale, stock, matching vehicles, "
            "or current dealer inventory. faq = dealership warranty, policy, "
            "inspection, document or business-process question. other = greeting "
            "or general automotive question."
        )
    )


classifier = llm.with_structured_output(IntentResult)


def classify_node(state: AutoMateState) -> AutoMateState:
    """Use the LLM to classify the incoming message into one of three routes."""
    question = state.get("message", "").strip()
    if not question:
        return {"intent": "other", "reply": "Please enter a message."}

    prompt = (
        "Classify the message into exactly one of inventory, faq, other. "
        "Use inventory for live dealer stock searches; faq for dealership policies "
        "and procedures; other for greetings or general automotive explanations. "
        "Return the structured intent only.\\n\\nMessage: " + question
    )
    try:
        result = classifier.invoke(prompt)
        return {"intent": result.intent}
    except Exception:
        return {
            "intent": "other",
            "reply": "I could not classify that request reliably. Please rephrase it.",
        }


def route_by_intent(state: AutoMateState) -> Literal["inventory", "faq", "other"]:
    """Select the next node using the classifier result."""
    intent = state.get("intent", "other")
    return intent if intent in {"inventory", "faq", "other"} else "other"


def inventory_node(state: AutoMateState) -> AutoMateState:
    """Search authorised local dealership inventory using Python filters."""
    question = state.get("message", "").lower()
    if not INVENTORY_FILE.exists():
        return {
            "matches": [],
            "sources": ["inventory_template.csv"],
            "reply": "The inventory file is missing. Ask staff to provide the current inventory.",
        }

    with INVENTORY_FILE.open("r", newline="", encoding="utf-8-sig") as file:
        rows = list(csv.DictReader(file))

    if not rows:
        return {
            "matches": [],
            "sources": ["inventory_template.csv"],
            "reply": "The inventory is empty. Ask dealership staff to add current vehicle records.",
        }

    budget = None
    match = re.search(r"(\d+(?:\.\d+)?)\s*lakh", question)
    if match:
        budget = int(float(match.group(1)) * 100000)
    else:
        match = re.search(r"(?:₹|rs\.?\s*)(\d{4,})", question)
        if match:
            budget = int(match.group(1))

    fuel = next((x for x in ["petrol", "diesel", "cng", "electric", "hybrid"] if x in question), "")
    transmission = next((x for x in ["automatic", "manual"] if x in question), "")
    body = next((x for x in ["suv", "hatchback", "sedan", "mpv"] if x in question), "")

    specific_terms = [
        word for word in re.findall(r"[a-z0-9]+", question)
        if len(word) > 3 and word not in {
            "find", "show", "available", "under", "below", "with", "from",
            "cars", "car", "stock", "inventory", "price", "budget", "automatic",
            "manual", "petrol", "diesel", "electric", "vehicle", "vehicles",
            "hatchback", "sedan", "please", "have", "want"
        }
    ]

    results = []
    for row in rows:
        if str(row.get("status", "")).strip().upper() != "AVAILABLE":
            continue
        try:
            price = int(float(row.get("asking_price_inr", 0)))
        except (ValueError, TypeError):
            continue
        if budget is not None and price > budget:
            continue
        if fuel and fuel not in str(row.get("fuel_type", "")).lower():
            continue
        if transmission and transmission not in str(row.get("transmission", "")).lower():
            continue
        if body and body not in str(row.get("body_type", "")).lower():
            continue

        searchable = " ".join(
            str(row.get(k, "")) for k in
            ["make", "model", "variant", "year", "location", "body_type"]
        ).lower()
        if specific_terms and not any(term in searchable for term in specific_terms):
            continue
        results.append(row)

    if not results:
        return {
            "matches": [],
            "sources": ["inventory_template.csv"],
            "reply": "No matching vehicle marked AVAILABLE was found in the inventory file. Please confirm with dealership staff.",
        }

    lines = []
    for row in results[:5]:
        lines.append(
            f"{row.get('vehicle_id')} | {row.get('year')} {row.get('make')} "
            f"{row.get('model')} {row.get('variant')} | "
            f"₹{int(float(row.get('asking_price_inr', 0))):,} | "
            f"{row.get('fuel_type')} | {row.get('transmission')} | "
            f"{row.get('body_type')} | {row.get('location')} | "
            f"Verified: {row.get('last_verified_at')}"
        )

    evidence = "\\n".join(lines)
    prompt = (
        "You are AutoMate AI's inventory specialist. Answer only from these "
        "inventory rows. Never invent stock or details. Ask staff to reconfirm "
        "availability before a visit.\\n\\nCustomer request: "
        + state.get("message", "") + "\\n\\nInventory rows:\\n" + evidence
    )
    answer = llm.invoke(prompt).content
    return {
        "matches": results[:5],
        "sources": ["inventory_template.csv"],
        "reply": str(answer),
    }


DEALERSHIP_FAQ = [
    "Inspection: buyers should arrange an independent mechanical inspection and review available service records.",
    "Warranty: coverage is vehicle- and dealer-specific; never promise it unless an approved written warranty document confirms it.",
    "Ownership transfer: requirements vary by jurisdiction; staff must check current official transport department requirements.",
    "Availability: stock must be checked against the current inventory. An old advertisement does not prove availability.",
]


def faq_node(state: AutoMateState) -> AutoMateState:
    """Answer dealership policy questions using approved reference facts."""
    prompt = (
        "You are AutoMate AI's dealership FAQ specialist. Answer only from these "
        "reference facts. If they do not answer the question, say the information "
        "is not in the available FAQ and ask the user to check with staff. Never "
        "invent policy or legal requirements. Respond only in English.\\n\\n"
        + "\\n".join(DEALERSHIP_FAQ)
        + "\\n\\nQuestion: " + state.get("message", "")
    )
    answer = llm.invoke(prompt).content
    return {"reply": str(answer), "sources": ["DEALERSHIP_FAQ in task.py"]}


def other_node(state: AutoMateState) -> AutoMateState:
    """Handle greetings and general automotive questions."""
    prompt = (
        "You are AutoMate AI, an English-only automotive assistant. Respond to "
        "greetings and general automotive questions. Do not claim live stock, "
        "dealer CRM, or external service access. Do not invent current prices, "
        "availability, mileage, ratings, warranty, or legal requirements. "
        "Be concise and neutral.\\n\\nUser: " + state.get("message", "")
    )
    answer = llm.invoke(prompt).content
    return {"reply": str(answer), "sources": []}


builder = StateGraph(AutoMateState)
builder.add_node("classify", classify_node)
builder.add_node("inventory_agent", inventory_node)
builder.add_node("faq_agent", faq_node)
builder.add_node("general_agent", other_node)
builder.add_edge(START, "classify")
builder.add_conditional_edges(
    "classify",
    route_by_intent,
    {
        "inventory": "inventory_agent",
        "faq": "faq_agent",
        "other": "general_agent",
    },
)
builder.add_edge("inventory_agent", END)
builder.add_edge("faq_agent", END)
builder.add_edge("general_agent", END)
automate_graph = builder.compile()


def chat(message: str) -> dict:
    """Run a message through the graph and return its shared state."""
    if not message.strip():
        raise ValueError("Message cannot be empty.")
    result = automate_graph.invoke({"message": message.strip()})
    return {
        "intent": result.get("intent", "other"),
        "reply": result.get("reply", ""),
        "sources": result.get("sources", []),
        "matches": result.get("matches", []),
    }


def run_chat() -> None:
    """Run the interactive AutoMate AI graph."""
    print("AutoMate AI — LangGraph Dealership Assistant")
    print("Routes: inventory, faq, other. Type exit to stop.")
    while True:
        message = input("\\nYou: ").strip()
        if message.lower() in {"exit", "quit", "bye"}:
            print("AutoMate AI: Goodbye.")
            break
        try:
            result = chat(message)
            print(f"\\n[Route: {result['intent']}]")
            print("\\nAutoMate AI:", result["reply"])
            if result["sources"]:
                print("Sources:", ", ".join(result["sources"]))
        except Exception as error:
            detail = str(error).lower()
            if "429" in detail or "rate limit" in detail:
                print("AutoMate AI: Rate limit reached. Wait and try again.")
            else:
                print(f"AutoMate AI: Request failed ({type(error).__name__}). Check your API key and model.")


if __name__ == "__main__":
    run_chat()
