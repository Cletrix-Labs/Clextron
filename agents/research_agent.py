from __future__ import annotations

import os

from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI


SYSTEM_PROMPT = (
    "You are Clextron's research agent. "
    "Give concise, useful, and well-structured answers with clear headings. "
    "If the topic is ambiguous, state the assumption you are making."
)


def _build_model() -> ChatGoogleGenerativeAI:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError(
            "GEMINI_API_KEY is not set. Create a .env file with your Gemini API key."
        )

    return ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=0.2,
        google_api_key=api_key,
    )


def research_topic(topic: str) -> str:
    if not topic or not topic.strip():
        raise ValueError("topic must not be empty")

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", SYSTEM_PROMPT),
            (
                "human",
                "Research this topic and return: summary, key points, practical next steps, and a short conclusion. Topic: {topic}",
            ),
        ]
    )

    chain = prompt | _build_model()
    response = chain.invoke({"topic": topic.strip()})
    return response.content