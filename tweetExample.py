'''
This is an example of usning tweepy to scrape Twitter Data based on a hashtag of your choice.
'''

import tweepy
import csv
import pandas as pd
CONSUMER_KEY = 'ltXoBgzF9LqA1M7XHDRhuGWEv'
CONSUMER_SECRET = '2J9nJ8XGYou050YHRJk5pTkAOmyhSeJ3jZlzhq2Dnyfn4YAFIJ'

ACCESS_TOKEN = '2899848858-YTSlSMiyxU2yHkWimjmLHjukUvmjNwxYOj7AE08'
ACCESS_SECRET = 'J7T3NtTZBk3vfFP0ggycipzvUCNirYtYoDQE9CgWe1AqQ'


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth,wait_on_rate_limit=True)
#####United Airlines
# Open/Create a file to append data
csvFile = open('giants6.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)
csvWriter.writerow(["TimeStamp", "Tweet", "Location"])
for tweet in tweepy.Cursor(api.search,q="#Giants",count=100,
                           lang="en",
                           since="2017-10-15").items():
    print (tweet.created_at, tweet.text, tweet.user.location)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8'), tweet.user.location])
