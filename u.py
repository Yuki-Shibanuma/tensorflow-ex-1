import tensorflow as tf
from tensorflow import keras

model = keras.models.load_model("model.h5")

fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

predictions = model.predict(test_images)
print(predictions[0])
