"""
Description:
    This module defines the Period End event.
"""

from typing import Optional

from src import templates
from src.events.event import Event
from src.game_data import GameData

class PeriodEnd(Event):
    """
    Description:
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
        Return a five-character code representing the event type.
        """
        return "PDEND"

    def get_post(self, game_data : GameData) -> Optional[str]:
        """
        Description:
            Return the event string for a period end event.
        """

        event_values = {
            "period":     self.get_period_string(),
            "venue":      game_data.venue,
            "city":       game_data.city,
            "home_team":  game_data.home.location,
            "away_team":  game_data.away.location,
            "home_goals": self.home_goals,
            "away_goals": self.away_goals,
            "home_shots": game_data.home_shots,
            "away_shots": game_data.away_shots,
            "hashtags":   game_data.hashtags
        }
        return templates.PERIOD_END_TEMPLATE.format(**event_values)
