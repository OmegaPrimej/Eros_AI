import spacy
nlp = spacy.load("en_core_web_sm")
text = input("Enter your text: ")
doc = nlp(text)
print("Tokens:",)
print("Entities:",)
