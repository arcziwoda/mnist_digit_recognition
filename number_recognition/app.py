from ml.data_loader import load_data
from ml.inference import make_predictions
from ml.train import train_model
from ml.metrics import calculate_metrics, display_metrics
from ml.model import SimpleNN
from gui.gui import display_predictions


def run_app():

    train_loader, test_loader = load_data(batch_size=64)
    model = SimpleNN()

    model = train_model(model, train_loader)

    images, labels, predictions = make_predictions(model, test_loader)

    display_metrics(calculate_metrics(labels, predictions))

    display_predictions(images, labels, predictions)


if __name__ == "__main__":
    run_app()
