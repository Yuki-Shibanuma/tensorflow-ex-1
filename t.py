import numpy as np
import matplotlib.pyplot as plt

import tensorflow as tf
import keras

from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten
from keras.optimizers import SGD
import tensorflow_hub as hub


print("tensorflow.version:", tf.__version__)
print("keras.version", keras.__version__)

classifier_url = "https://tfhub.dev/google/tf2-preview/mobilenet_v2/classification/2"

IMAGE_SHAPE = (224, 224)
classifier = tf.keras.Sequential([
    hub.KerasLayer(classifier_url, input_shape=IMAGE_SHAPE+(3,))
])
