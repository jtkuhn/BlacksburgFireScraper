import tweepy
import json
from tweepy import OAuthHandler
import secrets

def checkAllowedApiCalls():
    jsonF = api.rate_limit_status();

    rlj = open('output/RateLimitJson.json', 'w+')
    json.dump(jsonF, rlj);
    rlj.close();


auth = OAuthHandler(secrets.consumer_key, secrets.consumer_secret)
auth.set_access_token(secrets.access_token, secrets.access_token_secret)

api = tweepy.API(auth)




emojiFile = open('output/EmojiFile.json', 'w+', errors='xmlcharrefreplace')

status = api.get_status('840607860144787456')

emojiFile.write(status.text)
emojiFile.write('\n')
#print(status.text)



checkAllowedApiCalls()
emojiFile.close()
