from nltk.wsd import lesk
from nltk.tokenize import word_tokenize

x = "Sunrise (or sunup) is the moment when the upper rim of the Sun appears on the horizon in the morning,[1] at the start of the Sun path. The term can also refer to the entire process of the solar disk crossing the horizon."
y = "A mouse (pl.: mice) is a small rodent. Characteristically, mice are known to have a pointed snout, small rounded ears, a body-length scaly tail, and a high breeding rate. The best known mouse species is the common house mouse (Mus musculus). Mice are also popular as pets. In some places, certain kinds of field mice are locally common. They are known to invade homes for food and shelter."

line = lesk(word_tokenize(y), "mouse")
print(line.definition())