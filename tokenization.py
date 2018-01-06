import pandas as pd

from textblob import TextBlob as tb

'''
This is an example of how one could load in tweets and convert to sentiment scores and find average sentiment. 
'''

df = pd.read_csv('~/PycharmProjects/untitled3/giants4.csv', header = 0)

print(df.head())
print(type(df))




tweets = []
sentiment_scores = []



for index, entry in df.iterrows():
    tweet = tb(entry['Tweet'])
    sentiment_scores.append(tweet.sentiment.polarity)

df["sentiment"] = sentiment_scores
df = df[df.sentiment != 0]

for index, entry in df.iterrows():
    tweets.append({"timestamp":entry['TimeStamp'], "tweet":preprocess(entry["Tweet"]), "location":entry['Location'],  "sentiment":sentiment_scores[index]})

print(tweets)

print (sum(df.sentiment)/  len(df.sentiment))
