"""
This module contains the Outputter class, which is the base class for output interfaces.
"""

from abc import ABC, abstractmethod
from typing import Optional

class Outputter(ABC):
    """
    The Outputter class is the base class for output interfaces, such as the tweeter and
        printer classes.
    """

    @abstractmethod
    def post(self, _text : str) -> Optional[int]:
        """
        Print the specified text.
        """

    @abstractmethod
    def reply(self, _parent : Optional[int], _text : str) -> Optional[int]:
        """
        Print a reply to the given parent with the specified text.
        """

    @abstractmethod
    def post_with_media(self, _text : str, _media : str) -> Optional[int]:
        """
        Send a tweet with the specified text and media attachement.
        """

    @abstractmethod
    def reply_with_media(self, _parent : Optional[int], _text : str, _media : str) -> Optional[int]:
        """
        Send a reply to the given parent with the specified text and media attachement.
        """

    @abstractmethod
    def has_posted_today(self, _query : str = "") -> bool:
        """
        Return a boolean indicating whether or not we've posted today.
        """
