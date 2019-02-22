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

# Goal: Built machine learning model from the iris
# data set that can predict the species of a new
# set of measurements.

# In order to determine how well our model performs,
# we need to run it on data it has not seen before, `
# that is, we need to run it on a new set of measurements
# and see where our model categorizes this new item.

# To do this, we can split our data up into two sets;
# a training and testing set. The training set will be
# what our model uses to learn, and the test set will be
# the remaining set that assesses whether the model is 
# able to accurately predict the outcome of the measurements
# from this set.

# We will be using a 75/25 split for train/test respectively.
# That is, we will be training our model on 75% of our data,
# and then testing on the remaining 25%. What split percentage
# you use is up to you, but a 75/25 split is a reasonable rule
# to use as a starting point.

# Split our dataset into training and testing sets.


