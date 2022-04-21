"""
Description:
    Unit tests for the Schedule class.
"""

import unittest

from datetime import datetime
from datetime import timezone
from test.test_data import schedule_events
from src import schedule

class TestSchedule(unittest.TestCase):
    """
    Description:
        Unit tests for the Schedule class.
    """

    def test_valid_game_id(self):
        """
        Description:
            Test retrieving the game ID from schedule data when the
            ID is valid.
        """
        actual   = schedule.get_game_id(schedule_events.valid_schedule_data)
        expected = 2021021162
        self.assertEqual(expected, actual)


    def test_invalid_game_id(self):
        """
        Description:
            Test retrieving the game ID from schedule data when the
            ID is not valid.
        """
        actual   = schedule.get_game_id(schedule_events.invalid_schedule_data)
        expected = -1
        self.assertEqual(expected, actual)


    def test_valid_start_time(self):
        """
        Description:
            Test retrieving the game start time from schedule data when the
            start time is valid.
        """
        actual   = schedule.get_start_time(schedule_events.valid_schedule_data)
        expected = datetime(2022, 4, 11, 23, 0, tzinfo=timezone.utc)
        self.assertEqual(expected, actual)


    def test_invalid_start_time(self):
        """
        Description:
            Test retrieving the game start time from schedule data when the
            start time is invalid.
        """
        actual   = schedule.get_start_time(schedule_events.invalid_schedule_data)
        expected = -1
        self.assertEqual(expected, actual)
