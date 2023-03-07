"""
This module defines the Reply object.
"""

from typing import Optional

from src.command.command import Command, Priority
from src.data.game_data import GameData
from src.data.line_score import LineScore
from src.events.event import Event
from src.logger import log
from src.output import output

class Reply(Command):
    """
    This command is used to post a reply for the given event.
    """

    def __init__(self, current : Event, previous : Event, game : GameData, line : LineScore):
        self.current    : Event     = current
        self.previous   : Event     = previous
        self.game_data  : GameData  = game
        self.line_score : LineScore = line
        super().__init__("Reply", Priority.NORMAL)

    def execute(self) -> None:
        """
        Execute the command.
        """
        if self.previous.__class__ != self.current.__class__:
            log.error("Attempted to generate reply between unlike classes")
            return

        tweet_id : Optional[int] = None
        text     : Optional[str] = self.current.get_reply(self.game_data,
                                                          self.line_score,
                                                          self.previous)

        if self.previous.has_tweeted and text is not None:
            tweet_id = output.reply(self.previous.tweet_id, text)

        self.current.tweet_id = tweet_id
