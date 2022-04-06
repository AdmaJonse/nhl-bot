import os
import tweepy

from os.path import join, dirname, abspath
from dotenv import load_dotenv

from src import logger

# maximum tweet length in characters
max_length = 240 # characters

class Tweeter:

    def read_config(self):

        # load constants from .env
        parent_dir = dirname(dirname(abspath(__file__)))
        config_dir = join(parent_dir, "config")
        dotenv_file = join(config_dir, '.env')
        load_dotenv(dotenv_file)

        # read the authentication keys
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
        if 0 < len(text) <= max_length:
            logger.log_info("Tweet:\n" + text)
            try:
                self.api.update_status(text)
            except:
                logger.log_error("error - could not send tweet.")
