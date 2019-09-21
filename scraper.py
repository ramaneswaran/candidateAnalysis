from dotenv import load_dotenv
load_dotenv()

import os
import tweepy

CONSUMER_TOKEN = os.getenv("CONSUMER_TOKEN")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")

#OAuth 2 Authentication

auth =  tweepy.AppAuthHandler(CONSUMER_TOKEN, CONSUMER_SECRET)

api = tweepy.API(auth)

for tweet in tweepy.Cursor(api.search, q='#trump2020').items(1):
    print(tweet.text)
