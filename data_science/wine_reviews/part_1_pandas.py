# Video inspired from the kernel on Kaggle here:
# https://www.kaggle.com/residentmario/creating-reading-and-writing-reference

# The data for this video can be downloaded here:
# https://www.kaggle.com/zynicide/wine-reviews

# pip install pandas
import pandas as pd

"""
There are two core objects in pandas: 
the DataFrame and the Series.
"""

### DataFrame ###
"""
A DataFrame is a table. It contains an array of 
individual entries, each of which has a certain value. 
Each entry corresponds with a row (or record) and a column.

For example, consider the following simple DataFrame:
"""
print(pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]}))

"""
DataFrame entries are not limited to integers. For instance, 
here's a DataFrame whose values are str strings:
"""
print(pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']}))

"""
The dictionary-list constructor assigns values to the 
column labels, but just uses an ascending count from 0
(0, 1, 2, 3, ...) for the row labels. Sometimes this 
is OK, but oftentimes we will want to assign these 
labels ourselves.

The list of row labels used in a DataFrame is known as 
an Index. We can assign values to it by using an index 
parameter in our constructor:
"""
print(pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B']))

### Series ###

"""
A Series, by contrast, is a sequence of data values. 
If a DataFrame is a table, a Series is a list. And in 
fact you can create one with nothing more than a list:
"""
print(pd.Series([1, 2, 3, 4, 5]))

"""
A Series is, in essence, a single column of a DataFrame. 
So you can assign column values to the Series the same way
as before, using an index parameter. However, a Series do 
not have a column name, it only has one overall name:
"""
print(pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A'))


