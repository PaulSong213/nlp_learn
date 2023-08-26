import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")

with open("data/wiki_us.txt", "r") as f:
    text = f.read()

doc = nlp(text)

sentence1 = list(doc.sents)[0]

token2 = sentence1[3]

# for ent in doc.ents:
#     print(ent.text, ent.label_)

displacy.render(doc, style="ent", jupyter=True)
