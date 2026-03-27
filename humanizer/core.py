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
        text (str): input text
        tone (str): casual | formal | genz
        noise_level (float): 0.0 → clean, 1.0 → very noisy
        seed (int): for reproducibility

    Returns:
        str: transformed text
    """

    pipeline = HumanizerPipeline({
        "pipeline": {
            "tone": tone,
            "noise_level": noise_level,
            "seed": seed
        }
    })

    return pipeline.run(text)