from __future__ import annotations

import os

from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

from agents.research_agent import SUPPORTED_LANGUAGES


def _build_model() -> ChatGoogleGenerativeAI:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError(
            "GEMINI_API_KEY is not set. Create a .env file with your Gemini API key."
        )

    return ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        temperature=0.3,
        google_api_key=api_key,
    )


def explain_concept(concept: str, language: str = "english") -> str:
    """
    Explain any concept in the requested language with examples and depth.
    """
    if not concept or not concept.strip():
        raise ValueError("concept must not be empty")

    language_lower = language.lower().strip()
    if language_lower not in SUPPORTED_LANGUAGES:
        supported = ", ".join(SUPPORTED_LANGUAGES.keys())
        raise ValueError(f"Language not supported. Choose from: {supported}")

    lang_name = SUPPORTED_LANGUAGES[language_lower]

    system_prompt = (
        f"You are Clextron's language agent. Explain complex concepts clearly and simply. "
        f"Use real-world examples. Target students of all levels. Respond in {lang_name}."
    )

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            (
                "human",
                "Explain this concept clearly with examples: {concept}. "
                "Use simple language that students can understand.",
            ),
        ]
    )

    chain = prompt | _build_model()
    response = chain.invoke({"concept": concept.strip()})
    return response.content
