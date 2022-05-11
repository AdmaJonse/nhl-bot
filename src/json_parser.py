"""
Description:
    This module handles parsing of the JSON game data.
"""

import json
import requests

from src import events
from src import printer
from src import tweeter
from src import logger

class Parser:
    """
    Description:
        This class defines the JSON parser.
    """

    def __init__(self, game_id):

        # initialize our variables
        self.game_id = game_id
        self.is_game_over = False
        self.data = []
        self.new_records = []
        self.last_event = 0
        self.events = {}

        # load initial data
        self.get_new_records()
        self.write_data()

        self.printer = printer.Printer(self.data)

        # Silently process all events prior to intialization. We want
        # to find the last event in the list so that we can start
        # processing only new events from this point.
        for record in self.new_records:
            event = events.to_event(record)
            self.check_for_game_over(event)
            self.last_event = event.event_id

        logger.log_info("starting event processing from ID: " + str(self.last_event))


    def get_data(self):
        """
        Description:
            This function retrieves the latest JSON data record for the current
            game from the NHL website.
        """
        url       = "https://statsapi.web.nhl.com/api/v1/game/" + str(self.game_id) + "/feed/live"
        params    = ""
        request   = requests.get(url, params)
        self.data = request.json()


    def get_new_records(self):
        """
        Description:
            This method applies a filter to game events to ensure that we only
            parse events that are new or have been updated.
        """

        # Filter out all play data that has already been processed
        def filter_events(data):
            event = events.to_event(data)
            is_new_event = event.event_id > self.last_event
            try:
                is_updated_event = self.events[event.event_id]["event"] != event
            except KeyError:
                is_updated_event = False
            return is_new_event or is_updated_event

        self.get_data()
        all_plays = self.data["liveData"]["plays"]["allPlays"]
        self.new_records = [data for data in all_plays if filter_events(data)]


    def write_data(self):
        """
        Description:
            Write the game data to a JSON file.
        """
        filename="data.json"
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(self.data, file, ensure_ascii=False, indent=4)


    def check_for_game_over(self, event):
        """
        Description:
            Determine whether the given event indicates that the game is over.
        """
        self.is_game_over = event.__class__ == events.GameEnd
        if self.is_game_over:
            logger.log_info("Game Over.")


    def generate_tweet(self, event):
        """
        Description:
            Create and send a tweet based on the given event.
        """
        tweet_id = 0
        text = self.printer.get_event_string(event)
        if len(text) > 0:
            tweet_id = tweeter.tweet(text)
        return tweet_id


    def generate_reply(self, previous_event, current_event, parent_id):
        """
        Description:
            Create and send a reply to the given tweet based on the
            deltas between the previous and current events.
        """
        tweet_id = 0
        text = self.printer.get_reply_string(previous_event, current_event)
        if len(text) > 0:
            tweet_id = tweeter.reply(text, parent_id)
        return tweet_id


    def parse(self):
        """
        Description:
            Parse new event records from the game data and handle any new events.
        """
        self.get_new_records()
        for record in self.new_records:

            tweet_id  = 0
            event = events.to_event(record)
            logger.log_info(str(event))

            try:
                parent_id      = self.events[event.event_id]["tweet_id"]
                previous_event = self.events[event.event_id]["event"]
            except KeyError:
                parent_id = 0

            # update any records stored by the printer
            self.printer.update_line_score(self.data["liveData"]["linescore"])

            if parent_id <= 0:
                tweet_id = self.generate_tweet(event)
            else:
                logger.log_info("=====> event updated: " + str(parent_id))
                tweet_id = self.generate_reply(previous_event, event, parent_id)

            self.events[event.event_id] = {"tweet_id": tweet_id, "event": event}
            self.last_event = event.event_id
            self.check_for_game_over(event)
