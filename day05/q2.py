#!/usr/bin/env python
s1="The world is darwinian"
s2="Chaos rules the world"
s3="Darwinian rules apply to all"
query="lorem ipsum"
from pandas import Series as ser
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.metrics.pairwise import cosine_similarity
tfidf=TfidfVectorizer()
#cos=cosine_similarity()
dataset=pd.read_csv('/home/ai11/lorem_ipsum',delimiter='\.',header=None)
dataset=dataset.fillna('')
#m=tfidf.fit(dataset)
#print tfidf.vocabulary_
#ma=tfidf.fit_transform(dataset)
#print ma
q=ser(query)
#print type(q)
#print type(dataset.iloc[0])
s=pd.concat([q,dataset.iloc[0]])
d=list(s)
print d
ma=tfidf.fit_transform(d)
c=cosine_similarity(ma,dense_output=True)
print c
