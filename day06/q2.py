#!/usr/bin/env python
from textblob import TextBlob
import tweepy
consumer_key = '0htEpfdbFuqgCvxrRXVFHYXGc'
consumer_secret = 'C6tFvHVT1MsH7YYrMqIxrdclwFECMGLhTQB3DMSBxZZETRAROu'

access_token = '199500984-5DaTlHtNGzb6DiDGtHBR0xrWgQiXg2YblkO9Mfd5'
access_token_secret = 'FyuaL0NGxNvHNoBFr9tM6q2mwMjranonSZbA5BDTH11tg'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
public_tweets=api.user_timeline(screen_name='FIFAcom')
tmp=[]
k=0
for tweet in public_tweets:
 k+=1
 tmp.append(tweet)
 print tweet
pola=0
for i in str(tmp).split('.'):
 t1=TextBlob(i)
 pola+=t1.sentiment.polarity
print pola/k
