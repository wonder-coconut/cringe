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
