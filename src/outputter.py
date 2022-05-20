"""
Description:
    This module contains the Outputter class, which is the base class for output interfaces.
"""

from typing import Optional

class Outputter:
    """
    Description:
        The Outputter class is the base class for output interfaces, such as the tweeter and
        printer classes. This class simply defines the interface. Child classes should override
        the methods defined below.
    """

    null_output = None
    has_posted  = False

    def post(self, _text : str) -> Optional[int]:
        """
        Description:
            Print the specified text.
        """
        return self.null_output


    def reply(self, _text : str, _parent_id : int) -> Optional[int]:
        """
        Description:
            Print a reply to the given parent with the specified text.
        """
        return self.null_output


    def has_posted_today(self):
        """
        Description:
            Return a boolean indicating whether or not we've posted today.
        """
        return self.has_posted
