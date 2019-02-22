# Iris Classification Model: Machine learning model that will
# allow us to classify species of iris flowers. This application
# will introduce many rudimentary features and concepts of machine
# learning and is a good use case for these types of models.

# Use case: Botanist wants to determine the species of an
# iris flower based on characteristics of that flower. For
# instance attributes including petal length, width, etc.
# are the "features" that determine the classification
# of a given iris flower. 

# Import the iris dataset as provided by the sklearn
# Python module:
from sklearn.datasets import load_iris
iris = load_iris()

# Iris object returned is a 'Bunch' object. This is similar to a 
# Python dictionary as it cntains keys and values:
# print(iris.keys())

# Value of DESCR is a description of the dataset.
# Here are the first few values of the description
print(iris['DESCR'][:200] + "\n...")

# The value with key "target_names" consists of an
# array of strings with species that we intent to predict.
iris['target_names']

