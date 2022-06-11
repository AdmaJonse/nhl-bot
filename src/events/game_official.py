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
        return str(self.id) + " - " + str(self.time) + " = Game Official - " + self.description

    def __eq__(self, other):
        return (isinstance(self, GameOfficial) and
                isinstance(other, GameOfficial))

    @property
    def id(self) -> str:
        return "GAME-OFFICIAL"
