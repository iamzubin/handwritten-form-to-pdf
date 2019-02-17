import tensorflow as tf
from tensorflow import keras

from keras.models import load_model
from keras.datasets import mnist

(X_train, y_train), (X_test, y_test) = mnist.load_data()

X_test = X_test.reshape(10000, 784)
X_test = X_test.astype('float32')


mnist_model = load_model('./results/keras_mnist.h5')

mnist_model.summary()

loss_and_metrics = mnist_model.evaluate(X_test, y_test, verbose=2)

print("Test Loss", loss_and_metrics[0])
print("Test Accuracy", loss_and_metrics[1])
