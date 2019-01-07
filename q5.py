#!/usr/bin/env python
from textblob import TextBlob
print("Enter the stuff");
sont=raw_input("")
sent=TextBlob(sont)
print("corrected stuff");
print(sent.translate(to='de'));




