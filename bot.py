import tweepy
from secrets import *

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

result = api.search(q = '"my cat"', count = 1, rpp = 1)
print result