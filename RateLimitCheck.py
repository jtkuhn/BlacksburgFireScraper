import tweepy
from tweepy import OAuthHandler
import json
import secrets

def updateRateLimitJson(api):
    jsonF = api.rate_limit_status();

    rlj = open('output/RateLimitJson.json', 'w+')
    json.dump(jsonF, rlj);
    rlj.close();

if __name__ == "__main__":
    auth = OAuthHandler(secrets.consumer_key, secrets.consumer_secret)
    auth.set_access_token(secrets.access_token, secrets.access_token_secret)

    api = tweepy.API(auth)

    updateRateLimitJson(api)
