from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()
text = input("Enter sentence: ")

for word in word_tokenize(text):
    print(word, "->", ps.stem(word))