import tweepy
import json
from tweepy import OAuthHandler

def checkAllowedApiCalls():
    jsonF = api.rate_limit_status();

    rlj = open('RateLimitJson.json', 'w+')
    json.dump(jsonF, rlj);
    rlj.close();

consumer_key = ''

#============================================#

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

checkAllowedApiCalls()