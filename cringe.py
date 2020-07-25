import tweepy

def getToken(num):
    tokenFile = open('TOKEN.txt','r')
    tokenTxt = tokenFile.read()
    return tokenTxt[num]

# Authenticate to Twitter
auth = tweepy.OAuthHandler(getToken(0), 
    getToken(1))
auth.set_access_token(getToken(2), 
    getToken(3))

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

