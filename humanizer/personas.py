"""
Persona-based humanization — wraps humanize() with pre-built user archetypes.
Persona definitions are in configs/personas.yaml.
"""
import yaml
import os
from .core import humanize

PERSONAS_PATH = os.path.join(os.path.dirname(__file__), "../configs/personas.yaml")

with open(PERSONAS_PATH, "r") as f:
    _PERSONAS_CONFIG = yaml.safe_load(f).get("personas", {})


def list_personas() -> list:
    """Return available persona names."""
    return list(_PERSONAS_CONFIG.keys())


def humanize_as(text: str, persona: str, seed: int = None) -> str:
    """
    Humanize text using a named persona's tone and noise settings.

    Args:
        text: input string
        persona: persona name (e.g. 'genz_user', 'formal_user')
        seed: optional random seed

    Returns:
        humanized string
    """
    if persona not in _PERSONAS_CONFIG:
        raise ValueError(f"Unknown persona '{persona}'. Available: {list_personas()}")

    cfg = _PERSONAS_CONFIG[persona]
    return humanize(
        text,
        tone=cfg.get("tone", "casual"),
        noise_level=cfg.get("noise_level", 0.2),
        seed=seed,
    )
