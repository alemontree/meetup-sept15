import csv
import os
# to make unicode work
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import credentials

# twitter api wrapper
import tweepy

consumer_key = credentials.consumer_key
consumer_secret = credentials.consumer_secret
access_key = credentials.access_key
access_secret = credentials.access_secret

# get mah tweets
def download_tweets():
    username = "mishnayder"
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    # authenticate to the twitter api with your credentials
    api = tweepy.API(auth)

    # how many tweets to get (limit 200)
    num_tweets = 100
    
    # access your timeline
    tweets = api.user_timeline(screen_name = username, count = num_tweets)
    
    # start a list to hold your tweet info
    my_tweets = []
    
    for tweet in tweets:
        my_tweets.append([username, tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")])

    # write it out to a csv
    with open("{0}_tweets.csv".format(username), 'w+') as file:
        writer = csv.writer(file, delimiter='|')
        writer.writerows(my_tweets)

if __name__ == '__main__':
    download_tweets()
