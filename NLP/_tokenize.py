from nltk.tokenize import word_tokenize, sent_tokenize

line = 'The Natural Language Toolkit, or more commonly NLTK, is a suite of libraries and programs for symbolic and statistical natural language processing (NLP) for English written in the Python programming language. It supports classification, tokenization, stemming, tagging, parsing, and semantic reasoning functionalities.[4] It was developed by Steven Bird and Edward Loper in the Department of Computer and Information Science at the University of Pennsylvania.[5]'


word = word_tokenize(line)
print("word_tokenize", word)

print("-----------------------------------------------------------------------------")

sent = sent_tokenize(line)
for i in sent:
    print(i)
    print()

print("sent_tokenize", sent)