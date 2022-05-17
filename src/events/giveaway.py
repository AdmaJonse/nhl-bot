"""
Description:
    This module defines the Giveaway event.
"""

from src.events.event import Event, get_player_name

class Giveaway(Event):
    """
    Description:
        The Giveaway event.
    """

    def __init__(self, data):
        super().__init__(data)
        self._player = get_player_name(data, "PlayerID")

    def __str__(self):
        return str(self.event_id) + " = Giveaway - " + self.description

    @property
    def player(self) -> str:
        """Getter for the player."""
        return self._player

    @player.setter
    def player(self, player : str):
        """Setter for the player."""
        self._player = player
