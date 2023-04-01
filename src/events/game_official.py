"""
This module defines the Game Official event.
"""

from src.events.event import Event
from src.utils import pad_code

class GameOfficial(Event):
    """
    The Game Official event.
    """

    def __str__(self):
        return str(self.id) + " - " + str(self.time) + " = Game Official - " + self.description

    def __eq__(self, other):
        return (isinstance(self, GameOfficial) and
                isinstance(other, GameOfficial))

    @property
    def code(self) -> str:
        """
        Return a seven-character code representing the event type.
        """
        code : str = "GAMEOFF"
        return pad_code(code)

    @property
    def id(self) -> str:
        return "GAME-OFFICIAL"
