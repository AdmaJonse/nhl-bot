"""
Description:
    This module provides an interface for querying the NHL API's schedule data.
"""

from datetime import datetime
from datetime import timedelta
import pytz
import requests

from src import logger

# Colorado Avalanche team ID in the NHL API
TEAM_ID      = 21
SCHEDULE_API = "https://statsapi.web.nhl.com/api/v1/schedule"
TIME_FORMAT  = "%Y-%m-%dT%H:%M:%SZ"
DATE_FORMAT  = "%Y-%m-%d"
TIME_ZONE    = pytz.timezone("US/Eastern")


def time_to_string(time):
    """
    Description:
        Return the given datetime object as a time string formatted
        using the time format constant.
    """
    return time.strftime(TIME_FORMAT)


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
    logger.log_info("current time: " + time_to_string(current_time))
    return current_time


def get_current_date():
    """
    Description:
        Return the current date localized using the time zone constant.
    """
    current_date = datetime.now(TIME_ZONE).replace(hour=0, minute=0, second=0, microsecond=0)
    logger.log_info("current date: " + date_to_string(current_date))
    return current_date


def get_tomorrow():
    """
    Description:
        Return the tomorrow's date localized using the time zone constant.
    """
    current_date = get_current_date()
    tomorrow     = current_date + timedelta(days=1)
    logger.log_info("tomorrow's date: " + date_to_string(tomorrow))
    return tomorrow


def get_schedule_json(date=get_current_date()):
    """
    Description:
        Return the JSON record describing the team's games that are
        scheduled today.
    """
    url     = SCHEDULE_API + "?teamId=" + str(TEAM_ID) + "&date=" + date_to_string(date)
    params  = ""
    logger.log_info("getting schedule JSON from: " + url)
    request = requests.get(url, params)
    return request.json()


def get_game_id(data=get_schedule_json()):
    """
    Description:
        Return the game ID from the given JSON schedule record.
    """
    try:
        game_id = data["dates"][0]["games"][0]["gamePk"]
        logger.log_info("game id: " + str(game_id))
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
        TIME_ZONE.localize(start_time)
        logger.log_info("game start time: " + str(start_time))
        return start_time
    except IndexError:
        return -1
    except KeyError:
        return -1
