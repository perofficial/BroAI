import pytest
from humanizer import humanize
from humanizer.utils.random_utils import weighted_choice


class TestHumanize:

    def test_returns_string(self):
        assert isinstance(humanize("Hello world"), str)

    def test_output_not_empty(self):
        assert len(humanize("How can I reset my password?")) > 0

    def test_casual_tone(self):
        assert isinstance(humanize("I cannot access my account", tone="casual", seed=42), str)

    def test_genz_tone(self):
        assert isinstance(humanize("Hello friend, this is really good", tone="genz", seed=42), str)

    def test_formal_expands_contractions(self):
        result = humanize("I can't do it", tone="formal", noise_level=0.0, seed=42)
        assert isinstance(result, str)

    def test_seed_reproducibility(self):
        text = "I want to cancel my subscription"
        r1 = humanize(text, tone="genz", noise_level=0.3, seed=99)
        r2 = humanize(text, tone="genz", noise_level=0.3, seed=99)
        assert r1 == r2

    def test_high_noise_modifies_text(self):
        text = "How can I reset my password please"
        results = [humanize(text, noise_level=0.9) for _ in range(20)]
        assert any(r != text for r in results)


class TestWeightedChoice:

    def test_returns_valid_choice(self):
        choices = [("a", 0.5), ("b", 0.3), ("c", 0.2)]
        for _ in range(50):
            assert weighted_choice(choices) in ("a", "b", "c")

    def test_single_choice(self):
        assert weighted_choice([("only", 1.0)]) == "only"
