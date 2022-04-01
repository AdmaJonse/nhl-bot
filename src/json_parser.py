import json
import printer
import requests
import time

from datetime import datetime
from datetime import timedelta


TEST_GAME=2021021080
time_format = "%Y-%m-%dT%H:%M:%SZ"


class Parser:

    def __init__(self, id):
        self.game_id = id
        self.is_game_over = False
        self.get_data()
        self.new_records = ""
        self.printer = printer.Printer(self.data["gameData"])
        self.test_time = datetime.strptime("2022-04-01T01:08:18Z", time_format)


    def increment_test_time(self):
        self.test_time += timedelta(seconds=59)


    def get_data(self):
        
        url    = "https://statsapi.web.nhl.com/api/v1/game/" + str(self.game_id) + "/feed/live"
        params = ""

        print("getting data for game: " + str(self.game_id))
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
            
            current_time = datetime.now()
            event_time = datetime.strptime(e["about"]["dateTime"], time_format)
            #is_current = abs(current_time - event_time) < timedelta(minutes=1)
            is_current = timedelta(0) < (self.test_time - event_time) < timedelta(minutes=1)
            return is_current

        self.new_records = [event for event in self.data["liveData"]["plays"]["allPlays"] if filter(event)]


    @get_latest_data
    def write_data(self):
        filename="data.json"
        print("writing data to file: " + filename)
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, ensure_ascii=False, indent=4)


    @get_latest_data
    def parse(self):
        print("parsing data...")
        for event in self.new_records:
            self.printer.print_event(event)
            if event["result"]["event"] == "Game End":
                self.set_game_over

    
    def set_game_over(self):
        self.is_game_over = True
        

parser = Parser(TEST_GAME)

#write_data(data)
while (not parser.is_game_over):
    parser.parse()
    time.sleep(1)
    parser.increment_test_time()

print("Game over!")
