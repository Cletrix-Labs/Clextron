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
    "afrikaans": "Afrikaans",
    "amharic": "Amharic",
    "hindi": "Hindi",
    "bengali": "Bengali",
    "bulgarian": "Bulgarian",
    "chinese": "Chinese (Simplified)",
    "croatian": "Croatian",
    "czech": "Czech",
    "danish": "Danish",
    "dutch": "Dutch",
    "estonian": "Estonian",
    "filipino": "Filipino",
    "finnish": "Finnish",
    "tamil": "Tamil",
    "telugu": "Telugu",
    "kannada": "Kannada",
    "malayalam": "Malayalam",
    "marathi": "Marathi",
    "gujarati": "Gujarati",
    "punjabi": "Punjabi",
    "urdu": "Urdu",
    "nepali": "Nepali",
    "sinhala": "Sinhala",
    "french": "French",
    "german": "German",
    "greek": "Greek",
    "hausa": "Hausa",
    "hebrew": "Hebrew",
    "hungarian": "Hungarian",
    "indonesian": "Indonesian",
    "italian": "Italian",
    "spanish": "Spanish",
    "portuguese": "Portuguese",
    "japanese": "Japanese",
    "korean": "Korean",
    "latvian": "Latvian",
    "lithuanian": "Lithuanian",
    "malay": "Malay",
    "norwegian": "Norwegian",
    "persian": "Persian",
    "polish": "Polish",
    "romanian": "Romanian",
    "russian": "Russian",
    "serbian": "Serbian",
    "slovak": "Slovak",
    "slovenian": "Slovenian",
    "swahili": "Swahili",
    "swedish": "Swedish",
    "thai": "Thai",
    "turkish": "Turkish",
    "ukrainian": "Ukrainian",
    "vietnamese": "Vietnamese",
    "yoruba": "Yoruba",
    "zulu": "Zulu",
    "arabic": "Arabic",
}


def normalize_language_key(language: str) -> str:
    return language.lower().strip()


def resolve_language_name(language: str) -> tuple[str, str]:
    language_key = normalize_language_key(language)
    if language_key not in SUPPORTED_LANGUAGES:
        supported = ", ".join(SUPPORTED_LANGUAGES.keys())
        raise ValueError(f"Language not supported. Choose from: {supported}")

    return language_key, SUPPORTED_LANGUAGES[language_key]


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

    _language_key, lang_name = resolve_language_name(language)
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