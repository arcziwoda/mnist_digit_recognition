from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


def calculate_metrics(labels, predictions, average="macro"):
    accuracy = accuracy_score(labels, predictions)
    precision = precision_score(labels, predictions, average=average)
    recall = recall_score(labels, predictions, average=average)
    f1 = f1_score(labels, predictions, average=average)
    correct_count, incorrect_count = classification_counts(labels, predictions)

    metrics = {
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1_score": f1,
        "correct_count": correct_count,
        "incorrect_count": incorrect_count,
    }
    return metrics


def display_metrics(metrics):
    print("### Metrics ###")
    for metric, value in metrics.items():
        formatted_value = f"{value:.4f}" if isinstance(value, float) else str(value)
        print(f"{metric.capitalize()}: {formatted_value}")


def classification_counts(labels, predictions):
    correct = sum(l == p for l, p in zip(labels, predictions))
    total = len(labels)
    incorrect = total - correct
    return (int(correct), int(incorrect))
