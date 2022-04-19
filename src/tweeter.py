"""
Description:
    This module provides an interface to Twitter than can be used to
    authenticate, tweet and reply.
"""

from os.path import join, dirname, abspath
import os
from dotenv import load_dotenv
import tweepy
from src import logger

# maximum tweet length in characters
MAX_LENGTH = 240 # characters

class Tweeter:
    """
    Description:
        This class provides an interface to Twitter than can be used to
        authenticate, tweet and reply.
    """

    def read_config(self):
        """
        Description:
            Read authentication details from the .env file.
        """

        # load constants from .env
        parent_dir = dirname(dirname(abspath(__file__)))
        config_dir = join(parent_dir, "config")
        dotenv_file = join(config_dir, '.env')
        load_dotenv(dotenv_file)

        # read the authentication keys
        self.bearer_token        = os.getenv("BEARER_TOKEN")
        self.consumer_key        = os.getenv("CONSUMER_KEY")
        self.consumer_secret     = os.getenv("CONSUMER_SECRET")
        self.access_token        = os.getenv("ACCESS_TOKEN")
        self.access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")


    def __init__(self):
        self.read_config()
        auth = tweepy.OAuth1UserHandler(self.consumer_key,
                                        self.consumer_secret,
                                        self.access_token,
                                        self.access_token_secret)
        self.api = tweepy.API(auth)


    def tweet(self, text):
        """
        Description:
            Send a tweet with the specified text.
        """

        tweet_id = 0

        if len(text) <= MAX_LENGTH:
            logger.log_info("Tweet:\n" + text)
            # try:
            #     status = self.api.update_status(text)
            #     tweet_id = status.id
            # except tweepy.TweepyException:
            #     logger.log_error("error - could not send tweet.")
        else:
            logger.log_error("error - tweet is longer than the maximum length")

        return tweet_id


    def reply(self, text, parent_id):
        """
        Description:
            Send a reply to the given parent tweet with the specified text.
        """

        reply_id = 0

        if parent_id > 0:
            if len(text) <= MAX_LENGTH:
                logger.log_info("Reply to tweet " + str(parent_id) + ":\n" + text)
                # try:
                #     status = self.api.update_status(status=text, in_reply_to_status_id=parent_id)
                #     reply_id = status.id
                # except tweepy.TweepyException:
                #     logger.log_error("error - could not send reply")
            else:
                logger.log_error("error - tweet is longer than the maximum length")
        else:
            logger.log_error("error - could not reply to tweet with invalid ID: " + str(parent_id))

        return reply_id
