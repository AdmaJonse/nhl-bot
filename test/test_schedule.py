import unittest

from datetime import datetime
from datetime import timezone
from src import schedule
from test import test_data

class TestSchedule(unittest.TestCase):

    def test_valid_game_id(self):
        actual   = schedule.get_game_id(test_data.valid_schedule_data)
        expected = 2021021162
        self.assertEqual(expected, actual)


    def test_invalid_game_id(self):
        actual   = schedule.get_game_id(test_data.invalid_schedule_data)
        expected = -1
        self.assertEqual(expected, actual)


    def test_valid_start_time(self):
        actual   = schedule.get_start_time(test_data.valid_schedule_data)
        expected = datetime(2022, 4, 11, 23, 0, tzinfo=timezone.utc)
        self.assertEqual(expected, actual)


    def test_invalid_start_time(self):
        actual   = schedule.get_start_time(test_data.invalid_schedule_data)
        expected = -1
        self.assertEqual(expected, actual)