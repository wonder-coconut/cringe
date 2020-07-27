import tweepy
import time
import threading


def getToken(ind):
    tokenFile = open("TOKEN.txt")
    tokencontent = tokenFile.read()
    tokenTxt = tokencontent.split("\n")
    return tokenTxt[ind]

#auth
auth = tweepy.OAuthHandler(getToken(0),getToken(1))
auth.set_access_token(getToken(2),getToken(3))

#api object
try:
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    print("authentication succesfull")
except:
    print("auth error")


def timeRepeater():
    print(f"tweeting at {time.ctime()}")
    api.update_status(f"[bot]sex is cringe\ntimestamp:\t{time.ctime()}")

    threading.Timer(43200,timeRepeater).start()

timeRepeater()