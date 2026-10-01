import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

text = input("Enter sentence: ")
words = word_tokenize(text)

print(nltk.pos_tag(words))