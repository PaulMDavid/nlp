#!/usr/bin/env python
from textblob import TextBlob
x=open('filesa.txt','r+')
tex=x.readline()
x=TextBlob(tex)
wlist=x.tags
i=0
for word in wlist:
 i=i+1
print i
j=0
for sent in x.sentences:
 j+=1
print j
s=x.sentences
print(x.sentences)
print(x.words)
wsort=sorted(wlist)
print wsort
for w in x.tags:
 if(x.tags=='NN') or(x.tags=='NNS'):
  print(w+" "+str(x.tag))
print "DIs Abt"+str(s[0])
