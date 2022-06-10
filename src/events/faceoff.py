"""
Description:
    This module defines the Faceoff event.
"""

from typing import Any, Optional

from src.events.event import Event, get_player_name
from src.exceptions import InsufficientData

class Faceoff(Event):
    """
    Description:
        The Faceoff event.
    """

    def __init__(self, data : Any):
        super().__init__(data)
        self._winner : Optional[str] = get_player_name(data, "Winner")
        self._loser  : Optional[str] = get_player_name(data, "Loser")

        if self.winner is None:
            raise InsufficientData

        if self.loser is None:
            raise InsufficientData

    def __str__(self):
        return str(self.id) + " - " + str(self.time) + " = Faceoff - " + self.description

    def __eq__(self, other):
        return (isinstance(self, Faceoff) and
                isinstance(other, Faceoff) and
                self.period == other.period and
                self.time   == other.time and
                self.winner == other.winner and
                self.loser  == other.loser)

    @property
    def code(self) -> str:
        """
        Return a four letter code representing the event type.
        """
        return "FCOFF"

    @property
    def winner(self) -> Optional[str]:
        """Getter for the winner."""
        return self._winner

    @winner.setter
    def winner(self, winner : str):
        """Setter for the winner."""
        self._winner = winner

    @property
    def loser(self) -> Optional[str]:
        """Getter for the loser."""
        return self._loser

    @loser.setter
    def loser(self, loser : str):
        """Setter for the loser."""
        self._loser = loser
