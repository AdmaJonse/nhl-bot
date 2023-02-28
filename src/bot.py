"""
This module handles the main logic to check for game updates.
"""

from datetime import datetime, timedelta
from typing import Optional

import time
import pause

from src import feed
from src import logger
from src import media
from src import schedule

# How frequently we check for game updates (in seconds)
FREQUENCY = 5  # seconds

def wait_until_game_start():
    """
    This function will wait until the start of the given game.
    """
    game_time    : Optional[datetime] = schedule.get_start_time()
    current_time : Optional[datetime] = schedule.get_current_time()
    if game_time > current_time:
        logger.log_info("Waiting until game start: " + schedule.time_to_string(game_time))
        pause.until(game_time)


def wait_until_morning():
    """
    This function will wait until the next day.
    """
    current_time : datetime = schedule.get_current_time()
    noon : datetime = schedule.get_noon()
    if current_time > noon:
        noon += timedelta(days=1)
    logger.log_info("Pausing until: " + schedule.time_to_string(noon))
    pause.until(noon)


def check_for_updates():
    """
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
            feed_parser  : feed.Parser  = feed.Parser(game_id)
            media_parser : media.Parser = media.Parser(feed_parser)
            wait_until_game_start()

            while not feed_parser.is_game_over:
                feed_parser.parse()
                media_parser.parse()
                time.sleep(FREQUENCY)

        else:
            logger.log_info("There is no game today.")

        wait_until_morning()
