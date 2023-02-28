"""
This module is used to generate tweet text based on a given event.
"""

from typing import Any, Optional
from datetime import datetime
import pytz

from src.events.event import Event
from src.data.game_data import GameData
from src.output import templates

class Generator:
    """
    The Generator class is used to generate tweet and reply text from given events and
    game data.
    """

    def __init__(self, data : GameData):
        self.game_data : GameData = GameData(data)


    def update_line_score(self, data : Any):
        """
        Update the line score.
        """
        self.game_data.line_score = data


    def get_event_string(self, event : Event) -> Optional[str]:
        """
        Return the event string for an event.
        """
        return event.get_post(self.game_data)


    def get_auto_reply_string(self, event : Event) -> Optional[str]:
        """
        Return the auto reply string for an event.
        """
        return event.get_auto_reply(self.game_data)


    def get_reply_string(self, previous : Event, current : Event) -> Optional[str]:
        """
        Return the reply string for an event.
        """
        return current.get_reply(self.game_data, previous)


    def get_game_day_string(self) -> Optional[str]:
        """
        Return the text of the game day post.
        """

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
        return text
