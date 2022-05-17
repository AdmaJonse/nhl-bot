"""
Description:
    This module defines the Game Scheduled event.
"""

from src.events.event import Event

class GameScheduled(Event):
    """
    Description:
        The Game Scheduled event.
    """

    def __str__(self):
        return str(self.event_id) + " = Game Scheduled - " + self.description

    def __eq__(self, other):
        return self.__class__ == other.__class__
