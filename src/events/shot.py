"""
Description:
    This module defines the Shot event.
"""

from typing import Optional

from src.events.event import Event, get_player_name
from src.exceptions import InsufficientData

class Shot(Event):
    """
    Description:
        The Shot event.
    """

    def __init__(self, data):
        super().__init__(data)
        self._shooter : Optional[str] = get_player_name(data, "Shooter")
        self._goalie  : Optional[str] = get_player_name(data, "Goalie")

        if self.shooter is None:
            raise InsufficientData

        if self.goalie is None:
            raise InsufficientData

    def __str__(self):
        return str(self.id) + " - " + str(self.time) + " = Shot - " + self.description

    def __eq__(self, other):
        return (isinstance(self, Shot) and
                isinstance(other, Shot) and
                self.period  == other.period and
                self.time    == other.time and
                self.shooter == other.shooter and
                self.goalie  == other.goalie)

    @property
    def code(self) -> str:
        """
        Return a five-character code representing the event type.
        """
        return " SHOT"

    @property
    def shooter(self) -> Optional[str]:
        """Getter for the shooter."""
        return self._shooter

    @shooter.setter
    def shooter(self, shooter : str):
        """Setter for the shooter."""
        self._shooter = shooter

    @property
    def goalie(self) -> Optional[str]:
        """Getter for the goalie."""
        return self._goalie

    @goalie.setter
    def goalie(self, goalie : str):
        """Setter for the goalie."""
        self._goalie = goalie
