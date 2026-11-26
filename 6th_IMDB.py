import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from gensim.models import Word2Vec          # pip install gensim

df = pd.read_csv("IMDB Dataset.csv")        # Kaggle: IMDB Dataset of 50K Movie Reviews
reviews = (df["review"].head(1000).str.lower()
           .str.replace(r"[^a-z\s]", "", regex=True))

cv = CountVectorizer(max_features=2000)
bow = cv.fit_transform(reviews)
print(cv.get_feature_names_out()[:20])
print(bow.toarray()[:5, :20])

arr = bow.toarray()
normalized = arr / (arr.sum(axis=1, keepdims=True) + 1e-10)   # 1e-10 avoids divide-by-zero
print(normalized[:5, :20].round(3))

tfidf = TfidfVectorizer(max_features=2000).fit_transform(reviews)
print(tfidf[:5, :20].toarray().round(3))

sentences = [r.split() for r in reviews]
model = Word2Vec(sentences, vector_size=100, window=5, min_count=2, workers=1)
print(model.wv["movie"][:10])
print(model.wv.most_similar("movie", topn=5))