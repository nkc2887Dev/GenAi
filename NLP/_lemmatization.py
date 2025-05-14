from nltk.stem import WordNetLemmatizer

wl = WordNetLemmatizer()

print("WordNetLemmatizer word:", wl.lemmatize("mice"))
print("WordNetLemmatizer word:", wl.lemmatize("hello"))