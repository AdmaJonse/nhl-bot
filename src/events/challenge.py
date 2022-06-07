"""
Description:
    This module contains the Challenge event.
"""

from typing import Any, Optional

from src import templates
from src.events.event import Event, get_team
from src.exceptions import InsufficientData
from src.game_data import GameData

class Challenge(Event):
    """
    Description:
        The Challenge event.
    """

    def __init__(self, data : Any):
        super().__init__(data)
        self._team : Optional[str] = get_team(data)

        if self.team is None:
            raise InsufficientData

    def __str__(self):
        return str(self.time) + " = Challenge - " + self.description

    def __eq__(self, other):
        return (isinstance(self, Challenge) and
                isinstance(other, Challenge) and
                self.period  == other.period and
                self.time    == other.time)

    @property
    def team(self) -> Optional[str]:
        """Getter for the team."""
        return self._team

    @team.setter
    def team(self, team : str):
        """Setter for the team."""
        self._team = team

    def get_post(self, game_data : GameData) -> Optional[str]:
        """
        Description:
            Return the event string for a challenge event.
        """
        event_values = {
            "team":     game_data.get_team_string(self.team),
            "hashtags": game_data.hashtags
        }
        return templates.CHALLENGE_TEMPLATE.format(**event_values)
