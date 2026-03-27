def evaluate_text(text):
    words = text.split()

    # % parole modificate (proxy umano)
    short_words = sum(1 for w in words if len(w) <= 2)

    # presenza elementi umani
    human_tokens = ["pls", "yo", "uh", "idk", "lol", "u", "r"]
    human_score = sum(1 for w in words if w.lower() in human_tokens)

    score = (short_words + human_score) / max(len(words), 1)

    return score


def evaluate_file(path):
    with open(path, "r") as f:
        lines = [l.strip() for l in f if l.strip()]

    scores = [evaluate_text(l) for l in lines]

    avg = sum(scores) / len(scores)

    print(f"\n📊 Average score: {round(avg, 3)}")

    return avg


if __name__ == "__main__":
    evaluate_file("output/output_humanized.txt")