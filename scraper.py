#  Importing the required packages

import os
import re
import tweepy
import json
from dotenv import load_dotenv
load_dotenv()

class scraper():
    def __init__(self, CONSUMER_TOKEN, CONSUMER_SECRET):
        self.CONSUMER_SECRET  = CONSUMER_SECRET
        self.CONSUMER_TOKEN = CONSUMER_TOKEN

    def auth(self):
        #OAuth 2 Authentication
        try:
            self.auth =  tweepy.AppAuthHandler(CONSUMER_TOKEN, CONSUMER_SECRET)
            self.api = tweepy.API(self.auth)
        except:
            print('Error: Authentication Failed')
    def display(self):
        for tweet in tweepy.Cursor(self.api.search, q='@BernieSanders@SenSanders').items(10):
            print(tweet.text)

    def clean_tweet(self, tweet):
        ''' 
        Utility function to clean tweet text by removing links, special characters 
        using simple regex statements. 
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split()) 

    def get_tweets(self, query, candidate, count=10):
        tweets = tweepy.Cursor(self.api.search, q=query+' -filter:retweets').items(10)
        
        data = []
        #Looping through the tweets
        for tweet in tweets:
        
           row = []
           row.append(tweet.id)
           row.append(self.clean_tweet(tweet.text))
           row.append(tweet.created_at.year)
           row.append(tweet.created_at.month)
           row.append(tweet.created_at.day)
           row.append(tweet.retweet_count)
           data.append(row)

        for data_row in data:
            print(data_row)        
        
CONSUMER_TOKEN = os.getenv("CONSUMER_TOKEN")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")


scrape = scraper(CONSUMER_TOKEN,CONSUMER_SECRET)
scrape.auth()
scrape.get_tweets('#Sanders2020', 'sanders')


#Creating list of key words

candidates = {
    "sanders" : ['#Sanders2020', '@SenSanders', '@BernieSanders'],
    "trump" : ['#Trump2020', '@realDonaldTrump'],
    "biden" : ['#Biden2020', '@JoeBiden']
}

