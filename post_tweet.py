import os
import tweepy
import credentials

consumer_key = credentials.consumer_key
consumer_secret = credentials.consumer_secret
access_key = credentials.access_key
access_secret = credentials.access_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth)

api.update_status(status="@musegarden https://github.com/alemontree/tweetmapper")
