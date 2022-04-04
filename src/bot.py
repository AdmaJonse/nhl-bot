import datetime
import pause
import time

from src import logger
from src import json_parser
from src import schedule

from datetime import datetime
from datetime import timedelta
from datetime import timezone

# How frequently we check for game updates (in seconds)
frequency = 10  # seconds

def check_for_updates():

    while True:

        logger.log_info("Checking for a game today...")

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
            
            while (not parser.is_game_over):
                parser.parse()
                time.sleep(frequency)

        else:
            logger.log_info("There is no game today. Sleeping until tomorrow.")
            
        logger.log_info("Pausing until tomorrow...")
        tomorrow = datetime.today() + timedelta(days=1)
        pause.until(tomorrow)