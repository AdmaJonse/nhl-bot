"""
Description:
    This module contains the Outputter class, which is the base class for output interfaces.
"""

from abc import ABC, abstractmethod
from typing import Optional

class Outputter(ABC):
    """
    Description:
        The Outputter class is the base class for output interfaces, such as the tweeter and
        printer classes.
    """

    @abstractmethod
    def post(self, _text : str) -> Optional[int]:
        """
        Description:
            Print the specified text.
        """

    @abstractmethod
    def reply(self, _text : str, _parent_id : Optional[int]) -> Optional[int]:
        """
        Description:
            Print a reply to the given parent with the specified text.
        """

    @abstractmethod
    def has_posted_today(self, _query : str = ""):
        """
        Description:
            Return a boolean indicating whether or not we've posted today.
        """
