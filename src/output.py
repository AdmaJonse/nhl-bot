"""
Description:
    This module defines the output method.
"""

from typing import Optional

from src.outputter import Outputter
from src.printer import Printer
from src.tweeter import Tweeter

DRY_RUN = False

outputter : Outputter = Tweeter()

if DRY_RUN:
    outputter = Printer()


def post(text : str) -> Optional[int]:
    """
    Description:
        Public function that will send a tweet with the specified text.
    """
    return outputter.post(text)


def reply(text : str, parent_id : int) -> Optional[int]:
    """
    Description:
        Public function that will send a reply with the specified text to the
        tweet with the given parent_id.
    """
    return outputter.reply(text, parent_id)
