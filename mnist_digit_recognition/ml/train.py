import torch.nn as nn
import torch.optim as optim


def train_model(model, data_loader, epochs=5):
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    print("Running training...")
    for epoch in range(epochs):
        model.train()
        running_loss = 0.0
        for images, labels in data_loader:
            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            running_loss += loss.item()

        print(f"Epoch {epoch+1}, loss: {running_loss/len(data_loader)}")

    return model
