"""
Description:
    This is an output interface intended for dry runs. Rather than tweeting, it will
    simply print the any tweets to the logs.
"""

import uuid
from src import logger
from src.outputter import Outputter

# pylint: disable=R0201

class Printer(Outputter):
    """
    Description:
        This class provides an interface to Twitter than can be used to
        authenticate, tweet and reply.
    """

    def post(self, text):
        """
        Description:
            Print the specified text.
        """
        tweet_id = uuid.uuid1().int
        logger.log_info("Tweet:\n" + text)
        return tweet_id


    def reply(self, text, parent_id):
        """
        Description:
            Print a reply to the given parent with the specified text.
        """
        reply_id = uuid.uuid1().int
        if parent_id > 0:
            logger.log_info("Reply to parent " + str(parent_id) + "\n: " + text)
        return reply_id
