"""
This module defines the Period End event.
"""

from typing import Optional

from src.output import templates
from src.events.event import Event
from src.data.game_data import GameData
from src.data.line_score import LineScore
from src.utils import pad_code

class PeriodEnd(Event):
    """
    The Period End event.
    """

    def __str__(self):
        return str(self.id) + " - " + str(self.time) + " = Period End - " + self.description

    def __eq__(self, other):
        return (isinstance(self, PeriodEnd) and
                isinstance(other, PeriodEnd) and
                self.period == other.period)

    @property
    def code(self) -> str:
        """
        Return a seven-character code representing the event type.
        """
        code : str = "PEREND"
        return pad_code(code)

    @property
    def id(self) -> str:
        return "PER" + str(self.period.number) + "-END"

    def get_post(self, game_data : GameData, line_score : LineScore) -> Optional[str]:
        """
        Return the event string for a period end event.
        """

        event_values = {
            "period":     str(self.period),
            "venue":      game_data.venue,
            "home_team":  game_data.home.location,
            "away_team":  game_data.away.location,
            "home_goals": self.score.home_goals,
            "away_goals": self.score.away_goals,
            "home_shots": line_score.home_shots,
            "away_shots": line_score.away_shots,
            "hashtags":   game_data.hashtags
        }
        return templates.PERIOD_END_TEMPLATE.format(**event_values)
