from nltk.stem import LancasterStemmer, PorterStemmer, SnowballStemmer, RegexpStemmer

l = LancasterStemmer()
r = RegexpStemmer("ing")
p = PorterStemmer()
s = SnowballStemmer("english")

word = "changing"
print("Original word:", word)
print("LancasterStemmer:", l.stem(word))
print("RegexpStemmer:", r.stem(word))
print("PorterStemmer:", p.stem(word))
print("SnowballStemmer:", s.stem(word))