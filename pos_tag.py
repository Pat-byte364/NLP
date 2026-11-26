import nltk  # type: ignore
from nltk.tokenize import word_tokenize
from nltk import pos_tag

sentence = "The smart boy is reading an interesting book"
words = word_tokenize(sentence)
tags = pos_tag(words)

nouns = verbs = adjs = 0 
for word, tag in tags:
    if tag.startswith("NN"):
        nouns+= 1
    elif tag.startswith("VB"):
        verbs+= 1
    elif tag.startswith("JJ"):
        adjs += 1
print("Nouns: ", nouns)
print("Verb: ", verbs)
print("Adjectives: : ", adjs)