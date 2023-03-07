"""
This module is used to generate tweet text based on a given event.
"""

from typing import Optional, overload

from src.command.command_queue import command_queue
from src.command.post import Post
from src.command.post_highlight import PostHighlight
from src.command.reply import Reply
from src.events.event import Event
from src.data.game_data import GameData
from src.data.highlight import Highlight
from src.data.line_score import LineScore
from src.observer.observer import Observer
from src import stores
from src.logger import log


class Generator(Observer):
    """
    The Generator class is used to generate tweet and reply text from given events and
    game data.
    """

    def __init__(self):
        self._game_data: Optional[GameData] = None
        self._line_score: Optional[LineScore] = None
        stores.game_data.subscribe(self)
        stores.line_score.subscribe(self)


    @overload
    def update(self, subject: Optional[GameData]) -> None:
        """
        Update the stored copy of the game data when notified by the subject.
        """
        self._game_data = subject


    @overload
    def update(self, subject: Optional[LineScore]) -> None:
        """
        Update the stored copy of the line score when notified by the subject.
        """
        self._line_score = subject


    def update(self, subject):
        """
        Handle an update from the subject.
        """
        if isinstance(subject, Optional[GameData]):
            self._game_data = subject
        elif isinstance(subject, Optional[LineScore]):
            self._line_score = subject
        else:
            log.info("Unexpected type for update.")


    def create_post(self, event: Event) -> None:
        """
        Create a post for the given event using the stored copy of the game data and line score.
        """
        if self._game_data is not None and self._line_score is not None:
            command_queue.enqueue(Post(event, self._game_data, self._line_score))


    def create_reply(self, current: Event, previous: Event) -> None:
        """
        Create a reply for the given event using the stored copy of the game data and line score.
        """
        if self._game_data is not None and self._line_score is not None:
            command_queue.enqueue(Reply(current, previous, self._game_data, self._line_score))


    def create_highlight(self, highlight: Highlight, event : Event) -> None:
        """
        Post a highlight as a reply to the corresponding event.
        """
        if self._game_data is not None and event is not None and event.has_tweeted:
            parent: Optional[int] = event.tweet_id
            if parent is not None:
                command_queue.enqueue(PostHighlight(highlight, parent, self._game_data))


generator = Generator()
