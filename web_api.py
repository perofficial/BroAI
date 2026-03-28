"""
BroAI FastAPI server — connects the humanizer pipeline to the web.
Run with: uvicorn web_api:app --reload
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import yaml
import os
from humanizer import humanize, HumanizerPipeline

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


CONFIG_PATH = os.path.join(os.path.dirname(__file__), "config", "production.yaml")

if not os.path.exists(CONFIG_PATH):
    raise RuntimeError(f"Config not found: {CONFIG_PATH}")

with open(CONFIG_PATH, "r") as f:
    config = yaml.safe_load(f) or {}

app = FastAPI(
    title="BroAI Humanizer API",
    description="Transform flat AI text into realistic human-like output.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class HumanizeRequest(BaseModel):
    text: str = Field(..., min_length=1, max_length=5000)
    tone: str = Field(default="casual", pattern="^(casual|formal|genz)$")
    noise_level: float = Field(default=0.2, ge=0.0, le=1.0)
    seed: int | None = Field(default=None)


class HumanizeResponse(BaseModel):
    original: str
    humanized: str
    tone: str
    noise_level: float


@app.post("/humanize", response_model=HumanizeResponse)
def humanize_text(req: HumanizeRequest):
    result = humanize(
        text=req.text,
        tone=req.tone,
        noise_level=req.noise_level,
        seed=req.seed,
    )
    return HumanizeResponse(
        original=req.text,
        humanized=result,
        tone=req.tone,
        noise_level=req.noise_level,
    )


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "default_tone": config.get("pipeline", {}).get("tone", "casual"),
        "default_noise": config.get("pipeline", {}).get("noise_level", 0.2),
    }
