from mnist_digit_recognition.ml.data_loader import load_data
from mnist_digit_recognition.ml.inference import make_predictions
from mnist_digit_recognition.ml.train import train_model
from mnist_digit_recognition.ml.metrics import calculate_metrics, display_metrics
from mnist_digit_recognition.ml.model import SimpleNN
from mnist_digit_recognition.gui.gui import display_predictions


def app():

    train_loader, test_loader = load_data(batch_size=64)
    model = SimpleNN()

    model = train_model(model, train_loader)

    images, labels, predictions = make_predictions(model, test_loader)

    display_metrics(calculate_metrics(labels, predictions))

    display_predictions(images, labels, predictions)


if __name__ == "__main__":
    app()
