"""
Description:
    This module contains the Blocked Shot event.
"""

from typing import Any

from src.events.event import Event, get_player_name

class BlockedShot(Event):
    """
    Description:
        The Blocked Shot event.
    """

    def __init__(self, data : Any):
        super().__init__(data)
        self._shooter = get_player_name(data, "Shooter")
        self._blocker = get_player_name(data, "Blocker")

    def __str__(self):
        return str(self.event_id) + " = Blocked Shot - " + self.description

    @property
    def shooter(self) -> str:
        """Getter for the shooter."""
        return self._shooter

    @shooter.setter
    def shooter(self, shooter : str):
        """Setter for the shooter."""
        self._shooter = shooter

    @property
    def blocker(self) -> str:
        """Getter for the blocker."""
        return self._blocker

    @blocker.setter
    def blocker(self, blocker : str):
        """Setter for the blocker."""
        self._blocker = blocker
