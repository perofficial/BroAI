import os
import csv
from humanizer import humanize
from configs.presets import PRESETS

INPUT_FILE = "data/clean_queries.txt"
OUTPUT_FILE = "output/synthetic_dataset.csv"


def load_queries(path: str) -> list:
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]


def generate_variations(text: str) -> list:
    return [
        {"preset": name, "synthetic": humanize(text, **params)}
        for name, params in PRESETS.items()
    ]


def save_to_csv(rows: list, path: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["original", "preset", "synthetic"])
        for row in rows:
            writer.writerow([row["original"], row["preset"], row["synthetic"]])


def main():
    print("Loading queries...")
    queries = load_queries(INPUT_FILE)
    print(f"Loaded {len(queries)} queries")

    dataset = []
    print("Generating synthetic data...")
    for q in queries:
        for variation in generate_variations(q):
            dataset.append({"original": q, **variation})

    print(f"Generated {len(dataset)} samples")
    save_to_csv(dataset, OUTPUT_FILE)
    print(f"Saved dataset to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
