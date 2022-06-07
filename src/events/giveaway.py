"""
Description:
    This module defines the Giveaway event.
"""

from typing import Optional

from src.events.event import Event, get_player_name
from src.exceptions import InsufficientData

class Giveaway(Event):
    """
    Description:
        The Giveaway event.
    """

    def __init__(self, data):
        super().__init__(data)
        self._player : Optional[str] = get_player_name(data, "PlayerID")

        if self.player is None:
            raise InsufficientData

    def __str__(self):
        return str(self.time) + " = Giveaway - " + self.description

    def __eq__(self, other):
        return (isinstance(self, Giveaway) and
                isinstance(other, Giveaway) and
                self.period == other.period and
                self.time   == other.time and
                self.player == other.player)

    @property
    def player(self) -> Optional[str]:
        """Getter for the player."""
        return self._player

    @player.setter
    def player(self, player : str):
        """Setter for the player."""
        self._player = player
