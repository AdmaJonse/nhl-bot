"""
Description:
    This module contains the Blocked Shot event.
"""

from typing import Any, Optional

from src.events.event import Event, get_player_name
from src.exceptions import InsufficientData

class BlockedShot(Event):
    """
    Description:
        The Blocked Shot event.
    """

    def __init__(self, data : Any):
        super().__init__(data)
        self._shooter : Optional[str] = get_player_name(data, "Shooter")
        self._blocker : Optional[str] = get_player_name(data, "Blocker")

        if self.shooter is None:
            raise InsufficientData

        if self.blocker is None:
            raise InsufficientData

    def __str__(self):
        return str(self.time) + " = Blocked Shot - " + self.description

    def __eq__(self, other):
        return (isinstance(self, BlockedShot) and
                isinstance(other, BlockedShot) and
                self.period  == other.period and
                self.time    == other.time and
                self.shooter == other.shooter and
                self.blocker == other.blocker)

    @property
    def shooter(self) -> Optional[str]:
        """Getter for the shooter."""
        return self._shooter

    @shooter.setter
    def shooter(self, shooter : str):
        """Setter for the shooter."""
        self._shooter = shooter

    @property
    def blocker(self) -> Optional[str]:
        """Getter for the blocker."""
        return self._blocker

    @blocker.setter
    def blocker(self, blocker : str):
        """Setter for the blocker."""
        self._blocker = blocker
