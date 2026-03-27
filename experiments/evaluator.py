"""
Dataset-level evaluator — called by run.py or standalone.
"""
from experiments.evaluate_output import evaluate_text


def evaluate_dataset(rows: list) -> dict:
    """
    Args:
        rows: list of dicts with at least a 'synthetic' key

    Returns:
        dict with total_samples, avg_length, avg_score
    """
    total = len(rows)
    if total == 0:
        return {"total_samples": 0, "avg_length": 0, "avg_score": 0}

    avg_length = sum(len(r["synthetic"].split()) for r in rows) / total
    avg_score = sum(evaluate_text(r["synthetic"]) for r in rows) / total

    return {
        "total_samples": total,
        "avg_length": round(avg_length, 2),
        "avg_score": round(avg_score, 3),
    }
