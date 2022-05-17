"""
Description:
    This module defines the Missed Shot event.
"""

from typing import Optional

from src.events.event import Event, get_player_name

class MissedShot(Event):
    """
    Description:
        The Missed Shot event.
    """

    def __init__(self, data):
        super().__init__(data)
        self._shooter = get_player_name(data, "Shooter")
        self._goalie  = get_player_name(data, "Unknown")

    def __str__(self):
        return str(self.event_id) + " = Missed Shot - " + self.description

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