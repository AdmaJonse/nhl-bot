"""
Description:
    This is an output interface intended for dry runs. Rather than tweeting, it will
    simply print the any tweets to the logs.
"""

import uuid
from typing import Optional

from src import logger
from src.outputter import Outputter

class Printer(Outputter):
    """
    Description:
        This class provides an interface to Twitter than can be used to
        authenticate, tweet and reply.
    """

    def post(self, text : str) -> Optional[int]:
        """
        Description:
            Print the specified text.
        """
        tweet_id : Optional[int] = uuid.uuid1().int
        logger.log_info("Tweet:\n" + text)
        return tweet_id


    def reply(self, text, parent_id : Optional[int]) -> Optional[int]:
        """
        Description:
            Print a reply to the given parent with the specified text.
        """
        reply_id : Optional[int] = uuid.uuid1().int
        if parent_id is not None and parent_id > 0:
            logger.log_info("Reply to parent " + str(parent_id) + ":\n" + text)
        return reply_id


    def has_posted_today(self, _query : str = ""):
        """
        Description:
            Return a boolean indicating whether or not we've posted today.
        """
        return True
