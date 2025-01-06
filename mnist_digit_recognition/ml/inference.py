import torch


def make_predictions(model, data_loader):
    images_list, labels_list, predictions = [], [], []

    model.eval()
    with torch.no_grad():
        for images, labels in data_loader:
            outputs = model(images)
            _, predicted = torch.max(outputs, dim=1)

            images_list.extend(images.cpu().numpy().squeeze())
            labels_list.extend(labels.tolist())
            predictions.extend(predicted.tolist())

    return images_list, labels_list, predictions


def get_mismatched_predictions(images, labels, predictions):
    mismatched = [
        (img, true, pred)
        for img, true, pred in zip(images, labels, predictions)
        if true != pred
    ]
    if mismatched:
        mismatched_images, mismatched_labels, mismatched_predictions = zip(*mismatched)
        return (
            list(mismatched_images),
            list(mismatched_labels),
            list(mismatched_predictions),
        )
    return [], [], []
