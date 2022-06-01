import json
import tweepy


config = json.load(open("./config.json", "r"))
BEARER_TOKEN = config["BEARER_TOKEN"]
API_KEY = config["API_KEY"]
API_SECRET = config["API_SECRET"]
ACCESS_TOKEN = config["ACCESS_TOKEN"]
ACCESS_TOKEN_SECRET = config["ACCESS_TOKEN_SECRET"]
client = tweepy.Client(BEARER_TOKEN, API_KEY, API_SECRET,
                       ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

searchText = "タコピー"
next_token = ""
allTweetsCount = 0
extractedTweetsCount = 0
for i in range(1):
    if i == 0:
        tweets = client.search_recent_tweets(
            query=searchText, max_results=10, tweet_fields=["entities", "lang", "public_metrics"])
    else:
        tweets = client.search_recent_tweets(
            query=searchText, max_results=10, next_token=next_token, tweet_fields=["lang", "public_metrics"])
    for tweet in tweets.data:
        if tweet.lang == "ja" and (tweet.entities is None or "mentions" not in tweet.entities):
            print("-------------------------------------------")
            print(tweet.text)
            print("fav:" + str(tweet.public_metrics["like_count"]))
            extractedTweetsCount += 1
        allTweetsCount += 1
    if "next_token" not in tweets.meta:
        break
    else:
        next_token = tweets.meta["next_token"]

print("AllTweet:" + str(allTweetsCount))
print("ExtractedTweet:" + str(extractedTweetsCount))
