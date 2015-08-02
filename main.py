#!/usr/bin/python
import tweepy
import config


auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)

api = tweepy.API(auth)

#print api.rate_limit_status()
#timelineonhome = api.home_timeline()
#api.send_direct_message(user = 'awangga',text = 'halo testing sending dm dari api')
#api.send_direct_message(user = 'awangga',text = 'halo testing sending dm dari api')
#for tweet in timelineonhome:
#	print tweet.text
#follow back follower
for follower in tweepy.Cursor(api.followers).items():
	follower.follow()
	print follower.screen_name
	api.send_direct_message(user = follower.screen_name,text = config.message)
#get list of follower
#for follower in tweepy.Cursor(api.followers).items():
#	print follower.screen_name
	
#print api.followers()
#print api.direct_messages()
#api.create_friendship(garditya)
