"""
Description:
    This module defines the Game End event.
"""

from typing import Optional

from src import templates
from src.events.event import Event
from src.game_data import GameData
from src.utils import pad_code

class GameEnd(Event):
    """
    Description:
        The Game End event.
    """

    def __str__(self):
        return str(self.id) + " - " + str(self.time) + " = Game End - " + self.description

    def __eq__(self, other):
        return (isinstance(self, GameEnd) and
                isinstance(other, GameEnd))

    @property
    def code(self) -> str:
        """
        Return a seven-character code representing the event type.
        """
        code : str = "GAMEEND"
        return pad_code(code)

    @property
    def id(self) -> str:
        return "GAME-END"

    def get_post(self, game_data : GameData) -> Optional[str]:
        """
        Description:
            Return the event string for a game end event.
        """
        home = game_data.home.location
        away = game_data.away.location

        event_values = {
            "winner":     home if self.home_goals > self.away_goals else away,
            "home_team":  home,
            "away_team":  away,
            "home_goals": self.home_goals,
            "away_goals": self.away_goals,
            "hashtags":   game_data.hashtags
        }
        return templates.GAME_END_TEMPLATE.format(**event_values)
