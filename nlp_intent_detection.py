.Here's the `nlp_intent_detection.py` script:

```python
import spacy

nlp = spacy.load("en_core_web_sm")

def detect_intent(text):
    doc = nlp(text)
    intent = ""
    for token in doc:
        if token.text.lower() == "book":
            intent = "booking"
        elif token.text.lower() == "cancel":
            intent = "cancellation"
    return intent

text = input("Enter your query: ")
print(detect_intent(text))
