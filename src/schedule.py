"""
Description:
    This module provides an interface for querying the NHL API's schedule data.
"""

from datetime import datetime
from datetime import timedelta
from datetime import timezone
import requests

# Colorado Avalanche team ID in the NHL API
TEAM_ID      = 21
SCHEDULE_API = "https://statsapi.web.nhl.com/api/v1/schedule"
TIME_FORMAT  = "%Y-%m-%dT%H:%M:%SZ"


def get_schedule_json():
    """
    Description:
        Return the JSON record describing the team's games that are
        scheduled today.
    """
    date    = datetime.today() - timedelta(hours=4)
    url     = SCHEDULE_API + "?teamId=" + str(TEAM_ID) + "&date=" + date.strftime("%Y-%m-%d")
    params  = ""
    request = requests.get(url, params)
    return request.json()


def get_game_id(data=get_schedule_json()):
    """
    Description:
        Return the game ID from the given JSON schedule record.
    """
    try:
        game_id = data["dates"][0]["games"][0]["gamePk"]
        return game_id
    except IndexError:
        return -1
    except KeyError:
        return -1


def get_start_time(data=get_schedule_json()):
    """
    Description:
        Return the game start time from the given JSON schedule record.
    """
    try:
        start_time = datetime.strptime(data["dates"][0]["games"][0]["gameDate"], TIME_FORMAT)
        return start_time.replace(tzinfo=timezone.utc)
    except IndexError:
        return -1
    except KeyError:
        return -1
