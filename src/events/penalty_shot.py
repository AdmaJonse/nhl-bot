"""
This module defines the Penalty Shot event.
"""

from typing import Optional

from src.logger import log
from src.output import templates
from src.events.event import Event, get_player_name, get_team, get_value
from src.exceptions import InsufficientData
from src.data.game_data import GameData
from src.data.line_score import LineScore
from src.utils import initials, pad_blob, pad_code

class PenaltyShot(Event):
    """
    The Penalty Shot event.
    """

    def __init__(self, data):
        super().__init__(data)

        reason = get_value(data, "result", "secondaryType")

        self._taker    : Optional[str] = get_player_name(data, "PenaltyOn")
        self._drawn_by : Optional[str] = get_player_name(data, "DrewBy")
        self._reason   : Optional[str] = None
        self._team     : Optional[str] = get_team(data)

        if reason is not None:
            self._reason = reason.lower().replace("ps - ", "")

        if self.taker is None:
            raise InsufficientData

        if self.reason is None:
            raise InsufficientData

        if self.team is None:
            raise InsufficientData

    def __str__(self):
        return str(self.id) + " - " + str(self.time) + " = Penalty - " + self.description

    def __eq__(self, other):
        return (isinstance(self, PenaltyShot) and
                isinstance(other, PenaltyShot) and
                self.period   == other.period and
                self.time     == other.time and
                self.taker    == other.taker and
                self.drawn_by == other.drawn_by and
                self.reason   == other.reason)

    @property
    def code(self) -> str:
        """
        Return a seven-character code representing the event type.
        """
        code : str = "PENSHOT"
        return pad_code(code)

    @property
    def blob(self) -> str:
        """
        Return a unique identifier that describes this specific event.
        """
        taker : str = initials(self.taker)
        drawn : str = initials(self.drawn_by)
        blob  : str = taker + "ON" + drawn
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
            "team":     game_data.get_opposition(self.team),
            "penalty":  self.reason,
            "player":   self.taker,
            "hashtags": game_data.hashtags
        }
        return templates.PENALTY_SHOT_TEMPLATE.format(**event_values)
