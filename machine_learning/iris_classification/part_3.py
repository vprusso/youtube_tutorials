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
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1)



