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
        return str(self.event_id) + " = Stoppage - " + self.description
