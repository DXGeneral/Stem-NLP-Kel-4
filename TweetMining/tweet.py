import tweepy
from tweepy import OAuthHandler
 
consumer_key = 'tbXUij0Auakryoljyh6GbRTjT'
consumer_secret = 'l5BX4AvA5sr1rSTk7m82kyxdWSr6App7TamvCOVhTqg5gcQ1uK'
access_token = '321787319GSH9sxzlA9qsJFp9NnWXu4aBJyjQFy5tIw49LOef'
access_secret = ' n4bub6B82yAfqTgzYm4vQLCb2a0JPas6aGPMtb2gX08Ly'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)
for tweet in api.search(q="google"):
	print(tweet.text)
	print('\n')