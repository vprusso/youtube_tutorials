# LucidProgramming -- Natural Language Processing in Python: Part 1
# YouTube Video: https://www.youtube.com/watch?v=tP783g97C5o

# Prior to running this script, you will require Python to be installed on 
# your machine. If so, you may run the following command via pip:
#   pip install nltk
# Once installed, you should be able to follow along with the 
# remainder of this script. 

import nltk

# Run this command to download all collections to be used for the NLP tutorials:
nltk.download()

# Now that we've downloaded all the NLTK corpus content, let us go ahead and
# load in the text from Lewis Carroll's "Alice in Wonderland" via Gutenberg:
from nltk.text import Text
alice = Text(nltk.corpus.gutenberg.words('carroll-alice.txt'))

# NLTK also provides other texts from Gutenberg. We can view those by 
# running the following command:
print(nltk.corpus.gutenberg.fileids())

# There are many more text data sets provided by NLTK. For now, we will
# just focus on what types of analysis tools NLTK provides to us on the 
# text "Alice in Wonderland" by Lewis Carroll:

# Word Count: How many words are contained in "Alice in Wonderland"?
# Note that this includes punctuation as well as traditional words.
print(type(alice))
print(len(alice))

# Unique Word Count: How many unique words are present in 
# "Alice in Wonderland"? For instance, the above line would 
# count the word "the" on each occurrence. 
print(len(set(alice)))

# Specific Word Count: How many times does a specific word occur 
# in a text?
print(alice.count("Alice"))

# Concordance: Shows occurence of word in context of use.
# We can check where the term "alice" appears in "Alice in Wonderland".
alice.concordance("Alice")

# Dispersion Plot: Location of where a word is in the text.
# Example:
#   Give a visual representation of where the words "Alice", "Rabbit",
#   "Hatter", and "Queen" appear in "Alice in Wonderland". 
alice.dispersion_plot(["Alice", "Rabbit", "Hatter", "Queen"])

# The word "Alice" is consistently used throughout the entire text, while 
# the word "Queen" is found closer to the end of the text. This makes sense,
# since Alice does not encounter the Red Queen until later in the book.

# Frequency Distributions: What are the most frequent words (specifically,
# tokens), that are used in a given text.
# Example:
#   Generate the most frequent tokens in "Alice in Wonderland":

# First, use NLTK to generate a frequncy distribution dictionary-like object.
fdist = nltk.FreqDist(alice)

# What are the top 50 most common words in "Alice in Wonderland"?
fdist.plot(50, cumulative=True, title="50 most common tokens in Alice in Wonderland")

# Observe that the x-axis consists of punctuation, which may not 
# be precisely what we are going for. It is possible to remove this 
# from the words that we plot by filtering out the punctuation.
fdist_no_punc = nltk.FreqDist(
        dict((word, freq) for word, freq in fdist.items() if word.isalpha()))

fdist_no_punc.plot(50,
                   cumulative=True, 
                   title="50 most common tokens (no punctuation)")

# This plot gives us a bit more useful information, but it still contains an 
# awful lot of punctuation that we do not particularly care to see. In a 
# similar fashion, we may filter this out. 

# We may not obtain too much information on the above plot, since 
# many of the words on the x-axis are words like "and", "the", "in",
# etc. These types of common English words are referred to as 
# stopwords. NLTK provides a method to identify such words.
stopwords = nltk.corpus.stopwords.words('english')
fdist_no_punc_no_stopwords = nltk.FreqDist(
        dict((word, freq) for word, freq in fdist.items() if word not in stopwords and word.isalpha()))

# Replot fdist after stopwords filtered out. 
fdist_no_punc_no_stopwords.plot(50, 
                                cumulative=True, 
                                title="50 most common tokens (no stopwords or punctuation)")


