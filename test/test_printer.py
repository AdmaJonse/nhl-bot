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
from src import events


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
        event    = events.to_event(game_events.game_scheduled_data)
        actual   = self.printer.get_event_string(event)
        expected = ""
        self.assertEqual(expected, actual)


    def test_game_end_dispatcher(self):
        """
        Description:
            Test the expected output of a game end event.
        """
        event    = events.to_event(game_events.game_end_data)
        actual   = self.printer.get_event_string(event)
        expected = "\nThe game is over. Washington wins!\n\nFinal Score:\nWashington: 4\nBoston: 2\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)


    def test_game_official_dispatcher(self):
        """
        Description:
            Test the expected output of a game official event.
        """
        event    = events.to_event(game_events.game_official_data)
        actual   = self.printer.get_event_string(event)
        expected = ""
        self.assertEqual(expected, actual)


    def test_faceoff_dispatcher(self):
        """
        Description:
            Test the expected output of a faceoff event.
        """
        event    = events.to_event(miscellaneous_events.faceoff_data)
        actual   = self.printer.get_event_string(event)
        expected = ""
        self.assertEqual(expected, actual)


    def test_stoppage_dispatcher(self):
        """
        Description:
            Test the expected output of a stoppage event.
        """
        event    = events.to_event(miscellaneous_events.stoppage_data)
        actual   = self.printer.get_event_string(event)
        expected = ""
        self.assertEqual(expected, actual)


    def test_shot_dispatcher(self):
        """
        Description:
            Test the expected output of a shot event.
        """
        event    = events.to_event(miscellaneous_events.shot_data)
        actual   = self.printer.get_event_string(event)
        expected = ""
        self.assertEqual(expected, actual)


    def test_hit_dispatcher(self):
        """
        Description:
            Test the expected output of a hit event.
        """
        event    = events.to_event(miscellaneous_events.hit_data)
        actual   = self.printer.get_event_string(event)
        expected = ""
        self.assertEqual(expected, actual)


    def test_blocked_shot_dispatcher(self):
        """
        Description:
            Test the expected output of a blocked shot event.
        """
        event    = events.to_event(miscellaneous_events.blocked_shot_data)
        actual   = self.printer.get_event_string(event)
        expected = ""
        self.assertEqual(expected, actual)


    def test_giveaway_dispatcher(self):
        """
        Description:
            Test the expected output of a giveaway event.
        """
        event    = events.to_event(miscellaneous_events.giveaway_data)
        actual   = self.printer.get_event_string(event)
        expected = ""
        self.assertEqual(expected, actual)


    def test_takeaway_dispatcher(self):
        """
        Description:
            Test the expected output of a takeaway event.
        """
        event    = events.to_event(miscellaneous_events.takeaway_data)
        actual   = self.printer.get_event_string(event)
        expected = ""
        self.assertEqual(expected, actual)


    def test_missed_shot_dispatcher(self):
        """
        Description:
            Test the expected output of a missed shot event.
        """
        event    = events.to_event(miscellaneous_events.missed_shot_data)
        actual   = self.printer.get_event_string(event)
        expected = ""
        self.assertEqual(expected, actual)


    def test_penalty_dispatcher(self):
        """
        Description:
            Test the expected output of a penalty event.
        """
        event    = events.to_event(penalty_events.penalty_data)
        actual   = self.printer.get_event_string(event)
        expected = "\nThere is a penalty on Washington.\n\nNic Dowd\n2 minute minor for hi-sticking\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)


    def test_penalty_no_taker_dispatcher(self):
        """
        Description:
            Test the expected output of a penalty event when no
            penalty taker is present in the event data.
        """
        event    = events.to_event(penalty_events.penalty_data_no_taker)
        actual   = self.printer.get_event_string(event)
        expected = ""
        self.assertEqual(expected, actual)


    def test_penalty_shot_dispatcher(self):
        """
        Description:
            Test the expected output of a penalty shot event.
        """
        event    = events.to_event(penalty_events.penalty_shot_data)
        actual   = self.printer.get_event_string(event)
        expected = "\nThat's a penalty shot for Washington!\n\nThe infraction is against Brenden Dillon for hooking on breakaway.\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)


    def test_period_ready_dispatcher(self):
        """
        Description:
            Test the expected output of a period ready event.
        """
        event    = events.to_event(period_events.period_ready_data)
        actual   = self.printer.get_event_string(event)
        expected = ""
        self.assertEqual(expected, actual)


    def test_period_start_dispatcher(self):
        """
        Description:
            Test the expected output of a period start event.
        """
        event    = events.to_event(period_events.period_start_data)
        actual   = self.printer.get_event_string(event)
        expected = "\nThe second period is starting at Capital One Arena in Washington.\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)


    def test_period_end_dispatcher(self):
        """
        Description:
            Test the expected output of a period end event.
        """
        event    = events.to_event(period_events.period_end_data)
        actual   = self.printer.get_event_string(event)
        expected = "\nThe first period is over at Capital One Arena.\n\nGoals\nWashington: 0\nBoston: 0\n\nShots on Goal\nWashington: 33\nBoston: 30\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)


    def test_period_official_dispatcher(self):
        """
        Description:
            Test the expected output of a period official event.
        """
        event    = events.to_event(period_events.period_official_data)
        actual   = self.printer.get_event_string(event)
        expected = ""
        self.assertEqual(expected, actual)


    def test_goal_dispatcher(self):
        """
        Description:
            Test the expected output of a goal event.
        """
        event    = events.to_event(goal_events.goal_data)
        actual   = self.printer.get_event_string(event)
        expected = "\nWashington goal!\n\nScored by John Carlson with 15:49 remaining in the 2nd period.\n\nWashington: 1\nBoston: 0\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)


    def test_goal_no_scorer_dispatcher(self):
        """
        Description:
            Test the expected output of a goal event when no scorer is present
            in the event data.
        """
        event    = events.to_event(goal_events.goal_data_no_scorer)
        actual   = self.printer.get_event_string(event)
        expected = ""
        self.assertEqual(expected, actual)


    def test_challenge_dispatcher(self):
        """
        Description:
            Test the expected output of a coach's challenge event.
        """
        event    = events.to_event(miscellaneous_events.challenge_data)
        actual   = self.printer.get_event_string(event)
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
        event    = events.to_event(game_events.game_scheduled_data)
        actual   = self.printer.get_game_scheduled_string(event)
        expected = ""
        self.assertEqual(expected, actual)


    def test_game_end(self):
        """
        Description:
            Test the expected output of a game end event.
        """
        event    = events.to_event(game_events.game_end_data)
        actual   = self.printer.get_game_end_string(event)
        expected = "\nThe game is over. Washington wins!\n\nFinal Score:\nWashington: 4\nBoston: 2\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)


    def test_game_official(self):
        """
        Description:
            Test the expected output of a game official event.
        """
        event    = events.to_event(game_events.game_official_data)
        actual   = self.printer.get_game_official_string(event)
        expected = ""
        self.assertEqual(expected, actual)


    def test_faceoff(self):
        """
        Description:
            Test the expected output of a faceoff event.
        """
        event    = events.to_event(miscellaneous_events.faceoff_data)
        actual   = self.printer.get_faceoff_string(event)
        expected = ""
        self.assertEqual(expected, actual)


    def test_stoppage(self):
        """
        Description:
            Test the expected output of a stoppage event.
        """
        event    = events.to_event(miscellaneous_events.stoppage_data)
        actual   = self.printer.get_stoppage_string(event)
        expected = ""
        self.assertEqual(expected, actual)


    def test_shot(self):
        """
        Description:
            Test the expected output of a shot event.
        """
        event    = events.to_event(miscellaneous_events.shot_data)
        actual   = self.printer.get_shot_string(event)
        expected = ""
        self.assertEqual(expected, actual)


    def test_hit(self):
        """
        Description:
            Test the expected output of a hit event.
        """
        event    = events.to_event(miscellaneous_events.hit_data)
        actual   = self.printer.get_hit_string(event)
        expected = ""
        self.assertEqual(expected, actual)


    def test_blocked_shot(self):
        """
        Description:
            Test the expected output of a blocked shot event.
        """
        event    = events.to_event(miscellaneous_events.blocked_shot_data)
        actual   = self.printer.get_blocked_shot_string(event)
        expected = ""
        self.assertEqual(expected, actual)


    def test_giveaway(self):
        """
        Description:
            Test the expected output of a giveaway event.
        """
        event    = events.to_event(miscellaneous_events.giveaway_data)
        actual   = self.printer.get_giveaway_string(event)
        expected = ""
        self.assertEqual(expected, actual)


    def test_takeaway(self):
        """
        Description:
            Test the expected output of a takeaway event.
        """
        event    = events.to_event(miscellaneous_events.takeaway_data)
        actual   = self.printer.get_takeaway_string(event)
        expected = ""
        self.assertEqual(expected, actual)


    def test_missed_shot(self):
        """
        Description:
            Test the expected output of a missed shot event.
        """
        event    = events.to_event(miscellaneous_events.missed_shot_data)
        actual   = self.printer.get_missed_shot_string(event)
        expected = ""
        self.assertEqual(expected, actual)


    def test_penalty(self):
        """
        Description:
            Test the expected output of a penalty event.
        """
        event    = events.to_event(penalty_events.penalty_data)
        actual   = self.printer.get_penalty_string(event)
        expected = "\nThere is a penalty on Washington.\n\nNic Dowd\n2 minute minor for hi-sticking\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)


    def test_penalty_no_taker(self):
        """
        Description:
            Test the expected output of a penalty event when no
            penalty taker is present in the event data.
        """
        event    = events.to_event(penalty_events.penalty_data_no_taker)
        actual   = self.printer.get_penalty_string(event)
        expected = ""
        self.assertEqual(expected, actual)


    def test_penalty_shot(self):
        """
        Description:
            Test the expected output of a penalty shot event.
        """
        event    = events.to_event(penalty_events.penalty_shot_data)
        actual   = self.printer.get_penalty_shot_string(event)
        expected = "\nThat's a penalty shot for Washington!\n\nThe infraction is against Brenden Dillon for hooking on breakaway.\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)


    def test_period_ready(self):
        """
        Description:
            Test the expected output of a period ready event.
        """
        event    = events.to_event(period_events.period_ready_data)
        actual   = self.printer.get_period_ready_string(event)
        expected = ""
        self.assertEqual(expected, actual)


    def test_period_start(self):
        """
        Description:
            Test the expected output of a period start event.
        """
        event    = events.to_event(period_events.period_start_data)
        actual   = self.printer.get_period_start_string(event)
        expected = "\nThe second period is starting at Capital One Arena in Washington.\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)


    def test_period_end(self):
        """
        Description:
            Test the expected output of a period end event.
        """
        event    = events.to_event(period_events.period_end_data)
        actual   = self.printer.get_period_end_string(event)
        expected = "\nThe first period is over at Capital One Arena.\n\nGoals\nWashington: 0\nBoston: 0\n\nShots on Goal\nWashington: 33\nBoston: 30\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)


    def test_period_official(self):
        """
        Description:
            Test the expected output of a period official event.
        """
        event    = events.to_event(period_events.period_official_data)
        actual   = self.printer.get_period_official_string(event)
        expected = ""
        self.assertEqual(expected, actual)


    def test_goal(self):
        """
        Description:
            Test the expected output of a goal event.
        """
        event    = events.to_event(goal_events.goal_data)
        actual   = self.printer.get_goal_string(event)
        expected = "\nWashington goal!\n\nScored by John Carlson with 15:49 remaining in the 2nd period.\n\nWashington: 1\nBoston: 0\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)


    def test_goal_no_scorer(self):
        """
        Description:
            Test the expected output of a goal event when no scorer is present
            in the event data.
        """
        event    = events.to_event(goal_events.goal_data_no_scorer)
        actual   = self.printer.get_goal_string(event)
        expected = ""
        self.assertEqual(expected, actual)


    def test_power_play_goal(self):
        """
        Description:
            Test the expected output of a power play goal event.
        """
        event    = events.to_event(goal_events.power_play_goal_data)
        actual   = self.printer.get_goal_string(event)
        expected = "\nPower play goal for Boston!\n\nScored by J.T. Miller with 18:05 remaining in the 1st period.\n\nWashington: 1\nBoston: 0\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)


    def test_short_handed_goal(self):
        """
        Description:
            Test the expected output of a short-handed goal event.
        """
        event    = events.to_event(goal_events.short_handed_goal_data)
        actual   = self.printer.get_goal_string(event)
        expected = "\nShort-handed goal for Boston!\n\nScored by J.T. Miller with 18:05 remaining in the 1st period.\n\nWashington: 1\nBoston: 0\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)


    def test_empty_net_goal(self):
        """
        Description:
            Test the expected output of an empty net goal event.
        """
        event    = events.to_event(goal_events.empty_net_goal_data)
        actual   = self.printer.get_goal_string(event)
        expected = "\nEmpty net goal for Boston!\n\nScored by J.T. Miller with 18:05 remaining in the 1st period.\n\nWashington: 1\nBoston: 0\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)


    def test_challenge(self):
        """
        Description:
            Test the expected output of a coach's challenge event.
        """
        event    = events.to_event(miscellaneous_events.challenge_data)
        actual   = self.printer.get_official_challenge_string(event)
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
        previous = events.GameScheduled(miscellaneous_events.null_event)
        event    = events.to_event(game_events.game_scheduled_data)
        actual   = self.printer.get_game_scheduled_reply(previous, event)
        expected = ""
        self.assertEqual(expected, actual)


    def test_game_end_reply(self):
        """
        Description:
            Test the expected output of a reply to a game end event.
        """
        previous = events.GameEnd(miscellaneous_events.null_event)
        event    = events.to_event(game_events.game_end_data)
        actual   = self.printer.get_game_end_reply(previous, event)
        expected = ""
        self.assertEqual(expected, actual)


    def test_game_official_reply(self):
        """
        Description:
            Test the expected output of a reply to a game official event.
        """
        previous = events.GameOfficial(miscellaneous_events.null_event)
        event    = events.to_event(game_events.game_official_data)
        actual   = self.printer.get_game_official_reply(previous, event)
        expected = ""
        self.assertEqual(expected, actual)


    def test_faceoff_reply(self):
        """
        Description:
            Test the expected output of a reply to a faceoff event.
        """
        previous = events.Faceoff(miscellaneous_events.null_event)
        event    = events.to_event(miscellaneous_events.faceoff_data)
        actual   = self.printer.get_faceoff_reply(previous, event)
        expected = ""
        self.assertEqual(expected, actual)


    def test_stoppage_reply(self):
        """
        Description:
            Test the expected output of a reply to a stoppage event.
        """
        previous = events.Stoppage(miscellaneous_events.null_event)
        event    = events.to_event(miscellaneous_events.stoppage_data)
        actual   = self.printer.get_stoppage_reply(previous, event)
        expected = ""
        self.assertEqual(expected, actual)


    def test_shot_reply(self):
        """
        Description:
            Test the expected output of a reply to a shot event.
        """
        previous = events.Shot(miscellaneous_events.null_event)
        event    = events.to_event(miscellaneous_events.shot_data)
        actual   = self.printer.get_shot_reply(previous, event)
        expected = ""
        self.assertEqual(expected, actual)


    def test_hit_reply(self):
        """
        Description:
            Test the expected output of a reply to a hit event.
        """
        previous = events.Hit(miscellaneous_events.null_event)
        event    = events.to_event(miscellaneous_events.hit_data)
        actual   = self.printer.get_hit_reply(previous, event)
        expected = ""
        self.assertEqual(expected, actual)


    def test_blocked_shot_reply(self):
        """
        Description:
            Test the expected output of a reply to a blocked shot event.
        """
        previous = events.BlockedShot(miscellaneous_events.null_event)
        event    = events.to_event(miscellaneous_events.blocked_shot_data)
        actual   = self.printer.get_blocked_shot_reply(previous, event)
        expected = ""
        self.assertEqual(expected, actual)


    def test_giveaway_reply(self):
        """
        Description:
            Test the expected output of a reply to a giveaway event.
        """
        previous = events.Giveaway(miscellaneous_events.null_event)
        event    = events.to_event(miscellaneous_events.giveaway_data)
        actual   = self.printer.get_giveaway_reply(previous, event)
        expected = ""
        self.assertEqual(expected, actual)


    def test_takeaway_reply(self):
        """
        Description:
            Test the expected output of a reply to a takeaway event.
        """
        previous = events.Takeaway(miscellaneous_events.null_event)
        event    = events.to_event(miscellaneous_events.takeaway_data)
        actual   = self.printer.get_takeaway_reply(previous, event)
        expected = ""
        self.assertEqual(expected, actual)


    def test_missed_shot_reply(self):
        """
        Description:
            Test the expected output of a reply to a missed shot event.
        """
        previous = events.MissedShot(miscellaneous_events.null_event)
        event    = events.to_event(miscellaneous_events.missed_shot_data)
        actual   = self.printer.get_missed_shot_reply(previous, event)
        expected = ""
        self.assertEqual(expected, actual)


    def test_penalty_reply(self):
        """
        Description:
            Test the expected output of a reply to a penalty event.
        """
        previous = events.Penalty(miscellaneous_events.null_event)
        event    = events.to_event(penalty_events.penalty_data)
        actual   = self.printer.get_penalty_reply(previous, event)
        expected = ""
        self.assertEqual(expected, actual)


    def test_period_ready_reply(self):
        """
        Description:
            Test the expected output of a reply to a period ready event.
        """
        previous = events.PeriodReady(miscellaneous_events.null_event)
        event    = events.to_event(period_events.period_ready_data)
        actual   = self.printer.get_period_ready_reply(previous, event)
        expected = ""
        self.assertEqual(expected, actual)


    def test_period_start_reply(self):
        """
        Description:
            Test the expected output of a reply to a period start event.
        """
        previous = events.PeriodStart(miscellaneous_events.null_event)
        event    = events.to_event(period_events.period_start_data)
        actual   = self.printer.get_period_start_reply(previous, event)
        expected = ""
        self.assertEqual(expected, actual)


    def test_period_end_reply(self):
        """
        Description:
            Test the expected output of a reply to a period end event.
        """
        previous = events.PeriodEnd(miscellaneous_events.null_event)
        event    = events.to_event(period_events.period_end_data)
        actual   = self.printer.get_period_end_reply(previous, event)
        expected = ""
        self.assertEqual(expected, actual)


    def test_period_official_reply(self):
        """
        Description:
            Test the expected output of a reply to a period official event.
        """
        previous = events.PeriodOfficial(miscellaneous_events.null_event)
        event    = events.to_event(period_events.period_official_data)
        actual   = self.printer.get_period_official_reply(previous, event)
        expected = ""
        self.assertEqual(expected, actual)


    def test_goal_reply(self):
        """
        Description:
            Test the expected output of a reply to a goal event.
        """
        previous = events.Goal(miscellaneous_events.null_event)
        event    = events.to_event(goal_events.goal_data)
        actual   = self.printer.get_goal_reply(previous, event)
        expected = "\nThere has been update to the Washington goal scored with 15:49 remaining in the 2nd period.\n\nJohn Carlson (14) Slap Shot, assists: Conor Sheary (20)\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)


    def test_goal_reply_scorer_change(self):
        """
        Description:
            Test the expected output of a reply to a goal event where
            the goal scorer has changed.
        """
        previous = events.Goal(goal_events.goal_data_scorer_change)
        event    = events.to_event(goal_events.goal_data)
        actual   = self.printer.get_goal_reply(previous, event)
        expected = "\nThe goal is now being awarded to John Carlson.\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)


    def test_goal_reply_primary_assist_change(self):
        """
        Description:
            Test the expected output of a reply to a goal event where
            the primary assist has chnaged.
        """
        previous = events.Goal(goal_events.goal_data_two_assists)
        event    = events.to_event(goal_events.goal_data_primary_assist_change)
        actual   = self.printer.get_goal_reply(previous, event)
        expected = "\nThe assists have been changed on this goal. The primary assist has been awarded to Alex Ovechkin.\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)

    
    def test_goal_reply_secondary_assist_change(self):
        """
        Description:
            Test the expected output of a reply to a goal event where
            the secondary assist has changed.
        """
        previous = events.Goal(goal_events.goal_data_two_assists)
        event    = events.to_event(goal_events.goal_data_secondary_assist_change)
        actual   = self.printer.get_goal_reply(previous, event)
        expected = "\nThe assists have been changed on this goal. The secondary assist has been awarded to Alex Ovechkin.\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)


    def test_goal_reply_time_change(self):
        """
        Description:
            Test the expected output of a reply to a goal event where
            the time of the goal has changed.
        """
        previous = events.Goal(goal_events.goal_data)
        event    = events.to_event(goal_events.goal_data_time_change)
        actual   = self.printer.get_goal_reply(previous, event)
        expected = "\nThe time of this goal has been changed. The scoresheet now indicates this goal occurred with 15:50 remaining in the 2nd period.\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)


    def test_goal_reply_primary_assist_added(self):
        """
        Description:
            Test the expected output of a reply to a goal event where
            a primary assist has been added.
        """
        previous = events.Goal(goal_events.goal_data_no_assists)
        event    = events.to_event(goal_events.goal_data_one_assist)
        actual   = self.printer.get_goal_reply(previous, event)
        expected = "\nA primary assist has been awarded to Conor Sheary.\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)


    def test_goal_reply_secondary_assist_added(self):
        """
        Description:
            Test the expected output of a reply to a goal event where
            a secondary assist has been added.
        """
        previous = events.Goal(goal_events.goal_data_one_assist)
        event    = events.to_event(goal_events.goal_data_two_assists)
        actual   = self.printer.get_goal_reply(previous, event)
        expected = "\nA secondary assist has been awarded to Adam Jones.\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)


    def test_goal_reply_both_assists_added(self):
        """
        Description:
            Test the expected output of a reply to a goal event where
            both a primary and a secondary assist have been added.
        """
        previous = events.Goal(goal_events.goal_data_no_assists)
        event    = events.to_event(goal_events.goal_data_two_assists)
        actual   = self.printer.get_goal_reply(previous, event)
        expected = "\nAssists have been awarded to Conor Sheary and Adam Jones.\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)


    def test_challenge_reply(self):
        """
        Description:
            Test the expected output of a reply to a coach's challenge event.
        """
        previous = events.Challenge(miscellaneous_events.null_event)
        event    = events.to_event(miscellaneous_events.challenge_data)
        actual   = self.printer.get_official_challenge_reply(previous, event)
        expected = ""
        self.assertEqual(expected, actual)
