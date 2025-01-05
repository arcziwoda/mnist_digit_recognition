# MNIST Digit Recognition with PyTorch

This project is a simple application for recognizing handwritten digits using the MNIST dataset. It was developed as a learning exercise to explore PyTorch, focusing on implementing a basic neural network for classification tasks.

The application trains a model, evaluates its performance using standard metrics, and includes a graphical interface for visualizing predictions.

## Features

- **Training**: A fully connected neural network is trained on the MNIST dataset.
- **Evaluation**: Standard metrics like accuracy, precision, recall, and F1-score are calculated.
- **Visualization**: An interactive GUI allows users to navigate through predictions, displaying true labels and model predictions.

## Requirements

Ensure you have the following installed:

- Python 3.11
- Make (for `Makefile` automation)
- Poetry

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/arcziwoda/mnist_digit_recognition.git
   cd mnist_digit_recognition
   ```

2. Use the provided `Makefile` to install dependencies and set up the environment:

   ```bash
   make install
   ```

## Usage

To run the application, simply execute the following command:

```bash
make run
```

## Metrics

The application calculates the following metrics:

- **Accuracy**
- **Precision**
- **Recall**
- **F1-score**
- **Number of correctly and incorrectly classified images**

## File Structure

```
number_recognition/
│
├── app.py                 # Entry point for the application
├── ml/                    # Core ML logic
│   ├── data_loader.py     # Data loading functions
│   ├── inference.py       # Inference logic
│   ├── metrics.py         # Metric calculations
│   ├── model.py           # Neural network definition
│   └── train.py           # Training logic
└── gui/
    └── gui.py             # GUI for visualizing predictions
```

## Why This Project?

This project was developed as a first encounter with PyTorch, offering an opportunity to:

- Learn PyTorch basics.
- Implement a simple machine learning pipeline from data loading to model evaluation.
- Explore interactive visualizations for model predictions.
