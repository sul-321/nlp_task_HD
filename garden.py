import spacy

nlp = spacy.load("en_core_web_sm")

gardenpath_sentences = [
    "The old man the boat.",
    "The horse raced past the barn fell.",
    "The man who hunts ducks out on weekends.",
    "The cotton clothing is made of grows in Mississippi.",
    "The bandage was wound around the wound."
]

for sentence in gardenpath_sentences:
    doc = nlp(sentence)
    print("Sentence:", sentence)
    print("Tokens:", [token.text for token in doc])
    print("Entities:", [(ent.text, ent.label_) for ent in doc.ents])
    print()
