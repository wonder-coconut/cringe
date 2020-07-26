import tweepy
import time
import threading

print("welcome back")

def getToken(ind):
    tokenFile = open("TOKEN.txt")
    tokencontent = tokenFile.read()
    tokenTxt = tokencontent.split("\n")
    return tokenTxt[ind]


#stream class
class MyStreamListener(tweepy.StreamListener):
    
    def __init__(self,api):
        self.api = api
        self.me = api.me()

    def on_status(self,tweet):
        try:
            if "#cringe" in tweet.text.lower():
                print(f"#cringe found in {tweet.text}, replying")
                api.update_status("@bottestingOwO cringe",tweet.id)
                print("success")
            else:
                print(f"{tweet.user.name} \t {tweet.text}")
        except:
            print("failure")
    
    def on_error(self,status):
        if status == 420: #nice
            print("rate limit exceeded,killing bot")
            return False

        else:
            print("error")



#twitter authentication
auth = tweepy.OAuthHandler(getToken(0),getToken(1))
auth.set_access_token(getToken(2),getToken(3))

#api object
api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

#tweet listener
tweets_listener = MyStreamListener(api)
stream = tweepy.Stream(api.auth, tweets_listener)
stream.filter(follow = ["1284123616682991617"],languages = ["en"])