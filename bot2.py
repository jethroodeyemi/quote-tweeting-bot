import tweepy
import time

def timer(days):
    twitter_auth_keys = { 
        "consumer_key"        : "",
        "consumer_secret"     : "",
        "access_token"        : "",
        "access_token_secret" : ""
    }
 
    auth = tweepy.OAuthHandler(
            twitter_auth_keys['consumer_key'],
            twitter_auth_keys['consumer_secret']
            )
    auth.set_access_token(
            twitter_auth_keys['access_token'],
            twitter_auth_keys['access_token_secret']
            )
    api = tweepy.API(auth)
 
    media = api.media_upload(f"images/{days}.png")
    tweet = f"Days left till Buhari leaves Aso Rock: {days} \n#BuhariCountdown"
    api.update_status(status=tweet, media_ids=[media.media_id])
    return

def main():
    days=829
    for i in range(1,829):
        timer(days-i)
        time.sleep(86400)

if __name__ == "__main__":
    main()
