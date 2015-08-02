import tweepy
import config

class Rolly():
	def __init__(self):
		self.auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
		self.auth.set_access_token(config.access_token, config.access_token_secret)
		self.api = tweepy.API(auth)
	
	def sendBroadcastDM(self):
		for follower in tweepy.Cursor(api.followers).items():
			print follower.screen_name
			api.send_direct_message(user = follower.screen_name,text = config.message)
	
	def followBack(self):
		for follower in tweepy.Cursor(api.followers).items():
			follower.follow()
