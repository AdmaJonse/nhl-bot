"""
Description:
    The main process for the NHL twitter bot application.
"""

from datetime import datetime
from src import bot
from src import logger


if __name__ == "__main__":
    logger.log_info("Application deployed at: " + str(datetime.now()))
    bot.check_for_updates()
