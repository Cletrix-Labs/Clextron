from __future__ import annotations

from dataclasses import dataclass
import os

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field

from agents.language_agent import explain_concept
from agents.research_agent import SUPPORTED_LANGUAGES, normalize_language_key, research_topic


load_dotenv()

app = FastAPI(title="Clextron", version="0.1.0")
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ResearchRequest(BaseModel):
    topic: str = Field(..., min_length=1, description="Topic to research")
    language: str = Field(default="english", description="Language for response")


class ResearchResponse(BaseModel):
    topic: str
    language: str
    result: str


class ExplainRequest(BaseModel):
    concept: str = Field(..., min_length=1, description="Concept to explain")
    language: str = Field(default="english", description="Language for explanation")


class ExplainResponse(BaseModel):
    concept: str
    language: str
    result: str


class LanguageOption(BaseModel):
    key: str
    name: str


@dataclass(frozen=True)
class AppStatus:
    status: str = "ok"
    service: str = "Clextron"


def _handle_agent_error(exc: Exception) -> HTTPException:
    message = str(exc)
    lowered = message.lower()
    if "429" in message or "quota" in lowered or "rate limit" in lowered:
        return HTTPException(
            status_code=429,
            detail="API quota reached for today. Try again later or use a different Gemini project key.",
        )
    return HTTPException(status_code=500, detail=message)


@app.get("/")
def root(request: Request):
    language_options = [
        {"key": key, "name": SUPPORTED_LANGUAGES[key]}
        for key in sorted(SUPPORTED_LANGUAGES.keys())
    ]
    return templates.TemplateResponse(
        request,
        "index.html",
        {
            "language_options": language_options,
            "default_language": "english",
        },
    )


@app.get("/health", response_model=AppStatus)
def health() -> AppStatus:
    return AppStatus()


@app.get("/languages", response_model=list[LanguageOption])
def languages() -> list[LanguageOption]:
    return [
        LanguageOption(key=key, name=SUPPORTED_LANGUAGES[key])
        for key in sorted(SUPPORTED_LANGUAGES.keys())
    ]


@app.post("/research", response_model=ResearchResponse)
def research(request: ResearchRequest) -> ResearchResponse:
    language_key = normalize_language_key(request.language)
    try:
        result = research_topic(request.topic, language_key)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except Exception as exc:  # pragma: no cover
        raise _handle_agent_error(exc) from exc

    return ResearchResponse(topic=request.topic, language=language_key, result=result)


@app.post("/explain", response_model=ExplainResponse)
def explain(request: ExplainRequest) -> ExplainResponse:
    language_key = normalize_language_key(request.language)
    try:
        result = explain_concept(request.concept, language_key)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except Exception as exc:  # pragma: no cover
        raise _handle_agent_error(exc) from exc

    return ExplainResponse(concept=request.concept, language=language_key, result=result)