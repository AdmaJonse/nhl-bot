"""
Description:
    This module defines the Penalty event.
"""

from typing import Optional

from src import logger
from src import templates
from src.events.event import Event, get_player_name, get_team, get_value
from src.game_data import GameData

class Penalty(Event):
    """
    Description:
        The Penalty event.
    """

    def __init__(self, data):

        super().__init__(data)

        reason   = get_value(data, "result", "secondaryType")
        severity = get_value(data, "result", "penaltySeverity")

        self._taker    = get_player_name(data, "PenaltyOn")
        self._drawn_by = get_player_name(data, "DrewBy")
        self._reason   = None if reason is None else reason.lower()
        self._severity = None if severity is None else severity.lower()
        self._minutes  = get_value(data, "result", "penaltyMinutes")
        self._team     = get_team(data)
        self._auto_reply = True

        if self._reason == "minor":
            self._reason = None


    def __str__(self):
        return str(self.event_id) + " = Penalty - " + self.description

    def __eq__(self, other):
        return (self.__class__ == other.__class__ and
                self.taker     == other.taker and
                self.drawn_by  == other.drawn_by and
                self.reason    == other.reason and
                self.severity  == other.severity and
                self.minutes   == other.minutes)

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
    def severity(self) -> str:
        """Getter for the severity."""
        return self._severity

    @severity.setter
    def severity(self, severity : str):
        """Setter for the severity."""
        self._severity = severity

    @property
    def minutes(self) -> int:
        """Getter for the minutes."""
        return self._minutes

    @minutes.setter
    def minutes(self, minutes : int):
        """Setter for the minutes."""
        self._minutes = minutes

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
            "penalized_team": game_data.get_team_string(self.team),
            "penalty":        self.reason,
            "player":         self.taker,
            "minutes":        self.minutes,
            "severity":       self.severity,
            "hashtags":       game_data.hashtags
        }
        return templates.PENALTY_TEMPLATE.format(**event_values)


    def get_auto_reply(self, game_data : GameData) -> Optional[str]:
        """
        Description:
            Return the event string for a penalty or penalty shot event.
        """

        text : Optional[str] = None

        # Don't send the auto reply until the initial post has been made
        if not self.has_tweeted:
            return None

        if self.taker is None:
            return None

        if self.reason is None:
            return None

        if self.team is None:
            return None

        if game_data.power_play is None:
            return None

        event_values = {
            "home_team":      game_data.home.location,
            "away_team":      game_data.away.location,
            "home_skaters":   game_data.power_play.home_skaters,
            "away_skaters":   game_data.power_play.away_skaters,
            "time_remaining": game_data.power_play.time_remaining,
            "hashtags":       game_data.hashtags
        }

        if game_data.power_play.team is None:
            text = templates.EVEN_STRENGTH_TEMPLATE.format(**event_values)
        elif game_data.power_play.team == "home":
            text = templates.HOME_POWER_PLAY_TEMPLATE.format(**event_values)
        elif game_data.power_play.team == "away":
            text = templates.AWAY_POWER_PLAY_TEMPLATE.format(**event_values)
        else:
            text = None
        return text
