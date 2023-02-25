"""
Description:
    This module provides an interface to Twitter than can be used to
    authenticate, tweet and reply.
"""

from datetime import datetime, timedelta
from typing import List, Optional
import os
from os.path import join, dirname, abspath
from dotenv import load_dotenv
import tweepy
import pytz

from src import logger
from src.outputter import Outputter

# maximum tweet length
MAX_LENGTH = 240 # characters

class Tweeter(Outputter):
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
        parent_dir  : str = dirname(dirname(abspath(__file__)))
        config_dir  : str = join(parent_dir, "config")
        dotenv_file : str = join(config_dir, '.env')
        load_dotenv(dotenv_file)

        # read the authentication keys
        self.bearer_token        : str = os.getenv("BEARER_TOKEN")
        self.consumer_key        : str = os.getenv("CONSUMER_KEY")
        self.consumer_secret     : str = os.getenv("CONSUMER_SECRET")
        self.access_token        : str = os.getenv("ACCESS_TOKEN")
        self.access_token_secret : str = os.getenv("ACCESS_TOKEN_SECRET")


    def __init__(self):
        self.read_config()
        auth     : tweepy.OAuth1UserHandler = tweepy.OAuth1UserHandler(self.consumer_key,
                                                                       self.consumer_secret,
                                                                       self.access_token,
                                                                       self.access_token_secret)
        self.api : tweepy.API = tweepy.API(auth)


    def post(self, text : str) -> Optional[int]:
        """
        Description:
            Send a tweet with the specified text.
        """

        tweet_id : Optional[int] = None

        if len(text) <= MAX_LENGTH:

            logger.log_info("Tweet:\n" + text)

            try:
                status   = self.api.update_status(text)
                tweet_id = status.id
            except tweepy.TweepyException:
                logger.log_error("error - could not send tweet.")

        else:
            logger.log_error("error - tweet is longer than the maximum length")

        return tweet_id


    def reply(self, text : str, parent_id : Optional[int]) -> Optional[int]:
        """
        Description:
            Send a reply to the given parent tweet with the specified text.
        """

        reply_id : Optional[int] = None

        if parent_id is not None and parent_id > 0:
            if len(text) <= MAX_LENGTH:

                logger.log_info("Reply to tweet " + str(parent_id) + ":\n" + text)

                try:
                    status   = self.api.update_status(status=text, in_reply_to_status_id=parent_id)
                    reply_id = status.id
                except tweepy.TweepyException:
                    logger.log_error("error - could not send reply")

            else:
                logger.log_error("error - tweet is longer than the maximum length")
        else:
            logger.log_error("error - could not reply to tweet with invalid ID: " + str(parent_id))

        return reply_id


    def get_today_posts(self, query : str = "") -> List[tweepy.Tweet]:
        """
        Description:
            Return a list of tweets that were created today. If a query is
            provided, return only tweets that include the query as a substring.
        """

        all_tweets   : List[tweepy.Tweet] = self.api.user_timeline(count=50, exclude_replies=True)
        today_tweets : List[tweepy.Tweet] = []
        period       : timedelta          = timedelta(hours=23, minutes=59)

        for tweet in all_tweets:
            if ((datetime.now(pytz.utc) - tweet.created_at) < period and
                query in tweet.text):
                today_tweets.append(tweet)

        return today_tweets


    def has_posted_today(self, query : str = "") -> bool:
        """
        Description:
            Return a boolean indicating whether or not a tweet has been sent today.
        """
        tweets = self.get_today_posts(query)
        return len(tweets) > 0
