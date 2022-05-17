"""
Description:
    This module is used to generate tweet text based on a given event.
"""

from typing import Any, Optional

from src.events.event import Event
from src.game_data import GameData

class Generator:
    """
    Description:
        The Generator class is used to generate tweet and reply text from given events and
        game data.
    """

    def __init__(self, data : GameData):
        self.game_data : GameData = GameData(data)


    def update_line_score(self, data : Any):
        """
        Description:
            Update the line score.
        """
        self.game_data.line_score(data)


    def get_event_string(self, event : Event) -> Optional[str]:
        """
        Description:
            Return the event string for an event.
        """
        return event.get_post(self.game_data)


    def get_reply_string(self, previous : Event, current : Event) -> Optional[str]:
        """
        Description:
            Return the reply string for an event.
        """
        return current.get_reply(self.game_data, previous)
