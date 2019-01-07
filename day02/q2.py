#!/usr/bin/env python
from textblob import Word
x=raw_input("u know wat to do")
x=Word(x)
print(x.singularize())

