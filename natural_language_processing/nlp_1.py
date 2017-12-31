import nltk

from nltk.text import Text

# Run this command to download all collections to be used for the NLP tutorials:
#nltk.download()

# Now that we've downloaded all the NLTK corpus content, let us go ahead and
# load in the text from Lewis Carroll's "Alice in Wonderland" via Gutenberg:
alice = Text(nltk.corpus.gutenberg.words('carroll-alice.txt'))

# NLTK also provides other texts from Gutenberg. We can view those by 
# running the following command:
print(nltk.corpus.gutenberg.fileids())

# There are many more text data sets provided by NLTK. For now, we will
# just focus on what types of analysis tools NLTK provides to us on the 
# text "Alice in Wonderland" by Lewis Carroll:

# Word Count: How many words are contained in "Alice in Wonderland"?
# Note that this includes punctuation as well as traditional words.
print(len(alice))

# Unique Word Count: How many unique words are present in 
# "Alice in Wonderland"? For instance, the above line would 
# count the word "the" on each occurrence. 
print(len(set(alice)))

# Concordance: Shows occurence of word in context of use.
# We can check where the term "alice" appears in "Alice in Wonderland".
alice.concordance("alice")

# Dispersion Plot: Location of where a word is in the text.
# Example:
#   Give a visual representation of where the words "Alice", "Rabbit",
#   "Hatter", and "Queen" appear in "Alice in Wonderland". 
alice.dispersion_plot(["Alice", "Rabbit", "Hatter", "Queen"])

# The word "Alice" is consistently used throughout the entire text, while 
# the word "Queen" is found closer to the end of the text. This makes sense,
# since Alice does not encounter the Red Queen until later in the book.


