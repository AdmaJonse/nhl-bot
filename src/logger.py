import logging
import sys

class Logger:

    def __init__(self):

        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter('| %(levelname)s | %(message)s')
        
        stdout_handler = logging.StreamHandler(sys.stdout)
        stdout_handler.setLevel(logging.DEBUG)
        stdout_handler.setFormatter(formatter)
        
        file_handler = logging.FileHandler('job.log')
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)
        self.logger.addHandler(stdout_handler)


    def info(self, msg):
        self.logger.info(msg)


    def error(self, msg):
        self.logger.error(msg)


    def verbose(self, msg):
        self.logger.debug(msg)


log = Logger()


def log_info(msg):
    log.info(msg)


def log_error(msg):
    log.error(msg)


def log_verbose(msg):
    log.verbose(msg)