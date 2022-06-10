"""
Description:
    This module defines the Hit event.
"""

from typing import Optional

from src.events.event import Event, get_player_name
from src.exceptions import InsufficientData

class Hit(Event):
    """
    Description:
        The Hit event.
    """

    def __init__(self, data):
        super().__init__(data)
        self._hitter : Optional[str] = get_player_name(data, "Hitter")
        self._hittee : Optional[str] = get_player_name(data, "Hittee")

        if self.hitter is None:
            raise InsufficientData

        if self.hittee is None:
            raise InsufficientData

    def __str__(self):
        return str(self.id) + " - " + str(self.time) + " = Hit - " + self.description

    def __eq__(self, other):
        return (isinstance(self, Hit) and
                isinstance(other, Hit) and
                self.period == other.period and
                self.time   == other.time and
                self.hitter == other.hitter and
                self.hittee == other.hittee)

    @property
    def code(self) -> str:
        """
        Return a four letter code representing the event type.
        """
        return "  HIT"

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
