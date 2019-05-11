from __future__ import absolute_import, division, print_function

import pathlib

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

#print(tf.__version__)

dataset_path = keras.utils.get_file("auto-mpg.data", 
                                    "https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data")

column_names = ['MPG','Cylinders','Displacement','Horsepower','Weight',
                'Acceleration', 'Model Year', 'Origin']

raw_dataset = pd.read_csv(dataset_path,
                          names=column_names,
                          na_values="?",
                          comment="\t",
                          sep=" ",
                          skipinitialspace=True)

dataset = raw_dataset.copy()
print(dataset.tail())

