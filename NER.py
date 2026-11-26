import spacy
nlp = spacy.load("en_core_web_sm")

text = """ Sundar Pichai is the CEO of Google.
He was born in Chennai and studied at Stanford University.
Google is headquartered in California."""

doc = nlp(text)

print("Named Entities: ")
for ent in doc.ents:
    print(ent.text, "-->", ent.label_ )