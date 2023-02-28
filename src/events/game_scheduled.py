"""
This module defines the Game Scheduled event.
"""

from src.events.event import Event
from src.utils import pad_code

class GameScheduled(Event):
    """
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
        Return a seven-character code representing the event type.
        """
        code : str = "GAMESCHEDULED"
        return pad_code(code)

    @property
    def id(self) -> str:
        return "GAME-SCHEDULED"
