import nltk 
nltk.download("wordnet")
nltk.download("omw-1.4")
from nltk.corpus import wordnet as wn

word = input("Enter word: ")
syn, ant, hyper, hypo = set(), set(), set(), set()

for s in wn.synsets(word):
    hyper.update(h.name() for h in s.hypernyms())
    hypo.update(h.name() for h in s.hyponyms())
    for l in s.lemmas():
        syn.add(l.name())
        for a in l.antonyms():
            ant.add(a.name())

print("Synoyms: ", syn)
print("Antonyms: ", ant if ant else "No antonym found")
print("Hypernyms: ", hyper)
print("Hyponyms: ", hypo)