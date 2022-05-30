"""
Description:
    This module defines the Penalty Shot event.
"""

from typing import Optional

from src import logger
from src import templates
from src.events.event import Event, get_player_name, get_team, get_value
from src.game_data import GameData

class PenaltyShot(Event):
    """
    Description:
        The Penalty Shot event.
    """

    def __init__(self, data):
        super().__init__(data)

        reason = get_value(data, "result", "secondaryType")

        self._taker    = get_player_name(data, "PenaltyOn")
        self._drawn_by = get_player_name(data, "DrewBy")
        self._reason   = None if reason is None else reason.lower().replace("ps - ", "")
        self._team     = get_team(data)

    def __str__(self):
        return str(self.event_id) + " = Penalty - " + self.description

    def __eq__(self, other):
        return (self.__class__ == other.__class__ and
                self.taker     == other.taker and
                self.drawn_by  == other.drawn_by and
                self.reason    == other.reason)

    @property
    def taker(self) -> Optional[str]:
        """Getter for the taker."""
        return self._taker

    @taker.setter
    def taker(self, taker : str):
        """Setter for the taker."""
        self._taker = taker

    @property
    def drawn_by(self) -> Optional[str]:
        """Getter for the drawn_by property."""
        return self._drawn_by

    @drawn_by.setter
    def drawn_by(self, drawn_by : str):
        """Setter for the _drawn_by property."""
        self._taker = drawn_by

    @property
    def reason(self) -> str:
        """Getter for the reason."""
        return self._reason

    @reason.setter
    def reason(self, reason : str):
        """Setter for the reason."""
        self._reason = reason

    @property
    def team(self) -> str:
        """Getter for the team."""
        return self._team

    @team.setter
    def team(self, team : str):
        """Setter for the team."""
        self._team = team

    def get_post(self, game_data : GameData) -> Optional[str]:
        """
        Description:
            Return the event string for a penalty or penalty shot event.
        """

        if self.taker is None:
            logger.log_error("Could not determine penalty taker. Delaying tweet.")
            return None

        if self.reason is None:
            logger.log_error("Could not determine penalty. Delaying tweet.")
            return None

        if self.team is None:
            logger.log_error("Could not determine penalized team. Delaying tweet.")
            return None

        event_values = {
            "team":     game_data.get_opposition(self.team),
            "penalty":  self.reason,
            "player":   self.taker,
            "hashtags": game_data.hashtags
        }
        return templates.PENALTY_SHOT_TEMPLATE.format(**event_values)
