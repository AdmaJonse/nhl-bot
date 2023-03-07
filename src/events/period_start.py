"""
This module defines the Period Start event.
"""

from typing import Optional

from src.output import templates
from src.events.event import Event
from src.data.game_data import GameData
from src.data.line_score import LineScore
from src.utils import pad_code

class PeriodStart(Event):
    """
    The Period Start event.
    """

    def __str__(self):
        return str(self.id) + " - " + str(self.time) + " = Period Start - " + self.description

    def __eq__(self, other):
        return (isinstance(self, PeriodStart) and
                isinstance(other, PeriodStart) and
                self.period == other.period)

    @property
    def code(self) -> str:
        """
        Return a seven-character code representing the event type.
        """
        code : str = "PERSTART"
        return pad_code(code)

    @property
    def id(self) -> str:
        return "PER" + str(self.period.number) + "-START"

    def get_post(self, game_data : GameData, _line_score : LineScore) -> Optional[str]:
        """
        Return the event string for a period start event.
        """
        event_values = {
            "period":   str(self.period),
            "venue":    game_data.venue,
            "hashtags": game_data.hashtags
        }
        return templates.PERIOD_START_TEMPLATE.format(**event_values)
