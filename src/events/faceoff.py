"""
Description:
    This module defines the Faceoff event.
"""

from typing import Any

from src.events.event import Event, get_player_name

class Faceoff(Event):
    """
    Description:
        The Faceoff event.
    """

    def __init__(self, data : Any):
        super().__init__(data)
        self._winner = get_player_name(data, "Winner")
        self._loser  = get_player_name(data, "Loser")

    def __str__(self):
        return str(self.event_id) + " = Faceoff - " + self.description

    @property
    def winner(self) -> str:
        """Getter for the winner."""
        return self._winner

    @winner.setter
    def winner(self, winner : str):
        """Setter for the winner."""
        self._winner = winner

    @property
    def loser(self) -> str:
        """Getter for the loser."""
        return self._loser

    @loser.setter
    def loser(self, loser : str):
        """Setter for the loser."""
        self._loser = loser
