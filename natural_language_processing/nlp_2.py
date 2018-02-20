# LucidProgramming -- Natural Language Processing in Python: Part 2

# Part 2 Blog Post: http://vprusso.github.io/blog/2018/natural-language-processing-python-2/ 
# Part 2 YouTube Video: https://www.youtube.com/watch?v=n3_mZ47ZVxA 

# Start off my importing the NLTK module.
import nltk

# Refer to Part 1 where this syntax is explained in greater detail. 
# We will continue to use Lewis Carroll's "Alice in Wonderland" as 
# our primary exploratory text for NLP.
from nltk.text import Text
alice = Text(nltk.corpus.gutenberg.words('carroll-alice.txt'))
fdist = nltk.FreqDist(alice)

################################################################################
# We shall pepper in a few NLP terms from time to time to reduce the 
# overwhelm of encountering too many new terms all at once. 

# Hapaxes: Words that occur exactly once in the text. 
# https://en.wikipedia.org/wiki/Hapax_legomenon
print(fdist.hapaxes())

# Collocations: A pair or group of words that are habitually juxtaposed. 
# https://en.wikipedia.org/wiki/Collocation
# A general example may be "red wine". In the context of "Alice in Wonderland", 
# a more specific example may be something like "Red Queen" or "White Rabbit". 
print(alice.collocations())

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
print(alice_words)

# Get characters from "Alice in Wonderland":
alice_chars = nltk.corpus.gutenberg.raw('carroll-alice.txt')
print(alice_chars)

# Get sentences from "Alice in Wonderland": 
alice_sents = nltk.corpus.gutenberg.sents('carroll-alice.txt')
print(alice_sents)

# With the above chars, words, and sentences extracted from "Alice in Wonderland", 
# we can make use of these to calculate some cursory information on the text:

# Average word length:
print(int(len(alice_chars) / len(alice_words)))

# Average sentence length:
print(int(len(alice_words) / len(alice_sents)))

# Let us turn the above two metrics into functions, and determine the average 
# word length and sentence length of all the texts in the Gutenberg collection. 


def avg_word_len(num_chars, num_words):
    return int(num_chars/num_words)


def avg_sent_len(num_words, num_sents):
    return int(num_words/num_sents)

for file_id in nltk.corpus.gutenberg.fileids():
    num_chars = len(nltk.corpus.gutenberg.raw(file_id))
    num_words = len(nltk.corpus.gutenberg.words(file_id))
    num_sents = len(nltk.corpus.gutenberg.sents(file_id))

    print(file_id + 
          " has an average word length of " + 
          str(avg_word_len(num_chars, num_words)) + 
          " and an average sentence length of " + 
          str(avg_sent_len(num_words, num_sents)))

# Sentence length tends to vary, while word length among all of these texts 
# is consistent.

# Note that the gutenberg fileids only have a small subset of text compared
# to the large amount of content found on Project Gutenberg.  

# If you wish to process a text from Project Gutenberg accessed via the web, 
# one may use the urllib module to import via the internet. 
from urllib.request import urlopen 

# This URL corresponds to "The Picture of Dorian Grey" by Oscar Wilde.
url = "https://www.gutenberg.org/cache/epub/174/pg174.txt" 
raw = urlopen(url).read().decode('utf-8')

# Once the raw content has been extracted, we convert this content to something 
# that NLTK can understand and process. This should look somewhat familiar if 
# you have consulted Part 1 of this tutorial. 
dorian_grey = nltk.Text(nltk.word_tokenize(raw))

# Once the text has been converted to an NLTK Text object, we can process it 
# just like we have been doing previously. For example, here we convert the 
# text object to a frequency distribution and calculate the hapaxes. 
fdist_dorian = nltk.FreqDist(dorian_grey)
print(fdist_dorian.hapaxes())

# The above approach is not limited to text from Project Gutenberg, but is 
# broadly applicable to any text that can be obtained from a direct URL.

# Let us consider another text resource that NLTK allows us to process. One of 
# them is various web and chat data. The first one we shall focus on his 
# web text. 

# We can print out the file ids of the webtext collection to see what is provided:
for file_id in nltk.corpus.webtext.fileids():
    print(file_id) 

# We see a list of text files. For more information on the content of each of these 
# file, you can consult:
# https://github.com/teropa/nlp/tree/master/resources/corpora/webtext

# Very briefly:
# firefox.txt: Firefox support forum.
# grail.txt: Movie script from "Monty Python and the Holy Grail".
# overheard.txt: Overheard conversation in New York.
# pirates.txt: Movie script from Pirates of the Caribean.
# singles.txt: Singles ad. 
# wine.txt: "Fine Wine Diary" reviews.

# Observe that many of the ways in which we access and processed text from 
# gutenberg carry over into processing the webtext data. This is a common
# theme for all of the text resources provided by NLTK, and makes it easier
# to apply functionality for one text resource to another in a general fashion.
num_grail_words = len(nltk.corpus.webtext.words('grail.txt'))
num_grail_chars = len(nltk.corpus.webtext.raw('grail.txt'))
num_grail_sents = len(nltk.corpus.webtext.sents('grail.txt'))

print(avg_word_len(num_grail_chars, num_grail_words))
print(avg_sent_len(num_grail_words, num_grail_sents))

# Inaugural Address Corpus:

# This is a collection of presidential inaugural addresses; the speech that the 
# president makes prior to officially starting their term in office. 

# Let us print out the files provided to us via the inaugural corpus:
for file_id in nltk.corpus.inaugural.fileids():
    print(file_id) 

# Each file consists of the format: X-Y, where X is the four digit year, and 
# Y is the last name of the president giving the inaugural address. 

# Let us loop through each address. While doing so, let us keep a running tally 
# of the number of times the word "America" is used in each address.

# Loop through each inaugural address:
for fileid in nltk.corpus.inaugural.fileids():
    america_count = 0 
    # Loop through all words in current inaugural address:
    for w in nltk.corpus.inaugural.words(fileid):
        # We convert the word to lowercase before checking 
        # This makes checking for the occurrence more consistent.
        # Note that the "startswith" function also catches words like 
        # "American", "Americans", etc.
        if w.lower().startswith('america'):
            america_count += 1
    # Output both the inaugural address name and count for America:
    president = fileid[5:-4]
    year = fileid[:4]
    print("President " + president + 
          " of year " + year + 
          " said America " + str(america_count) + " times. ")

# Say I also want to see how many times the word "citizen" is present in
# each of the inaugural addresses. It may be preferable to consider a plot
# output as opposed to one that simply outputs to terminal.

# Let us consider a conditional frequency distribution, that is a frequency
# distribution that is a collection of frequency distributions run under
# different conditions.

# Recall the FreqDist function took a list as input. NLTK provides a 
# ConditionalFreqDist function as well which takes a list of pairs. 
# Each pair has the form (condition, event). 

# In our example, we care about the case when either the word "America"
# or "citizen" is used in each of the inaugural addresses. In other words, 
# encountering the phrase "America" or "citizen" are the conditions we 
# care about, and the events are one for each year of the inaugural address. 

cfd = nltk.ConditionalFreqDist(
            (target, fileid[:4])
            for fileid in nltk.corpus.inaugural.fileids() 
            for w in nltk.corpus.inaugural.words(fileid)
            for target in ['america', 'citizen']
            if w.lower().startswith(target))
cfd.plot()


