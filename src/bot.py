"""
Description:
    This module handles the main logic to check for game updates.
"""

from datetime import datetime
from datetime import timedelta
from datetime import timezone

import time
import pause

from src import logger
from src import json_parser
from src import schedule

# How frequently we check for game updates (in seconds)
FREQUENCY = 5  # seconds

def check_for_updates():
    """
    Description:
        This method will check for a game on the current date. If a game is
        found, it will trigger game event parsing at game time. If no game is
        found, it will pause until tomorrow.
    """

    while True:

        logger.log_info("Checking for a game today...")
        today = datetime.today()

        # Determine if there is a game today.
        game_id = schedule.get_game_id()

        if game_id >= 0:

            logger.log_info("There is a game today: " + str(game_id))

            # Wait until game time
            game_time = schedule.get_start_time()

            if game_time > datetime.now(timezone.utc):
                logger.log_info("Waiting until game start: " + str(game_time))
                pause.until(game_time)

            parser = json_parser.Parser(game_id)

            while not parser.is_game_over:
                parser.parse()
                time.sleep(FREQUENCY)

        else:
            logger.log_info("There is no game today.")

        # Pause until tomorrow at 12:00 UTC
        tomorrow = today.replace(hour=12, minute=0, second=0, microsecond=0) + timedelta(days=1)
        logger.log_info("Pausing until: " + str(tomorrow))
        pause.until(tomorrow)
