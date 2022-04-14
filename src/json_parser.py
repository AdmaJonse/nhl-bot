import json
import requests

from src import printer
from src import logger


def get_event_id(data):
    return data["about"]["eventIdx"]

class Parser:

    def __init__(self, id):

        # initialize our variables
        self.game_id = id
        self.is_game_over = False
        self.data = []
        self.new_records = []
        self.last_event = 0
        self.tweets = {}
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
        url    = "https://statsapi.web.nhl.com/api/v1/game/" + str(self.game_id) + "/feed/live"
        params = ""
        r = requests.get(url, params)
        self.data = r.json()


    def get_latest_data(f):
        def wrapper(self, *args, **kwargs):
            self.get_new_records()
            return f(self, *args, **kwargs)
        return wrapper


    def get_new_records(self):

        # Filter out all play data that has already been processed
        def filter(e):
            event_id = get_event_id(e)
            is_new_event = event_id > self.last_event
            try:
                is_updated_event = self.events[event_id] != e
            except:
                is_updated_event = False
            return is_new_event or is_updated_event

        self.get_data()
        self.new_records = [event for event in self.data["liveData"]["plays"]["allPlays"] if filter(event)]


    def write_data(self):
        filename="data.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, ensure_ascii=False, indent=4)


    def check_for_game_over(self, data):
        event_type = data["result"]["event"] 
        self.is_game_over = event_type == "Game End"
        if self.is_game_over:
            logger.log_info("Game Over.")        


    @get_latest_data
    def parse(self):
        for event in self.new_records:

            logger.log_info("Event: \n" + str(event))

            tweet_id  = 0
            event_id  = get_event_id(event)
            parent_id = self.tweets.get(event_id, 0)
            
            # update any records stored by the printer
            self.printer.update_line_score(self.data["liveData"]["linescore"])

            if parent_id <= 0:
                tweet_id = self.printer.generate_tweet(event)
            else:
                tweet_id = self.printer.generate_reply(event, parent_id)

            self.tweets[event_id] = tweet_id
            self.events[event_id] = event
            self.last_event = event_id
            self.check_for_game_over(event)