from __future__ import annotations

from dataclasses import dataclass

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field

from agents.research_agent import research_topic, SUPPORTED_LANGUAGES
from agents.language_agent import explain_concept


load_dotenv()

app = FastAPI(title="Clextron", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ResearchRequest(BaseModel):
    topic: str = Field(..., min_length=1, description="Topic to research")
    language: str = Field(default="english", description="Language for response (e.g., english, hindi, tamil, spanish, french)")


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


@dataclass(frozen=True)
class AppStatus:
    status: str = "ok"
    service: str = "Clextron"


@app.get("/")
def root() -> HTMLResponse:
        return HTMLResponse(
                """
                <!doctype html>
                <html lang="en">
                    <head>
                        <meta charset="utf-8" />
                        <meta name="viewport" content="width=device-width, initial-scale=1" />
                        <title>Clextron</title>
                        <style>
                            :root {
                                color-scheme: dark;
                                --bg: #0b1020;
                                --panel: rgba(17, 24, 39, 0.92);
                                --text: #e5eefc;
                                --muted: #9fb2d1;
                                --accent: #66e3ff;
                                --accent-2: #8b5cf6;
                            }
                            * { box-sizing: border-box; }
                            body {
                                margin: 0;
                                min-height: 100vh;
                                display: grid;
                                place-items: center;
                                font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
                                background:
                                    radial-gradient(circle at top, rgba(102, 227, 255, 0.18), transparent 28%),
                                    radial-gradient(circle at bottom right, rgba(139, 92, 246, 0.16), transparent 26%),
                                    var(--bg);
                                color: var(--text);
                                padding: 24px;
                            }
                            .card {
                                width: min(720px, 100%);
                                border: 1px solid rgba(159, 178, 209, 0.2);
                                border-radius: 24px;
                                padding: clamp(24px, 4vw, 36px);
                                background: linear-gradient(180deg, rgba(17, 24, 39, 0.98), rgba(10, 15, 30, 0.94));
                                box-shadow: 0 24px 80px rgba(0, 0, 0, 0.35);
                            }
                            .eyebrow {
                                display: inline-block;
                                padding: 6px 12px;
                                border-radius: 999px;
                                background: rgba(102, 227, 255, 0.12);
                                color: var(--accent);
                                font-size: 12px;
                                letter-spacing: 0.08em;
                                text-transform: uppercase;
                            }
                            h1 {
                                margin: 18px 0 12px;
                                font-size: clamp(2.25rem, 5vw, 4rem);
                                line-height: 1.02;
                            }
                            p {
                                margin: 0 0 18px;
                                color: var(--muted);
                                font-size: 1.05rem;
                                line-height: 1.65;
                            }
                            .panel {
                                margin-top: 26px;
                                padding: 18px;
                                border-radius: 18px;
                                border: 1px solid rgba(159, 178, 209, 0.14);
                                background: rgba(255, 255, 255, 0.03);
                            }
                            label {
                                display: block;
                                margin-bottom: 10px;
                                font-size: 0.92rem;
                                color: var(--muted);
                            }
                            .input-row {
                                display: grid;
                                grid-template-columns: 1fr auto;
                                gap: 12px;
                            }
                            input {
                                width: 100%;
                                min-height: 48px;
                                border-radius: 14px;
                                border: 1px solid rgba(159, 178, 209, 0.22);
                                background: rgba(5, 10, 20, 0.85);
                                color: var(--text);
                                padding: 0 14px;
                                outline: none;
                                font: inherit;
                            }
                            input::placeholder {
                                color: rgba(159, 178, 209, 0.65);
                            }
                            input:focus {
                                border-color: rgba(102, 227, 255, 0.6);
                                box-shadow: 0 0 0 4px rgba(102, 227, 255, 0.12);
                            }
                            .actions {
                                display: flex;
                                gap: 12px;
                                flex-wrap: wrap;
                                margin-top: 24px;
                            }
                            a {
                                text-decoration: none;
                                color: inherit;
                            }
                            .button {
                                display: inline-flex;
                                align-items: center;
                                justify-content: center;
                                min-height: 46px;
                                padding: 0 16px;
                                border-radius: 14px;
                                border: 1px solid rgba(159, 178, 209, 0.24);
                                background: rgba(255, 255, 255, 0.04);
                                color: var(--text);
                                transition: transform 0.15s ease, border-color 0.15s ease, background 0.15s ease;
                            }
                            .button.primary {
                                background: linear-gradient(135deg, var(--accent), var(--accent-2));
                                color: #08111f;
                                border-color: transparent;
                                font-weight: 700;
                            }
                            .button.primary:disabled {
                                opacity: 0.7;
                                cursor: wait;
                            }
                            .button:hover {
                                transform: translateY(-1px);
                                border-color: rgba(102, 227, 255, 0.45);
                            }
                            .meta {
                                margin-top: 24px;
                                display: grid;
                                gap: 10px;
                                color: var(--muted);
                                font-size: 0.95rem;
                            }
                            code {
                                color: #d8f6ff;
                            }
                            pre {
                                margin: 14px 0 0;
                                padding: 16px;
                                border-radius: 16px;
                                overflow: auto;
                                white-space: pre-wrap;
                                word-break: break-word;
                                background: rgba(5, 10, 20, 0.88);
                                border: 1px solid rgba(159, 178, 209, 0.16);
                                color: #dce9ff;
                                min-height: 128px;
                            }
                            .status {
                                margin-top: 10px;
                                font-size: 0.92rem;
                                color: var(--muted);
                            }
                            .status.error {
                                color: #fca5a5;
                            }
                            .status.success {
                                color: #86efac;
                            }
                            @media (max-width: 640px) {
                                .input-row {
                                    grid-template-columns: 1fr;
                                }
                                .button.primary {
                                    width: 100%;
                                }
                            }
                        </style>
                    </head>
                    <body>
                        <main class="card">
                            <span class="eyebrow">Clextron is running</span>
                            <h1>AI research agents for students.</h1>
                            <p>
                                Use the API to send a topic to the research agent, or open the docs to try the
                                interactive FastAPI interface.
                            </p>
                            <section class="panel" aria-label="Research demo">
                                <label for="topic">Try the research agent</label>
                                <div class="input-row">
                                    <input id="topic" name="topic" type="text" placeholder="Example: renewable energy" value="renewable energy" />
                                    <button class="button primary" id="runButton" type="button">Run Research</button>
                                </div>
                                <div class="status" id="status">Ready to research.</div>
                                <pre id="output">The response will appear here.</pre>
                            </section>
                            <div class="actions">
                                <a class="button primary" href="/docs">Open API Docs</a>
                                <a class="button" href="/health">View Health JSON</a>
                                <a class="button" href="/research">Research Endpoint</a>
                            </div>
                            <div class="meta">
                                <div>POST <code>/research</code> with JSON like <code>{"topic":"renewable energy"}</code></div>
                                <div>Set <code>GEMINI_API_KEY</code> in <code>.env</code> before using the agent.</div>
                            </div>
                        </main>
                        <script>
                            const topicInput = document.getElementById("topic");
                            const runButton = document.getElementById("runButton");
                            const status = document.getElementById("status");
                            const output = document.getElementById("output");

                            const setStatus = (message, type = "") => {
                                status.className = `status ${type}`.trim();
                                status.textContent = message;
                            };

                            const runResearch = async () => {
                                const topic = topicInput.value.trim();
                                if (!topic) {
                                    setStatus("Enter a topic first.", "error");
                                    return;
                                }

                                runButton.disabled = true;
                                setStatus("Researching topic...", "");
                                output.textContent = "Loading...";

                                try {
                                    const response = await fetch("/research", {
                                        method: "POST",
                                        headers: { "Content-Type": "application/json" },
                                        body: JSON.stringify({ topic }),
                                    });

                                    const payload = await response.json();
                                    if (!response.ok) {
                                        throw new Error(payload.detail || "Research request failed.");
                                    }

                                    setStatus("Research complete.", "success");
                                    output.textContent = payload.result;
                                } catch (error) {
                                    setStatus(error.message, "error");
                                    output.textContent = "No research output yet.";
                                } finally {
                                    runButton.disabled = false;
                                }
                            };

                            runButton.addEventListener("click", runResearch);
                            topicInput.addEventListener("keydown", (event) => {
                                if (event.key === "Enter") {
                                    runResearch();
                                }
                            });
                        </script>
                    </body>
                </html>
                """.strip(),
                media_type="text/html",
        )


@app.get("/health", response_model=AppStatus)
def health() -> AppStatus:
        return AppStatus()


@app.post("/research", response_model=ResearchResponse)
def research(request: ResearchRequest) -> ResearchResponse:
    try:
        result = research_topic(request.topic, request.language)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except Exception as exc:  # pragma: no cover - runtime guard for model failures
        raise HTTPException(status_code=500, detail=str(exc)) from exc

    return ResearchResponse(topic=request.topic, language=request.language, result=result)


@app.post("/explain", response_model=ExplainResponse)
def explain(request: ExplainRequest) -> ExplainResponse:
    try:
        result = explain_concept(request.concept, request.language)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except Exception as exc:  # pragma: no cover - runtime guard for model failures
        raise HTTPException(status_code=500, detail=str(exc)) from exc

    return ExplainResponse(concept=request.concept, language=request.language, result=result)