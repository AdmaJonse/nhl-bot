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
        return str(self.id) + " - " + str(self.time) + " = Game Scheduled - " + self.description

    def __eq__(self, other):
        return (isinstance(self, GameScheduled) and
                isinstance(other, GameScheduled))

    @property
    def code(self) -> str:
        """
        Return a five-character code representing the event type.
        """
        return "GMSCD"
