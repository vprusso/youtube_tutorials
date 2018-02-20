# LucidProgramming -- Natural Language Processing in Python: Part 3

# Part 3 Blog Post: http://vprusso.github.io/blog/2018/natural-language-processing-python-3/
# Part 3 YouTube Video: https://www.youtube.com/watch?v=0Rc3452U6b8

# Start off by importing the NLTK module.
import nltk

# In this tutorial, we shall take a break from the core natural language processing
# content, and do something primarily just for kicks.

# We shall make use of what we have learned thus far in NLTK to generate a
# *word cloud* (also known as *tag cloud*). This is a fun and interesting
# way in which to visually represent how prominent certain words are in
# a text resource.

# In order to follow along with this tutorial, you will require the
# Python modules "matplotlib" and "wordcloud" Both of these can be
# installed on your machine by navigating to a terminal and typing:
#    pip install wordcloud
#    pip install matplotlib
# More information on these packages can be found at the following
# respective links:
# https://amueller.github.io/word_cloud/
# https://matplotlib.org/

# Let us start off by importing the modules we just installed:
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Next, let us generate a really basic and simple word cloud, based
# on just a single Python string.
text = "all your base are belong to us"

# Generating a word cloud with no optional parameters based on the
# above string:
basecloud = WordCloud().generate(text)

# Finally, use matplotlib to render the word cloud:
plt.imshow(basecloud)
plt.axis("off")
plt.show()


# Since we will be using these three lines quite frequently, let
# us wrap them in a function for easier access.
def plot_wordcloud(wordcloud):
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()


# You will notice that the words "base", "us" and "belong" are
# present in the word cloud, but the remaining words of "your",
# "are", "to", and "all" are absent.

# This is because the wordcloud module ignores stopwords by
# default. Refer to Part 1 of the NLTK tutorial if the concept
# of stopwords is new to you.

# If we wish, we can specify our own set of stopwords, instead
# of the stopwords provided by default.
wordcloud = WordCloud(stopwords={'to', 'of'}).generate(text)
plot_wordcloud(wordcloud)

# Another optional parameter for WordCloud is that of
# relative_scaling, which corresponds to how the size of the
# text in the word cloud scales based on the content.

# With `relative_scaling=0`, only the ranks of the words are
# considered. If we alter this to `relative_scaling=1.0`, then
# a word that appears twice as frequently will appear twice the
# size. By default, `relative_scaling=0.5`.

# Add in a few more occurrences of the word "base" to illustrate
# the effect of relative scaling.
text_base = "all your base are belong to us base base base base"
wordcloud = WordCloud(relative_scaling=1.0,
                      stopwords={'to', 'of'}).generate(text_base)
plot_wordcloud(wordcloud)

# Note that the word "base" in the world cloud is relatively much
# larger than the other words.

# Recall from Part 2 of this series where we accessed the Inaugural
# Address corpus provided by NLTK.

# Let us read in the raw content of the 1789 inaugural address of
# Washington and the 2009 address of Obama.
washington = nltk.corpus.inaugural.raw('1789-Washington.txt')
obama = nltk.corpus.inaugural.raw('2009-Obama.txt')

# Word cloud for Washington:
wordcloud = WordCloud(relative_scaling=1.0).generate(washington)
plot_wordcloud(wordcloud)


# By default, if the WordCloud function is not provided a dictionary of stopwords,
# the WordCloud function will use the ones provided by default. This is okay, but 
# perhaps we notice in the word cloud generated above that words such as "every" 
# and "will" are present, but are not particularly useful in extracting information 
# into what makes Washington's address more unique over others. 

# What we can do then is to add in the words "every" and "will" into the set of 
# stopwords that the WordCloud function considers. 

from wordcloud import STOPWORDS
stopwords = set(STOPWORDS)
stopwords.add("every")
stopwords.add("will")
wordcloud = WordCloud(stopwords=stopwords, relative_scaling=1.0).generate(washington)
plot_wordcloud(wordcloud)

# Word cloud for Obama:
wordcloud = WordCloud(relative_scaling=1.0).generate(obama)
plot_wordcloud(wordcloud)

# For this next example, you will need two other Python modules installed,
# if you do not already have it:
#     pip install PIL
#     pip install numpy
# The PIL module is used primarily for image processing. We will use it in
# the following example (inspired by:
# https://amueller.github.io/word_cloud/auto_examples/a_new_hope.html#sphx-glr-auto-examples-a-new-hope-py)

import numpy as np
from PIL import Image
from os import path

import nltk
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Read in the George Washington image as a numpy array. The image is from:
# http://weclipart.com/george+washington+silhouette+clip+art/d/6952286
img = Image.open(path.join(path.dirname(__file__), 
                           "supplementary_files", 
                           "washington.jpg"))
mask = np.array(img)

text = nltk.corpus.inaugural.raw('1789-Washington.txt')

wc = WordCloud(max_words=1000, mask=mask).generate(text)

wc.to_file("washington_word_cloud.png")
plt.imshow(wc)
plt.axis("off")
plt.show()
