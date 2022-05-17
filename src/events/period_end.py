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
        return str(self.event_id) + " = Period End - " + self.description

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.period == other.period

    def get_post(self, game_data : GameData) -> Optional[str]:
        """
        Description:
            Return the event string for a period end event.
        """

        event_values = {
            "period":     self.get_period_string(),
            "venue":      game_data.venue,
            "home_team":  game_data.home.location,
            "away_team":  game_data.away.location,
            "home_goals": self.home_goals,
            "away_goals": self.away_goals,
            "home_shots": game_data.home_shots,
            "away_shots": game_data.away_shots,
            "hashtags":   game_data.hashtags
        }
        return templates.PERIOD_END_TEMPLATE.format(**event_values)