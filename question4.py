import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

nltk.download('wordnet')
nltk.download('punkt')
nltk.download('punkt_tab')

text = input("Enter sentence: ")
lem = WordNetLemmatizer()

for word in word_tokenize(text):
    print(word, "->", lem.lemmatize(word))