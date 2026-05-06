from __future__ import annotations

import os

from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI


SYSTEM_PROMPT = (
    "You are Clextron's research agent. "
    "Give concise, useful, and well-structured answers with clear headings. "
    "If the topic is ambiguous, state the assumption you are making."
)

SUPPORTED_LANGUAGES = {
    "english": "English",
    "hindi": "Hindi",
    "tamil": "Tamil",
    "spanish": "Spanish",
    "french": "French",
    "portuguese": "Portuguese",
    "german": "German",
    "italian": "Italian",
    "japanese": "Japanese",
    "korean": "Korean",
    "chinese": "Chinese (Simplified)",
    "arabic": "Arabic",
}


def _build_model() -> ChatGoogleGenerativeAI:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError(
            "GEMINI_API_KEY is not set. Create a .env file with your Gemini API key."
        )

    return ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        temperature=0.2,
        google_api_key=api_key,
    )


def research_topic(topic: str, language: str = "english") -> str:
    if not topic or not topic.strip():
        raise ValueError("topic must not be empty")

    language_lower = language.lower().strip()
    if language_lower not in SUPPORTED_LANGUAGES:
        supported = ", ".join(SUPPORTED_LANGUAGES.keys())
        raise ValueError(f"Language not supported. Choose from: {supported}")

    lang_name = SUPPORTED_LANGUAGES[language_lower]
    system_msg = f"{SYSTEM_PROMPT} Respond in {lang_name}."

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_msg),
            (
                "human",
                "Research this topic in {language} and return: summary, key points, practical next steps, and a short conclusion. Topic: {topic}",
            ),
        ]
    )

    chain = prompt | _build_model()
    response = chain.invoke({"topic": topic.strip(), "language": lang_name})
    return response.content