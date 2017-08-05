import os
import tweepy
from tweepy import OAuthHandler
import RateLimitCheck
import secrets

twitter_account_name = 'blacksburgfire'
count_per_api_call = 20


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


def writeStatusesToFile(namedFile, statuses):
        for status in statuses:
            namedFile.write(status.text)
            namedFile.write('\n')


def createOutputDir():
    try:
        os.makedirs("output")
    except OSError:
        pass


def canRequestStatuses(number):
	return RateLimitCheck.canRequestUserStatuses(api, number)


print("Beginning execution", flush=True)
auth = OAuthHandler(secrets.consumer_key, secrets.consumer_secret)
auth.set_access_token(secrets.access_token, secrets.access_token_secret)

api = tweepy.API(auth)

userVar = api.get_user(twitter_account_name)
status_count = userVar.statuses_count
status_total_divided = (status_count / count_per_api_call) + 1

if not canRequestStatuses(status_total_divided):
	print("Made too many API calls - can't currently get user statuses. Please wait a few minutes and try again.", flush=True)
	exit()

createOutputDir()

statusFile = open('output/StatusFile.txt', 'w+', errors='xmlcharrefreplace')

print("Getting the first chunk of statuses", flush=True)
statuses = api.user_timeline(twitter_account_name)
lowestId = getLowestStatusId(statuses)
writeStatusesToFile(statusFile, statuses)


index = 0
while index < status_total_divided:
	print("Getting the next chunk of statuses... chunk #" + str(index + 2), flush=True)
	statuses = api.user_timeline(twitter_account_name, count=count_per_api_call, max_id=lowestId)
	lowestId = getLowestStatusId(statuses)
	if lowestId == -1:
		break;
	writeStatusesToFile(statusFile, statuses)
	index = index + 1



statusFile.close()
print("Finished getting statuses")










RateLimitCheck.updateRateLimitJson(api)
