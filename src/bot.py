"""
Description:
    This module handles the main logic to check for game updates.
"""

from datetime import datetime
from typing import Optional

import socket
import time
import os
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


def wait_until_tomorrow():
    """
    Description:
        This function will wait until the next day.
    """
    tomorrow : datetime = schedule.get_tomorrow().replace(hour=12)
    logger.log_info("Pausing until: " + schedule.date_to_string(tomorrow))
    pause.until(tomorrow)


def check_for_updates():
    """
    Description:
        This function will check for a game on the current date. If a game is
        found, it will trigger game event parsing at game time. If no game is
        found, it will pause until tomorrow.
    """

    listen()

    while True:

        logger.log_info("Checking for a game today...")

        # Determine if there is a game today
        game_id : Optional[int] = schedule.get_game_id()

        if game_id is not None and game_id >= 0:

            logger.log_info("There is a game today: " + str(game_id))
            parser : json_parser.Parser = json_parser.Parser(game_id)
            wait_until_game_start()

            while not parser.is_game_over:
                parser.parse()
                time.sleep(FREQUENCY)

        else:
            logger.log_info("There is no game today.")

        wait_until_tomorrow()


def listen():
    """
    Description:
        Listen on the port defined by Google Cloud and print any data received.
    """
    port = int(os.getenv("PORT", "8080"))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', port))
