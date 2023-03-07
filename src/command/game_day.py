"""
This module defines a command that will create a post on game days to indicate the time
that the game is scheduled to start.
"""

from typing import Optional

from datetime import datetime
import pytz

from src.command.command import Command, Priority
from src.data.game_data import GameData
from src.output import output, templates


class GameDay(Command):
    """
    This class defines a command that will create a post on game days to indicate the time
    that the game is scheduled to start.
    """

    def __init__(self, data: GameData):
        self.game_data : GameData = data
        super().__init__("Game Day", Priority.NORMAL)

    def execute(self) -> None:
        """
        Execute the command.
        """

        if not output.has_posted_today("game day"):
            text : Optional[str] = None
            time : datetime      = self.game_data.date.astimezone(pytz.timezone("America/Denver"))

            event_values = {
                "home_team": self.game_data.home.location,
                "away_team": self.game_data.away.location,
                "venue":     self.game_data.venue,
                "time":      time.strftime("%I:%M %p %Z"),
                "hashtags":  self.game_data.hashtags
            }
            text = templates.GAME_DAY_TEMPLATE.format(**event_values)
            output.post(text)
