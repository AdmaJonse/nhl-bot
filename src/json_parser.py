"""
Description:
    This module handles parsing of the JSON game data.
"""

from typing import Any, Dict, Optional

import json
import requests

from src.events.game_official import GameOfficial
from src.events.event import Event
from src import event_factory
from src import generator
from src import logger
from src import output


NHL_API_URL : str = "https://statsapi.web.nhl.com/api/v1/game/"

class Parser:
    """
    Description:
        This class defines the JSON parser.
    """

    def __init__(self, game_id : int):

        # initialize our variables
        self.game_id      : int              = game_id
        self.is_game_over : bool             = False
        self.data         : Any              = []
        self.new_records  : Any              = []
        self.last_event   : int              = 0
        self.events       : Dict[str, Event] = {}

        # load initial data
        self.get_new_records()
        self.write_data()

        self.generator : generator.Generator = generator.Generator(self.data)

        self.post_game_day()

        # Silently process all events prior to intialization. We want
        # to find the last event in the list so that we can start
        # processing only new events from this point.
        for record in self.new_records:
            event = event_factory.create(record)
            if event is not None:
                self.check_for_game_over(event)
                self.events[event.id] = event


    def get_data(self):
        """
        Description:
            This function retrieves the latest JSON data record for the current
            game from the NHL website.
        """
        url       : str = NHL_API_URL + str(self.game_id) + "/feed/live"
        params    : str = ""
        request   : Any = requests.get(url, params)
        self.data = request.json()


    def get_new_records(self):
        """
        Description:
            This method applies a filter to game events to ensure that we only
            parse events that are new or have been updated.
        """

        # Filter out all play data that has already been processed
        def filter_events(data):

            event : Event = event_factory.create(data)

            if event is not None:

                is_new_event     : bool  = event.id not in self.events
                is_updated_event : bool  = False

                try:
                    if not is_new_event:
                        is_updated_event = (self.events[event.id] != event)
                except KeyError:
                    is_updated_event = False

                return is_new_event or is_updated_event

        self.get_data()
        all_plays : Any = self.data["liveData"]["plays"]["allPlays"]
        self.new_records = [data for data in all_plays if filter_events(data)]


    def write_data(self):
        """
        Description:
            Write the game data to a JSON file.
        """
        filename : str = "data.json"
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(self.data, file, ensure_ascii=False, indent=4)


    def check_for_game_over(self, event : Optional[Event]):
        """
        Description:
            Determine whether the given event indicates that the game is over.
        """
        if event is not None:
            self.is_game_over = event.__class__ == GameOfficial
            if self.is_game_over:
                logger.log_info("Game Over.")


    def update_generator(self):
        """
        Description:
            Update the line score data stored by the generator.
        """
        self.generator.update_line_score(self.data["liveData"]["linescore"])


    def generate_tweet(self, event : Event):
        """
        Description:
            Create and send a tweet based on the given event.
        """

        tweet_id : Optional[int] = None
        text     : Optional[str] = self.generator.get_event_string(event)

        if text is not None:
            tweet_id = output.post(text)

        event.tweet_id = tweet_id

        if event.has_tweeted and event.auto_reply:
            reply_text : Optional[str] = self.generator.get_auto_reply_string(event)
            if reply_text is not None:
                event.tweet_id = output.reply(reply_text, tweet_id)


    def generate_reply(self, previous : Event, current : Event):
        """
        Description:
            Create and send a reply to the given tweet based on the
            deltas between the previous and current events.
        """

        if previous.__class__ != current.__class__:
            logger.log_error("Attempted to generated reply between unlike classes")
            return

        tweet_id : Optional[int] = None
        text     : Optional[str] = self.generator.get_reply_string(previous, current)

        if previous.has_tweeted and text is not None:
            tweet_id = output.reply(text, previous.tweet_id)

        current.tweet_id = tweet_id


    def post_game_day(self):
        """
        Description:
            Create and send a post indicating that today is game day. This should always be the
            first post of the day. If we have already posted today, it may indicate that we've
            restarted the application. In this case, we will not post in order to avoid a
            duplicate.
        """

        if not output.has_posted_today():
            text : Optional[str] = self.generator.get_game_day_string()
            if text is not None:
                output.post(text)


    def parse(self):
        """
        Description:
            Parse new event records from the game data and handle any new events.
        """

        self.get_new_records()
        self.update_generator()

        for record in self.new_records:

            event    : Optional[Event] = event_factory.create(record)
            previous : Optional[Event] = None

            if event is not None:

                logger.log_info(event)

                if event.id in self.events:
                    previous = self.events[event.id]

                if previous is not None and previous.has_tweeted:
                    self.generate_reply(previous, event)
                else:
                    self.generate_tweet(event)

                self.events[event.id] = event
                self.check_for_game_over(event)
