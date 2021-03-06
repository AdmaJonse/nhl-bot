"""
Description:
    This module defines the Period Start event.
"""

from typing import Optional

from src import templates
from src.events.event import Event
from src.game_data import GameData
from src.utils import pad_code

class PeriodStart(Event):
    """
    Description:
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
        return "PER" + str(self.period) + "-START"

    def get_post(self, game_data : GameData) -> Optional[str]:
        """
        Description:
            Return the event string for a period start event.
        """
        event_values = {
            "period":   self.get_period_string(),
            "venue":    game_data.venue,
            "city":     game_data.city,
            "hashtags": game_data.hashtags
        }
        return templates.PERIOD_START_TEMPLATE.format(**event_values)
