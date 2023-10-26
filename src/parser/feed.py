"""
This module handles parsing of the JSON live feed data.
"""

from typing import Any, Optional

from src import event_factory
from src.command.command_queue import command_queue
from src.event_list import event_list
from src.logger import log
from src.events.game_official import GameOfficial
from src.events.event import Event
from src.parser.parser import Parser


def check_for_game_over(event: Optional[Event]):
    """
    Determine whether the given event indicates that the game is over.
    """
    if event is not None and event.__class__ == GameOfficial:
        log.info("Game Over.")
        command_queue.stop()


class FeedParser(Parser):
    """
    This class defines the parser for the live feed data.
    """

    def __init__(self, game_id: int):
        super().__init__(game_id, "/feed/live")
        self.new_records: Any = []
        self.get_new_records()

        # Silently process all events prior to initialization. We want
        # to find the last event in the list so that we can start
        # processing only new events from this point.
        for record in self.new_records:
            event = event_factory.create(record)
            if event is not None:
                check_for_game_over(event)
                event_list.add(event)


    def get_new_records(self):
        """
        This method applies a filter to game events to ensure that we only
        parse events that are new or have been updated.
        """

        # Filter out all play data that has already been processed
        def filter_events(data):

            event: Event = event_factory.create(data)

            if event is None:
                return False

            is_new_event: bool = not event_list.exists(event.id)
            is_updated_event: bool = False

            try:
                if not is_new_event:
                    is_updated_event = event_list.get(event.id) != event
            except KeyError:
                is_updated_event = False

            return is_new_event or is_updated_event

        self.get_data()
        all_plays: Any = self.data["liveData"]["plays"]["allPlays"]
        self.new_records = [data for data in all_plays if filter_events(data)]


    def parse(self):
        """
        Parse new event records from the game data and handle any new events.
        """

        self.get_new_records()

        for record in self.new_records:

            event: Optional[Event] = event_factory.create(record)

            if event is not None:
                log.info(event)
                event_list.add(event)
                check_for_game_over(event)
