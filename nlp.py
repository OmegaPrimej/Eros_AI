import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

class NLP:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))

    def tokenize(self, text):
        tokens = word_tokenize(text)
        tokens =
        return tokens

    def remove_stop_words(self, tokens):
        return
