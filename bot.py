import os
import tweepy
from dotenv import load_dotenv

class bot:

    def read_config(self):
        load_dotenv()
        self.bearer_token = os.getenv("BEARER_TOKEN")
        self.consumer_key = os.getenv("CONSUMER_KEY")
        self.consumer_secret = os.getenv("CONSUMER_SECRET")
        self.access_token = os.getenv("ACCESS_TOKEN")
        self.access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

    def __init__(self):
        self.read_config()
        auth = tweepy.OAuth1UserHandler(self.consumer_key, self.consumer_secret, self.access_token, self.access_token_secret)
        self.api = tweepy.API(auth)

    def tweet(self, text):
        self.api.update_status(text)

# b = bot()
# b.tweet("testing, testing...")