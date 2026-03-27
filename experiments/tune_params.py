"""
Grid-search over tone × noise_level combinations to find the best params.
Run: python -m experiments.tune_params
"""
from humanizer import humanize
from experiments.evaluate_output import evaluate_text

TEXTS = [
    "How can I reset my password?",
    "I cannot access my account",
    "Where is my order?",
    "I want to cancel my subscription",
]

NOISE_LEVELS = [0.05, 0.10, 0.20, 0.35, 0.50]
TONES = ["casual", "genz", "formal"]
SAMPLES_PER_COMBO = 5


def run_grid():
    results = []

    for tone in TONES:
        for noise in NOISE_LEVELS:
            outputs = [
                humanize(text, tone=tone, noise_level=noise)
                for text in TEXTS
                for _ in range(SAMPLES_PER_COMBO)
            ]
            scores = [evaluate_text(o) for o in outputs]
            avg = sum(scores) / len(scores)
            results.append({"tone": tone, "noise": noise, "score": avg})

    print("\n=== TUNING RESULTS ===\n")
    for r in sorted(results, key=lambda x: abs(x["score"] - 0.20)):
        flag = " ✓" if 0.15 <= r["score"] <= 0.25 else ""
        print(f"tone={r['tone']:<8} noise={r['noise']:.2f} → score={r['score']:.3f}{flag}")


if __name__ == "__main__":
    run_grid()
