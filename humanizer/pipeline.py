from .style import apply_style
from .noise import inject_noise


class HumanizerPipeline:

    def __init__(self, config: dict):
        self.config = config

    def run(self, text: str) -> str:

        pipeline_cfg = self.config.get("pipeline", {})

        tone = pipeline_cfg.get("tone", "casual")
        noise_level = pipeline_cfg.get("noise_level", 0.05)
        seed = pipeline_cfg.get("seed", None)

        # Step 1: style transformation
        text = apply_style(text, tone)

        # Step 2: noise injection
        text = inject_noise(text, noise_level, seed)

        return text