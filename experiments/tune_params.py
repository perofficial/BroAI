import random
from humanizer import humanize

TEXTS = [
    "How can I reset my password?",
    "I cannot access my account",
    "Where is my order?",
    "I want to cancel my subscription"
]

noise_levels = [0.1, 0.3, 0.5, 0.7, 0.9]
tones = ["casual", "genz"]


def evaluate(text):
    words = text.split()

    typo_like = ["teh", "pls", "u", "r", "ur", "msg"]
    
    score = 0

    for w in words:
        w_clean = w.lower()

        # typo da dizionario
        if w_clean in typo_like:
            score += 1

        # typo "random" (parole strane)
        elif len(w_clean) > 4 and not w_clean.isalpha():
            score += 0.5

        # parola modificata (tipo swap lettere)
        elif any(char.isdigit() for char in w_clean):
            score += 0.5

    return score / max(len(words), 1)


results = []

for tone in tones:
    for n in noise_levels:

        outputs = []

        for text in TEXTS:
            for _ in range(5):
                out = humanize(text, tone=tone, noise_level=n)
                outputs.append(out)

        scores = [evaluate(o) for o in outputs]
        avg_score = sum(scores) / len(scores)

        results.append({
            "tone": tone,
            "noise": n,
            "score": avg_score
        })


print("\n=== RESULTS ===\n")

for r in results:
    print(f"tone={r['tone']} | noise={r['noise']} → score={round(r['score'], 3)}")