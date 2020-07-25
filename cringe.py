import json
import tweepy

print("twitter time yeet")

#tweet listener stream
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, tweet):
        print(f"{tweet.user.name}:{tweet.text}")
        print("retweeting")
        try:
            api.retweet(tweet.id)
            print("retweeted")
        except:
            print("failure")

    def on_error(self, status):
        print("Error detected")


def getToken(num):
    tokenFile = open("TOKEN.txt")
    tokencontent  = tokenFile.read()
    tokenTxt = tokencontent.split('\n')
    return tokenTxt[num]

#OAuth
auth = tweepy.OAuthHandler(getToken(0),getToken(1))
auth.set_access_token(getToken(2),getToken(3))

#API object
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

#API object for stream listener
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
myStream.filter(follow=["1284123616682991617"])
