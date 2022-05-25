import json
import tweepy

config = json.load(open("./config.json", "r"))
API_KEY = config["API_KEY"]
API_SECRET = config["API_SECRET"]
ACCESS_TOKEN = config["ACCESS_TOKEN"]
ACCESS_TOKEN_SECRET = config["ACCESS_TOKEN_SECRET"]
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)
tweets = api.search_tweets(q=["Python"], count=10)

for tweet in tweets:
    print("-----------------")
    print(tweet.text)
