"""
Unit tests for the Schedule class.
"""

import unittest
from unittest.mock import patch

from datetime import datetime
from test.test_data import schedule_events
import pytz

from src import schedule

TIME_ZONE = pytz.timezone("US/Eastern")

class TestSchedule(unittest.TestCase):
    """
    Unit tests for the Schedule class.
    """

    def test_get_schedule_gameday(self):
        """
        Test to determine if we are getting the expected schedule data on
            a game day.
        """
        with patch('src.schedule.get_current_date') as mock_schedule:
            mock_schedule.return_value = datetime(year=2022, month=4, day=29)
            data = schedule.get_schedule_json()
            self.assertEqual(data["totalItems"], 1)
            self.assertEqual(data["totalEvents"], 0)
            self.assertEqual(data["totalGames"], 1)
            self.assertEqual(data["totalMatches"], 0)
            self.assertEqual(data["dates"][0]["date"], "2022-04-29")
            self.assertEqual(data["dates"][0]["games"][0]["gamePk"], 2021021308)


    def test_get_schedule_offday(self):
        """
        Test to determine if we are getting the expected schedule data on
            an off day.
        """
        with patch('src.schedule.get_current_date') as mock_schedule:
            mock_schedule.return_value = datetime(year=2022, month=5, day=1)
            data = schedule.get_schedule_json()
            self.assertEqual(data["totalItems"], 0)
            self.assertEqual(data["totalEvents"], 0)
            self.assertEqual(data["totalGames"], 0)
            self.assertEqual(data["totalMatches"], 0)
            self.assertEqual(data["dates"], [])


    def test_valid_game_id(self):
        """
        Test retrieving the game ID from schedule data when the
            ID is valid.
        """
        with patch('src.schedule.get_schedule_json') as mock_schedule:
            mock_schedule.return_value = schedule_events.valid_schedule_data
            actual   = schedule.get_game_id()
            expected = 2021021162
            self.assertEqual(expected, actual)


    def test_invalid_game_id(self):
        """
        Test retrieving the game ID from schedule data when the
            ID is not valid.
        """
        with patch('src.schedule.get_schedule_json') as mock_schedule:
            mock_schedule.return_value = schedule_events.invalid_schedule_data
            actual   = schedule.get_game_id()
            expected = None
            self.assertEqual(expected, actual)


    def test_valid_start_time(self):
        """
        Test retrieving the game start time from schedule data when the
            start time is valid.
        """
        with patch('src.schedule.get_schedule_json') as mock_schedule:
            mock_schedule.return_value = schedule_events.valid_schedule_data
            actual   = schedule.get_start_time()
            expected = datetime(2022, 4, 11, 23, 0, tzinfo=pytz.utc)
            self.assertEqual(expected, actual)


    def test_invalid_start_time(self):
        """
        Test retrieving the game start time from schedule data when the
            start time is invalid.
        """
        with patch('src.schedule.get_schedule_json') as mock_schedule:
            mock_schedule.return_value = schedule_events.invalid_schedule_data
            actual   = schedule.get_start_time()
            expected = None
            self.assertEqual(expected, actual)
