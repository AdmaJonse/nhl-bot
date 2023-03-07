"""
This module defines the list of registered parsers.
"""

from typing import List

from src.parser.content import ContentParser
from src.parser.feed import FeedParser
from src.parser.line_score import LineScoreParser
from src.parser.parser import Parser


class Parsers:
    """
    This class defines the list of registered parsers.
    """

    def __init__(self):
        self._parsers: List[Parser] = []


    def set_game(self, game_id: int) -> None:
        """
        Register parsers for the given game ID.
        """

        # We must register the feed parser first here. Its constructor will parse every event
        # that has already occurred and add them to the event list. Since the Game Data and Line
        # Score haven't been set yet, no posts will occur. This behaviour is desirable because
        # we don't want to post old events in case we've had to restart the bot.

        self._parsers = [
            FeedParser(game_id),
            ContentParser(game_id),
            LineScoreParser(game_id)
        ]


    def parse(self) -> None:
        """
        Trigger a parse from all registered parsers.
        """
        for parser in self._parsers:
            parser.parse()


    def clear(self) -> None:
        """
        Remove all parsers from the list of registered parsers.
        """
        self._parsers = []


parsers: Parsers = Parsers()
