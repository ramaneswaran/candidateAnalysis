#  Importing the required packages

import os
import tweepy
from dotenv import load_dotenv
load_dotenv()

class scraper():
    def __init__(self, CONSUMER_TOKEN, CONSUMER_SECRET):
        self.CONSUMER_SECRET  = CONSUMER_SECRET
        self.CONSUMER_TOKEN = CONSUMER_TOKEN

    def auth(self):
        #OAuth 2 Authentication

        self.auth =  tweepy.AppAuthHandler(CONSUMER_TOKEN, CONSUMER_SECRET)
        self.api = tweepy.API(self.auth)

    def display(self):
        for tweet in tweepy.Cursor(self.api.search, q='@BernieSanders@SenSanders').items(10):
            print(tweet.text)




CONSUMER_TOKEN = os.getenv("CONSUMER_TOKEN")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")


scrape = scraper(CONSUMER_TOKEN,CONSUMER_SECRET)
scrape.auth()
scrape.display()


#Creating list of key words

sanders = ['#Sanders2020', '@SenSanders', '@BernieSanders']

trump = ['#Trump2020', '@realDonaldTrump']

biden = ['#Biden2020', '@JoeBiden']

