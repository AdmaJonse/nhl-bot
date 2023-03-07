"""
This module defines the Post Highlight command.
"""

from typing import Optional

from src.command.command import Command, Priority
from src.data.game_data import GameData
from src.data.highlight import Highlight
from src.events.event import Event
from src.output import output
from src.stores import game_data

class PostHighlight(Command):
    """
    This class defines the Post Highlight command.
    """

    def __init__(self, highlight : Highlight, event : Event):
        self.highlight  : Highlight          = highlight
        self.event      : Event              = event
        self.game_data  : Optional[GameData] = game_data.get_data()
        super().__init__("Post Highlight", Priority.NORMAL)


    def execute(self) -> None:
        """
        Execute the command.
        """
        if self.game_data is not None:
            text = self.highlight.get_post(self.game_data)
            if self.event.has_tweeted and self.event.tweet_id is not None:
                output.reply_with_media(self.event.tweet_id, text, self.highlight.video)
