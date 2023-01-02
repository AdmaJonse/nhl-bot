"""
Description:
    Unit tests for the generator class.
"""

import unittest
from test.test_data import game_events
from test.test_data import goal_events
from test.test_data import miscellaneous_events
from test.test_data import penalty_events
from test.test_data import period_events

from src import game_data
from src import generator
from src import event_factory

from src.events.blocked_shot import BlockedShot
from src.events.challenge import Challenge
from src.events.faceoff import Faceoff
from src.events.game_end import GameEnd
from src.events.game_official import GameOfficial
from src.events.game_scheduled import GameScheduled
from src.events.giveaway import Giveaway
from src.events.goal import Goal
from src.events.hit import Hit
from src.events.missed_shot import MissedShot
from src.events.penalty import Penalty
from src.events.penalty_shot import PenaltyShot
from src.events.period_end import PeriodEnd
from src.events.period_official import PeriodOfficial
from src.events.period_ready import PeriodReady
from src.events.period_start import PeriodStart
from src.events.shot import Shot
from src.events.stoppage import Stoppage
from src.events.takeaway import Takeaway


class TestGenerator(unittest.TestCase):
    """
    Description:
        Unit tests for the generator class.
    """

    @classmethod
    def setUpClass(cls):
        cls.generator = generator.Generator(game_events.game_data)

    #################################################
    # Event Dispatcher
    #################################################

    def test_game_scheduled(self):
        """
        Description:
            Test the expected output of a game scheduled event.
        """
        event    = event_factory.create(game_events.game_scheduled_data)
        actual   = self.generator.get_event_string(event)
        expected = None
        self.assertEqual(expected, actual)


    def test_game_end_regulation(self):
        """
        Description:
            Test the expected output of a game end event.
        """
        self.generator.game_data = game_data.GameData(game_events.game_data)
        event    = event_factory.create(game_events.game_end_data)
        actual   = self.generator.get_event_string(event)
        expected = "\nThe game is over. Washington wins!\n\nFinal:\nWashington: 4\nBoston: 2\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)


    def test_game_end_overtime(self):
        """
        Description:
            Test the expected output of a game end event.
        """
        self.generator.game_data = game_data.GameData(game_events.game_data_overtime)
        event    = event_factory.create(game_events.game_end_overtime_data)
        actual   = self.generator.get_event_string(event)
        expected = "\nThe game is over. Washington wins!\n\nFinal/OT:\nWashington: 4\nBoston: 3\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)


    def test_game_end_shootout(self):
        """
        Description:
            Test the expected output of a game end event.
        """
        self.generator.game_data = game_data.GameData(game_events.game_data_shootout)
        event    = event_factory.create(game_events.game_end_shootout_data)
        actual   = self.generator.get_event_string(event)
        expected = "\nThe game is over. Washington wins!\n\nFinal/SO:\nWashington: 5\nBoston: 4\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)


    def test_game_official(self):
        """
        Description:
            Test the expected output of a game official event.
        """
        event    = event_factory.create(game_events.game_official_data)
        actual   = self.generator.get_event_string(event)
        expected = None
        self.assertEqual(expected, actual)


    def test_faceoff(self):
        """
        Description:
            Test the expected output of a faceoff event.
        """
        event    = event_factory.create(miscellaneous_events.faceoff_data)
        actual   = self.generator.get_event_string(event)
        expected = None
        self.assertEqual(expected, actual)


    def test_stoppage(self):
        """
        Description:
            Test the expected output of a stoppage event.
        """
        event    = event_factory.create(miscellaneous_events.stoppage_data)
        actual   = self.generator.get_event_string(event)
        expected = None
        self.assertEqual(expected, actual)


    def test_shot(self):
        """
        Description:
            Test the expected output of a shot event.
        """
        event    = event_factory.create(miscellaneous_events.shot_data)
        actual   = self.generator.get_event_string(event)
        expected = None
        self.assertEqual(expected, actual)


    def test_hit(self):
        """
        Description:
            Test the expected output of a hit event.
        """
        event    = event_factory.create(miscellaneous_events.hit_data)
        actual   = self.generator.get_event_string(event)
        expected = None
        self.assertEqual(expected, actual)


    def test_blocked_shot(self):
        """
        Description:
            Test the expected output of a blocked shot event.
        """
        event    = event_factory.create(miscellaneous_events.blocked_shot_data)
        actual   = self.generator.get_event_string(event)
        expected = None
        self.assertEqual(expected, actual)


    def test_giveaway(self):
        """
        Description:
            Test the expected output of a giveaway event.
        """
        event    = event_factory.create(miscellaneous_events.giveaway_data)
        actual   = self.generator.get_event_string(event)
        expected = None
        self.assertEqual(expected, actual)


    def test_takeaway(self):
        """
        Description:
            Test the expected output of a takeaway event.
        """
        event    = event_factory.create(miscellaneous_events.takeaway_data)
        actual   = self.generator.get_event_string(event)
        expected = None
        self.assertEqual(expected, actual)


    def test_missed_shot(self):
        """
        Description:
            Test the expected output of a missed shot event.
        """
        event    = event_factory.create(miscellaneous_events.missed_shot_data)
        actual   = self.generator.get_event_string(event)
        expected = None
        self.assertEqual(expected, actual)


    def test_penalty(self):
        """
        Description:
            Test the expected output of a penalty event.
        """
        event    = event_factory.create(penalty_events.penalty_data)
        actual   = self.generator.get_event_string(event)
        expected = "\nThere is a penalty on Washington.\n\nNic Dowd will serve a 2 minute minor for hi-sticking.\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)


    def test_penalty_no_taker(self):
        """
        Description:
            Test the expected output of a penalty event when no
            penalty taker is present in the event data.
        """
        event    = event_factory.create(penalty_events.penalty_data_no_taker)
        expected = None
        self.assertEqual(expected, event)


    def test_penalty_shot(self):
        """
        Description:
            Test the expected output of a penalty shot event.
        """
        event    = event_factory.create(penalty_events.penalty_shot_data)
        actual   = self.generator.get_event_string(event)
        expected = "\nThat's a penalty shot for Washington!\n\nThe infraction is against Brenden Dillon for hooking on breakaway.\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)


    def test_period_ready(self):
        """
        Description:
            Test the expected output of a period ready event.
        """
        event    = event_factory.create(period_events.period_ready_data)
        actual   = self.generator.get_event_string(event)
        expected = None
        self.assertEqual(expected, actual)


    def test_period_start(self):
        """
        Description:
            Test the expected output of a period start event.
        """
        event    = event_factory.create(period_events.period_start_data)
        actual   = self.generator.get_event_string(event)
        expected = "\nThe second period is starting at Capital One Arena.\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)


    def test_period_end(self):
        """
        Description:
            Test the expected output of a period end event.
        """
        event    = event_factory.create(period_events.period_end_data)
        actual   = self.generator.get_event_string(event)
        expected = "\nThe first period is over at Capital One Arena.\n\nGoals\nWashington: 0\nBoston: 0\n\nShots on Goal\nWashington: 33\nBoston: 30\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)


    def test_period_official(self):
        """
        Description:
            Test the expected output of a period official event.
        """
        event    = event_factory.create(period_events.period_official_data)
        actual   = self.generator.get_event_string(event)
        expected = None
        self.assertEqual(expected, actual)


    def test_goal(self):
        """
        Description:
            Test the expected output of a goal event.
        """
        event    = event_factory.create(goal_events.goal_data)
        actual   = self.generator.get_event_string(event)
        expected = "\nWashington goal!\n\nScored by John Carlson with 15:49 remaining in the 2nd period.\n\nAssisted by Conor Sheary.\n\nWashington: 1\nBoston: 0\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)


    def test_goal_no_scorer(self):
        """
        Description:
            Test the expected output of a goal event when no scorer is present
            in the event data.
        """
        event    = event_factory.create(goal_events.goal_data_no_scorer)
        expected = None
        self.assertEqual(expected, event)


    def test_challenge(self):
        """
        Description:
            Test the expected output of a coach's challenge event.
        """
        event    = event_factory.create(miscellaneous_events.challenge_data)
        actual   = self.generator.get_event_string(event)
        expected = "\nBoston is challenging the ruling on the play.\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)


    def test_goalpost(self):
        """
        Description:
            Test the expected output of a ping event.
        """
        event    = event_factory.create(miscellaneous_events.goalpost_data)
        actual   = self.generator.get_event_string(event)
        expected = "\nPing!\n\nAndrew Cogliano's shot on Jordan Binnington hit the post.\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)


    def test_crossbar(self):
        """
        Description:
            Test the expected output of a ping event.
        """
        event    = event_factory.create(miscellaneous_events.crossbar_data)
        actual   = self.generator.get_event_string(event)
        expected = "\nPing!\n\nNazem Kadri's shot on Jordan Binnington hit the crossbar.\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)


    #################################################
    # Event Replies
    #################################################

    def test_game_scheduled_reply(self):
        """
        Description:
            Test the expected output of a reply to a game scheduled event.
        """
        previous = GameScheduled(miscellaneous_events.null_event)
        event    = event_factory.create(game_events.game_scheduled_data)
        actual   = self.generator.get_reply_string(previous, event)
        expected = None
        self.assertEqual(expected, actual)


    def test_game_end_reply(self):
        """
        Description:
            Test the expected output of a reply to a game end event.
        """
        previous = GameEnd(miscellaneous_events.null_event)
        event    = event_factory.create(game_events.game_end_data)
        actual   = self.generator.get_reply_string(previous, event)
        expected = None
        self.assertEqual(expected, actual)


    def test_game_official_reply(self):
        """
        Description:
            Test the expected output of a reply to a game official event.
        """
        previous = GameOfficial(miscellaneous_events.null_event)
        event    = event_factory.create(game_events.game_official_data)
        actual   = self.generator.get_reply_string(previous, event)
        expected = None
        self.assertEqual(expected, actual)


    def test_faceoff_reply(self):
        """
        Description:
            Test the expected output of a reply to a faceoff event.
        """
        previous = Faceoff(miscellaneous_events.null_event)
        event    = event_factory.create(miscellaneous_events.faceoff_data)
        actual   = self.generator.get_reply_string(previous, event)
        expected = None
        self.assertEqual(expected, actual)


    def test_stoppage_reply(self):
        """
        Description:
            Test the expected output of a reply to a stoppage event.
        """
        previous = Stoppage(miscellaneous_events.null_event)
        event    = event_factory.create(miscellaneous_events.stoppage_data)
        actual   = self.generator.get_reply_string(previous, event)
        expected = None
        self.assertEqual(expected, actual)


    def test_shot_reply(self):
        """
        Description:
            Test the expected output of a reply to a shot event.
        """
        previous = Shot(miscellaneous_events.null_event)
        event    = event_factory.create(miscellaneous_events.shot_data)
        actual   = self.generator.get_reply_string(previous, event)
        expected = None
        self.assertEqual(expected, actual)


    def test_hit_reply(self):
        """
        Description:
            Test the expected output of a reply to a hit event.
        """
        previous = Hit(miscellaneous_events.null_event)
        event    = event_factory.create(miscellaneous_events.hit_data)
        actual   = self.generator.get_reply_string(previous, event)
        expected = None
        self.assertEqual(expected, actual)


    def test_blocked_shot_reply(self):
        """
        Description:
            Test the expected output of a reply to a blocked shot event.
        """
        previous = BlockedShot(miscellaneous_events.null_event)
        event    = event_factory.create(miscellaneous_events.blocked_shot_data)
        actual   = self.generator.get_reply_string(previous, event)
        expected = None
        self.assertEqual(expected, actual)


    def test_giveaway_reply(self):
        """
        Description:
            Test the expected output of a reply to a giveaway event.
        """
        previous = Giveaway(miscellaneous_events.null_event)
        event    = event_factory.create(miscellaneous_events.giveaway_data)
        actual   = self.generator.get_reply_string(previous, event)
        expected = None
        self.assertEqual(expected, actual)


    def test_takeaway_reply(self):
        """
        Description:
            Test the expected output of a reply to a takeaway event.
        """
        previous = Takeaway(miscellaneous_events.null_event)
        event    = event_factory.create(miscellaneous_events.takeaway_data)
        actual   = self.generator.get_reply_string(previous, event)
        expected = None
        self.assertEqual(expected, actual)


    def test_missed_shot_reply(self):
        """
        Description:
            Test the expected output of a reply to a missed shot event.
        """
        previous = MissedShot(miscellaneous_events.null_event)
        event    = event_factory.create(miscellaneous_events.missed_shot_data)
        actual   = self.generator.get_reply_string(previous, event)
        expected = None
        self.assertEqual(expected, actual)


    def test_penalty_reply(self):
        """
        Description:
            Test the expected output of a reply to a penalty event.
        """
        previous = Penalty(miscellaneous_events.null_event)
        event    = event_factory.create(penalty_events.penalty_data)
        actual   = self.generator.get_reply_string(previous, event)
        expected = None
        self.assertEqual(expected, actual)


    def test_penalty_shot_reply(self):
        """
        Description:
            Test the expected output of a reply to a penalty event.
        """
        previous = PenaltyShot(miscellaneous_events.null_event)
        event    = event_factory.create(penalty_events.penalty_shot_data)
        actual   = self.generator.get_reply_string(previous, event)
        expected = None
        self.assertEqual(expected, actual)


    def test_period_ready_reply(self):
        """
        Description:
            Test the expected output of a reply to a period ready event.
        """
        previous = PeriodReady(miscellaneous_events.null_event)
        event    = event_factory.create(period_events.period_ready_data)
        actual   = self.generator.get_reply_string(previous, event)
        expected = None
        self.assertEqual(expected, actual)


    def test_period_start_reply(self):
        """
        Description:
            Test the expected output of a reply to a period start event.
        """
        previous = PeriodStart(miscellaneous_events.null_event)
        event    = event_factory.create(period_events.period_start_data)
        actual   = self.generator.get_reply_string(previous, event)
        expected = None
        self.assertEqual(expected, actual)


    def test_period_end_reply(self):
        """
        Description:
            Test the expected output of a reply to a period end event.
        """
        previous = PeriodEnd(miscellaneous_events.null_event)
        event    = event_factory.create(period_events.period_end_data)
        actual   = self.generator.get_reply_string(previous, event)
        expected = None
        self.assertEqual(expected, actual)


    def test_period_official_reply(self):
        """
        Description:
            Test the expected output of a reply to a period official event.
        """
        previous = PeriodOfficial(miscellaneous_events.null_event)
        event    = event_factory.create(period_events.period_official_data)
        actual   = self.generator.get_reply_string(previous, event)
        expected = None
        self.assertEqual(expected, actual)


    def test_goal_reply_scorer_change(self):
        """
        Description:
            Test the expected output of a reply to a goal event where
            the goal scorer has changed.
        """
        previous = Goal(goal_events.goal_data_scorer_change)
        event    = event_factory.create(goal_events.goal_data)
        actual   = self.generator.get_reply_string(previous, event)
        expected = "\nThe goal is now being awarded to John Carlson.\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)


    def test_goal_reply_primary_assist_change(self):
        """
        Description:
            Test the expected output of a reply to a goal event where
            the primary assist has chnaged.
        """
        previous = Goal(goal_events.goal_data_two_assists)
        event    = event_factory.create(goal_events.goal_data_primary_assist_change)
        actual   = self.generator.get_reply_string(previous, event)
        expected = "\nThe assists have been changed on this goal. The primary assist has been awarded to Alex Ovechkin.\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)


    def test_goal_reply_secondary_assist_change(self):
        """
        Description:
            Test the expected output of a reply to a goal event where
            the secondary assist has changed.
        """
        previous = Goal(goal_events.goal_data_two_assists)
        event    = event_factory.create(goal_events.goal_data_secondary_assist_change)
        actual   = self.generator.get_reply_string(previous, event)
        expected = "\nThe assists have been changed on this goal. The secondary assist has been awarded to Alex Ovechkin.\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)


    def test_goal_reply_time_change(self):
        """
        Description:
            Test the expected output of a reply to a goal event where
            the time of the goal has changed.
        """
        previous = Goal(goal_events.goal_data)
        event    = event_factory.create(goal_events.goal_data_time_change)
        actual   = self.generator.get_reply_string(previous, event)
        expected = "\nThe time of this goal has been changed. The scoresheet now indicates this goal occurred with 15:50 remaining in the 2nd period.\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)


    def test_goal_reply_primary_assist_added(self):
        """
        Description:
            Test the expected output of a reply to a goal event where
            a primary assist has been added.
        """
        previous = Goal(goal_events.goal_data_no_assists)
        event    = event_factory.create(goal_events.goal_data_one_assist)
        actual   = self.generator.get_reply_string(previous, event)
        expected = "\nA primary assist has been awarded to Conor Sheary.\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)


    def test_goal_reply_secondary_assist_added(self):
        """
        Description:
            Test the expected output of a reply to a goal event where
            a secondary assist has been added.
        """
        previous = Goal(goal_events.goal_data_one_assist)
        event    = event_factory.create(goal_events.goal_data_two_assists)
        actual   = self.generator.get_reply_string(previous, event)
        expected = "\nA secondary assist has been awarded to Adam Jones.\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)


    def test_goal_reply_both_assists_added(self):
        """
        Description:
            Test the expected output of a reply to a goal event where
            both a primary and a secondary assist have been added.
        """
        previous = Goal(goal_events.goal_data_no_assists)
        event    = event_factory.create(goal_events.goal_data_two_assists)
        actual   = self.generator.get_reply_string(previous, event)
        expected = "\nAssists have been awarded to Conor Sheary and Adam Jones.\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)


    def test_challenge_reply(self):
        """
        Description:
            Test the expected output of a reply to a coach's challenge event.
        """
        previous = Challenge(miscellaneous_events.null_event)
        event    = event_factory.create(miscellaneous_events.challenge_data)
        actual   = self.generator.get_reply_string(previous, event)
        expected = None
        self.assertEqual(expected, actual)
