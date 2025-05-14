import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

line  = ["my name is nk. ", "my name is dev"]

df = pd.DataFrame({ "name": line })

print(df)

cv = CountVectorizer()
new_data = cv.fit_transform(df["name"]).toarray()
print(new_data)

cv.vocabulary_
print(cv.vocabulary_)