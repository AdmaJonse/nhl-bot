import json
import printer
import requests

from datetime import datetime
from datetime import timedelta
from datetime import timezone


def get_event_id(data):
    return data["about"]["eventIdx"]

class Parser:

    def __init__(self, id):
        self.game_id = id
        self.is_game_over = False
        self.get_data()
        self.new_records = ""
        self.last_event = 0
        self.printer = printer.Printer(self.data)


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

        # Filter out all play data that didn't occur in the previous minute
        def filter(e):

            # Event occurred in the last five minutes
            time_format = "%Y-%m-%dT%H:%M:%SZ"
            current_time = datetime.now(timezone.utc)
            event_time = datetime.strptime(e["about"]["dateTime"], time_format).replace(tzinfo=timezone.utc)
            is_time_current = timedelta(0) < (current_time - event_time) < timedelta(minutes=5)
            
            # Event ID is greater than the last record parsed
            event_code = get_event_id(e)
            is_id_current = event_code > self.last_event

            return is_time_current and is_id_current


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
            print("Game Over.")


    @get_latest_data
    def parse(self):
        for event in self.new_records:
            self.printer.update_line_score(self.data["liveData"]["linescore"])
            self.printer.print_event(event)
            self.last_event = get_event_id(event)
            self.check_for_game_over(event)
