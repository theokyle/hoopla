import string
from nltk.stem import PorterStemmer

def clean(message):
    table = str.maketrans("", "", string.punctuation);
    clean_string = message.translate(table)
    return clean_string.lower()

def tokenize_text(text):
    with open("./data/stopwords.txt", "r") as file:
        stop_words = file.read().splitlines()

    stemmer = PorterStemmer()

    text = clean(text)
    tokens = text.split(" ")
    valid_tokens = []
    for token in tokens:
        if token and token not in stop_words:
            valid_tokens.append(stemmer.stem(token))
    return valid_tokens

def has_matching_token(query, title):
    queryTokens = tokenize_text(query)
    titleTokens = tokenize_text(title)
    for queryToken in queryTokens:
        for titleToken in titleTokens:
            if queryToken in titleToken:
                return True
    return False