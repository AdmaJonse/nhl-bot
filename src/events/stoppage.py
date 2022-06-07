"""
Description:
    This module defines the Stoppage event.
"""

from src.events.event import Event

class Stoppage(Event):
    """
    Description:
        The Stoppage event.
    """

    def __str__(self):
        return str(self.time) + " = Stoppage - " + self.description

    def __eq__(self, other):
        return (isinstance(self, Stoppage) and
                isinstance(other, Stoppage) and
                self.period  == other.period and
                self.time    == other.time)
