import json
import printer
import requests

TEST_GAME=2021021080

def get_data(id):
    print("getting data for game: " + str(id))
    URL = "https://statsapi.web.nhl.com/api/v1/game/" + str(id) + "/feed/live"
    PARAMS = ""

    r = requests.get(url = URL, params = PARAMS)
    data = r.json()
    return r.json()

def write_data(data):
    filename="data.json"
    print("writing data to file: " + filename)
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def parse(p, data):
    print("parsing data...")
    for event in data["liveData"]["plays"]["allPlays"]:
        p.print_event(event)
        


data = get_data(TEST_GAME)

#write_data(data)
p = printer.Printer(data["gameData"])
parse(p, data)

