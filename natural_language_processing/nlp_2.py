# LucidProgramming -- Natural Language Processing in Python: Part 2

# Part 1 Blog Post: http://vprusso.github.io/blog/2018/natural-language-processing-python-1/ 
# Part 1 YouTube Video: https://www.youtube.com/watch?v=tP783g97C5o 

# Start off my importing the NLTK module.
import nltk

# Refer to Part 1 where this syntax is explained in greater detail. 
# We will continue to use Lewis Carroll's "Alice in Wonderland" as 
# our primary exploratory text for NLP.
alice = nltk.corpus.gutenberg.words('carroll-alice.txt')
fdist = nltk.FreqDist(alice)

################################################################################
# We shall pepper in a few NLP terms from time to time to reduce the 
# overwhelm of encountering too many new terms all at once. 

# Hapaxes: Words that occur exactly once in the text. 
# https://en.wikipedia.org/wiki/Hapax_legomenon
#print(fdist.hapaxes())

# Collocations: A pair or group of words that are habitually juxtaposed. 
# https://en.wikipedia.org/wiki/Collocation
# A general example may be "red wine". In the context of "Alice in Wonderland", 
# a more specific example may be something like "Red Queen" or "White Rabbit". 
#print(alice.collocations())

# Bigrams: A pair of consecutive written units (i.e. letters, syllables, or words).
# https://en.wikipedia.org/wiki/Bigram
# XXX
################################################################################

# Recall in Part 1, we ran the following command:
# nltk.download()
# This command was responsible for downloading various collections of text that 
# we can use to run various NLP functions on. Thus far, we have made use of the 
# Gutenberg collection of text to read in "Alice in Wonderland".

# There are a few more things to note about how one may access the Gutenberg data. 

# Get words from text (what we did in Part 1):
alice_words = nltk.corpus.gutenberg.words('carroll-alice.txt')
# Note that Python does not print out the entire list or words. The ellipsis 
# (...) sequence denotes that there is more content that is supressed from output.
#print(alice_words)

# Get characters from "Alice in Wonderland":
alice_chars = nltk.corpus.gutenberg.raw('carroll-alice.txt')
#print(alice_chars)

# Get sentences from "Alice in Wonderland": 
alice_sents = nltk.corpus.gutenberg.sents('carroll-alice.txt')
#print(alice_sents)

# With the above chars, words, and sentences extracted from "Alice in Wonderland", 
# we can make use of these to calculate some cursory information on the text:

# Average word length:
#print(int(len(alice_chars) / len(alice_words)))

# Average sentence length:
#print(int(len(alice_words) / len(alice_sents)))

# Let us turn the above two metrics into functions, and determine the average 
# word length and sentence length of all the texts in the Gutenberg collection. 

def avg_word_len(num_chars, num_words):
    return int(num_chars/num_words)

def avg_sent_len(num_words, num_sents):
    return int(num_words/num_sents)

#for txt in nltk.corpus.gutenberg.fileids():
#    num_chars = len(nltk.corpus.gutenberg.raw(txt))
#    num_words = len(nltk.corpus.gutenberg.words(txt))
#    num_sents = len(nltk.corpus.gutenberg.sents(txt))
#
#    print(txt + 
#          " has an average word length of " + 
#          str(avg_word_len(num_chars, num_words)) + 
#          " and an average sentence length of " + 
#          str(avg_sent_len(num_words, num_sents)))

# Sentence length tends to vary, while word length among all of these texts 
# is consistent.

# Note that the gutenberg fileids only have a small subset of text compared
# to the large amount of content found on Project Gutenberg.  

# If you wish to process a text from Project Gutenberg accessed via the web, 
# one may use the urllib module to import via the internet. 
#from urllib.request import urlopen 

# This URL corresponds to "The Picture of Dorian Grey" by Oscar Wilde.
#url = "https://www.gutenberg.org/cache/epub/174/pg174.txt" 
#raw = urlopen(url).read().decode('utf-8')

# Once the raw content has been extracted, we convert this content to something 
# that NLTK can understand and process. This should look somewhat familiar if 
# you have consulted Part 1 of this tutorial. 
#dorian_grey = nltk.Text(nltk.word_tokenize(raw))

# Once the text has been converted to an NLTK Text object, we can process it 
# just like we have been doing previously. For example, here we convert the 
# text object to a frequency distribution and calculate the hapaxes. 
#fdist_dorian = nltk.FreqDist(dorian_grey)
#print(fdist_dorian.hapaxes())

# The above approach is not limited to text from Project Gutenberg, but is 
# broadly applicable to any text that can be obtained from a direct URL.

# Let us consider other text resource that NLTK allows us to process. 



# Accessing Text in Chapter 2 and part of Chapter 3 (TODO)
