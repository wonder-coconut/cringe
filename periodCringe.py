import tweepy
import time
import threading


def getToken(ind):
    tokenFile = open("tokens/TOKEN2.txt")
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

global index
index = 0


def rick(c):
    return "#dalitlivesmatter\n#DalitLivesMatter\n#JusticeForHathrasVictim\n#JusticeForBalrampurVictim\n Expose them."


def timeRepeater(index):
    text = rick(index)
    print(f"tweeting at {time.ctime()}")
    api.update_status(f"\n--------------\n{text}\n--------------\ntimestamp:\t{time.ctime()}")
    print("tweeted succesfully")
    
    threading.Timer(300,timeRepeater,args=[index+1]).start() #repeats every 4 hours with index increment #args is supposed to be an iterable(personal ref)

timeRepeater(index)

