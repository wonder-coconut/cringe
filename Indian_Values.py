import tweepy

def getToken(ind):
    tokenFile = open("tokens/TOKEN3.txt")
    tokencontent = tokenFile.read()
    tokenTxt = tokencontent.split("\n")
    return tokenTxt[ind]

#twitter authentication
auth = tweepy.OAuthHandler(getToken(0),getToken(1))
auth.set_access_token(getToken(2),getToken(3))

#api object
try:
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    print("authentication succesfull")
except:
    print("auth error")

tweet = input(" ")
api.update_status(tweet)