from .pipeline import HumanizerPipeline


def humanize(
    text: str,
    tone: str = "casual",
    noise_level: float = 0.05,
    seed: int = None
) -> str:
    """
    Main public API.

    Args:
        text (str): input text to humanize
        tone (str): casual | formal | genz
        noise_level (float): 0.0 = clean, 1.0 = very noisy
        seed (int): optional seed for reproducibility

    Returns:
        str: humanized text
    """
    pipeline = HumanizerPipeline({
        "tone": tone,
        "noise_level": noise_level,
        "seed": seed,
    })
    return pipeline.run(text)
