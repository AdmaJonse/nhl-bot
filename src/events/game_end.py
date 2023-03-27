"""
This module defines the Game End event.
"""

from src.events.event import Event
from src.utils import pad_code


class GameEnd(Event):
    """
    The Game End event.
    """

    def __str__(self):
        return str(self.id) + " - " + str(self.time) + " = Game End - " + self.description

    def __eq__(self, other):
        return (isinstance(self, GameEnd) and
                isinstance(other, GameEnd))

    @property
    def code(self) -> str:
        """
        Return a seven-character code representing the event type.
        """
        code: str = "GAMEEND"
        return pad_code(code)

    @property
    def id(self) -> str:
        return "GAME-END"
