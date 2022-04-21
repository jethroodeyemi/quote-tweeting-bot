import tweepy
import time

def timer(days):
    twitter_auth_keys = { 
        "consumer_key"        : "CNpeVrrmf57DOrWzETKpzwRA6",
        "consumer_secret"     : "yfypGXmBQ72QxPuMXFq7AcJ8hA9N8br1Pu7D9YRtlLVEABhyNr",
        "access_token"        : "1243164206481973249-1yoxu697UWVezOsU5q6CN1DImPpim6",
        "access_token_secret" : "qWgAV18xfNRfwqC6nkjLQSP5yOZx8KeZgoMT3HtOGrAZ2"
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
