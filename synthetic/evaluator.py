def evaluate_dataset(rows):
    total = len(rows)
    avg_length = sum(len(r["synthetic"].split()) for r in rows) / total

    return {
        "total_samples": total,
        "avg_length": avg_length
    }