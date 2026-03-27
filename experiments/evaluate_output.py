"""
Evaluate the human-likeness of generated text.
Target score: 0.15–0.25 = realistic.
  < 0.15 → too clean / robotic
  > 0.25 → too noisy
"""

HUMAN_TOKENS = {"pls", "yo", "uh", "um", "idk", "lol", "u", "r", "like",
                "ngl", "tbh", "fr", "bro", "dude", "nah", "lowkey", "literally"}


def evaluate_text(text: str) -> float:
    words = text.split()
    if not words:
        return 0.0

    short_words = sum(1 for w in words if len(w) <= 2)
    human_score = sum(1 for w in words if w.lower() in HUMAN_TOKENS)

    return (short_words + human_score) / len(words)


def evaluate_file(path: str) -> float:
    with open(path, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]

    if not lines:
        print("No lines found.")
        return 0.0

    scores = [evaluate_text(line) for line in lines]
    avg = sum(scores) / len(scores)

    print(f"\n📊 Evaluated {len(lines)} lines")
    print(f"   Min score  : {min(scores):.3f}")
    print(f"   Max score  : {max(scores):.3f}")
    print(f"   Avg score  : {avg:.3f}")

    if avg < 0.15:
        print("   → Text is too clean. Increase noise_level.")
    elif avg > 0.25:
        print("   → Text is too noisy. Decrease noise_level.")
    else:
        print("   → Score is in the realistic range.")

    return avg


if __name__ == "__main__":
    evaluate_file("output/output_humanized.txt")
