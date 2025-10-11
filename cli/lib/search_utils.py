import string

def clean(message):
    table = str.maketrans("", "", string.punctuation);
    clean_string = message.translate(table)
    return clean_string.lower()
