import scraper as sc
import os


CONSUMER_TOKEN = os.getenv("CONSUMER_TOKEN")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")

#Connecting to twitter application

scrape = sc.scraper(CONSUMER_TOKEN,CONSUMER_SECRET)
scrape.auth()

#Creating list of key words

candidates = {
    "sanders" : '#sanders2020' ,
    "trump" : '#Trump2020',
    "biden" : '#Biden2020',
}



#Collecting data and storing in csv files
def collect_candidate_data():
    for candidate in candidates:
        tweets = scrape.get_tweets(candidates[candidate])
        scrape.store_tweets(tweets, candidate)



