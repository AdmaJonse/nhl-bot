"""
Description:
    This module defines the output method.
"""

from typing import Optional

from src.outputter import Outputter
from src.printer import Printer
from src.tweeter import Tweeter

class Output:
    """
    Description:
        This class defines the output method to be used and any internal state of the
        output interface.
    """

    def __init__(self):
        self._dry_run   : bool      = False
        self._outputter : Outputter = Tweeter()

        if self.dry_run:
            self._outputter = Printer()
        else:
            self._outputter = Tweeter()


    @property
    def dry_run(self) -> bool:
        """
        Description:
            Return a boolean indicating whether or not we're in dry run mode.
        """
        return self._dry_run


    @dry_run.setter
    def dry_run(self, flag : bool):
        """
        Description:
            Set the dry run flag.
        """
        self._dry_run = flag

        if self.dry_run:
            self._outputter = Printer()
        else:
            self._outputter = Tweeter()


    @property
    def outputter(self) -> Outputter:
        """
        Description:
            Return the registered outputter instance.
        """
        return self._outputter


output = Output()


def post(text : str) -> Optional[int]:
    """
    Description:
        Public function that will send a tweet with the specified text.
    """
    return output.outputter.post(text)


def reply(text : str, parent_id : Optional[int]) -> Optional[int]:
    """
    Description:
        Public function that will send a reply with the specified text to the
        tweet with the given parent_id.
    """
    return output.outputter.reply(text, parent_id)


def has_posted_today() -> bool:
    """
    Description:
        Return a boolean indicating whether or not we've posted today.
    """
    return output.outputter.has_posted_today()
