"""
Description:
    This module handles parsing of the JSON game data.
"""

import json
import requests

from src import printer
from src import logger


def get_event_id(event):
    """
    Description:
        Return the event ID for the given event.
    """
    return event["about"]["eventIdx"]

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
        for event in self.new_records:
            self.last_event = get_event_id(event)

        logger.log_info("starting event processing from ID: " + str(self.last_event))


    def get_data(self):
        """
        Description:
            This function retrieves the latest JSON data record for the current
            game from the NHL website.
        """
        url     = "https://statsapi.web.nhl.com/api/v1/game/" + str(self.game_id) + "/feed/live"
        params  = ""
        request = requests.get(url, params)
        self.data = request.json()

    @staticmethod
    def get_latest_events(function):
        """
        Description:
            This is a decorator that is used to ensure we're viewing the latest
            event data. It should be used to decorate methods that parse event
            data.
        """
        def wrapper(self, *args, **kwargs):
            self.get_new_records()
            return function(self, *args, **kwargs)
        return wrapper


    def get_new_records(self):
        """
        Description:
            This method applies a filter to game events to ensure that we only
            parse events that are new or have been updated.
        """

        # Filter out all play data that has already been processed
        def filter_events(event):
            event_id = get_event_id(event)
            is_new_event = event_id > self.last_event
            try:
                is_updated_event = self.events[event_id]["event"] != event
            except KeyError:
                is_updated_event = False
            return is_new_event or is_updated_event

        self.get_data()
        all_plays = self.data["liveData"]["plays"]["allPlays"]
        self.new_records = [event for event in all_plays if filter_events(event)]


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
        event_type = event["result"]["event"]
        self.is_game_over = event_type == "Game End"
        if self.is_game_over:
            logger.log_info("Game Over.")


    @get_latest_events
    def parse(self):
        """
        Description:
            Parse new event records from the game data and handle any new events.
        """
        for event in self.new_records:

            logger.log_info("Event: \n" + str(event))

            tweet_id  = 0
            event_id  = get_event_id(event)

            try:
                parent_id      = self.events[event_id]["tweet_id"]
                previous_event = self.events[event_id]["event"]
            except KeyError:
                parent_id = 0

            # update any records stored by the printer
            self.printer.update_line_score(self.data["liveData"]["linescore"])

            if parent_id <= 0:
                tweet_id = self.printer.generate_tweet(event)
            else:
                tweet_id = self.printer.generate_reply(previous_event, event, parent_id)

            self.events[event_id] = {"tweet_id": tweet_id, "event": event}
            self.last_event = event_id
            self.check_for_game_over(event)
