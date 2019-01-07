#!/usr/bin/env python
from textblob import TextBlob
sont=TextBlob("Display the sentences in the paragraph.ii. Display the words in the paragraph.iii. Display the noun phrases in the paragraph.")
sent=sont.noun_phrases;
print("nouns");
print(sent);




