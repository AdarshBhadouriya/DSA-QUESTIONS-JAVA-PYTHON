import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')

text = input("Enter sentence: ")
words = word_tokenize(text)
stop = set(stopwords.words('english'))

filtered = [w for w in words if w.lower() not in stop]

print("Original:", text)
print("Filtered:", " ".join(filtered))