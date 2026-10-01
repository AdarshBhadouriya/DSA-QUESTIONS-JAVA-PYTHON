import re

text = input("Enter paragraph: ")

tokens = re.findall(
    r'https?://\S+|[\w.+-]+@[\w.-]+\.\w+|\d+|[a-zA-Z]+|[^\w\s]',
    text
)

for t in tokens:
    if t.startswith(("http://", "https://")):
        print(t, "- URL")
    elif "@" in t and "." in t:
        print(t, "- Email")
    elif t.isdigit():
        print(t, "- Number")
    elif t.isalpha():
        print(t, "- Word")
    elif t in ".,!?;:":
        print(t, "- Punctuation")
    else:
        print(t, "- Special Symbol")