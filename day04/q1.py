#!/usr/bin/env python
from textblob import TextBlob
from textblob import Word
import math
s1=("""Python is a 2000 made-for-TV horror movie directed by Richard
Clabaugh. The film features several cult favorite actors, including William
Zabka of The Karate Kid fame, Wil Wheaton, Casper Van Dien, Jenny McCarthy,
Keith Coogan, Robert Englund (best known for his role as Freddy Krueger in the
A Nightmare on Elm Street series of films), Dana Barron, David Bowe, and Sean
Whalen. The film concerns a genetically engineered snake, a python, that
escapes and unleashes itself on a small town. It includes the classic final
girl scenario evident in films like Friday the 13th. It was filmed in Los Angeles,
 California and Malibu, California. Python was followed by two sequels: Python
 II (2002) and Boa vs. Python (2004), both also made-for-TV films.""")
d1=TextBlob(s1)
doclist=[d1]
dic={}
for s1 in doclist:
 wordlist=d1.words
 for word in wordlist:
  #print word
  tf=d1.words.count(word)
  #print tf
  dic.update({word: tf})
print dic

