from nltk.tokenize import word_tokenize
from nltk.collocations import BigramCollocationFinder, TrigramCollocationFinder, ngrams

line = "This is a simple example showing off bigram collocations is a  in NLTK. i am a tech"
word = word_tokenize(line)

# print(word)

b = BigramCollocationFinder.from_words(word)
# print(b.ngram_fd.items())

# for bigram, freq in b.ngram_fd.items():
#     print(f"{bigram}: {freq}")

t = TrigramCollocationFinder.from_words(word)
# print(t.ngram_fd.items())

n = ngrams(word, 1)

# for i in n:
#     print(i)


