import tensorflow as tf

from tensorflow import keras

import numpy as np
import matplotlib.pyplot as plt

fashion_mnist = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

#print(train_images.shape)
#print(len(train_images))

#print(train_labels)


#print(test_images.shape)

#plt.figure()
#plt.imshow(train_images[1])
#plt.colorbar()
#plt.grid(False)
#plt.show()

train_images = train_images / 255.0
test_images = test_images / 255.0

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(10, activation=tf.nn.softmax)
    ])

model.compile(optimizer="adam",
              loss="sparse_categorical_crossentropy",
              metrics=["accuracy"])

model.fit(train_images, train_labels, epochs=5)

#test_loss, test_acc = model.evaluate(test_images, test_labels)
#print(f"Test Accuracy: {test_acc}")

predictions = model.predict(test_images)

print(predictions[0])

print(np.argmax(predictions[0]))

print(test_labels[0])
