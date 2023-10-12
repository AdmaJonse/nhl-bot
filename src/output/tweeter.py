"""
This module provides an interface to Twitter than can be used to
    authenticate, tweet and reply.
"""

from typing import List, Optional
import os
from os.path import join, dirname, abspath
from dotenv import load_dotenv
import tweepy

from src.logger import log
from src.output.outputter import Outputter

# maximum tweet length
MAX_LENGTH = 240 # characters

class Tweeter(Outputter):
    """
    This class provides an interface to Twitter than can be used to
        authenticate, tweet and reply.
    """

    def read_config(self):
        """
        Read authentication details from the .env file.
        """

        # load constants from .env
        parent_dir  : str = dirname(dirname(dirname(abspath(__file__))))
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
        self.client : tweepy.Client = tweepy.Client(bearer_token=self.bearer_token,
                                                    consumer_key=self.consumer_key,
                                                    consumer_secret=self.consumer_secret,
                                                    access_token=self.access_token,
                                                    access_token_secret=self.access_token_secret)


    def post(self, text : str) -> Optional[int]:
        """
        Send a tweet with the specified text.
        """

        tweet_id : Optional[int] = None

        if len(text) <= MAX_LENGTH:

            log.info("Tweet:\n" + text)

            try:
                status   = self.client.create_tweet(text=text)
                tweet_id = status.data['id']
            except tweepy.TweepyException:
                log.error("error - could not send tweet")

        else:
            log.error("error - tweet is longer than the maximum length")

        return tweet_id


    def reply(self, parent : Optional[int], text : str) -> Optional[int]:
        """
        Send a reply to the given parent tweet with the specified text.
        """

        reply_id : Optional[int] = None

        if parent is not None and parent > 0:
            if len(text) <= MAX_LENGTH:

                log.info("Reply to tweet " + str(parent) + ":\n" + text)

                try:
                    status   = self.client.create_tweet(text=text, in_reply_to_tweet_id=parent)
                    reply_id = status.data['id']
                except tweepy.TweepyException:
                    log.error("error - could not send reply")

            else:
                log.error("error - tweet is longer than the maximum length")
        else:
            log.error("error - could not reply to tweet with invalid ID: " + str(parent))

        return reply_id


    # pylint: disable=R0201
    def upload_video(self, _url : str) -> Optional[str]:
        """
        Download the .mp4 from the given URL, perform a media upload, clean up and then
        return the media ID string.
        """
        return None


    def post_with_media(self, _text : str, _media : str) -> Optional[int]:
        """
        Send a tweet with the specified text.
        """
        return None


    def reply_with_media(self, _parent : Optional[int], _text : str, _media : str) -> Optional[int]:
        """
        Send a reply to the given parent tweet with the specified text.
        """
        return None


    # pylint: disable=R0201
    def get_today_posts(self, _query : str = "") -> List[tweepy.Tweet]:
        """
        Return a list of tweets that were created today. If a query is
        provided, return only tweets that include the query as a substring.
        """
        return []


    def has_posted_today(self, _query : str = "") -> bool:
        """
        Return a boolean indicating whether or not a tweet has been sent today.
        """
        return True
