import tweepy

print("twitter time yeet")

def getToken(num):
    tokenFile = open("TOKEN.txt")
    tokencontent  = tokenFile.read()
    tokenTxt = tokencontent.split('\n')
    return tokenTxt[num]

auth = tweepy.OAuthHandler(getToken(0),getToken(1))
auth.set_access_token(getToken(2),getToken(3))

api = tweepy.API(auth)

mentions = api.mentions_timeline()

for mention in mentions:
    print(str(mention.id) + "\t" + mention.text)