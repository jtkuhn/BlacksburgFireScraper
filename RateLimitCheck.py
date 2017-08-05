import tweepy
from tweepy import OAuthHandler
import json
import secrets

def updateRateLimitJson(api):
    jsonF = api.rate_limit_status();

    rlj = open('output/RateLimitJson.json', 'w+')
    json.dump(jsonF, rlj);
    rlj.close();

def printVal(api):
	jsonF = api.rate_limit_status();
	print(jsonF["resources"]["statuses"]["/statuses/user_timeline"]["remaining"])

def canRequestUserStatuses(api, number):
	jsonF = api.rate_limit_status();
	numberAllowed = jsonF["resources"]["statuses"]["/statuses/user_timeline"]["remaining"]
	print("Asking if I can request " + str(number) + " statuses. I am allowed to request " + str(numberAllowed) + " statuses.\n")
	if number < numberAllowed:
		return True
	else:
		return False

if __name__ == "__main__":
    auth = OAuthHandler(secrets.consumer_key, secrets.consumer_secret)
    auth.set_access_token(secrets.access_token, secrets.access_token_secret)

    api = tweepy.API(auth)

    updateRateLimitJson(api)
