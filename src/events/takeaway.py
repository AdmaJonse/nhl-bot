"""
Description:
    This module defines the Takeaway event.
"""

from typing import Optional

from src.events.event import Event, get_player_name
from src.exceptions import InsufficientData
from src.utils import initials, pad

class Takeaway(Event):
    """
    Description:
        The Takeaway event.
    """

    def __init__(self, data):
        super().__init__(data)
        self._player : Optional[str] = get_player_name(data, "PlayerID")

        if self.player is None:
            raise InsufficientData

    def __str__(self):
        return str(self.id) + " - " + str(self.time) + " = Takeaway - " + self.description

    def __eq__(self, other):
        return (isinstance(self, Takeaway) and
                isinstance(other, Takeaway) and
                self.period  == other.period and
                self.time    == other.time and
                self.player  == other.player)

    @property
    def code(self) -> str:
        """
        Return a five-character code representing the event type.
        """
        return " TAKE"

    @property
    def blob(self) -> str:
        """
        Return a unique identifier that describes this specific event.
        """
        blob : str = initials(self.player)
        return pad(blob, 6)

    @property
    def player(self) -> Optional[str]:
        """Getter for the player."""
        return self._player

    @player.setter
    def player(self, player : str):
        """Setter for the player."""
        self._player = player
