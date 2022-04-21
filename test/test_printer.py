"""
Description:
    Unit tests for the Printer class.
"""

import unittest
from test.test_data import game_events
from test.test_data import goal_events
from test.test_data import miscellaneous_events
from test.test_data import penalty_events
from test.test_data import period_events
from src import printer


class TestPrinter(unittest.TestCase):
    """
    Description:
        Unit tests for the Printer class.
    """

    @classmethod
    def setUpClass(cls):
        cls.printer = printer.Printer(game_events.game_data)

    #################################################
    # Event Dispatcher
    #################################################

    def test_game_scheduled_dispatcher(self):
        """
        Description:
            Test the expected output of a game scheduled event.
        """
        actual   = self.printer.get_event_string(game_events.game_scheduled_data)
        expected = ""
        self.assertEqual(expected, actual)


    def test_game_end_dispatcher(self):
        """
        Description:
            Test the expected output of a game end event.
        """
        actual   = self.printer.get_event_string(game_events.game_end_data)
        expected = "\nThe game is over. Washington wins!\n\nFinal Score:\nWashington: 4\nBoston: 2\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)


    def test_game_official_dispatcher(self):
        """
        Description:
            Test the expected output of a game official event.
        """
        actual   = self.printer.get_event_string(game_events.game_official_data)
        expected = ""
        self.assertEqual(expected, actual)


    def test_faceoff_dispatcher(self):
        """
        Description:
            Test the expected output of a faceoff event.
        """
        actual   = self.printer.get_event_string(miscellaneous_events.faceoff_data)
        expected = ""
        self.assertEqual(expected, actual)


    def test_stoppage_dispatcher(self):
        """
        Description:
            Test the expected output of a stoppage event.
        """
        actual   = self.printer.get_event_string(miscellaneous_events.stoppage_data)
        expected = ""
        self.assertEqual(expected, actual)


    def test_shot_dispatcher(self):
        """
        Description:
            Test the expected output of a shot event.
        """
        actual   = self.printer.get_event_string(miscellaneous_events.shot_data)
        expected = ""
        self.assertEqual(expected, actual)


    def test_hit_dispatcher(self):
        """
        Description:
            Test the expected output of a hit event.
        """
        actual   = self.printer.get_event_string(miscellaneous_events.hit_data)
        expected = ""
        self.assertEqual(expected, actual)


    def test_blocked_shot_dispatcher(self):
        """
        Description:
            Test the expected output of a blocked shot event.
        """
        actual   = self.printer.get_event_string(miscellaneous_events.blocked_shot_data)
        expected = ""
        self.assertEqual(expected, actual)


    def test_giveaway_dispatcher(self):
        """
        Description:
            Test the expected output of a giveaway event.
        """
        actual   = self.printer.get_event_string(miscellaneous_events.giveaway_data)
        expected = ""
        self.assertEqual(expected, actual)


    def test_takeaway_dispatcher(self):
        """
        Description:
            Test the expected output of a takeaway event.
        """
        actual   = self.printer.get_event_string(miscellaneous_events.takeaway_data)
        expected = ""
        self.assertEqual(expected, actual)


    def test_missed_shot_dispatcher(self):
        """
        Description:
            Test the expected output of a missed shot event.
        """
        actual   = self.printer.get_event_string(miscellaneous_events.missed_shot_data)
        expected = ""
        self.assertEqual(expected, actual)


    def test_penalty_dispatcher(self):
        """
        Description:
            Test the expected output of a penalty event.
        """
        actual   = self.printer.get_event_string(penalty_events.penalty_data)
        expected = "\nThere is a penalty on Washington.\n\nNic Dowd\n2 minute minor for hi-sticking\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)


    def test_penalty_no_taker_dispatcher(self):
        """
        Description:
            Test the expected output of a penalty event when no
            penalty taker is present in the event data.
        """
        actual   = self.printer.get_event_string(penalty_events.penalty_data_no_taker)
        expected = ""
        self.assertEqual(expected, actual)


    def test_penalty_shot_dispatcher(self):
        """
        Description:
            Test the expected output of a penalty shot event.
        """
        actual   = self.printer.get_event_string(penalty_events.penalty_shot_data)
        expected = "\nThat's a penalty shot for Washington!\n\nThe infraction is against Brenden Dillon for hooking on breakaway.\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)


    def test_period_ready_dispatcher(self):
        """
        Description:
            Test the expected output of a period ready event.
        """
        actual   = self.printer.get_event_string(period_events.period_ready_data)
        expected = ""
        self.assertEqual(expected, actual)


    def test_period_start_dispatcher(self):
        """
        Description:
            Test the expected output of a period start event.
        """
        actual   = self.printer.get_event_string(period_events.period_start_data)
        expected = "\nThe second period is starting at Capital One Arena in Washington.\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)


    def test_period_end_dispatcher(self):
        """
        Description:
            Test the expected output of a period end event.
        """
        actual   = self.printer.get_event_string(period_events.period_end_data)
        expected = "\nThe first period is over at Capital One Arena.\n\nGoals\nWashington: 0\nBoston: 0\n\nShots on Goal\nWashington: 33\nBoston: 30\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)


    def test_period_official_dispatcher(self):
        """
        Description:
            Test the expected output of a period official event.
        """
        actual   = self.printer.get_event_string(period_events.period_official_data)
        expected = ""
        self.assertEqual(expected, actual)


    def test_goal_dispatcher(self):
        """
        Description:
            Test the expected output of a goal event.
        """
        actual   = self.printer.get_event_string(goal_events.goal_data)
        expected = "\nWashington goal!\n\nScored by John Carlson with 15:49 remaining in the 2nd period.\n\nWashington: 1\nBoston: 0\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)


    def test_goal_no_scorer_dispatcher(self):
        """
        Description:
            Test the expected output of a goal event when no scorer is present
            in the event data.
        """
        actual   = self.printer.get_event_string(goal_events.goal_data_no_scorer)
        expected = ""
        self.assertEqual(expected, actual)


    def test_challenge_dispatcher(self):
        """
        Description:
            Test the expected output of a coach's challenge event.
        """
        actual   = self.printer.get_event_string(miscellaneous_events.challenge_data)
        expected = "\nBoston is challenging the ruling on the play.\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)

    #################################################
    # Event Posts
    #################################################

    def test_game_scheduled(self):
        """
        Description:
            Test the expected output of a game scheduled event.
        """
        actual   = self.printer.get_game_scheduled_string(game_events.game_scheduled_data)
        expected = ""
        self.assertEqual(expected, actual)


    def test_game_end(self):
        """
        Description:
            Test the expected output of a game end event.
        """
        actual   = self.printer.get_game_end_string(game_events.game_end_data)
        expected = "\nThe game is over. Washington wins!\n\nFinal Score:\nWashington: 4\nBoston: 2\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)


    def test_game_official(self):
        """
        Description:
            Test the expected output of a game official event.
        """
        actual   = self.printer.get_game_official_string(game_events.game_official_data)
        expected = ""
        self.assertEqual(expected, actual)


    def test_faceoff(self):
        """
        Description:
            Test the expected output of a faceoff event.
        """
        actual   = self.printer.get_faceoff_string(miscellaneous_events.faceoff_data)
        expected = ""
        self.assertEqual(expected, actual)


    def test_stoppage(self):
        """
        Description:
            Test the expected output of a stoppage event.
        """
        actual   = self.printer.get_stoppage_string(miscellaneous_events.stoppage_data)
        expected = ""
        self.assertEqual(expected, actual)


    def test_shot(self):
        """
        Description:
            Test the expected output of a shot event.
        """
        actual   = self.printer.get_shot_string(miscellaneous_events.shot_data)
        expected = ""
        self.assertEqual(expected, actual)


    def test_hit(self):
        """
        Description:
            Test the expected output of a hit event.
        """
        actual   = self.printer.get_hit_string(miscellaneous_events.hit_data)
        expected = ""
        self.assertEqual(expected, actual)


    def test_blocked_shot(self):
        """
        Description:
            Test the expected output of a blocked shot event.
        """
        actual   = self.printer.get_blocked_shot_string(miscellaneous_events.blocked_shot_data)
        expected = ""
        self.assertEqual(expected, actual)


    def test_giveaway(self):
        """
        Description:
            Test the expected output of a giveaway event.
        """
        actual   = self.printer.get_giveaway_string(miscellaneous_events.giveaway_data)
        expected = ""
        self.assertEqual(expected, actual)


    def test_takeaway(self):
        """
        Description:
            Test the expected output of a takeaway event.
        """
        actual   = self.printer.get_takeaway_string(miscellaneous_events.takeaway_data)
        expected = ""
        self.assertEqual(expected, actual)


    def test_missed_shot(self):
        """
        Description:
            Test the expected output of a missed shot event.
        """
        actual   = self.printer.get_missed_shot_string(miscellaneous_events.missed_shot_data)
        expected = ""
        self.assertEqual(expected, actual)


    def test_penalty(self):
        """
        Description:
            Test the expected output of a penalty event.
        """
        actual   = self.printer.get_penalty_string(penalty_events.penalty_data)
        expected = "\nThere is a penalty on Washington.\n\nNic Dowd\n2 minute minor for hi-sticking\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)


    def test_penalty_no_taker(self):
        """
        Description:
            Test the expected output of a penalty event when no
            penalty taker is present in the event data.
        """
        actual   = self.printer.get_penalty_string(penalty_events.penalty_data_no_taker)
        expected = ""
        self.assertEqual(expected, actual)


    def test_penalty_shot(self):
        """
        Description:
            Test the expected output of a penalty shot event.
        """
        actual   = self.printer.get_penalty_string(penalty_events.penalty_shot_data)
        expected = "\nThat's a penalty shot for Washington!\n\nThe infraction is against Brenden Dillon for hooking on breakaway.\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)


    def test_period_ready(self):
        """
        Description:
            Test the expected output of a period ready event.
        """
        actual   = self.printer.get_period_ready_string(period_events.period_ready_data)
        expected = ""
        self.assertEqual(expected, actual)


    def test_period_start(self):
        """
        Description:
            Test the expected output of a period start event.
        """
        actual   = self.printer.get_period_start_string(period_events.period_start_data)
        expected = "\nThe second period is starting at Capital One Arena in Washington.\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)


    def test_period_end(self):
        """
        Description:
            Test the expected output of a period end event.
        """
        actual   = self.printer.get_period_end_string(period_events.period_end_data)
        expected = "\nThe first period is over at Capital One Arena.\n\nGoals\nWashington: 0\nBoston: 0\n\nShots on Goal\nWashington: 33\nBoston: 30\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)


    def test_period_official(self):
        """
        Description:
            Test the expected output of a period official event.
        """
        actual   = self.printer.get_period_official_string(period_events.period_official_data)
        expected = ""
        self.assertEqual(expected, actual)


    def test_goal(self):
        """
        Description:
            Test the expected output of a goal event.
        """
        actual   = self.printer.get_goal_string(goal_events.goal_data)
        expected = "\nWashington goal!\n\nScored by John Carlson with 15:49 remaining in the 2nd period.\n\nWashington: 1\nBoston: 0\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)


    def test_goal_no_scorer(self):
        """
        Description:
            Test the expected output of a goal event when no scorer is present
            in the event data.
        """
        actual   = self.printer.get_goal_string(goal_events.goal_data_no_scorer)
        expected = ""
        self.assertEqual(expected, actual)


    def test_power_play_goal(self):
        """
        Description:
            Test the expected output of a power play goal event.
        """
        actual   = self.printer.get_goal_string(goal_events.power_play_goal_data)
        expected = "\nPower play goal for Boston!\n\nScored by J.T. Miller with 18:05 remaining in the 1st period.\n\nWashington: 1\nBoston: 0\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)


    def test_short_handed_goal(self):
        """
        Description:
            Test the expected output of a short-handed goal event.
        """
        actual   = self.printer.get_goal_string(goal_events.short_handed_goal_data)
        expected = "\nShort-handed goal for Boston!\n\nScored by J.T. Miller with 18:05 remaining in the 1st period.\n\nWashington: 1\nBoston: 0\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)


    def test_empty_net_goal(self):
        """
        Description:
            Test the expected output of an empty net goal event.
        """
        actual   = self.printer.get_goal_string(goal_events.empty_net_goal_data)
        expected = "\nEmpty net goal for Boston!\n\nScored by J.T. Miller with 18:05 remaining in the 1st period.\n\nWashington: 1\nBoston: 0\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)


    def test_challenge(self):
        """
        Description:
            Test the expected output of a coach's challenge event.
        """
        actual   = self.printer.get_official_challenge_string(miscellaneous_events.challenge_data)
        expected = "\nBoston is challenging the ruling on the play.\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)


    #################################################
    # Event Replies
    #################################################

    def test_game_scheduled_reply(self):
        """
        Description:
            Test the expected output of a reply to a game scheduled event.
        """
        previous_data = {}
        actual   = self.printer.get_game_scheduled_reply(previous_data, game_events.game_scheduled_data)
        expected = ""
        self.assertEqual(expected, actual)


    def test_game_end_reply(self):
        """
        Description:
            Test the expected output of a reply to a game end event.
        """
        previous_data = {}
        actual   = self.printer.get_game_end_reply(previous_data, game_events.game_end_data)
        expected = ""
        self.assertEqual(expected, actual)


    def test_game_official_reply(self):
        """
        Description:
            Test the expected output of a reply to a game official event.
        """
        previous_data = {}
        actual   = self.printer.get_game_official_reply(previous_data, game_events.game_official_data)
        expected = ""
        self.assertEqual(expected, actual)


    def test_faceoff_reply(self):
        """
        Description:
            Test the expected output of a reply to a faceoff event.
        """
        previous_data = {}
        actual   = self.printer.get_faceoff_reply(previous_data, miscellaneous_events.faceoff_data)
        expected = ""
        self.assertEqual(expected, actual)


    def test_stoppage_reply(self):
        """
        Description:
            Test the expected output of a reply to a stoppage event.
        """
        previous_data = {}
        actual   = self.printer.get_stoppage_reply(previous_data, miscellaneous_events.stoppage_data)
        expected = ""
        self.assertEqual(expected, actual)


    def test_shot_reply(self):
        """
        Description:
            Test the expected output of a reply to a shot event.
        """
        previous_data = {}
        actual   = self.printer.get_shot_reply(previous_data, miscellaneous_events.shot_data)
        expected = ""
        self.assertEqual(expected, actual)


    def test_hit_reply(self):
        """
        Description:
            Test the expected output of a reply to a hit event.
        """
        previous_data = {}
        actual   = self.printer.get_hit_reply(previous_data, miscellaneous_events.hit_data)
        expected = ""
        self.assertEqual(expected, actual)


    def test_blocked_shot_reply(self):
        """
        Description:
            Test the expected output of a reply to a blocked shot event.
        """
        previous_data = {}
        actual   = self.printer.get_blocked_shot_reply(previous_data, miscellaneous_events.blocked_shot_data)
        expected = ""
        self.assertEqual(expected, actual)


    def test_giveaway_reply(self):
        """
        Description:
            Test the expected output of a reply to a giveaway event.
        """
        previous_data = {}
        actual   = self.printer.get_giveaway_reply(previous_data, miscellaneous_events.giveaway_data)
        expected = ""
        self.assertEqual(expected, actual)


    def test_takeaway_reply(self):
        """
        Description:
            Test the expected output of a reply to a takeaway event.
        """
        previous_data = {}
        actual   = self.printer.get_takeaway_reply(previous_data, miscellaneous_events.takeaway_data)
        expected = ""
        self.assertEqual(expected, actual)


    def test_missed_shot_reply(self):
        """
        Description:
            Test the expected output of a reply to a missed shot event.
        """
        previous_data = {}
        actual   = self.printer.get_missed_shot_reply(previous_data, miscellaneous_events.missed_shot_data)
        expected = ""
        self.assertEqual(expected, actual)


    def test_penalty_reply(self):
        """
        Description:
            Test the expected output of a reply to a penalty event.
        """
        previous_data = {}
        actual   = self.printer.get_penalty_reply(previous_data, penalty_events.penalty_data)
        expected = ""
        self.assertEqual(expected, actual)


    def test_period_ready_reply(self):
        """
        Description:
            Test the expected output of a reply to a period ready event.
        """
        previous_data = {}
        actual   = self.printer.get_period_ready_reply(previous_data, period_events.period_ready_data)
        expected = ""
        self.assertEqual(expected, actual)


    def test_period_start_reply(self):
        """
        Description:
            Test the expected output of a reply to a period start event.
        """
        previous_data = {}
        actual   = self.printer.get_period_start_reply(previous_data, period_events.period_start_data)
        expected = ""
        self.assertEqual(expected, actual)


    def test_period_end_reply(self):
        """
        Description:
            Test the expected output of a reply to a period end event.
        """
        previous_data = {}
        actual   = self.printer.get_period_end_reply(previous_data, period_events.period_end_data)
        expected = ""
        self.assertEqual(expected, actual)


    def test_period_official_reply(self):
        """
        Description:
            Test the expected output of a reply to a period official event.
        """
        previous_data = {}
        actual   = self.printer.get_period_official_reply(previous_data, period_events.period_official_data)
        expected = ""
        self.assertEqual(expected, actual)


    def test_goal_reply(self):
        """
        Description:
            Test the expected output of a reply to a goal event.
        """
        previous_data = {}
        actual   = self.printer.get_goal_reply(previous_data, goal_events.goal_data)
        expected = ""
        self.assertEqual(expected, actual)


    def test_challenge_reply(self):
        """
        Description:
            Test the expected output of a reply to a coach's challenge event.
        """
        previous_data = {}
        actual   = self.printer.get_official_challenge_reply(previous_data, miscellaneous_events.challenge_data)
        expected = ""
        self.assertEqual(expected, actual)
