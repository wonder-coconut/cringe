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
        try:#replying to tweets with the hashtag cringe
            if "#cringe" in tweet.text:
                print(f"cringe found, replying to tweet id:{tweet.id}")
                api.update_status(status = f"@{tweet.user.screen_name} [bot] i have found cringe",in_reply_to_status_id = tweet.id)
                print(f"cringe replied")

            else:#printing live update tweets from my bot testing account
                print(f"{tweet.user.screen_name}\tsaid\t{tweet.text}")

        except:
            print("error")

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
api = tweepy.API(auth)

#tweet listener
tweets_listener = MyStreamListener(api)
stream = tweepy.Stream(api.auth, tweets_listener)
stream.filter(follow = ["1284123616682991617"],languages = ["en"])