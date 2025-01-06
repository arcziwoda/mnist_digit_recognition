import typer
from mnist_digit_recognition.ml.data_loader import load_data
from mnist_digit_recognition.ml.inference import (
    make_predictions,
    get_mismatched_predictions,
)
from mnist_digit_recognition.ml.train import train_model
from mnist_digit_recognition.ml.metrics import calculate_metrics, display_metrics
from mnist_digit_recognition.ml.model import SimpleNN, load_model, save_model
from mnist_digit_recognition.gui.gui import display_predictions

MODEL_PATH = "models/model.pth"

app = typer.Typer()


def get_or_train_model(batch_size: int = 64, epochs: int = 5):
    """
    Load a model from the given path or train a new one if not found.
    """
    model = load_model(MODEL_PATH)
    if model is None:
        typer.echo("Model not found. Training a new model...")
        train_loader, _ = load_data(batch_size=batch_size)
        model = SimpleNN()
        model = train_model(model, train_loader, epochs)
        save_model(model, MODEL_PATH)
        typer.echo("New model trained and saved.")
    return model


@app.command()
def train(batch_size: int = 64, epochs: int = 5):
    """
    Train and save the model on the training dataset.
    """
    train_loader, _ = load_data(batch_size=batch_size)
    model = SimpleNN()
    model = train_model(model, train_loader, epochs)
    save_model(model=model, path=MODEL_PATH)
    typer.echo("Model training completed.")


@app.command()
def metrics():
    """
    Calculate and display metrics on the test dataset.
    """
    _, test_loader = load_data()
    model = get_or_train_model()
    _, labels, predictions = make_predictions(model, test_loader)
    metric_results = calculate_metrics(labels, predictions)
    display_metrics(metric_results)


@app.command()
def view(mismatched: bool = False):
    """
    Run an interactive view to display predictions.

    Use --mismatched to display only mismatched predictions.
    """
    _, test_loader = load_data()
    model = get_or_train_model()
    images, labels, predictions = make_predictions(model, test_loader)

    if mismatched:
        images, labels, predictions = get_mismatched_predictions(
            images, labels, predictions
        )

    display_predictions(images, labels, predictions)


if __name__ == "__main__":
    app()
