# Iris Classification Model: Machine learning model that will allow us to 
# classify species of iris flowers. This application will introduce many
# rudimentary features and concepts of machine learning and is a good use case
# for these types of models.

# Use case: Botanist wants to determine the species of an iris flower based on
# characteristics of that flower. For instance attributes including petal 
# length, width, etc. are the "features" that determine the classification
# of a given iris flower.

# Import the iris dataset as provided by the sklearn Python module:
from sklearn.datasets import load_iris
iris = load_iris()

# Goal: Use k-nearest neighbors model to classify a given iris sample

# Algorithm finds the point in the training set closest to the new
# point corresponding to the new sample we are analyzing. It then
# assigns a label to this new point.

# We determine this by finding the k-closest neighbors to the given
# point and determine which predication has the majority class among
# the neightbors. We will start by considering one neighbor for now.

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

X_train, X_test, y_train, y_test = train_test_split(iris['data'], iris['target'], random_state=0)
knn = KNeighborsClassifier(n_neighbors=1)

knn.fit(X_train, y_train)

# Imagine that we obtained a new iris 
X_new = np.array([[5, 2.9, 1, 0.2]])
print(X_new.shape)

# We can use the predict function to use our model to offer a prediction as to
# what species our X_new corresponds to.
prediction = knn.predict(X_new)
print(prediction)

# We obtain an outcome of "0", which, if we consult the target names,
# this corresponds to the Setosa species.
print(iris['target_names'][prediction])

# Overall predication score for how likely our model was able to correctly
# predict the species of flower on the test set.
print(knn.score(X_test, y_test))



