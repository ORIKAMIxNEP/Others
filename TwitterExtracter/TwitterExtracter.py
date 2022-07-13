from flask import Flask, request
from flask_cors import CORS
import json
import tweepy

app = Flask(__name__)
CORS(
    app,
    supports_credentials=True
)


@app.route("/", methods=["GET"])
def TwitterExtracter():
    config = json.load(open("./config.json", "r"))
    BEARER_TOKEN = config["BEARER_TOKEN"]
    API_KEY = config["API_KEY"]
    API_SECRET = config["API_SECRET"]
    ACCESS_TOKEN = config["ACCESS_TOKEN"]
    ACCESS_TOKEN_SECRET = config["ACCESS_TOKEN_SECRET"]
    client = tweepy.Client(BEARER_TOKEN, API_KEY, API_SECRET,
                           ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    searchText = request.args.get("word")
    next_token = ""
    allTweetsCount = 0
    extractedTweetsCount = 0
    for i in range(5):
        if i == 0:
            tweets = client.search_recent_tweets(
                query=searchText, max_results=20, tweet_fields=["entities", "lang", "public_metrics"])
        else:
            tweets = client.search_recent_tweets(
                query=searchText, max_results=20, next_token=next_token, tweet_fields=["entities", "lang", "public_metrics"])
        TweetsData = {"tweets": []}
        for tweet in tweets.data:
            if tweet.lang == "ja" and (tweet.entities is None or ("mentions" not in tweet.entities and "urls" not in tweet.entities)):
                print("-------------------------------------------")
                print(tweet.text)
                print("fav:" + str(tweet.public_metrics["like_count"]))
                print(
                    dict({"tweet": tweet.text, "favorite": tweet.public_metrics["like_count"]}))
                TweetsData["tweets"].append(
                    dict({"tweet": tweet.text, "favorite": tweet.public_metrics["like_count"]}))
                print(TweetsData)
                extractedTweetsCount += 1
            allTweetsCount += 1
        if "next_token" not in tweets.meta:
            break
        else:
            next_token = tweets.meta["next_token"]

    print("-------------------------------------------")
    print("AllTweet:" + str(allTweetsCount))
    print("ExtractedTweet:" + str(extractedTweetsCount))
    print(TweetsData)
    return TweetsData


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=50001, debug=True)
