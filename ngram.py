import nltk
from collections import Counter
from nltk.util import ngrams

text = "I love Natural Language Processing and I love Machine Learning"
words = text.lower().split()
n = int(input("Enter N: "))

grams = list(ngrams(words, n))
counts = Counter(grams)

print("N-grams: ", grams)
print("Frequency: ", counts)

if n == 2:
    wc = Counter(words)
    for(w1, w2), C in counts.items():
        print(f"p({w1} {w2}) = {C / wc[w1]:.2f}")

seq = "I love Machine Learning"

P = 1

for a,b in zip(seq, seq[1:]):
    P *= counts[(a,b)] / wc[a]

print("P seq: ", P)