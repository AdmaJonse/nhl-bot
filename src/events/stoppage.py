"""
Description:
    This module defines the Stoppage event.
"""

from src.events.event import Event
from src.utils import pad

class Stoppage(Event):
    """
    Description:
        The Stoppage event.
    """

    def __str__(self):
        return str(self.id) + " - " + str(self.time) + " = Stoppage - " + self.description

    def __eq__(self, other):
        return (isinstance(self, Stoppage) and
                isinstance(other, Stoppage) and
                self.period  == other.period and
                self.time    == other.time)

    @property
    def code(self) -> str:
        """
        Return a five-character code representing the event type.
        """
        return " STOP"

    @property
    def blob(self) -> str:
        """
        Return a unique identifier that describes this specific event.
        """
        return pad(self.description, 6)
