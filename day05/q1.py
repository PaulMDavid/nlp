#!/usr/bin/env python
s1="The world is darwinian"
s2="Chaos rules the world"
s3="Darwinian rules apply to all"
query="world apply chaos"

from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.metrics.pairwise import cosine_similarity
tfidf=TfidfVectorizer()
#cos=cosine_similarity()
dataset=[s1,s2,s3]
m=tfidf.fit(dataset)
print tfidf.vocabulary_
ma=tfidf.fit_transform(dataset)
print ma
dataset=[query,s1,s2,s3]
ma=tfidf.fit_transform(dataset)
c=cosine_similarity(ma)
print c
