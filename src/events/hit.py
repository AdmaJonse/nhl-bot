"""
Description:
    This module defines the Hit event.
"""

from typing import Optional

from src.events.event import Event, get_player_name

class Hit(Event):
    """
    Description:
        The Hit event.
    """

    def __init__(self, data):
        super().__init__(data)
        self._hitter = get_player_name(data, "Hitter")
        self._hittee = get_player_name(data, "Hittee")

    def __str__(self):
        return str(self.event_id) + " = Hit - " + self.description

    @property
    def hitter(self) -> Optional[str]:
        """Getter for the hitter."""
        return self._hitter

    @hitter.setter
    def hitter(self, hitter : str):
        """Setter for the hitter."""
        self._hitter = hitter

    @property
    def hittee(self) -> Optional[str]:
        """Getter for the hittee."""
        return self._hittee

    @hittee.setter
    def hittee(self, hittee : str):
        """Setter for the hittee."""
        self._hittee = hittee
