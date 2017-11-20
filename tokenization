import pandas as pd
import re
from textblob import TextBlob as tb



df = pd.read_csv('~/PycharmProjects/untitled3/giants4.csv', header = 0)

print(df.head())
print(type(df))

emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""

regex_str = [
    emoticons_str,
    r'<[^>]+>', # HTML tags
    r'(?:@[\w_]+)', # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs

    r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
    r'(?:[\w_]+)', # other words
    r'(?:\S)' # anything else
]

tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)

def tokenize(s):
    return tokens_re.findall(s)

def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens

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
