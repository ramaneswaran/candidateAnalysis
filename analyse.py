from textblob import TextBlob 
import pandas as pd 
import numpy as np
import math
import os

def analyse_sentiment(tweet_text):

    sentiment = TextBlob(tweet_text).sentiment
    if sentiment.polarity >= 0:
        return 1
    else :
        return 0
        
#Candidates list

candidates = [
    {"name": "trump" ,
      "polarity": {'positive' : -1, 'negative' :-1 
        }
    },
    {"name": "sanders" ,
      "polarity": {'positive' : -1, 'negative' :-1 
        }
    },
    {"name": "biden" ,
      "polarity": {'positive' : -1, 'negative' :-1 
        }
    }
]


for candidate in candidates:
    
    name = candidate['name']
    df = pd.read_csv('data/'+name+'.csv', sep=';')
    df = df[pd.notnull(df['TEXT'])]

    #Analyse sentiment
    df['SENTIMENT'] = df['TEXT'].apply(analyse_sentiment)

    #Store polarity values
    candidate['polarity']['positive'] = df['SENTIMENT'].value_counts()[1]
    candidate['polarity']['negative'] = df['SENTIMENT'].value_counts()[0]


    #Updating the CSV FILE
    os.remove('data/'+name+'.csv')
    df.to_csv('data/'+name+'.csv', sep=';',index=False)            


