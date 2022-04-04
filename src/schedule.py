import requests

from src import logger

from datetime import datetime
from datetime import timezone

# Colorado Avalanche team ID in the NHL API
team_id = 21

schedule_api = "https://statsapi.web.nhl.com/api/v1/schedule"
time_format = "%Y-%m-%dT%H:%M:%SZ"


def get_schedule_json():
    date = datetime.today()
    url = schedule_api + "?teamId=" + str(team_id) + "&date=" + date.strftime("%Y-%m-%d")
    params = ""
    r = requests.get(url, params)
    return r.json()


def get_game_id():
    data = get_schedule_json()
    try:
        id = data["dates"][0]["games"][0]["gamePk"]
        return id
    except:
        logger.log_info("Could not find game.")
        return -1


def get_start_time():
    data = get_schedule_json()
    try:
        start_time = datetime.strptime(data["dates"][0]["games"][0]["gameDate"], time_format)
        return start_time.replace(tzinfo=timezone.utc)
    except:
        logger.log_info("Could not find game.")
        return -1