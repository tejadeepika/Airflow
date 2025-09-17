import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs


def run_twitter_etl():
    access_key = "IipGeQUKGT5PMp4tHLlMDKAut"
    access_secret = "KWy3d2pjEI1ev3TQMA5SsUI4QPO6C95LhhclZ5VTkCi8DqO4qQ"
    consumer_key = "951429404596436992-143WsOw6xpQTJ27ezFAfiring51mSLV"
    consumer_secret = "l7wVK9XzMI1te5WJ7IrxVYGnjX4B7cwzF8ZAUXGjJrXsw"

    # Twitter authentication
    auth = tweepy.OAuthHandler(access_key, access_secret)
    auth.set_access_token(consumer_key, consumer_secret)

    # # # Creating an API object
    api = tweepy.API(auth)
    tweets = api.user_timeline(screen_name='@elonmusk',
                               count=200,
                               include_rts=False,
                               tweet_mode='extended'
                               )

    list = []
    for tweet in tweets:
        text = tweet._json["full_text"]

        refined_tweet = {"user": tweet.user.screen_name,
                         'text': text,
                         'favorite_count': tweet.favorite_count,
                         'retweet_count': tweet.retweet_count,
                         'created_at': tweet.created_at}

        list.append(refined_tweet)

    df = pd.DataFrame(list)
    df.to_csv('refined_tweets.csv')