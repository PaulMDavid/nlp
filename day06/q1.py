#!/usr/bin/env python
from textblob import TextBlob
s2="Eminem is God"
t1=TextBlob(s2)
print(t1.sentiment)
