"""
This module defines the Shot event.
"""

from typing import Optional

from src import logger
from src.output import templates
from src.events.event import Event, get_player_name, get_team
from src.exceptions import InsufficientData
from src.data.game_data import GameData
from src.utils import initials, pad_blob, pad_code

class FailedShot(Event):
    """
    The Failed Shot event.
    """

    def __init__(self, data):
        super().__init__(data)
        self._team    : Optional[str] = get_team(data)
        self._shooter : Optional[str] = get_player_name(data, "Unknown", 1)
        self._goalie  : Optional[str] = get_player_name(data, "Unknown", 2)

        if self.team is None:
            raise InsufficientData

        if self.shooter is None:
            raise InsufficientData

        if self.goalie is None:
            raise InsufficientData


    def __str__(self):
        return str(self.id) + " - " + str(self.time) + " = Failed Shot - " + self.description

    def __eq__(self, other):
        return (isinstance(self, FailedShot) and
                isinstance(other, FailedShot) and
                self.shooter == other.shooter and
                self.goalie  == other.goalie and
                self.team    == other.team)

    @property
    def code(self) -> str:
        """
        Return a seven-character code representing the event type.
        """
        code : str = "FAILSHT"
        return pad_code(code)

    @property
    def blob(self) -> str:
        """
        Return a unique identifier that describes this specific event.
        """
        shooter : str = initials(self.shooter)
        goalie  : str = initials(self.goalie)
        blob    : str = shooter + "ON" + goalie
        return pad_blob(blob)

    @property
    def shooter(self) -> Optional[str]:
        """
        Getter for the shooter.
        """
        return self._shooter

    @shooter.setter
    def shooter(self, shooter : str):
        """
        Setter for the shooter.
        """
        self._shooter = shooter

    @property
    def goalie(self) -> Optional[str]:
        """
        Getter for the goalie.
        """
        return self._goalie

    @goalie.setter
    def goalie(self, goalie : str):
        """
        Setter for the goalie.
        """
        self._goalie = goalie

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


    def get_post(self, game_data : GameData) -> Optional[str]:
        """
        Return the event string for a failed shot event.
        """

        if self.team is None:
            logger.log_error("Could not determine team. Delaying tweet.")
            return None

        if self.shooter is None:
            logger.log_error("Could not determine shooter. Delaying tweet.")
            return None

        if self.goalie is None:
            logger.log_error("Could not determine goalie. Delaying tweet.")
            return None

        event_values = {
            "team":     game_data.get_team_string(self.team),
            "shooter":  self.shooter,
            "goalie":   self.goalie,
            "hashtags": game_data.hashtags
        }
        return templates.SHOOTOUT_MISS_TEMPLATE.format(**event_values)
