"""
This module defines the Post command.
"""

from typing import Optional

from src.command.command import Command, Priority
from src.data.game_data import GameData
from src.data.line_score import LineScore
from src.events.event import Event
from src.output import output

class Post(Command):
    """
    The Post command will post a tweet for a given event.
    """

    def __init__(self, event : Event, game_data : GameData, line_score : LineScore):
        self.event      : Event     = event
        self.game_data  : GameData  = game_data
        self.line_score : LineScore = line_score
        super().__init__("Post", Priority.NORMAL)

    def execute(self) -> None:
        """
        Execute the command.
        """
        tweet_id : Optional[int] = None
        text     : Optional[str] = self.event.get_post(self.game_data, self.line_score)

        if text is not None:
            tweet_id = output.post(text)

        self.event.tweet_id = tweet_id
