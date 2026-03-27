"""
Batch generator — produces multiple humanized variations from a list of texts.
"""
from .core import humanize
from configs.presets import PRESETS


def generate_batch(texts: list, preset: str = "balanced") -> list:
    """
    Generate one humanized variation per text using a named preset.

    Args:
        texts: list of input strings
        preset: preset name (lite | balanced | aggressive)

    Returns:
        list of dicts with keys: original, synthetic, preset
    """
    if preset not in PRESETS:
        raise ValueError(f"Unknown preset '{preset}'. Available: {list(PRESETS.keys())}")

    params = PRESETS[preset]
    return [
        {"original": text, "synthetic": humanize(text, **params), "preset": preset}
        for text in texts
    ]


def generate_all_presets(texts: list) -> list:
    """
    Generate one variation per preset for each input text.

    Returns:
        list of dicts with keys: original, synthetic, preset
    """
    rows = []
    for preset_name in PRESETS:
        rows.extend(generate_batch(texts, preset=preset_name))
    return rows
