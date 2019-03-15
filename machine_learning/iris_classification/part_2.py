# Iris Classification Model: Machine learning model that will allow us to
# classify species of iris flowers. This application will introduce many
# rudimentary features and concepts of machine learning and is a good use case
# for these types of models.

# Use case: Botanist wants to determine the species of an iris flower based on
# characteristics of that flower. For instance attributes including petal
# length, width, etc. are the "features" that determine the classification of a
# given iris flower.

# Will be used to generate plots:
import matplotlib.pyplot as plt

# Import the iris dataset as provided by the sklearn Python module:
from sklearn.datasets import load_iris
iris = load_iris()

# Store the features of the iris data set into a "features" variable.
features = iris.data.T

# For instance, the first index of the features object corresponds to
# all of the entries for the "sepal length (cm)":
print(features[0])
print(iris.feature_names[0])

# In a similar way, the second index of the features object corresponds
# to all of the entries for the "sepal width (cm)":
print(features[1])
print(iris.feature_names[1])

sepal_length = features[0]
sepal_width = features[1]
petal_length = features[2]

sepal_length_label = iris.feature_names[0]
sepal_width_label = iris.feature_names[1]
petal_length_label = iris.feature_names[2]

# Plot sepal length against sepal width:
plt.scatter(sepal_length, sepal_width, c=iris.target)
plt.xlabel(sepal_length_label)
plt.ylabel(sepal_width_label)

plt.show()

# Plot petal length against sepal width
plt.scatter(petal_length, sepal_width, c=iris.target)
plt.xlabel(petal_length_label)
plt.ylabel(sepal_width_label)

plt.show()
