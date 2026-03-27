from .style import apply_style
from .noise import inject_noise


class HumanizerPipeline:
    """
    Orchestrates style transformation and noise injection.
    """

    def __init__(self, config: dict = None):
        self.config = config or {}

    def run(self, text: str) -> str:
        tone = self.config.get("tone", "casual")
        noise = self.config.get("noise_level", 0.05)
        seed = self.config.get("seed", None)

        text = apply_style(text, tone)
        text = inject_noise(text, level=noise, seed=seed)
        return text
