import torch


def make_predictions(model, data_loader):
    predictions = []
    labels_list = []
    images_list = []

    model.eval()
    with torch.no_grad():
        for images, labels in data_loader:
            outputs = model(images)
            _, predicted = torch.max(outputs.data, 1)
            for i in range(len(images)):
                img = images[i].cpu().numpy().squeeze()
                images_list.append(img)
                labels_list.append(labels[i].item())
                predictions.append(predicted[i].item())

    return images_list, labels_list, predictions
