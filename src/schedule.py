"""
Description:
    This module provides an interface for querying the NHL API's schedule data.
"""

from datetime import datetime
from datetime import timedelta
from dateutil import parser
import pytz
import requests

from src import logger

# Colorado Avalanche team ID in the NHL API
TEAM_ID = 21

# NHL API URL
SCHEDULE_API = "https://statsapi.web.nhl.com/api/v1/schedule"

# Date and Time formats
NHL_TIME_FORMAT  = "%Y-%m-%dT%H:%M:%SZ"
TIME_FORMAT      = "%Y-%m-%d %H:%M:%S %Z%z"
DATE_FORMAT      = "%Y-%m-%d"
TIME_ZONE        = pytz.timezone("US/Eastern")


def time_to_string(time):
    """
    Description:
        Return the given datetime object as a time string formatted
        using the time format constant.
    """
    return time.astimezone(TIME_ZONE).strftime(TIME_FORMAT)


def date_to_string(date):
    """
    Description:
        Return the given datetime object as a date string formatted
        using the time format constant.
    """
    return date.strftime(DATE_FORMAT)


def get_current_time():
    """
    Description:
        Return the current time localized using the time zone constant.
    """
    current_time = datetime.now(TIME_ZONE)
    logger.log_verbose("current time: " + time_to_string(current_time))
    return current_time


def get_current_date():
    """
    Description:
        Return the current date localized using the time zone constant.
    """
    current_date = datetime.now(TIME_ZONE).replace(hour=0, minute=0, second=0, microsecond=0)
    logger.log_verbose("current date: " + date_to_string(current_date))
    return current_date


def get_tomorrow():
    """
    Description:
        Return the tomorrow's date localized using the time zone constant.
    """
    current_date = get_current_date()
    tomorrow     = current_date + timedelta(days=1)
    logger.log_verbose("tomorrow's date: " + date_to_string(tomorrow))
    return tomorrow


def get_schedule_json():
    """
    Description:
        Return the JSON record describing the team's games that are
        scheduled today.
    """
    date    = get_current_date()
    url     = SCHEDULE_API + "?teamId=" + str(TEAM_ID) + "&date=" + date_to_string(date)
    params  = ""
    logger.log_verbose("getting schedule JSON from: " + url)
    request = requests.get(url, params)
    return request.json()


def get_game_id():
    """
    Description:
        Return the game ID from the given JSON schedule record.
    """
    try:
        data    = get_schedule_json()
        game_id = data["dates"][0]["games"][0]["gamePk"]
        logger.log_verbose("game id: " + str(game_id))
        return game_id
    except IndexError:
        return -1
    except KeyError:
        return -1


def get_start_time():
    """
    Description:
        Return the game start time from the given JSON schedule record.
    """
    try:
        data       = get_schedule_json()
        start_time = parser.parse(data["dates"][0]["games"][0]["gameDate"])
        logger.log_verbose("game start time: " + time_to_string(start_time))
        return start_time
    except IndexError:
        return -1
    except KeyError:
        return -1
