import tweepy
import json
from tweepy import OAuthHandler
import numpy as np
 
consumer_key = 'OU4n6gpftucZHbF727ylx6pe3'
consumer_secret = '9G2RBxpTCQwXiUqhLlpvrnj4arzOLTKbAPhEhfSYJQs5Uv0onD'
access_token = '321787319GSH9sxzlA9qsJFp9NnWXu4aBJyjQFy5tIw49LOef'
access_secret = 'n4bub6B82yAfqTgzYm4vQLCb2a0JPas6aGPMtb2gX08Ly'
 
auth = OAuthHandler(consumer_key, consumer_secret)
#auth.set_access_token(access_token, access_secret)

"""
#TWEET MINING
api = tweepy.API(auth)
f = open('tweets.txt', 'w+', encoding="utf-8")
jumlah_data_yang_diinginkan = 1000
for i in list(['jaringan','4g','3g','koneksi','gsm','hdspa','edge']):
    for j in list(['lambat','lemot','lelet','goblok','anjing','bego','cacat']):
        for tweet in tweepy.Cursor(api.search, q=[i,j], tweet_mode='extended', geocode="-7.614529,110.712246,583km").items(jumlah_data_yang_diinginkan):
            obj = tweet._json
            #print(obj.keys())
            #print(obj['full_text'])
            f.write(obj['full_text'])
            f.write("\n")
f.close()
"""
    
# import Sastrawi package
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

# create stemmer
factory = StemmerFactory()
stemmer = factory.create_stemmer()

# stem
sentence = 'Perekonomian Indonesia sedang dalam pertumbuhan yang membanggakan'
output   = stemmer.stem(sentence)

print(output)
# ekonomi indonesia sedang dalam tumbuh yang bangga

print(stemmer.stem('Mereka meniru-nirukannya'))
# mereka tiru