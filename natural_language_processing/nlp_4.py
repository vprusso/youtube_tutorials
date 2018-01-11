# LucidProgramming -- Natural Language Processing in Python: Part 4

# Part 4 Blog Post: http://vprusso.github.io/blog/2018/natural-language-processing-python-4/
# Part 4 YouTube Video:  

"""
NLTK and WordNet
"""

# In this tutorial, we shall briefly go over the WordNet resource. NLTK
# provides direct access to this resource, and we shall import that here:
from nltk.corpus import wordnet as wn

# According to Wikipedia: https://en.wikipedia.org/wiki/WordNet
# "WordNet is a lexical database for the English language. It groups English
# words into sets of synonyms called **synsets**, which provide short
# definitions and usage examples and records a number of relations among
# these synonym sets or their members."

# WordNet is quite an extensive resource for NLP, and the fact that NLTK
# provides direct access to this resources is convenient. The official site
# for WordNet is provided here: https://wordnet.princeton.edu

# One primary use for WordNet is to determine the similarity between words.
# Take for example the following two sentences:
# 1. I learned natural language processing by resources found on the internet.
# 2. I learned natural language processing by resources found on the net.

# Both sentence 1. and 2. are the same, with the exception of the last word. 
# The words "internet" and "net" are synoynms, so the meaning of each sentence 
# is the same irrespective of whether "internet" or "net" is used at the end.

# We can use the wordnet module to determine the synsets (synonym sets) of 
# the word internet:
print(wn.synsets('internet'))

# The entry 'internet.n.01' is a synset for the word internet. 
# Each synonym in the set is referred to as a **lemma**. 
# We can print out the list of such synsets and their corresponding 
# lemmas.(Specifically, the pairing of a synset with a word is called a lemma):
print(wn.synset('internet.n.01').lemma_names())

# According to WordNet, the word "internet" is a synonym of the word "net" and 
# the word "cyberspace".

# For each synset, we can print out the definition as well as an example of 
# usage in a sentence for the given word:

# Definition of synset:
print(wn.synset('internet.n.01').definition())

# Example usage of synset:
print(wn.synset('internet.n.01').examples())

# As we can see, not all synsets have valid examples as we obtain the 
# empty list. However, for a word like "car" we can take a look at 
# the synsets:
print(wn.synsets('car'))

# Example usage of synset for "car":
print(wn.synset('car.n.01').examples())

# One may obtain the lemmas for a given synset as follows:
print(wn.synset('internet.n.01').lemmas())

# For a given lemma, we can also get the synsets corresponding 
# to that lemma.
print(wn.lemma('internet.n.01.net').synset())

"""
A Few More NLP Terms:
"""

# Hyponym: "a word of more specific meaning than a general or superordinate 
# term applicable to it. For example, spoon is a hyponym of cutlery."

# Let us explore this concept with the term "cat":

# First obtain the synsets for the term "cat":
print(wn.synsets('cat'))

# There are a few different synsets for this word. 
# Let us take a look at what the definition of 
# the synset 'cat.n.01' is:
print(wn.synset('cat.n.01').definition())

# It looks like that definition refers to the feline 
# variety of the term cat. Note that the second synset 
# is 'guy.n.01', as in someone who is a "cool cat". Let 
# us stick with the feline variety.

# Let us determine the hyponyms of the term "cat", and 
# store that into a variable `types_of_cats`.
cat = wn.synset('cat.n.01')
types_of_cats = cat.hyponyms()

# Now, let us loop through the hyponyms and see the 
# lemmas for each synset:
for synset in types_of_cats:
    for lemma in synset.lemmas():
        print(lemma.name())

# Note that terms like "domestic_cat" and "house_cat" are 
# more specific terms with respect to the term "cat", that is,
# they are hyponyms of the word "cat". 

# Hypernym: "a word with a broad meaning that more specific words fall
# under; a superordinate. For example, color is a hypernym of red. 

# A hyponym drills down to more specificity, while a hypernym goes 
# upward toward more generality.

# Example:
#   Cat <- Hypernym 
#       house_cat <- hyponym
print(wn.synset('house_cat.n.01').hypernyms())

# One way in which one may ascribe similarity between two different words 
# is to assign a score based on the distance in terms of hypernyms and 
# hyponyms.

"""
How Related are Two Words?
"""

# Let us take the terms we have learned thus far along with what WordNet 
# provides to us to define some metric as to how two words are related 
# to one another. 

# The `path_similarity` function returns a score denoting how similar two
# word senses are. The "path" in this case can be thought of as the distance 
# in terms of hypernyms/hyponyms, 
