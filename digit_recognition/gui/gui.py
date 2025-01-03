import matplotlib.pyplot as plt


class PredictionViewer:
    def __init__(self, images, labels, predictions):
        self.images = images
        self.labels = labels
        self.predictions = predictions
        self.current_index = 0

        self.fig, self.ax = plt.subplots()
        self.update_display()

        self.fig.canvas.mpl_connect("key_press_event", self.on_key_press)

    def update_display(self):
        self.ax.clear()
        img = self.images[self.current_index]
        true_label = self.labels[self.current_index]
        predicted_label = self.predictions[self.current_index]

        self.ax.imshow(img, cmap="gray")
        self.ax.set_title(f"True: {true_label}, Predicted: {predicted_label}")
        self.ax.axis("off")
        plt.draw()

    def on_key_press(self, event):
        if event.key == "right":
            self.current_index = (self.current_index + 1) % len(self.images)
            self.update_display()
        elif event.key == "left":
            self.current_index = (self.current_index - 1) % len(self.images)
            self.update_display()

    def show(self):
        plt.show()


def display_predictions(images, labels, predictions):
    viewer = PredictionViewer(images, labels, predictions)
    viewer.show()
