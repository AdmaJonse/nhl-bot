"""
Description:
    This module defines the Game Official event.
"""

from src.events.event import Event

class GameOfficial(Event):
    """
    Description:
        The Game Official event.
    """

    def __str__(self):
        return str(self.event_id) + " = Game Official - " + self.description

    def __eq__(self, other):
        return self.__class__ == other.__class__
