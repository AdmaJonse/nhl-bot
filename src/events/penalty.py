"""
This module defines the Penalty event.
"""

from typing import Optional

from src.logger import log
from src.output import templates
from src.events.event import Event, get_player_name, get_team, get_value
from src.exceptions import InsufficientData
from src.data.game_data import GameData
from src.data.line_score import LineScore
from src.utils import initials, pad_blob, pad_code

class Penalty(Event):
    """
    The Penalty event.
    """

    def __init__(self, data):

        super().__init__(data)

        reason   = get_value(data, "result", "secondaryType")
        severity = get_value(data, "result", "penaltySeverity")

        self._taker      : Optional[str] = get_player_name(data, "PenaltyOn")
        self._drawn_by   : Optional[str] = get_player_name(data, "DrewBy")
        self._reason     : Optional[str] = None if reason is None else reason.lower()
        self._severity   : Optional[str] = None if severity is None else severity.lower()
        self._minutes    : Optional[int] = get_value(data, "result", "penaltyMinutes")
        self._team       : Optional[str] = get_team(data)
        self._auto_reply : bool          = False

        if self.reason == "minor":
            self.reason = None

        if self.reason is not None and self._reason == "missing key [pd_151]":
            self.reason = "delaying game - unsuccessful challenge"

        if self.taker is None:
            raise InsufficientData

        if self.reason is None:
            raise InsufficientData

        if self.severity is None:
            raise InsufficientData

        if self.minutes is None:
            raise InsufficientData

        if self.team is None:
            raise InsufficientData

    def __str__(self):
        return str(self.id) + " - " + str(self.time) + " = Penalty - " + self.description

    def __eq__(self, other):
        return (isinstance(self, Penalty) and
                isinstance(other, Penalty) and
                self.period   == other.period and
                self.time     == other.time and
                self.taker    == other.taker and
                self.drawn_by == other.drawn_by and
                self.reason   == other.reason and
                self.severity == other.severity and
                self.minutes  == other.minutes)

    @property
    def code(self) -> str:
        """
        Return a seven-character code representing the event type.
        """
        code : str = "PENALTY"
        return pad_code(code)

    @property
    def blob(self) -> str:
        """
        Return a unique identifier that describes this specific event.
        """
        taker  : str = initials(self.taker)
        drawn  : str = initials(self.drawn_by)
        reason : str = initials(self.reason)[:2]
        blob   : str = taker + drawn + reason
        return pad_blob(blob)

    @property
    def taker(self) -> Optional[str]:
        """
        Getter for the taker.
        """
        return self._taker

    @taker.setter
    def taker(self, taker : str):
        """
        Setter for the taker.
        """
        self._taker = taker

    @property
    def drawn_by(self) -> Optional[str]:
        """
        Getter for the drawn_by property.
        """
        return self._drawn_by

    @drawn_by.setter
    def drawn_by(self, drawn_by : str):
        """
        Setter for the _drawn_by property.
        """
        self._taker = drawn_by

    @property
    def reason(self) -> Optional[str]:
        """
        Getter for the reason.
        """
        return self._reason

    @reason.setter
    def reason(self, reason : str):
        """
        Setter for the reason.
        """
        self._reason = reason

    @property
    def severity(self) -> Optional[str]:
        """
        Getter for the severity.
        """
        return self._severity

    @severity.setter
    def severity(self, severity : str):
        """
        Setter for the severity.
        """
        self._severity = severity

    @property
    def minutes(self) -> Optional[int]:
        """
        Getter for the minutes.
        """
        return self._minutes

    @minutes.setter
    def minutes(self, minutes : int):
        """
        Setter for the minutes.
        """
        self._minutes = minutes

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
        Return the event string for a penalty or penalty shot event.
        """

        if self.taker is None:
            log.error("Could not determine penalty taker. Delaying tweet.")
            return None

        if self.reason is None:
            log.error("Could not determine penalty. Delaying tweet.")
            return None

        if self.team is None:
            log.error("Could not determine penalized team. Delaying tweet.")
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
