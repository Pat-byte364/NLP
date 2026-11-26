import pandas as pd
import re
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from gensim.models import Word2Vec          # pip install gensim

# 1. Load dataset
df = pd.read_csv("data.csv")
print("Shape:", df.shape)

# 2. Build one text "document" per car from the text columns
text_cols = ["Make", "Model", "Engine Fuel Type", "Transmission Type",
             "Driven_Wheels", "Vehicle Size", "Vehicle Style", "Market Category"]
df[text_cols] = df[text_cols].fillna("")
df["text"] = df[text_cols].agg(" ".join, axis=1)

# 3. Preprocess: lowercase, replace non-letters with a SPACE
def preprocess(t):
    t = t.lower()
    t = re.sub(r"[^a-z\s]", " ", t)
    return re.sub(r"\s+", " ", t).strip()

docs = df["text"].apply(preprocess).tolist()
print("Doc 0:", docs[0])

# 4. Bag of Words - count occurrence
cv = CountVectorizer()
bow = cv.fit_transform(docs)
vocab = cv.get_feature_names_out()
print("BoW shape:", bow.shape)
row = bow[0].toarray()[0]
print({vocab[i]: int(row[i]) for i in row.nonzero()[0]})

# 5. Bag of Words - normalized count
arr = bow.toarray()
normalized = arr / (arr.sum(axis=1, keepdims=True) + 1e-10)
print({vocab[i]: round(float(normalized[0][i]), 3) for i in normalized[0].nonzero()[0]})

# 6. TF-IDF
tv = TfidfVectorizer()
tfidf = tv.fit_transform(docs)
print("TF-IDF shape:", tfidf.shape)
r = tfidf[0].toarray()[0]
top = r.argsort()[::-1][:5]
print([(tv.get_feature_names_out()[i], round(float(r[i]), 3)) for i in top])

# 7. Word2Vec
sentences = [d.split() for d in docs]
model = Word2Vec(sentences, vector_size=50, window=5, min_count=2,
                 workers=1, epochs=20, seed=42)
print("Embedding of 'bmw':", model.wv["bmw"][:5], "size:", len(model.wv["bmw"]))
print("Similar to 'coupe':", model.wv.most_similar("coupe", topn=4))