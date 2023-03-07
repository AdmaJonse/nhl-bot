"""
This module handles the main logic to check for game updates.
"""

from datetime import datetime, timedelta
from typing import Optional
from threading import Thread
import pause

from src import schedule
from src.command.command_queue import command_queue
from src.command.parse import Parse
from src.event_list import event_list
from src.highlight_list import highlight_list
from src.logger import log
from src.parsers import parsers


# How frequently we check for game updates (in seconds)
FREQUENCY = 5  # seconds


def wait_until_game_start():
    """
    This function will wait until the start of the given game.
    """
    game_time: Optional[datetime] = schedule.get_start_time()
    current_time: Optional[datetime] = schedule.get_current_time()
    if game_time > current_time:
        log.info("Waiting until game start: " +
                 schedule.time_to_string(game_time))
        pause.until(game_time)


def wait_until_morning():
    """
    This function will wait until the next day.
    """
    current_time: datetime = schedule.get_current_time()
    noon: datetime = schedule.get_noon()
    if current_time > noon:
        noon += timedelta(days=1)
    log.info("Pausing until: " + schedule.time_to_string(noon))
    pause.until(noon)


def scheduled_parsing():
    """
    Enqueue a parse command every five seconds.
    """
    while True:
        command_queue.enqueue(Parse())
        pause.seconds(5)


def check_for_updates():
    """
    This function will check for a game on the current date. If a game is
    found, it will trigger game event parsing at game time. If no game is
    found, it will pause until tomorrow.
    """
    while True:

        log.flush()
        log.info("Checking for a game today...")

        # Determine if there is a game today
        game_id: Optional[int] = schedule.get_game_id()

        if game_id is not None and game_id >= 0:

            log.info("There is a game today: " + str(game_id))
            wait_until_game_start()

            # Setup for the current
            parsers.set_game(game_id)
            parse_thread: Thread = Thread(target=scheduled_parsing)
            parse_thread.start()

            # Start processing commands from the queue. This is a blocking call. It will only
            # return once the Game Official event occurs and the corresponding stop is called.
            command_queue.start()

            # Perform any cleanup
            event_list.clear()
            highlight_list.clear()
            parsers.clear()

        else:
            log.info("There is no game today.")

        wait_until_morning()
