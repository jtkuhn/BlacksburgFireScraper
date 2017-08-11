import tweepy
from tweepy import OAuthHandler
import secrets
import RateLimitCheck

auth = OAuthHandler(secrets.consumer_key, secrets.consumer_secret)
auth.set_access_token(secrets.access_token, secrets.access_token_secret)

api = tweepy.API(auth)

emojiFile = open('output/EmojiFile.txt', 'w+', errors='xmlcharrefreplace')

status = api.get_status('840607860144787456')

emojiFile.write(status.text)
emojiFile.write('\n')

RateLimitCheck.updateRateLimitJson(api)
emojiFile.close()
