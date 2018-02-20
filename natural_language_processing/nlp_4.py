# LucidProgramming -- Natural Language Processing in Python: Part 4

# Part 4 Blog Post: http://vprusso.github.io/blog/2018/natural-language-processing-python-4/
# Part 4 YouTube Video: https://www.youtube.com/watch?v=byx3LDFiEZE

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
#   Cat <- hypernym
#       house_cat <- hyponym
print(wn.synset('house_cat.n.01').hypernyms())

# One way in which one may ascribe similarity between two different words
# is to assign a score based on the distance in terms of hypernyms and
# hyponyms. That is, how many levels up or down is a given word from
# the other we are attempting to compare it to.

"""
How Related are Two Words?
"""

# Let us take the terms we have learned thus far along with what WordNet
# provides to us to define some metric as to how two words are related
# to one another.

# There are a few ways in which to calculate the similarities between
# words.

# The `path_similarity` function returns a score denoting how similar two
# words are in terms of the distance between hypernyms/hyponyms.

# Let us calculate this metric of similarity between words
# "car" and "automobile".

# First, define the synsets for these terms:
car = wn.synset('car.n.01')
automobile = wn.synset('automobile.n.01')

# Now, call the `path_similarity` function. This function returns a score
# between 0 and 1, where 0 is no similarity between the hypernym/hyponym
# tree and a distance of 1 is the node which houses both of the words
# in terms of hypernyms/hyponyms is identical.
print(car.path_similarity(automobile))

# We see that "car" and "automobile" have the highest similarity possible,
# with a score of 1.0.

# This makes sense, since if we print out the synsets of "car", we see that
# one of the synonyms is indeed "automobile".

# Let us now take a look at the term "car" and "boat":
boat = wn.synset('boat.n.01')
print(car.path_similarity(boat))

# We see a lower number here. This again makes sense, since the traversal
# with respect to hypernyms/hyponyms from car to boat is certainly at least
# below 1.0.

# There are actually many more ways in which to define distances between words.
# 1. Wu-Palmer Similarity
# 2. Resnik Similarity
# 3. Jiang-Conrath Similarity
# 4. Lin Similarity

# These methods of similarity are all based on different metrics of what one
# uses to define similarity between two different words. Going over each of
# these methods in detail would go beyond the scope of this tutorial, but
# let us look at the Wu-Palmber similarity metric.

# The numerics obtained from this method may appear to be more intuitively
# pleasing than the `path_similarity` method.

# Let us attempt to use this metric to in the same way that we did for
# the `path_similarity` function.
print(car.wup_similarity(automobile))

# Okay, again for "car" and "automobile" we see a value of 1.0, that is
# the highest value of similarity correlation under this metric.

# Let us now attempt this metric with "car" and "boat":
print(car.wup_similarity(boat))

# This higher value is a bit more intuitively correct, as a boat and
# car are both modes of transport, yet they are also different enough
# to warrant a lower value. Let us continue with something even more
# seemingly unrelated to a car.
cat = wn.synset('cat.n.01')
print(car.wup_similarity(cat))

# We see an even lower number here, as one may expect between the terms 
# "car" and "cat" under this metric of word similarity. 
