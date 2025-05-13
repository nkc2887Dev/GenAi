from nltk.corpus import stopwords
from string import punctuation
from nltk.tokenize import word_tokenize
line = 'The Natural Language Toolkit, or more commonly NLTK, is a suite of libraries and programs for symbolic and statistical natural language processing (NLP) for English written in the Python programming language. It supports classification, tokenization, stemming, tagging, parsing, and semantic reasoning functionalities.[4] It was developed by Steven Bird and Edward Loper in the Department of Computer and Information Science at the University of Pennsylvania.[5]'

word = stopwords.words("english")
word_punctuation = list(punctuation) + word
# print(word)
# print(list_punctuation)

for i in word_tokenize(line):
    if i  not in word_punctuation:
        print(i)