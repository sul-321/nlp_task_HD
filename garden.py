'''
Kind note to marker:
This is a resubmission. Original marks:
Completeness: 2 / 4
Efficiency: 4 / 4
Style: 4 / 4
Documentation: 4 / 4

To fix:
1. You have not provided the required observations and commentary
try to apply these concepts in a few sentences and give a short explanation.
2. Please be sure to add your program to the Dropbox folder as you have been doing all along

These have now been applied. Thank you kindly. 
'''


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


# Two unusual entities that spaCy identified were "old man" and "wound" in the
# first and fifth sentences, respectively. I did not expect spaCy to recognize
# these as entities because they are not proper nouns or named entities.
# However, spaCy was able to identify them as entities by using its contextual
# understanding of language and its knowledge of common nouns and verb phrases.
