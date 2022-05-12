"""
Description:
    This module defines the output method.
"""

from src.printer import Printer
from src.tweeter import Tweeter

DRY_RUN = False

if DRY_RUN:
    outputter = Printer()
else:
    outputter = Tweeter()


def post(text):
    """
    Description:
        Public function that will send a tweet with the specified text.
    """
    return outputter.post(text)


def reply(text, parent_id):
    """
    Description:
        Public function that will send a reply with the specified text to the
        tweet with the given parent_id.
    """
    return outputter.reply(text, parent_id)
