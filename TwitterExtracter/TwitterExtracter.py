import json
import tweepy

config = json.load(open("./config.json", "r"))
API_KEY = config["API_KEY"]
API_SECRET = config["API_SECRET"]
ACCESS_TOKEN = config["ACCESS_TOKEN"]
ACCESS_TOKEN_SECRET = config["ACCESS_TOKEN_SECRET"]

client = tweepy.Client(None, API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

tweets = client.search_recent_tweets(query = "Python", max_results = 10)

for tweet in tweets.data:
    print("-----------------")
    print(tweet.text)
