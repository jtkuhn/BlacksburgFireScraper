import os
import tweepy
import json
from tweepy import OAuthHandler

twitter_account_name = 'blacksburgfire'
count_per_api_call = 20

def checkAllowedApiCalls():
    jsonF = api.rate_limit_status();

    rlj = open('RateLimitJson.json', 'w+')
    json.dump(jsonF, rlj);
    rlj.close();

def getLowestStatusId(tweets):
    try:
        lowest = tweets[0].id
        for tweet in tweets:
            if tweet.id < lowest:
                lowest = tweet.id
        lowest = lowest - 1
        return lowest
    except:
        return -1

def writeStatusesToJson(namedFile, statuses):
        for status in statuses:
            namedFile.write(status.text)
            namedFile.write('\n')

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

#============================================#

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

userVar = api.get_user(twitter_account_name)
status_count = userVar.statuses_count
status_total_divided = (status_count / count_per_api_call) + 1

statusFile = open('StatusFile.json', 'w+', errors='xmlcharrefreplace')
statuses = api.user_timeline(twitter_account_name)
lowestId = getLowestStatusId(statuses)
writeStatusesToJson(statusFile, statuses)


index = 0
while index < status_total_divided:
    statuses = api.user_timeline(twitter_account_name, count=count_per_api_call, max_id=lowestId)
    lowestId = getLowestStatusId(statuses)
    if lowestId == -1:
        break;
    writeStatusesToJson(statusFile, statuses)
    index = index + 1



statusFile.close()










checkAllowedApiCalls()
