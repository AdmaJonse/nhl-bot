"""
Description:
    This module handles the main logic to check for game updates.
"""

from datetime import datetime
from typing import Optional

import time
import pause

from src import logger
from src import json_parser
from src import schedule

# How frequently we check for game updates (in seconds)
FREQUENCY = 5  # seconds

def wait_until_game_start():
    """
    Description:
        This function will wait until the start of the given game.
    """
    game_time    : Optional[datetime] = schedule.get_start_time()
    current_time : Optional[datetime] = schedule.get_current_time()
    if game_time > current_time:
        logger.log_info("Waiting until game start: " + schedule.time_to_string(game_time))
        pause.until(game_time)


def wait_until_tomorrow(from_time : Optional[datetime] = None):
    """
    Description:
        This function will wait until the next day.
    """
    tomorrow : datetime = schedule.get_tomorrow(from_time).replace(hour=12)
    logger.log_info("Pausing until: " + schedule.date_to_string(tomorrow))
    pause.until(tomorrow)


def check_for_updates():
    """
    Description:
        This function will check for a game on the current date. If a game is
        found, it will trigger game event parsing at game time. If no game is
        found, it will pause until tomorrow.
    """
    while True:

        logger.flush()
        logger.log_info("Checking for a game today...")

        # Determine if there is a game today
        game_id : Optional[int] = schedule.get_game_id()

        if game_id is not None and game_id >= 0:

            logger.log_info("There is a game today: " + str(game_id))
            parser    : json_parser.Parser = json_parser.Parser(game_id)
            game_time : Optional[datetime] = schedule.get_start_time()
            wait_until_game_start()

            while not parser.is_game_over:
                parser.parse()
                time.sleep(FREQUENCY)

            wait_until_tomorrow(game_time)

        else:
            logger.log_info("There is no game today.")
            wait_until_tomorrow()
