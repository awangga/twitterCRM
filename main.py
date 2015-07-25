#!/usr/bin/python
import tweepy
import config
#import requests.packages.urllib3.contrib.pyopenssl
#urllib3.contrib.pyopenssl.inject_into_urllib3()

auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
	print tweet.text
	