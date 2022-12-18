"""
Description:
    This module defines logging behaviour for the application.
"""

import logging
import logging.handlers
import sys

class Logger:
    """
    Description:
        This class defines logging behaviour for the application.
    """

    def __init__(self):

        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter('| %(levelname)s | %(message)s')

        stdout_handler = logging.StreamHandler(sys.stdout)
        stdout_handler.setLevel(logging.INFO)
        stdout_handler.setFormatter(formatter)

        file_handler = logging.handlers.RotatingFileHandler("bot.log",
                                                            maxBytes=1000000,
                                                            backupCount=1)
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(formatter)

        self.logger.addHandler(stdout_handler)
        self.logger.addHandler(file_handler)


    def info(self, msg):
        """
        Description:
            Log the given message at the info level.
        """
        self.logger.info(msg)


    def error(self, msg):
        """
        Description:
            Log the given message at the error level.
        """
        self.logger.error(msg)


    def verbose(self, msg):
        """
        Description:
            Log the given message at the debug level.
        """
        self.logger.debug(msg)


log = Logger()


def log_info(msg):
    """
    Description:
        Log the given message at the info level.
    """
    log.info(msg)


def log_error(msg):
    """
    Description:
        Log the given message at the error level.
    """
    log.error(msg)


def log_verbose(msg):
    """
    Description:
        Log the given message at the debug level.
    """
    log.verbose(msg)
