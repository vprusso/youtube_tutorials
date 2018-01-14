# LucidProgramming -- Natural Language Processing in Python: Part 5

# Part 5 Blog Post: http://vprusso.github.io/blog/2018/natural-language-processing-python-5/
# Part 5 YouTube Video: https://www.youtube.com/watch?v=P2PMgnQSHYQ

# In this tutorial, we shall focus on **stemming** and
# **lemmatization**.

"""
Stemming
"""

# Let us first focus on the notion of stemming. According
# to Wikipedia: https://en.wikipedia.org/wiki/Stemming
# "Stemming is the process of reducing inflected (or sometimes
# derived) words to their word stem, base, or root form--generally
# a written word form."

# That definition is a bit hard to follow, so let us consider
# an example.

# Take the word "fishing". This word is based on the so-called
# stem, that is, the word "fish". Likewise, the stem of "fished",
# "fisher", etc. has the stem "fish".

# Writing your own function to determine the stem of a word is
# possible, although there are many potential edge cases. Many
# of these edge cases are automatically accounted for via the
# stemming tools provided by NLTK.

# Applications of Stemming:
# According to the previously mentioned Wikipeda article on
# stemming:
# "Stemming is used as an approximate method for grouping words
# with a similar basic meaning together. For example, a text
# mentioning "daffodils" is probably closely related to a
# text mentioning "daffodil" (without the "s"). But in some
# cases, words with the same stem have idiomatic meanings which
# are not closely related: a user searching for "marketing" will
# not be satisfied by most documents mentioning "markets" but
# not "marketing"".

# One well-known application of stemming is used when you search
# in Google. For instance, searching for the term "fish" will also

# yields results for the term "fishing" as well, since "fish" is
# the stem of "fishing" and is most likely related to the stem
# in this case.

# One of the stemming algorithms used via NLTK is the so-called
# **Porter Stemmer**:
# (http://www.cs.odu.edu/~jbollen/IR04/readings/readings5.pdf)
from nltk.stem import PorterStemmer

# Let us attempt to determine the stem for the following words in
# this word list:
porter = PorterStemmer()
word_list = ["connected", "connecting", "connection", "connections"]

for word in word_list:
    print(porter.stem(word))

# The Porter Stemmer identifies "connect" as the stem for
# each of the words in the list above.

# Let us take another example list of words:
word_list = ["argue", "argued", "argues", "arguing", "argus"]

for word in word_list:
    print(porter.stem(word))

# Note that the term "stem" and "root" are independent. The word
# "argue" is the root word of the above word list, but according
# to the definition of "stem", the term "argu" is the stem.

# NLTK also provides access to a number of other stemmer algorithms.

from nltk.stem import LancasterStemmer
from nltk.stem import SnowballStemmer

lancaster = LancasterStemmer()
snowball = SnowballStemmer(language='english')

# Using the Lancaster Stemmer on the "argue" word list:
for word in word_list:
    print(lancaster.stem(word))

# Using the Snowball Stemmer on the "argue" word list:
for word in word_list:
    print(snowball.stem(word))


# Notice that each stemming algorithm provides a different
# output. Delving into how each of these stemming algorithms
# work along with what the pros and cons of each are is beyond
# the scope of this video. However, if you would like a high level
# overview of when to use a particular stemming algorithm for your
# purposes, the following StackOverflow answer by Slater Tyranus
# provides a very well-written and concise summary of each:
# https://stackoverflow.com/questions/10554052/what-are-the-major-differences-and-benefits-of-porter-and-lancaster-stemming-alg/11210358

"""
Lemmatizing
"""

# According to Wikipedia, the definition of lemmatization is:
# https://en.wikipedia.org/wiki/Lemmatisation
# "The process of grouping together the inflected forms of
# a word so they can be analyzed as a single item, identified by
# the word's lemma, or dictionary form.

# Lemmatization and stemming are related, but different.
# The difference is that a stemmer operates on a single word
# *without* knowledge of the context, and therefore cannot
# discriminate between words which have different meaning
# depending on part of speech.

# Let us consider some examples of lemmatization and also
# of stemming to consider the contrast between the two ideas.

from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

# The `WordNetLemmatizer` class has a method called `lemmatize` which
# takes as arguments a word to lemmatize as well as what part of speech
# the word happens to be, i.e. noun, verb, adverb, etc.

# Let us attempt to determine the lemma for the word "bats":
print(lemmatizer.lemmatize("bats"))

# By default, the part of speech is noun (unless specified otherwise).
# Note that the lemmatizer is able to ascertain the lemma of the plural
# "bats" by the word "bat".

# Note that "bats" can be considered a noun, as in the plural for the
# type of animal for instance, but it may also be considered a verb,
# as in to "hit at" something.

# We can specify the part of speech to consider the word as by the optional
# `pos` argument, standing for "part-of-speech":
print(lemmatizer.lemmatize("bats", pos="v"))

# Let us now consider lemmatizing the word "better". In fact, let us lemmatize
# this word when the term better is an adjective, adverb, noun, and verb, 
# respectively.

# Adjective:
print(lemmatizer.lemmatize("better", pos="a"))

# Adverb:
print(lemmatizer.lemmatize("better", pos="r"))

# Noun:
print(lemmatizer.lemmatize("better", pos="n"))

# Verb:
print(lemmatizer.lemmatize("better", pos="v"))

# Notice that the lemmatization of "better" when considered to be a
# noun or verb stays as "better". Whereas when it is considered as
# an adjective it lemmatizes to "good" and when the part of speech
# is an adverb it lemmatizes to "well".

# If you consult Google's dictionary tool, you will notice this
# coincides with this categorization as well.





