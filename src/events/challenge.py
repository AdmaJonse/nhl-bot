"""
This module contains the Challenge event.
"""

from typing import Any, Optional

from src.output import templates
from src.events.event import Event, get_team
from src.exceptions import InsufficientData
from src.data.game_data import GameData
from src.data.line_score import LineScore
from src.utils import pad_blob, pad_code

class Challenge(Event):
    """
    The Challenge event.
    """

    def __init__(self, data : Any):
        super().__init__(data)
        self._team : Optional[str] = get_team(data)

        if self.team is None:
            raise InsufficientData

    def __str__(self):
        return str(self.id) + " - " + str(self.time) + " = Challenge - " + self.description

    def __eq__(self, other):
        return (isinstance(self, Challenge) and
                isinstance(other, Challenge) and
                self.period  == other.period and
                self.time    == other.time)

    @property
    def code(self) -> str:
        """
        Return a seven-character code representing the event type.
        """
        code : str = "CHALLENGE"
        return pad_code(code)

    @property
    def blob(self) -> str:
        """
        Return a unique identifier that describes this specific event.
        """
        return pad_blob(self.team)

    @property
    def team(self) -> Optional[str]:
        """
        Getter for the team.
        """
        return self._team

    @team.setter
    def team(self, team : str):
        """
        Setter for the team.
        """
        self._team = team

    def get_post(self, game_data : GameData, _line_score : LineScore) -> Optional[str]:
        """
        Return the event string for a challenge event.
        """
        event_values = {
            "team":     game_data.get_team_string(self.team),
            "hashtags": game_data.hashtags
        }
        return templates.CHALLENGE_TEMPLATE.format(**event_values)
