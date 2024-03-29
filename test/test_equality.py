"""
This module provides unit tests for determining equality of events and their ID property.
"""

import unittest

from test.test_data import blocked_shot_events
from test.test_data import challenge_events
from test.test_data import faceoff_events
from test.test_data import game_end_events
from test.test_data import game_official_events
from test.test_data import game_scheduled_events
from test.test_data import giveaway_events
from test.test_data import goal_events
from test.test_data import hit_events
from test.test_data import missed_shot_events
from test.test_data import penalty_events
from test.test_data import penalty_shot_events
from test.test_data import period_end_events
from test.test_data import period_official_events
from test.test_data import period_ready_events
from test.test_data import period_start_events
from test.test_data import ping_events
from test.test_data import shot_events
from test.test_data import stoppage_events
from test.test_data import takeaway_events

from src.events.blocked_shot import BlockedShot
from src.events.challenge import Challenge
from src.events.event import Event
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
from src.events.ping import Ping
from src.events.shot import Shot
from src.events.stoppage import Stoppage
from src.events.takeaway import Takeaway

class TestEquality(unittest.TestCase):
    """
    This class provides unit tests for determining equality of events and their ID property.
    """

    def test_blocked_shot_equality(self):
        """
        Test the equality operator for a BlockedShot event.
        """
        parent = Event(blocked_shot_events.blocked_shot_1)
        child1 = BlockedShot(blocked_shot_events.blocked_shot_1)
        child2 = BlockedShot(blocked_shot_events.blocked_shot_2)
        child3 = BlockedShot(blocked_shot_events.blocked_shot_3)
        child4 = BlockedShot(blocked_shot_events.blocked_shot_1)
        other  = Shot(shot_events.shot_1)

        # Test Case 1 - parent to child
        self.assertNotEqual(parent, child1)
        self.assertNotEqual(parent, child2)
        self.assertNotEqual(parent, child3)
        self.assertNotEqual(parent, child4)

        # Test Case 2 - Unlike instances
        self.assertNotEqual(child1, child2)
        self.assertNotEqual(child1, child3)
        self.assertNotEqual(child2, child3)
        self.assertNotEqual(child2, child4)
        self.assertNotEqual(child3, child4)

        # Test Case 3 - Like instances
        self.assertEqual(child1, child4)
        self.assertEqual(child4, child1)

        # Test Case 4 - Unlike classes
        self.assertNotEqual(child1, other)
        self.assertNotEqual(child2, other)
        self.assertNotEqual(child3, other)
        self.assertNotEqual(child4, other)

        # Test Case 5 - different eventid
        diff = BlockedShot(blocked_shot_events.blocked_shot_different_event_id)
        self.assertEqual(child1, diff)

        # Test Case 6 - different eventidx
        diff = BlockedShot(blocked_shot_events.blocked_shot_different_event_id_x)
        self.assertEqual(child1, diff)

        # Test Case 7 - different datetime
        diff = BlockedShot(blocked_shot_events.blocked_shot_different_datetime)
        self.assertEqual(child1, diff)

        # Test Case 8 - different period
        diff = BlockedShot(blocked_shot_events.blocked_shot_different_period)
        self.assertNotEqual(child1, diff)

        # Test Case 9 - different period time
        diff = BlockedShot(blocked_shot_events.blocked_shot_different_period_time)
        self.assertEqual(child1, diff)

        # Test Case 10 - different period time remaining
        diff = BlockedShot(blocked_shot_events.blocked_shot_different_period_time_remaining)
        self.assertNotEqual(child1, diff)

        # Test Case 11 - different shooter
        diff = BlockedShot(blocked_shot_events.blocked_shot_different_shooter)
        self.assertNotEqual(child1, diff)

        # Test Case 12 - different blocker
        diff = BlockedShot(blocked_shot_events.blocked_shot_different_blocker)
        self.assertNotEqual(child1, diff)


    def test_blocked_shot_id(self):
        """
        Test the ID property for a BlockedShot event.
        """
        parent = Event(blocked_shot_events.blocked_shot_1)
        child1 = BlockedShot(blocked_shot_events.blocked_shot_1)
        child2 = BlockedShot(blocked_shot_events.blocked_shot_2)
        child3 = BlockedShot(blocked_shot_events.blocked_shot_3)
        child4 = BlockedShot(blocked_shot_events.blocked_shot_1)
        other  = Shot(shot_events.shot_1)

        # Test Case 1 - parent to child
        self.assertNotEqual(parent.id, child1.id)
        self.assertNotEqual(parent.id, child2.id)
        self.assertNotEqual(parent.id, child3.id)
        self.assertNotEqual(parent.id, child4.id)

        # Test Case 2 - Unlike instances
        self.assertNotEqual(child1.id, child2.id)
        self.assertNotEqual(child1.id, child3.id)
        self.assertNotEqual(child2.id, child3.id)
        self.assertNotEqual(child2.id, child4.id)
        self.assertNotEqual(child3.id, child4.id)

        # Test Case 3 - Like instances
        self.assertEqual(child1.id, child4.id)
        self.assertEqual(child4.id, child1.id)

        # Test Case 4 - Unlike classes
        self.assertNotEqual(child1.id, other.id)
        self.assertNotEqual(child2.id, other.id)
        self.assertNotEqual(child3.id, other.id)
        self.assertNotEqual(child4.id, other.id)

        # Test Case 5 - different eventid
        diff = BlockedShot(blocked_shot_events.blocked_shot_different_event_id)
        self.assertEqual(child1.id, diff.id)

        # Test Case 6 - different eventidx
        diff = BlockedShot(blocked_shot_events.blocked_shot_different_event_id_x)
        self.assertEqual(child1.id, diff.id)

        # Test Case 7 - different datetime
        diff = BlockedShot(blocked_shot_events.blocked_shot_different_datetime)
        self.assertEqual(child1.id, diff.id)

        # Test Case 8 - different period
        diff = BlockedShot(blocked_shot_events.blocked_shot_different_period)
        self.assertNotEqual(child1.id, diff.id)

        # Test Case 9 - different period time
        diff = BlockedShot(blocked_shot_events.blocked_shot_different_period_time)
        self.assertEqual(child1.id, diff.id)

        # Test Case 10 - different period time remaining
        diff = BlockedShot(blocked_shot_events.blocked_shot_different_period_time_remaining)
        self.assertNotEqual(child1.id, diff.id)

        # Test Case 11 - different shooter
        diff = BlockedShot(blocked_shot_events.blocked_shot_different_shooter)
        self.assertNotEqual(child1.id, diff.id)

        # Test Case 12 - different blocker
        diff = BlockedShot(blocked_shot_events.blocked_shot_different_blocker)
        self.assertNotEqual(child1.id, diff.id)


    def test_challenge_equality(self):
        """
        Test the equality operator for a Challenge event.
        """
        parent = Event(challenge_events.challenge_1)
        child1 = Challenge(challenge_events.challenge_1)
        child2 = Challenge(challenge_events.challenge_2)
        child3 = Challenge(challenge_events.challenge_1)
        other  = Shot(shot_events.shot_1)

        # Test Case 1 - parent to child
        self.assertNotEqual(parent, child1)
        self.assertNotEqual(parent, child2)

        # Test Case 2 - Unlike instances
        self.assertNotEqual(child1, child2)

        # Test Case 3 - Like instances
        self.assertEqual(child1, child3)
        self.assertEqual(child3, child1)

        # Test Case 4 - Unlike classes
        self.assertNotEqual(child1, other)
        self.assertNotEqual(child2, other)
        self.assertNotEqual(child3, other)

        # Test Case 5 - different eventid
        diff = Challenge(challenge_events.challenge_different_event_id)
        self.assertEqual(child1, diff)

        # Test Case 6 - different eventidx
        diff = Challenge(challenge_events.challenge_different_event_id_x)
        self.assertEqual(child1, diff)

        # Test Case 7 - different datetime
        diff = Challenge(challenge_events.challenge_different_datetime)
        self.assertEqual(child1, diff)

        # Test Case 8 - different period
        diff = Challenge(challenge_events.challenge_different_period)
        self.assertNotEqual(child1, diff)

        # Test Case 9 - different period time
        diff = Challenge(challenge_events.challenge_different_period_time)
        self.assertEqual(child1, diff)

        # Test Case 10 - different period time remaining
        diff = Challenge(challenge_events.challenge_different_period_time_remaining)
        self.assertNotEqual(child1, diff)


    def test_challenge_id(self):
        """
        Test the ID property for a Challenge event.
        """
        parent = Event(challenge_events.challenge_1)
        child1 = Challenge(challenge_events.challenge_1)
        child2 = Challenge(challenge_events.challenge_2)
        child3 = Challenge(challenge_events.challenge_1)
        other  = Shot(shot_events.shot_1)

        # Test Case 1 - parent to child
        self.assertNotEqual(parent.id, child1.id)
        self.assertNotEqual(parent.id, child2.id)

        # Test Case 2 - Unlike instances
        self.assertNotEqual(child1.id, child2.id)

        # Test Case 3 - Like instances
        self.assertEqual(child1.id, child3.id)
        self.assertEqual(child3.id, child1.id)

        # Test Case 4 - Unlike classes
        self.assertNotEqual(child1.id, other.id)
        self.assertNotEqual(child2.id, other.id)
        self.assertNotEqual(child3.id, other.id)

        # Test Case 5 - different eventid
        diff = Challenge(challenge_events.challenge_different_event_id)
        self.assertEqual(child1.id, diff.id)

        # Test Case 6 - different eventidx
        diff = Challenge(challenge_events.challenge_different_event_id_x)
        self.assertEqual(child1.id, diff.id)

        # Test Case 7 - different datetime
        diff = Challenge(challenge_events.challenge_different_datetime)
        self.assertEqual(child1.id, diff.id)

        # Test Case 8 - different period
        diff = Challenge(challenge_events.challenge_different_period)
        self.assertNotEqual(child1.id, diff.id)

        # Test Case 9 - different period time
        diff = Challenge(challenge_events.challenge_different_period_time)
        self.assertEqual(child1.id, diff.id)

        # Test Case 10 - different period time remaining
        diff = Challenge(challenge_events.challenge_different_period_time_remaining)
        self.assertNotEqual(child1.id, diff.id)


    def test_faceoff_equality(self):
        """
        Test the equality operator for a Faceoff event.
        """
        parent = Event(faceoff_events.faceoff_1)
        child1 = Faceoff(faceoff_events.faceoff_1)
        child2 = Faceoff(faceoff_events.faceoff_2)
        child3 = Faceoff(faceoff_events.faceoff_3)
        child4 = Faceoff(faceoff_events.faceoff_1)
        other  = Shot(shot_events.shot_1)

        # Test Case 1 - parent to child
        self.assertNotEqual(parent, child1)
        self.assertNotEqual(parent, child2)
        self.assertNotEqual(parent, child3)
        self.assertNotEqual(parent, child4)

        # Test Case 2 - Unlike instances
        self.assertNotEqual(child1, child2)
        self.assertNotEqual(child1, child3)
        self.assertNotEqual(child2, child3)
        self.assertNotEqual(child2, child4)
        self.assertNotEqual(child3, child4)

        # Test Case 3 - Like instances
        self.assertEqual(child1, child4)
        self.assertEqual(child4, child1)

        # Test Case 4 - Unlike classes
        self.assertNotEqual(child1, other)
        self.assertNotEqual(child2, other)
        self.assertNotEqual(child3, other)
        self.assertNotEqual(child4, other)

        # Test Case 5 - different eventid
        diff = Faceoff(faceoff_events.faceoff_different_event_id)
        self.assertEqual(child1, diff)

        # Test Case 6 - different eventidx
        diff = Faceoff(faceoff_events.faceoff_different_event_id_x)
        self.assertEqual(child1, diff)

        # Test Case 7 - different datetime
        diff = Faceoff(faceoff_events.faceoff_different_datetime)
        self.assertEqual(child1, diff)

        # Test Case 8 - different period
        diff = Faceoff(faceoff_events.faceoff_different_period)
        self.assertNotEqual(child1, diff)

        # Test Case 9 - different period time
        diff = Faceoff(faceoff_events.faceoff_different_period_time)
        self.assertEqual(child1, diff)

        # Test Case 10 - different period time remaining
        diff = Faceoff(faceoff_events.faceoff_different_period_time_remaining)
        self.assertNotEqual(child1, diff)

        # Test Case 11 - different winner
        diff = Faceoff(faceoff_events.faceoff_different_winner)
        self.assertNotEqual(child1, diff)

        # Test Case 12 - different loser
        diff = Faceoff(faceoff_events.faceoff_different_loser)
        self.assertNotEqual(child1, diff)


    def test_faceoff_id(self):
        """
        Test the ID property for a Faceoff event.
        """
        parent = Event(faceoff_events.faceoff_1)
        child1 = Faceoff(faceoff_events.faceoff_1)
        child2 = Faceoff(faceoff_events.faceoff_2)
        child3 = Faceoff(faceoff_events.faceoff_3)
        child4 = Faceoff(faceoff_events.faceoff_1)
        other  = Shot(shot_events.shot_1)

        # Test Case 1 - parent to child
        self.assertNotEqual(parent.id, child1.id)
        self.assertNotEqual(parent.id, child2.id)
        self.assertNotEqual(parent.id, child3.id)
        self.assertNotEqual(parent.id, child4.id)

        # Test Case 2 - Unlike instances
        self.assertNotEqual(child1.id, child2.id)
        self.assertNotEqual(child1.id, child3.id)
        self.assertNotEqual(child2.id, child3.id)
        self.assertNotEqual(child2.id, child4.id)
        self.assertNotEqual(child3.id, child4.id)

        # Test Case 3 - Like instances
        self.assertEqual(child1.id, child4.id)
        self.assertEqual(child4.id, child1.id)

        # Test Case 4 - Unlike classes
        self.assertNotEqual(child1.id, other.id)
        self.assertNotEqual(child2.id, other.id)
        self.assertNotEqual(child3.id, other.id)
        self.assertNotEqual(child4.id, other.id)

        # Test Case 5 - different eventid
        diff = Faceoff(faceoff_events.faceoff_different_event_id)
        self.assertEqual(child1.id, diff.id)

        # Test Case 6 - different eventidx
        diff = Faceoff(faceoff_events.faceoff_different_event_id_x)
        self.assertEqual(child1.id, diff.id)

        # Test Case 7 - different datetime
        diff = Faceoff(faceoff_events.faceoff_different_datetime)
        self.assertEqual(child1.id, diff.id)

        # Test Case 8 - different period
        diff = Faceoff(faceoff_events.faceoff_different_period)
        self.assertNotEqual(child1.id, diff.id)

        # Test Case 9 - different period time
        diff = Faceoff(faceoff_events.faceoff_different_period_time)
        self.assertEqual(child1.id, diff.id)

        # Test Case 10 - different period time remaining
        diff = Faceoff(faceoff_events.faceoff_different_period_time_remaining)
        self.assertNotEqual(child1.id, diff.id)

        # Test Case 11 - different winner
        diff = Faceoff(faceoff_events.faceoff_different_winner)
        self.assertNotEqual(child1.id, diff.id)

        # Test Case 12 - different loser
        diff = Faceoff(faceoff_events.faceoff_different_loser)
        self.assertNotEqual(child1.id, diff.id)


    def test_game_end_equality(self):
        """
        Test the equality operator for a GameEnd event.
        """
        parent = Event(faceoff_events.faceoff_1)
        child1 = GameEnd(game_end_events.game_end_1)
        child2 = GameEnd(game_end_events.game_end_2)
        child3 = GameEnd(game_end_events.game_end_1)
        other  = Shot(shot_events.shot_1)

        # Test Case 1 - parent to child
        self.assertNotEqual(parent, child1)
        self.assertNotEqual(parent, child2)
        self.assertNotEqual(parent, child3)

        # Test Case 2 - Unlike instances
        self.assertEqual(child1, child2)
        self.assertEqual(child2, child3)

        # Test Case 3 - Like instances
        self.assertEqual(child1, child3)
        self.assertEqual(child3, child1)

        # Test Case 4 - Unlike classes
        self.assertNotEqual(child1, other)
        self.assertNotEqual(child2, other)
        self.assertNotEqual(child3, other)

        # Test Case 5 - different eventid
        diff = GameEnd(game_end_events.game_end_different_event_id)
        self.assertEqual(child1, diff)

        # Test Case 6 - different eventidx
        diff = GameEnd(game_end_events.game_end_different_event_id_x)
        self.assertEqual(child1, diff)

        # Test Case 7 - different datetime
        diff = GameEnd(game_end_events.game_end_different_datetime)
        self.assertEqual(child1, diff)

        # Test Case 8 - different period
        diff = GameEnd(game_end_events.game_end_different_period)
        self.assertEqual(child1, diff)

        # Test Case 9 - different period time
        diff = GameEnd(game_end_events.game_end_different_period_time)
        self.assertEqual(child1, diff)

        # Test Case 10 - different period time remaining
        diff = GameEnd(game_end_events.game_end_different_period_time_remaining)
        self.assertEqual(child1, diff)


    def test_game_end_id(self):
        """
        Test the ID property for a GameEnd event.
        """

        parent = Event(faceoff_events.faceoff_1)
        child1 = GameEnd(game_end_events.game_end_1)
        child2 = GameEnd(game_end_events.game_end_2)
        child3 = GameEnd(game_end_events.game_end_1)
        other  = Shot(shot_events.shot_1)

        # Test Case 1 - parent to child
        self.assertNotEqual(parent.id, child1.id)
        self.assertNotEqual(parent.id, child2.id)
        self.assertNotEqual(parent.id, child3.id)

        # Test Case 2 - Unlike instances
        self.assertEqual(child1.id, child2.id)
        self.assertEqual(child2.id, child3.id)

        # Test Case 3 - Like instances
        self.assertEqual(child1.id, child3.id)
        self.assertEqual(child3.id, child1.id)

        # Test Case 4 - Unlike classes
        self.assertNotEqual(child1.id, other.id)
        self.assertNotEqual(child2.id, other.id)
        self.assertNotEqual(child3.id, other.id)

        # Test Case 5 - different eventid
        diff = GameEnd(game_end_events.game_end_different_event_id)
        self.assertEqual(child1.id, diff.id)

        # Test Case 6 - different eventidx
        diff = GameEnd(game_end_events.game_end_different_event_id_x)
        self.assertEqual(child1.id, diff.id)

        # Test Case 7 - different datetime
        diff = GameEnd(game_end_events.game_end_different_datetime)
        self.assertEqual(child1.id, diff.id)

        # Test Case 8 - different period
        diff = GameEnd(game_end_events.game_end_different_period)
        self.assertEqual(child1.id, diff.id)

        # Test Case 9 - different period time
        diff = GameEnd(game_end_events.game_end_different_period_time)
        self.assertEqual(child1.id, diff.id)

        # Test Case 10 - different period time remaining
        diff = GameEnd(game_end_events.game_end_different_period_time_remaining)
        self.assertEqual(child1.id, diff.id)


    def test_game_official_equality(self):
        """
        Test the equality operator for a GameOfficial event.
        """
        parent = Event(faceoff_events.faceoff_1)
        child1 = GameOfficial(game_official_events.game_official_1)
        child2 = GameOfficial(game_official_events.game_official_2)
        child3 = GameOfficial(game_official_events.game_official_1)
        other  = Shot(shot_events.shot_1)

        # Test Case 1 - parent to child
        self.assertNotEqual(parent, child1)
        self.assertNotEqual(parent, child2)
        self.assertNotEqual(parent, child3)

        # Test Case 2 - Unlike instances
        self.assertEqual(child1, child2)
        self.assertEqual(child2, child3)

        # Test Case 3 - Like instances
        self.assertEqual(child1, child3)
        self.assertEqual(child3, child1)

        # Test Case 4 - Unlike classes
        self.assertNotEqual(child1, other)
        self.assertNotEqual(child2, other)
        self.assertNotEqual(child3, other)

        # Test Case 5 - different eventid
        diff = GameOfficial(game_official_events.game_official_different_event_id)
        self.assertEqual(child1, diff)

        # Test Case 6 - different eventidx
        diff = GameOfficial(game_official_events.game_official_different_event_id_x)
        self.assertEqual(child1, diff)

        # Test Case 7 - different datetime
        diff = GameOfficial(game_official_events.game_official_different_datetime)
        self.assertEqual(child1, diff)

        # Test Case 8 - different period
        diff = GameOfficial(game_official_events.game_official_different_period)
        self.assertEqual(child1, diff)

        # Test Case 9 - different period time
        diff = GameOfficial(game_official_events.game_official_different_period_time)
        self.assertEqual(child1, diff)

        # Test Case 10 - different period time remaining
        diff = GameOfficial(game_official_events.game_official_different_period_time_remaining)
        self.assertEqual(child1, diff)


    def test_game_official_id(self):
        """
        Test the ID property for a GameOfficial event.
        """

        parent = Event(faceoff_events.faceoff_1)
        child1 = GameOfficial(game_official_events.game_official_1)
        child2 = GameOfficial(game_official_events.game_official_2)
        child3 = GameOfficial(game_official_events.game_official_1)
        other  = Shot(shot_events.shot_1)

        # Test Case 1 - parent to child
        self.assertNotEqual(parent.id, child1.id)
        self.assertNotEqual(parent.id, child2.id)
        self.assertNotEqual(parent.id, child3.id)

        # Test Case 2 - Unlike instances
        self.assertEqual(child1.id, child2.id)
        self.assertEqual(child2.id, child3.id)

        # Test Case 3 - Like instances
        self.assertEqual(child1.id, child3.id)
        self.assertEqual(child3.id, child1.id)

        # Test Case 4 - Unlike classes
        self.assertNotEqual(child1.id, other.id)
        self.assertNotEqual(child2.id, other.id)
        self.assertNotEqual(child3.id, other.id)

        # Test Case 5 - different eventid
        diff = GameOfficial(game_official_events.game_official_different_event_id)
        self.assertEqual(child1.id, diff.id)

        # Test Case 6 - different eventidx
        diff = GameOfficial(game_official_events.game_official_different_event_id_x)
        self.assertEqual(child1.id, diff.id)

        # Test Case 7 - different datetime
        diff = GameOfficial(game_official_events.game_official_different_datetime)
        self.assertEqual(child1.id, diff.id)

        # Test Case 8 - different period
        diff = GameOfficial(game_official_events.game_official_different_period)
        self.assertEqual(child1.id, diff.id)

        # Test Case 9 - different period time
        diff = GameOfficial(game_official_events.game_official_different_period_time)
        self.assertEqual(child1.id, diff.id)

        # Test Case 10 - different period time remaining
        diff = GameOfficial(game_official_events.game_official_different_period_time_remaining)
        self.assertEqual(child1.id, diff.id)


    def test_game_scheduled_equality(self):
        """
        Test the equality operator for a GameScheduled event.
        """
        parent = Event(faceoff_events.faceoff_1)
        child1 = GameScheduled(game_scheduled_events.game_scheduled_1)
        child2 = GameScheduled(game_scheduled_events.game_scheduled_2)
        child3 = GameScheduled(game_scheduled_events.game_scheduled_1)
        other  = Shot(shot_events.shot_1)

        # Test Case 1 - parent to child
        self.assertNotEqual(parent, child1)
        self.assertNotEqual(parent, child2)
        self.assertNotEqual(parent, child3)

        # Test Case 2 - Unlike instances
        self.assertEqual(child1, child2)
        self.assertEqual(child2, child3)

        # Test Case 3 - Like instances
        self.assertEqual(child1, child3)
        self.assertEqual(child3, child1)

        # Test Case 4 - Unlike classes
        self.assertNotEqual(child1, other)
        self.assertNotEqual(child2, other)
        self.assertNotEqual(child3, other)

        # Test Case 5 - different eventid
        diff = GameScheduled(game_scheduled_events.game_scheduled_different_event_id)
        self.assertEqual(child1, diff)

        # Test Case 6 - different eventidx
        diff = GameScheduled(game_scheduled_events.game_scheduled_different_event_id_x)
        self.assertEqual(child1, diff)

        # Test Case 7 - different datetime
        diff = GameScheduled(game_scheduled_events.game_scheduled_different_datetime)
        self.assertEqual(child1, diff)

        # Test Case 8 - different period
        diff = GameScheduled(game_scheduled_events.game_scheduled_different_period)
        self.assertEqual(child1, diff)

        # Test Case 9 - different period time
        diff = GameScheduled(game_scheduled_events.game_scheduled_different_period_time)
        self.assertEqual(child1, diff)

        # Test Case 10 - different period time remaining
        diff = GameScheduled(game_scheduled_events.game_scheduled_different_period_time_remaining)
        self.assertEqual(child1, diff)


    def test_game_scheduled_id(self):
        """
        Test the ID property for a GameOfficial event.
        """

        parent = Event(faceoff_events.faceoff_1)
        child1 = GameScheduled(game_scheduled_events.game_scheduled_1)
        child2 = GameScheduled(game_scheduled_events.game_scheduled_2)
        child3 = GameScheduled(game_scheduled_events.game_scheduled_1)
        other  = Shot(shot_events.shot_1)

        # Test Case 1 - parent to child
        self.assertNotEqual(parent.id, child1.id)
        self.assertNotEqual(parent.id, child2.id)
        self.assertNotEqual(parent.id, child3.id)

        # Test Case 2 - Unlike instances
        self.assertEqual(child1.id, child2.id)
        self.assertEqual(child2.id, child3.id)

        # Test Case 3 - Like instances
        self.assertEqual(child1.id, child3.id)
        self.assertEqual(child3.id, child1.id)

        # Test Case 4 - Unlike classes
        self.assertNotEqual(child1.id, other.id)
        self.assertNotEqual(child2.id, other.id)
        self.assertNotEqual(child3.id, other.id)

        # Test Case 5 - different eventid
        diff = GameScheduled(game_scheduled_events.game_scheduled_different_event_id)
        self.assertEqual(child1.id, diff.id)

        # Test Case 6 - different eventidx
        diff = GameScheduled(game_scheduled_events.game_scheduled_different_event_id_x)
        self.assertEqual(child1.id, diff.id)

        # Test Case 7 - different datetime
        diff = GameScheduled(game_scheduled_events.game_scheduled_different_datetime)
        self.assertEqual(child1.id, diff.id)

        # Test Case 8 - different period
        diff = GameScheduled(game_scheduled_events.game_scheduled_different_period)
        self.assertEqual(child1.id, diff.id)

        # Test Case 9 - different period time
        diff = GameScheduled(game_scheduled_events.game_scheduled_different_period_time)
        self.assertEqual(child1.id, diff.id)

        # Test Case 10 - different period time remaining
        diff = GameScheduled(game_scheduled_events.game_scheduled_different_period_time_remaining)
        self.assertEqual(child1.id, diff.id)


    def test_giveaway_equality(self):
        """
        Test the equality operator for a Giveaway event.
        """
        parent = Event(giveaway_events.giveaway_1)
        child1 = Giveaway(giveaway_events.giveaway_1)
        child2 = Giveaway(giveaway_events.giveaway_2)
        child3 = Giveaway(giveaway_events.giveaway_3)
        child4 = Giveaway(giveaway_events.giveaway_1)
        other  = Shot(shot_events.shot_1)

        # Test Case 1 - parent to child
        self.assertNotEqual(parent, child1)
        self.assertNotEqual(parent, child2)
        self.assertNotEqual(parent, child3)
        self.assertNotEqual(parent, child4)

        # Test Case 2 - Unlike instances
        self.assertNotEqual(child1, child2)
        self.assertNotEqual(child1, child3)
        self.assertNotEqual(child2, child3)
        self.assertNotEqual(child2, child4)
        self.assertNotEqual(child3, child4)

        # Test Case 3 - Like instances
        self.assertEqual(child1, child4)
        self.assertEqual(child4, child1)

        # Test Case 4 - Unlike classes
        self.assertNotEqual(child1, other)
        self.assertNotEqual(child2, other)
        self.assertNotEqual(child3, other)
        self.assertNotEqual(child4, other)

        # Test Case 5 - different eventid
        diff = Giveaway(giveaway_events.giveaway_different_event_id)
        self.assertEqual(child1, diff)

        # Test Case 6 - different eventidx
        diff = Giveaway(giveaway_events.giveaway_different_event_id_x)
        self.assertEqual(child1, diff)

        # Test Case 7 - different datetime
        diff = Giveaway(giveaway_events.giveaway_different_datetime)
        self.assertEqual(child1, diff)

        # Test Case 8 - different period
        diff = Giveaway(giveaway_events.giveaway_different_period)
        self.assertNotEqual(child1, diff)

        # Test Case 9 - different period time
        diff = Giveaway(giveaway_events.giveaway_different_period_time)
        self.assertEqual(child1, diff)

        # Test Case 10 - different period time remaining
        diff = Giveaway(giveaway_events.giveaway_different_period_time_remaining)
        self.assertNotEqual(child1, diff)

        # Test Case 11 - different player
        diff = Giveaway(giveaway_events.giveaway_different_player)
        self.assertNotEqual(child1, diff)


    def test_giveaway_id(self):
        """
        Test the ID property for a Giveaway event.
        """
        parent = Event(giveaway_events.giveaway_1)
        child1 = Giveaway(giveaway_events.giveaway_1)
        child2 = Giveaway(giveaway_events.giveaway_2)
        child3 = Giveaway(giveaway_events.giveaway_3)
        child4 = Giveaway(giveaway_events.giveaway_1)
        other  = Shot(shot_events.shot_1)

        # Test Case 1 - parent to child
        self.assertNotEqual(parent.id, child1.id)
        self.assertNotEqual(parent.id, child2.id)
        self.assertNotEqual(parent.id, child3.id)
        self.assertNotEqual(parent.id, child4.id)

        # Test Case 2 - Unlike instances
        self.assertNotEqual(child1.id, child2.id)
        self.assertNotEqual(child1.id, child3.id)
        self.assertNotEqual(child2.id, child3.id)
        self.assertNotEqual(child2.id, child4.id)
        self.assertNotEqual(child3.id, child4.id)

        # Test Case 3 - Like instances
        self.assertEqual(child1.id, child4.id)
        self.assertEqual(child4.id, child1.id)

        # Test Case 4 - Unlike classes
        self.assertNotEqual(child1.id, other.id)
        self.assertNotEqual(child2.id, other.id)
        self.assertNotEqual(child3.id, other.id)
        self.assertNotEqual(child4.id, other.id)

        # Test Case 5 - different eventid
        diff = Giveaway(giveaway_events.giveaway_different_event_id)
        self.assertEqual(child1.id, diff.id)

        # Test Case 6 - different eventidx
        diff = Giveaway(giveaway_events.giveaway_different_event_id_x)
        self.assertEqual(child1.id, diff.id)

        # Test Case 7 - different datetime
        diff = Giveaway(giveaway_events.giveaway_different_datetime)
        self.assertEqual(child1.id, diff.id)

        # Test Case 8 - different period
        diff = Giveaway(giveaway_events.giveaway_different_period)
        self.assertNotEqual(child1.id, diff.id)

        # Test Case 9 - different period time
        diff = Giveaway(giveaway_events.giveaway_different_period_time)
        self.assertEqual(child1.id, diff.id)

        # Test Case 10 - different period time remaining
        diff = Giveaway(giveaway_events.giveaway_different_period_time_remaining)
        self.assertNotEqual(child1.id, diff.id)

        # Test Case 11 - different player
        diff = Giveaway(giveaway_events.giveaway_different_player)
        self.assertNotEqual(child1.id, diff.id)


    def test_goal_equality(self):
        """
        Test the equality operator for a Goal event.
        """
        parent = Event(giveaway_events.giveaway_1)
        child1 = Goal(goal_events.goal_1)
        child2 = Goal(goal_events.goal_2)
        child3 = Goal(goal_events.goal_3)
        child4 = Goal(goal_events.goal_1)
        other  = Shot(shot_events.shot_1)

        # Test Case 1 - parent to child
        self.assertNotEqual(parent, child1)
        self.assertNotEqual(parent, child2)
        self.assertNotEqual(parent, child3)
        self.assertNotEqual(parent, child4)

        # Test Case 2 - Unlike instances
        self.assertNotEqual(child1, child2)
        self.assertNotEqual(child1, child3)
        self.assertNotEqual(child2, child3)
        self.assertNotEqual(child2, child4)
        self.assertNotEqual(child3, child4)

        # Test Case 3 - Like instances
        self.assertEqual(child1, child4)
        self.assertEqual(child4, child1)

        # Test Case 4 - Unlike classes
        self.assertNotEqual(child1, other)
        self.assertNotEqual(child2, other)
        self.assertNotEqual(child3, other)
        self.assertNotEqual(child4, other)

        # Test Case 5 - different eventid
        diff = Goal(goal_events.goal_different_event_id)
        self.assertEqual(child1, diff)

        # Test Case 6 - different eventidx
        diff = Goal(goal_events.goal_different_event_id_x)
        self.assertEqual(child1, diff)

        # Test Case 7 - different datetime
        diff = Goal(goal_events.goal_different_datetime)
        self.assertEqual(child1, diff)

        # Test Case 8 - different period
        diff = Goal(goal_events.goal_different_period)
        self.assertNotEqual(child1, diff)

        # Test Case 9 - different period time
        diff = Goal(goal_events.goal_different_period_time)
        self.assertEqual(child1, diff)

        # Test Case 10 - different period time remaining
        diff = Goal(goal_events.goal_different_period_time_remaining)
        self.assertNotEqual(child1, diff)

        # Test Case 11 - different scorer
        diff = Goal(goal_events.goal_different_scorer)
        self.assertNotEqual(child1, diff)

        # Test Case 12 - different primary assist
        diff = Goal(goal_events.goal_different_primary_assist)
        self.assertNotEqual(child1, diff)

        # Test Case 13 - different secondary assist
        diff = Goal(goal_events.goal_different_secondary_assist)
        self.assertNotEqual(child1, diff)

        # Test Case 14 - different goalie
        diff = Goal(goal_events.goal_different_goalie)
        self.assertNotEqual(child1, diff)

        # Test Case 15 - different strength
        diff = Goal(goal_events.goal_different_strength)
        self.assertNotEqual(child1, diff)

        # Test Case 16 - different empty net
        diff = Goal(goal_events.goal_different_empty_net)
        self.assertNotEqual(child1, diff)

        # Test Case 17 - different team
        diff = Goal(goal_events.goal_different_team)
        self.assertNotEqual(child1, diff)


    def test_goal_id(self):
        """
        Test the ID property for a Goal event.
        """
        parent = Event(giveaway_events.giveaway_1)
        child1 = Goal(goal_events.goal_1)
        child2 = Goal(goal_events.goal_2)
        child3 = Goal(goal_events.goal_3)
        child4 = Goal(goal_events.goal_1)
        other  = Shot(shot_events.shot_1)

        # Test Case 1 - parent to child
        self.assertNotEqual(parent.id, child1.id)
        self.assertNotEqual(parent.id, child2.id)
        self.assertNotEqual(parent.id, child3.id)
        self.assertNotEqual(parent.id, child4.id)

        # Test Case 2 - Unlike instances
        self.assertNotEqual(child1.id, child2.id)
        self.assertNotEqual(child1.id, child3.id)
        self.assertNotEqual(child2.id, child3.id)
        self.assertNotEqual(child2.id, child4.id)
        self.assertNotEqual(child3.id, child4.id)

        # Test Case 3 - Like instances
        self.assertEqual(child1.id, child4.id)
        self.assertEqual(child4.id, child1.id)

        # Test Case 4 - Unlike classes
        self.assertNotEqual(child1.id, other.id)
        self.assertNotEqual(child2.id, other.id)
        self.assertNotEqual(child3.id, other.id)
        self.assertNotEqual(child4.id, other.id)

        # Test Case 5 - different eventid
        diff = Goal(goal_events.goal_different_event_id)
        self.assertEqual(child1.id, diff.id)

        # Test Case 6 - different eventidx
        diff = Goal(goal_events.goal_different_event_id_x)
        self.assertEqual(child1.id, diff.id)

        # Test Case 7 - different datetime
        diff = Goal(goal_events.goal_different_datetime)
        self.assertEqual(child1.id, diff.id)

        # Test Case 8 - different period
        diff = Goal(goal_events.goal_different_period)
        self.assertNotEqual(child1.id, diff.id)

        # Test Case 9 - different period time
        diff = Goal(goal_events.goal_different_period_time)
        self.assertEqual(child1.id, diff.id)

        # Test Case 10 - different period time remaining
        diff = Goal(goal_events.goal_different_period_time_remaining)
        self.assertNotEqual(child1.id, diff.id)

        # Test Case 11 - different scorer
        diff = Goal(goal_events.goal_different_scorer)
        self.assertEqual(child1.id, diff.id)

        # Test Case 12 - different primary assist
        diff = Goal(goal_events.goal_different_primary_assist)
        self.assertEqual(child1.id, diff.id)

        # Test Case 13 - different secondary assist
        diff = Goal(goal_events.goal_different_secondary_assist)
        self.assertEqual(child1.id, diff.id)

        # Test Case 14 - different goalie
        diff = Goal(goal_events.goal_different_goalie)
        self.assertEqual(child1.id, diff.id)

        # Test Case 15 - different strength
        diff = Goal(goal_events.goal_different_strength)
        self.assertEqual(child1.id, diff.id)

        # Test Case 16 - different empty net
        diff = Goal(goal_events.goal_different_empty_net)
        self.assertEqual(child1.id, diff.id)

        # Test Case 17 - different team
        diff = Goal(goal_events.goal_different_team)
        self.assertEqual(child1.id, diff.id)


    def test_hit_equality(self):
        """
        Test the equality operator for a Hit event.
        """
        parent = Event(hit_events.hit_1)
        child1 = Hit(hit_events.hit_1)
        child2 = Hit(hit_events.hit_2)
        child3 = Hit(hit_events.hit_3)
        child4 = Hit(hit_events.hit_1)
        other  = Shot(shot_events.shot_1)

        # Test Case 1 - parent to child
        self.assertNotEqual(parent, child1)
        self.assertNotEqual(parent, child2)
        self.assertNotEqual(parent, child3)
        self.assertNotEqual(parent, child4)

        # Test Case 2 - Unlike instances
        self.assertNotEqual(child1, child2)
        self.assertNotEqual(child1, child3)
        self.assertNotEqual(child2, child3)
        self.assertNotEqual(child2, child4)
        self.assertNotEqual(child3, child4)

        # Test Case 3 - Like instances
        self.assertEqual(child1, child4)
        self.assertEqual(child4, child1)

        # Test Case 4 - Unlike classes
        self.assertNotEqual(child1, other)
        self.assertNotEqual(child2, other)
        self.assertNotEqual(child3, other)
        self.assertNotEqual(child4, other)

        # Test Case 5 - different eventid
        diff = Hit(hit_events.hit_different_event_id)
        self.assertEqual(child1, diff)

        # Test Case 6 - different eventidx
        diff = Hit(hit_events.hit_different_event_id_x)
        self.assertEqual(child1, diff)

        # Test Case 7 - different datetime
        diff = Hit(hit_events.hit_different_datetime)
        self.assertEqual(child1, diff)

        # Test Case 8 - different period
        diff = Hit(hit_events.hit_different_period)
        self.assertNotEqual(child1, diff)

        # Test Case 9 - different period time
        diff = Hit(hit_events.hit_different_period_time)
        self.assertEqual(child1, diff)

        # Test Case 10 - different period time remaining
        diff = Hit(hit_events.hit_different_period_time_remaining)
        self.assertNotEqual(child1, diff)

        # Test Case 11 - different hitter
        diff = Hit(hit_events.hit_different_hitter)
        self.assertNotEqual(child1, diff)

        # Test Case 12 - different hittee
        diff = Hit(hit_events.hit_different_hittee)
        self.assertNotEqual(child1, diff)


    def test_hit_id(self):
        """
        Test the property ID for a Hit event.
        """
        parent = Event(hit_events.hit_1)
        child1 = Hit(hit_events.hit_1)
        child2 = Hit(hit_events.hit_2)
        child3 = Hit(hit_events.hit_3)
        child4 = Hit(hit_events.hit_1)
        other  = Shot(shot_events.shot_1)

        # Test Case 1 - parent to child
        self.assertNotEqual(parent.id, child1.id)
        self.assertNotEqual(parent.id, child2.id)
        self.assertNotEqual(parent.id, child3.id)
        self.assertNotEqual(parent.id, child4.id)

        # Test Case 2 - Unlike instances
        self.assertNotEqual(child1.id, child2.id)
        self.assertNotEqual(child1.id, child3.id)
        self.assertNotEqual(child2.id, child3.id)
        self.assertNotEqual(child2.id, child4.id)
        self.assertNotEqual(child3.id, child4.id)

        # Test Case 3 - Like instances
        self.assertEqual(child1.id, child4.id)
        self.assertEqual(child4.id, child1.id)

        # Test Case 4 - Unlike classes
        self.assertNotEqual(child1.id, other.id)
        self.assertNotEqual(child2.id, other.id)
        self.assertNotEqual(child3.id, other.id)
        self.assertNotEqual(child4.id, other.id)

        # Test Case 5 - different eventid
        diff = Hit(hit_events.hit_different_event_id)
        self.assertEqual(child1.id, diff.id)

        # Test Case 6 - different eventidx
        diff = Hit(hit_events.hit_different_event_id_x)
        self.assertEqual(child1.id, diff.id)

        # Test Case 7 - different datetime
        diff = Hit(hit_events.hit_different_datetime)
        self.assertEqual(child1.id, diff.id)

        # Test Case 8 - different period
        diff = Hit(hit_events.hit_different_period)
        self.assertNotEqual(child1.id, diff.id)

        # Test Case 9 - different period time
        diff = Hit(hit_events.hit_different_period_time)
        self.assertEqual(child1.id, diff.id)

        # Test Case 10 - different period time remaining
        diff = Hit(hit_events.hit_different_period_time_remaining)
        self.assertNotEqual(child1.id, diff.id)

        # Test Case 11 - different hitter
        diff = Hit(hit_events.hit_different_hitter)
        self.assertNotEqual(child1.id, diff.id)

        # Test Case 12 - different hittee
        diff = Hit(hit_events.hit_different_hittee)
        self.assertNotEqual(child1.id, diff.id)


    def test_missed_shot_equality(self):
        """
        Test the equality operator for a MissedShot event.
        """
        parent = Event(missed_shot_events.missed_shot_1)
        child1 = MissedShot(missed_shot_events.missed_shot_1)
        child2 = MissedShot(missed_shot_events.missed_shot_2)
        child3 = MissedShot(missed_shot_events.missed_shot_3)
        child4 = MissedShot(missed_shot_events.missed_shot_1)
        other  = Shot(shot_events.shot_1)

        # Test Case 1 - parent to child
        self.assertNotEqual(parent, child1)
        self.assertNotEqual(parent, child2)
        self.assertNotEqual(parent, child3)
        self.assertNotEqual(parent, child4)

        # Test Case 2 - Unlike instances
        self.assertNotEqual(child1, child2)
        self.assertNotEqual(child1, child3)
        self.assertNotEqual(child2, child3)
        self.assertNotEqual(child2, child4)
        self.assertNotEqual(child3, child4)

        # Test Case 3 - Like instances
        self.assertEqual(child1, child4)
        self.assertEqual(child4, child1)

        # Test Case 4 - Unlike classes
        self.assertNotEqual(child1, other)
        self.assertNotEqual(child2, other)
        self.assertNotEqual(child3, other)
        self.assertNotEqual(child4, other)

        # Test Case 5 - different eventid
        diff = MissedShot(missed_shot_events.missed_shot_different_event_id)
        self.assertEqual(child1, diff)

        # Test Case 6 - different eventidx
        diff = MissedShot(missed_shot_events.missed_shot_different_event_id_x)
        self.assertEqual(child1, diff)

        # Test Case 7 - different datetime
        diff = MissedShot(missed_shot_events.missed_shot_different_datetime)
        self.assertEqual(child1, diff)

        # Test Case 8 - different period
        diff = MissedShot(missed_shot_events.missed_shot_different_period)
        self.assertNotEqual(child1, diff)

        # Test Case 9 - different period time
        diff = MissedShot(missed_shot_events.missed_shot_different_period_time)
        self.assertEqual(child1, diff)

        # Test Case 10 - different period time remaining
        diff = MissedShot(missed_shot_events.missed_shot_different_period_time_remaining)
        self.assertNotEqual(child1, diff)

        # Test Case 11 - different shooter
        diff = MissedShot(missed_shot_events.missed_shot_different_shooter)
        self.assertNotEqual(child1, diff)

        # Test Case 12 - different goalie
        diff = MissedShot(missed_shot_events.missed_shot_different_goalie)
        self.assertNotEqual(child1, diff)


    def test_missed_shot_id(self):
        """
        Test the ID property for a MissedShot event.
        """
        parent = Event(missed_shot_events.missed_shot_1)
        child1 = MissedShot(missed_shot_events.missed_shot_1)
        child2 = MissedShot(missed_shot_events.missed_shot_2)
        child3 = MissedShot(missed_shot_events.missed_shot_3)
        child4 = MissedShot(missed_shot_events.missed_shot_1)
        other  = Shot(shot_events.shot_1)

        # Test Case 1 - parent to child
        self.assertNotEqual(parent.id, child1.id)
        self.assertNotEqual(parent.id, child2.id)
        self.assertNotEqual(parent.id, child3.id)
        self.assertNotEqual(parent.id, child4.id)

        # Test Case 2 - Unlike instances
        self.assertNotEqual(child1.id, child2.id)
        self.assertNotEqual(child1.id, child3.id)
        self.assertNotEqual(child2.id, child3.id)
        self.assertNotEqual(child2.id, child4.id)
        self.assertNotEqual(child3.id, child4.id)

        # Test Case 3 - Like instances
        self.assertEqual(child1.id, child4.id)
        self.assertEqual(child4.id, child1.id)

        # Test Case 4 - Unlike classes
        self.assertNotEqual(child1.id, other.id)
        self.assertNotEqual(child2.id, other.id)
        self.assertNotEqual(child3.id, other.id)
        self.assertNotEqual(child4.id, other.id)

        # Test Case 5 - different eventid
        diff = MissedShot(missed_shot_events.missed_shot_different_event_id)
        self.assertEqual(child1.id, diff.id)

        # Test Case 6 - different eventidx
        diff = MissedShot(missed_shot_events.missed_shot_different_event_id_x)
        self.assertEqual(child1.id, diff.id)

        # Test Case 7 - different datetime
        diff = MissedShot(missed_shot_events.missed_shot_different_datetime)
        self.assertEqual(child1.id, diff.id)

        # Test Case 8 - different period
        diff = MissedShot(missed_shot_events.missed_shot_different_period)
        self.assertNotEqual(child1.id, diff.id)

        # Test Case 9 - different period time
        diff = MissedShot(missed_shot_events.missed_shot_different_period_time)
        self.assertEqual(child1.id, diff.id)

        # Test Case 10 - different period time remaining
        diff = MissedShot(missed_shot_events.missed_shot_different_period_time_remaining)
        self.assertNotEqual(child1.id, diff.id)

        # Test Case 11 - different shooter
        diff = MissedShot(missed_shot_events.missed_shot_different_shooter)
        self.assertNotEqual(child1.id, diff.id)

        # Test Case 12 - different goalie
        diff = MissedShot(missed_shot_events.missed_shot_different_goalie)
        self.assertNotEqual(child1.id, diff.id)


    def test_penalty_shot_equality(self):
        """
        Test the equality operator for a PenaltyShot event.
        """
        parent = Event(penalty_shot_events.penalty_shot_1)
        child1 = PenaltyShot(penalty_shot_events.penalty_shot_1)
        child2 = PenaltyShot(penalty_shot_events.penalty_shot_2)
        child3 = PenaltyShot(penalty_shot_events.penalty_shot_3)
        child4 = PenaltyShot(penalty_shot_events.penalty_shot_1)
        other  = Shot(shot_events.shot_1)

        # Test Case 1 - parent to child
        self.assertNotEqual(parent, child1)
        self.assertNotEqual(parent, child2)
        self.assertNotEqual(parent, child3)
        self.assertNotEqual(parent, child4)

        # Test Case 2 - Unlike instances
        self.assertNotEqual(child1, child2)
        self.assertNotEqual(child1, child3)
        self.assertNotEqual(child2, child3)
        self.assertNotEqual(child2, child4)
        self.assertNotEqual(child3, child4)

        # Test Case 3 - Like instances
        self.assertEqual(child1, child4)
        self.assertEqual(child4, child1)

        # Test Case 4 - Unlike classes
        self.assertNotEqual(child1, other)
        self.assertNotEqual(child2, other)
        self.assertNotEqual(child3, other)
        self.assertNotEqual(child4, other)

        # Test Case 5 - different eventid
        diff = PenaltyShot(penalty_shot_events.penalty_shot_different_event_id)
        self.assertEqual(child1, diff)

        # Test Case 6 - different eventidx
        diff = PenaltyShot(penalty_shot_events.penalty_shot_different_event_id_x)
        self.assertEqual(child1, diff)

        # Test Case 7 - different datetime
        diff = PenaltyShot(penalty_shot_events.penalty_shot_different_datetime)
        self.assertEqual(child1, diff)

        # Test Case 8 - different period
        diff = PenaltyShot(penalty_shot_events.penalty_shot_different_period)
        self.assertNotEqual(child1, diff)

        # Test Case 9 - different period time
        diff = PenaltyShot(penalty_shot_events.penalty_shot_different_period_time)
        self.assertEqual(child1, diff)

        # Test Case 10 - different period time remaining
        diff = PenaltyShot(penalty_shot_events.penalty_shot_different_period_time_remaining)
        self.assertNotEqual(child1, diff)

        # Test Case 11 - different taker
        diff = PenaltyShot(penalty_shot_events.penalty_shot_different_taker)
        self.assertNotEqual(child1, diff)

        # Test Case 12 - different drawn by
        diff = PenaltyShot(penalty_shot_events.penalty_shot_different_drawn_by)
        self.assertNotEqual(child1, diff)

        # Test Case 13 - different reason
        diff = PenaltyShot(penalty_shot_events.penalty_shot_different_reason)
        self.assertNotEqual(child1, diff)


    def test_penalty_shot_id(self):
        """
        Test the ID property for a PenaltyShot event.
        """
        parent = Event(penalty_shot_events.penalty_shot_1)
        child1 = PenaltyShot(penalty_shot_events.penalty_shot_1)
        child2 = PenaltyShot(penalty_shot_events.penalty_shot_2)
        child3 = PenaltyShot(penalty_shot_events.penalty_shot_3)
        child4 = PenaltyShot(penalty_shot_events.penalty_shot_1)
        other  = Shot(shot_events.shot_1)

        # Test Case 1 - parent to child
        self.assertNotEqual(parent.id, child1.id)
        self.assertNotEqual(parent.id, child2.id)
        self.assertNotEqual(parent.id, child3.id)
        self.assertNotEqual(parent.id, child4.id)

        # Test Case 2 - Unlike instances
        self.assertNotEqual(child1.id, child2.id)
        self.assertNotEqual(child1.id, child3.id)
        self.assertNotEqual(child2.id, child3.id)
        self.assertNotEqual(child2.id, child4.id)
        self.assertNotEqual(child3.id, child4.id)

        # Test Case 3 - Like instances
        self.assertEqual(child1.id, child4.id)
        self.assertEqual(child4.id, child1.id)

        # Test Case 4 - Unlike classes
        self.assertNotEqual(child1.id, other.id)
        self.assertNotEqual(child2.id, other.id)
        self.assertNotEqual(child3.id, other.id)
        self.assertNotEqual(child4.id, other.id)

        # Test Case 5 - different eventid
        diff = PenaltyShot(penalty_shot_events.penalty_shot_different_event_id)
        self.assertEqual(child1.id, diff.id)

        # Test Case 6 - different eventidx
        diff = PenaltyShot(penalty_shot_events.penalty_shot_different_event_id_x)
        self.assertEqual(child1.id, diff.id)

        # Test Case 7 - different datetime
        diff = PenaltyShot(penalty_shot_events.penalty_shot_different_datetime)
        self.assertEqual(child1.id, diff.id)

        # Test Case 8 - different period
        diff = PenaltyShot(penalty_shot_events.penalty_shot_different_period)
        self.assertNotEqual(child1.id, diff.id)

        # Test Case 9 - different period time
        diff = PenaltyShot(penalty_shot_events.penalty_shot_different_period_time)
        self.assertEqual(child1.id, diff.id)

        # Test Case 10 - different period time remaining
        diff = PenaltyShot(penalty_shot_events.penalty_shot_different_period_time_remaining)
        self.assertNotEqual(child1.id, diff.id)

        # Test Case 11 - different taker
        diff = PenaltyShot(penalty_shot_events.penalty_shot_different_taker)
        self.assertNotEqual(child1.id, diff.id)

        # Test Case 12 - different drawn by
        diff = PenaltyShot(penalty_shot_events.penalty_shot_different_drawn_by)
        self.assertNotEqual(child1.id, diff.id)


    def test_penalty_equality(self):
        """
        Test the equality operator for a Penalty event.
        """
        parent = Event(penalty_events.penalty_1)
        child1 = Penalty(penalty_events.penalty_1)
        child2 = Penalty(penalty_events.penalty_2)
        child3 = Penalty(penalty_events.penalty_3)
        child4 = Penalty(penalty_events.penalty_1)
        other  = Shot(shot_events.shot_1)

        # Test Case 1 - parent to child
        self.assertNotEqual(parent, child1)
        self.assertNotEqual(parent, child2)
        self.assertNotEqual(parent, child3)
        self.assertNotEqual(parent, child4)

        # Test Case 2 - Unlike instances
        self.assertNotEqual(child1, child2)
        self.assertNotEqual(child1, child3)
        self.assertNotEqual(child2, child3)
        self.assertNotEqual(child2, child4)
        self.assertNotEqual(child3, child4)

        # Test Case 3 - Like instances
        self.assertEqual(child1, child4)
        self.assertEqual(child4, child1)

        # Test Case 4 - Unlike classes
        self.assertNotEqual(child1, other)
        self.assertNotEqual(child2, other)
        self.assertNotEqual(child3, other)
        self.assertNotEqual(child4, other)

        # Test Case 5 - different eventid
        diff = Penalty(penalty_events.penalty_different_event_id)
        self.assertEqual(child1, diff)

        # Test Case 6 - different eventidx
        diff = Penalty(penalty_events.penalty_different_event_id_x)
        self.assertEqual(child1, diff)

        # Test Case 7 - different datetime
        diff = Penalty(penalty_events.penalty_different_datetime)
        self.assertEqual(child1, diff)

        # Test Case 8 - different period
        diff = Penalty(penalty_events.penalty_different_period)
        self.assertNotEqual(child1, diff)

        # Test Case 9 - different period time
        diff = Penalty(penalty_events.penalty_different_period_time)
        self.assertEqual(child1, diff)

        # Test Case 10 - different period time remaining
        diff = Penalty(penalty_events.penalty_different_period_time_remaining)
        self.assertNotEqual(child1, diff)

        # Test Case 11 - different taker
        diff = Penalty(penalty_events.penalty_different_taker)
        self.assertNotEqual(child1, diff)

        # Test Case 12 - different drawn by
        diff = Penalty(penalty_events.penalty_different_drawn_by)
        self.assertNotEqual(child1, diff)

        # Test Case 13 - different reason
        diff = Penalty(penalty_events.penalty_different_reason)
        self.assertNotEqual(child1, diff)

        # Test Case 14 - different severity
        diff = Penalty(penalty_events.penalty_different_severity)
        self.assertNotEqual(child1, diff)

        # Test Case 15 - different minutes
        diff = Penalty(penalty_events.penalty_different_minutes)
        self.assertNotEqual(child1, diff)


    def test_penalty_id(self):
        """
        Test the ID property for a Penalty event.
        """
        parent = Event(penalty_events.penalty_1)
        child1 = Penalty(penalty_events.penalty_1)
        child2 = Penalty(penalty_events.penalty_2)
        child3 = Penalty(penalty_events.penalty_3)
        child4 = Penalty(penalty_events.penalty_1)
        other  = Shot(shot_events.shot_1)

        # Test Case 1 - parent to child
        self.assertNotEqual(parent.id, child1.id)
        self.assertNotEqual(parent.id, child2.id)
        self.assertNotEqual(parent.id, child3.id)
        self.assertNotEqual(parent.id, child4.id)

        # Test Case 2 - Unlike instances
        self.assertNotEqual(child1.id, child2.id)
        self.assertNotEqual(child1.id, child3.id)
        self.assertNotEqual(child2.id, child3.id)
        self.assertNotEqual(child2.id, child4.id)
        self.assertNotEqual(child3.id, child4.id)

        # Test Case 3 - Like instances
        self.assertEqual(child1.id, child4.id)
        self.assertEqual(child4.id, child1.id)

        # Test Case 4 - Unlike classes
        self.assertNotEqual(child1.id, other.id)
        self.assertNotEqual(child2.id, other.id)
        self.assertNotEqual(child3.id, other.id)
        self.assertNotEqual(child4.id, other.id)

        # Test Case 5 - different eventid
        diff = Penalty(penalty_events.penalty_different_event_id)
        self.assertEqual(child1.id, diff.id)

        # Test Case 6 - different eventidx
        diff = Penalty(penalty_events.penalty_different_event_id_x)
        self.assertEqual(child1.id, diff.id)

        # Test Case 7 - different datetime
        diff = Penalty(penalty_events.penalty_different_datetime)
        self.assertEqual(child1.id, diff.id)

        # Test Case 8 - different period
        diff = Penalty(penalty_events.penalty_different_period)
        self.assertNotEqual(child1.id, diff.id)

        # Test Case 9 - different period time
        diff = Penalty(penalty_events.penalty_different_period_time)
        self.assertEqual(child1.id, diff.id)

        # Test Case 10 - different period time remaining
        diff = Penalty(penalty_events.penalty_different_period_time_remaining)
        self.assertNotEqual(child1.id, diff.id)

        # Test Case 11 - different taker
        diff = Penalty(penalty_events.penalty_different_taker)
        self.assertNotEqual(child1.id, diff.id)

        # Test Case 12 - different drawn by
        diff = Penalty(penalty_events.penalty_different_drawn_by)
        self.assertNotEqual(child1.id, diff.id)

        # Test Case 13 - different reason
        diff = Penalty(penalty_events.penalty_different_reason)
        self.assertNotEqual(child1.id, diff.id)

        # Test Case 14 - different severity
        diff = Penalty(penalty_events.penalty_different_severity)
        self.assertEqual(child1.id, diff.id)

        # Test Case 15 - different minutes
        diff = Penalty(penalty_events.penalty_different_minutes)
        self.assertEqual(child1.id, diff.id)


    def test_period_end_equality(self):
        """
        Test the equality operator for a PeriodEnd event.
        """
        parent = Event(period_end_events.period_end_1)
        child1 = PeriodEnd(period_end_events.period_end_1)
        child2 = PeriodEnd(period_end_events.period_end_2)
        child3 = PeriodEnd(period_end_events.period_end_3)
        child4 = PeriodEnd(period_end_events.period_end_1)
        other  = Shot(shot_events.shot_1)

        # Test Case 1 - parent to child
        self.assertNotEqual(parent, child1)
        self.assertNotEqual(parent, child2)
        self.assertNotEqual(parent, child3)
        self.assertNotEqual(parent, child4)

        # Test Case 2 - Unlike instances
        self.assertNotEqual(child1, child2)
        self.assertNotEqual(child1, child3)
        self.assertNotEqual(child2, child3)
        self.assertNotEqual(child2, child4)
        self.assertNotEqual(child3, child4)

        # Test Case 3 - Like instances
        self.assertEqual(child1, child4)
        self.assertEqual(child4, child1)

        # Test Case 4 - Unlike classes
        self.assertNotEqual(child1, other)
        self.assertNotEqual(child2, other)
        self.assertNotEqual(child3, other)
        self.assertNotEqual(child4, other)

        # Test Case 5 - different eventid
        diff = PeriodEnd(period_end_events.period_end_different_event_id)
        self.assertEqual(child1, diff)

        # Test Case 6 - different eventidx
        diff = PeriodEnd(period_end_events.period_end_different_event_id_x)
        self.assertEqual(child1, diff)

        # Test Case 7 - different datetime
        diff = PeriodEnd(period_end_events.period_end_different_datetime)
        self.assertEqual(child1, diff)

        # Test Case 8 - different period
        diff = PeriodEnd(period_end_events.period_end_different_period)
        self.assertNotEqual(child1, diff)

        # Test Case 9 - different period time
        diff = PeriodEnd(period_end_events.period_end_different_period_time)
        self.assertEqual(child1, diff)

        # Test Case 10 - different period time remaining
        diff = PeriodEnd(period_end_events.period_end_different_period_time_remaining)
        self.assertEqual(child1, diff)


    def test_period_end_id(self):
        """
        Test the ID property for a PeriodEnd event.
        """
        parent = Event(period_end_events.period_end_1)
        child1 = PeriodEnd(period_end_events.period_end_1)
        child2 = PeriodEnd(period_end_events.period_end_2)
        child3 = PeriodEnd(period_end_events.period_end_3)
        child4 = PeriodEnd(period_end_events.period_end_1)
        other  = Shot(shot_events.shot_1)

        # Test Case 1 - parent to child
        self.assertNotEqual(parent.id, child1.id)
        self.assertNotEqual(parent.id, child2.id)
        self.assertNotEqual(parent.id, child3.id)
        self.assertNotEqual(parent.id, child4.id)

        # Test Case 2 - Unlike instances
        self.assertNotEqual(child1.id, child2.id)
        self.assertNotEqual(child1.id, child3.id)
        self.assertNotEqual(child2.id, child3.id)
        self.assertNotEqual(child2.id, child4.id)
        self.assertNotEqual(child3.id, child4.id)

        # Test Case 3 - Like instances
        self.assertEqual(child1.id, child4.id)
        self.assertEqual(child4.id, child1.id)

        # Test Case 4 - Unlike classes
        self.assertNotEqual(child1.id, other.id)
        self.assertNotEqual(child2.id, other.id)
        self.assertNotEqual(child3.id, other.id)
        self.assertNotEqual(child4.id, other.id)

        # Test Case 5 - different eventid
        diff = PeriodEnd(period_end_events.period_end_different_event_id)
        self.assertEqual(child1.id, diff.id)

        # Test Case 6 - different eventidx
        diff = PeriodEnd(period_end_events.period_end_different_event_id_x)
        self.assertEqual(child1.id, diff.id)

        # Test Case 7 - different datetime
        diff = PeriodEnd(period_end_events.period_end_different_datetime)
        self.assertEqual(child1.id, diff.id)

        # Test Case 8 - different period
        diff = PeriodEnd(period_end_events.period_end_different_period)
        self.assertNotEqual(child1.id, diff.id)

        # Test Case 9 - different period time
        diff = PeriodEnd(period_end_events.period_end_different_period_time)
        self.assertEqual(child1.id, diff.id)

        # Test Case 10 - different period time remaining
        diff = PeriodEnd(period_end_events.period_end_different_period_time_remaining)
        self.assertEqual(child1.id, diff.id)


    def test_period_official_equality(self):
        """
        Test the equality operator for a PeriodOfficial event.
        """
        parent = Event(period_official_events.period_official_1)
        child1 = PeriodOfficial(period_official_events.period_official_1)
        child2 = PeriodOfficial(period_official_events.period_official_2)
        child3 = PeriodOfficial(period_official_events.period_official_3)
        child4 = PeriodOfficial(period_official_events.period_official_1)
        other  = Shot(shot_events.shot_1)

        # Test Case 1 - parent to child
        self.assertNotEqual(parent, child1)
        self.assertNotEqual(parent, child2)
        self.assertNotEqual(parent, child3)
        self.assertNotEqual(parent, child4)

        # Test Case 2 - Unlike instances
        self.assertNotEqual(child1, child2)
        self.assertNotEqual(child1, child3)
        self.assertNotEqual(child2, child3)
        self.assertNotEqual(child2, child4)
        self.assertNotEqual(child3, child4)

        # Test Case 3 - Like instances
        self.assertEqual(child1, child4)
        self.assertEqual(child4, child1)

        # Test Case 4 - Unlike classes
        self.assertNotEqual(child1, other)
        self.assertNotEqual(child2, other)
        self.assertNotEqual(child3, other)
        self.assertNotEqual(child4, other)

        # Test Case 5 - different eventid
        diff = PeriodOfficial(period_official_events.period_official_different_event_id)
        self.assertEqual(child1, diff)

        # Test Case 6 - different eventidx
        diff = PeriodOfficial(period_official_events.period_official_different_event_id_x)
        self.assertEqual(child1, diff)

        # Test Case 7 - different datetime
        diff = PeriodOfficial(period_official_events.period_official_different_datetime)
        self.assertEqual(child1, diff)

        # Test Case 8 - different period
        diff = PeriodOfficial(period_official_events.period_official_different_period)
        self.assertNotEqual(child1, diff)

        # Test Case 9 - different period time
        diff = PeriodOfficial(period_official_events.period_official_different_period_time)
        self.assertEqual(child1, diff)

        # Test Case 10 - different period time remaining
        diff = PeriodOfficial(period_official_events.period_official_different_period_time_remaining)
        self.assertEqual(child1, diff)


    def test_period_official_id(self):
        """
        Test the ID property for a PeriodOfficial event.
        """
        parent = Event(period_official_events.period_official_1)
        child1 = PeriodOfficial(period_official_events.period_official_1)
        child2 = PeriodOfficial(period_official_events.period_official_2)
        child3 = PeriodOfficial(period_official_events.period_official_3)
        child4 = PeriodOfficial(period_official_events.period_official_1)
        other  = Shot(shot_events.shot_1)

        # Test Case 1 - parent to child
        self.assertNotEqual(parent.id, child1.id)
        self.assertNotEqual(parent.id, child2.id)
        self.assertNotEqual(parent.id, child3.id)
        self.assertNotEqual(parent.id, child4.id)

        # Test Case 2 - Unlike instances
        self.assertNotEqual(child1.id, child2.id)
        self.assertNotEqual(child1.id, child3.id)
        self.assertNotEqual(child2.id, child3.id)
        self.assertNotEqual(child2.id, child4.id)
        self.assertNotEqual(child3.id, child4.id)

        # Test Case 3 - Like instances
        self.assertEqual(child1.id, child4.id)
        self.assertEqual(child4.id, child1.id)

        # Test Case 4 - Unlike classes
        self.assertNotEqual(child1.id, other.id)
        self.assertNotEqual(child2.id, other.id)
        self.assertNotEqual(child3.id, other.id)
        self.assertNotEqual(child4.id, other.id)

        # Test Case 5 - different eventid
        diff = PeriodOfficial(period_official_events.period_official_different_event_id)
        self.assertEqual(child1.id, diff.id)

        # Test Case 6 - different eventidx
        diff = PeriodOfficial(period_official_events.period_official_different_event_id_x)
        self.assertEqual(child1.id, diff.id)

        # Test Case 7 - different datetime
        diff = PeriodOfficial(period_official_events.period_official_different_datetime)
        self.assertEqual(child1.id, diff.id)

        # Test Case 8 - different period
        diff = PeriodOfficial(period_official_events.period_official_different_period)
        self.assertNotEqual(child1.id, diff.id)

        # Test Case 9 - different period time
        diff = PeriodOfficial(period_official_events.period_official_different_period_time)
        self.assertEqual(child1.id, diff.id)

        # Test Case 10 - different period time remaining
        diff = PeriodOfficial(period_official_events.period_official_different_period_time_remaining)
        self.assertEqual(child1.id, diff.id)


    def test_period_ready_equality(self):
        """
        Test the equality operator for a PeriodReady event.
        """
        parent = Event(period_ready_events.period_ready_1)
        child1 = PeriodReady(period_ready_events.period_ready_1)
        child2 = PeriodReady(period_ready_events.period_ready_2)
        child3 = PeriodReady(period_ready_events.period_ready_3)
        child4 = PeriodReady(period_ready_events.period_ready_1)
        other  = Shot(shot_events.shot_1)

        # Test Case 1 - parent to child
        self.assertNotEqual(parent, child1)
        self.assertNotEqual(parent, child2)
        self.assertNotEqual(parent, child3)
        self.assertNotEqual(parent, child4)

        # Test Case 2 - Unlike instances
        self.assertNotEqual(child1, child2)
        self.assertNotEqual(child1, child3)
        self.assertNotEqual(child2, child3)
        self.assertNotEqual(child2, child4)
        self.assertNotEqual(child3, child4)

        # Test Case 3 - Like instances
        self.assertEqual(child1, child4)
        self.assertEqual(child4, child1)

        # Test Case 4 - Unlike classes
        self.assertNotEqual(child1, other)
        self.assertNotEqual(child2, other)
        self.assertNotEqual(child3, other)
        self.assertNotEqual(child4, other)

        # Test Case 5 - different eventid
        diff = PeriodReady(period_ready_events.period_ready_different_event_id)
        self.assertEqual(child1, diff)

        # Test Case 6 - different eventidx
        diff = PeriodReady(period_ready_events.period_ready_different_event_id_x)
        self.assertEqual(child1, diff)

        # Test Case 7 - different datetime
        diff = PeriodReady(period_ready_events.period_ready_different_datetime)
        self.assertEqual(child1, diff)

        # Test Case 8 - different period
        diff = PeriodReady(period_ready_events.period_ready_different_period)
        self.assertNotEqual(child1, diff)

        # Test Case 9 - different period time
        diff = PeriodReady(period_ready_events.period_ready_different_period_time)
        self.assertEqual(child1, diff)

        # Test Case 10 - different period time remaining
        diff = PeriodReady(period_ready_events.period_ready_different_period_time_remaining)
        self.assertEqual(child1, diff)


    def test_period_ready_id(self):
        """
        Test the ID property for a PeriodReady event.
        """
        parent = Event(period_ready_events.period_ready_1)
        child1 = PeriodReady(period_ready_events.period_ready_1)
        child2 = PeriodReady(period_ready_events.period_ready_2)
        child3 = PeriodReady(period_ready_events.period_ready_3)
        child4 = PeriodReady(period_ready_events.period_ready_1)
        other  = Shot(shot_events.shot_1)

        # Test Case 1 - parent to child
        self.assertNotEqual(parent.id, child1.id)
        self.assertNotEqual(parent.id, child2.id)
        self.assertNotEqual(parent.id, child3.id)
        self.assertNotEqual(parent.id, child4.id)

        # Test Case 2 - Unlike instances
        self.assertNotEqual(child1.id, child2.id)
        self.assertNotEqual(child1.id, child3.id)
        self.assertNotEqual(child2.id, child3.id)
        self.assertNotEqual(child2.id, child4.id)
        self.assertNotEqual(child3.id, child4.id)

        # Test Case 3 - Like instances
        self.assertEqual(child1.id, child4.id)
        self.assertEqual(child4.id, child1.id)

        # Test Case 4 - Unlike classes
        self.assertNotEqual(child1.id, other.id)
        self.assertNotEqual(child2.id, other.id)
        self.assertNotEqual(child3.id, other.id)
        self.assertNotEqual(child4.id, other.id)

        # Test Case 5 - different eventid
        diff = PeriodReady(period_ready_events.period_ready_different_event_id)
        self.assertEqual(child1.id, diff.id)

        # Test Case 6 - different eventidx
        diff = PeriodReady(period_ready_events.period_ready_different_event_id_x)
        self.assertEqual(child1.id, diff.id)

        # Test Case 7 - different datetime
        diff = PeriodReady(period_ready_events.period_ready_different_datetime)
        self.assertEqual(child1.id, diff.id)

        # Test Case 8 - different period
        diff = PeriodReady(period_ready_events.period_ready_different_period)
        self.assertNotEqual(child1.id, diff.id)

        # Test Case 9 - different period time
        diff = PeriodReady(period_ready_events.period_ready_different_period_time)
        self.assertEqual(child1.id, diff.id)

        # Test Case 10 - different period time remaining
        diff = PeriodReady(period_ready_events.period_ready_different_period_time_remaining)
        self.assertEqual(child1.id, diff.id)


    def test_period_start_equality(self):
        """
        Test the equality operator for a PeriodStart event.
        """
        parent = Event(period_start_events.period_start_1)
        child1 = PeriodStart(period_start_events.period_start_1)
        child2 = PeriodStart(period_start_events.period_start_2)
        child3 = PeriodStart(period_start_events.period_start_3)
        child4 = PeriodStart(period_start_events.period_start_1)
        other  = Shot(shot_events.shot_1)

        # Test Case 1 - parent to child
        self.assertNotEqual(parent, child1)
        self.assertNotEqual(parent, child2)
        self.assertNotEqual(parent, child3)
        self.assertNotEqual(parent, child4)

        # Test Case 2 - Unlike instances
        self.assertNotEqual(child1, child2)
        self.assertNotEqual(child1, child3)
        self.assertNotEqual(child2, child3)
        self.assertNotEqual(child2, child4)
        self.assertNotEqual(child3, child4)

        # Test Case 3 - Like instances
        self.assertEqual(child1, child4)
        self.assertEqual(child4, child1)

        # Test Case 4 - Unlike classes
        self.assertNotEqual(child1, other)
        self.assertNotEqual(child2, other)
        self.assertNotEqual(child3, other)
        self.assertNotEqual(child4, other)

        # Test Case 5 - different eventid
        diff = PeriodStart(period_start_events.period_start_different_event_id)
        self.assertEqual(child1, diff)

        # Test Case 6 - different eventidx
        diff = PeriodStart(period_start_events.period_start_different_event_id_x)
        self.assertEqual(child1, diff)

        # Test Case 7 - different datetime
        diff = PeriodStart(period_start_events.period_start_different_datetime)
        self.assertEqual(child1, diff)

        # Test Case 8 - different period
        diff = PeriodStart(period_start_events.period_start_different_period)
        self.assertNotEqual(child1, diff)

        # Test Case 9 - different period time
        diff = PeriodStart(period_start_events.period_start_different_period_time)
        self.assertEqual(child1, diff)

        # Test Case 10 - different period time remaining
        diff = PeriodStart(period_start_events.period_start_different_period_time_remaining)
        self.assertEqual(child1, diff)


    def test_period_start_id(self):
        """
        Test the ID property for a PeriodStart event.
        """
        parent = Event(period_start_events.period_start_1)
        child1 = PeriodStart(period_start_events.period_start_1)
        child2 = PeriodStart(period_start_events.period_start_2)
        child3 = PeriodStart(period_start_events.period_start_3)
        child4 = PeriodStart(period_start_events.period_start_1)
        other  = Shot(shot_events.shot_1)

        # Test Case 1 - parent to child
        self.assertNotEqual(parent.id, child1.id)
        self.assertNotEqual(parent.id, child2.id)
        self.assertNotEqual(parent.id, child3.id)
        self.assertNotEqual(parent.id, child4.id)

        # Test Case 2 - Unlike instances
        self.assertNotEqual(child1.id, child2.id)
        self.assertNotEqual(child1.id, child3.id)
        self.assertNotEqual(child2.id, child3.id)
        self.assertNotEqual(child2.id, child4.id)
        self.assertNotEqual(child3.id, child4.id)

        # Test Case 3 - Like instances
        self.assertEqual(child1.id, child4.id)
        self.assertEqual(child4.id, child1.id)

        # Test Case 4 - Unlike classes
        self.assertNotEqual(child1.id, other.id)
        self.assertNotEqual(child2.id, other.id)
        self.assertNotEqual(child3.id, other.id)
        self.assertNotEqual(child4.id, other.id)

        # Test Case 5 - different eventid
        diff = PeriodStart(period_start_events.period_start_different_event_id)
        self.assertEqual(child1.id, diff.id)

        # Test Case 6 - different eventidx
        diff = PeriodStart(period_start_events.period_start_different_event_id_x)
        self.assertEqual(child1.id, diff.id)

        # Test Case 7 - different datetime
        diff = PeriodStart(period_start_events.period_start_different_datetime)
        self.assertEqual(child1.id, diff.id)

        # Test Case 8 - different period
        diff = PeriodStart(period_start_events.period_start_different_period)
        self.assertNotEqual(child1.id, diff.id)

        # Test Case 9 - different period time
        diff = PeriodStart(period_start_events.period_start_different_period_time)
        self.assertEqual(child1.id, diff.id)

        # Test Case 10 - different period time remaining
        diff = PeriodStart(period_start_events.period_start_different_period_time_remaining)
        self.assertEqual(child1.id, diff.id)


    def test_ping_equality(self):
        """
        Test the equality operator for a Ping event.
        """
        parent = Event(ping_events.ping_1)
        child1 = Ping(ping_events.ping_1)
        child2 = Ping(ping_events.ping_2)
        child3 = Ping(ping_events.ping_3)
        child4 = Ping(ping_events.ping_1)
        other  = Shot(shot_events.shot_1)

        # Test Case 1 - parent to child
        self.assertNotEqual(parent, child1)
        self.assertNotEqual(parent, child2)
        self.assertNotEqual(parent, child3)
        self.assertNotEqual(parent, child4)

        # Test Case 2 - Unlike instances
        self.assertNotEqual(child1, child2)
        self.assertNotEqual(child1, child3)
        self.assertNotEqual(child2, child3)
        self.assertNotEqual(child2, child4)
        self.assertNotEqual(child3, child4)

        # Test Case 3 - Like instances
        self.assertEqual(child1, child4)
        self.assertEqual(child4, child1)

        # Test Case 4 - Unlike classes
        self.assertNotEqual(child1, other)
        self.assertNotEqual(child2, other)
        self.assertNotEqual(child3, other)
        self.assertNotEqual(child4, other)

        # Test Case 5 - different eventid
        diff = Ping(ping_events.ping_different_event_id)
        self.assertEqual(child1, diff)

        # Test Case 6 - different eventidx
        diff = Ping(ping_events.ping_different_event_id_x)
        self.assertEqual(child1, diff)

        # Test Case 7 - different datetime
        diff = Ping(ping_events.ping_different_datetime)
        self.assertEqual(child1, diff)

        # Test Case 8 - different period
        diff = Ping(ping_events.ping_different_period)
        self.assertNotEqual(child1, diff)

        # Test Case 9 - different period time
        diff = Ping(ping_events.ping_different_period_time)
        self.assertEqual(child1, diff)

        # Test Case 10 - different period time remaining
        diff = Ping(ping_events.ping_different_period_time_remaining)
        self.assertNotEqual(child1, diff)

        # Test Case 11 - different shooter
        diff = Ping(ping_events.ping_different_shooter)
        self.assertNotEqual(child1, diff)

        # Test Case 12 - different goalie
        diff = Ping(ping_events.ping_different_goalie)
        self.assertNotEqual(child1, diff)

        # Test Case 13 - different goal post
        diff = Ping(ping_events.ping_different_goal_post)
        self.assertNotEqual(child1, diff)


    def test_ping_id(self):
        """
        Test the ID property for a Ping event.
        """
        parent = Event(ping_events.ping_1)
        child1 = Ping(ping_events.ping_1)
        child2 = Ping(ping_events.ping_2)
        child3 = Ping(ping_events.ping_3)
        child4 = Ping(ping_events.ping_1)
        other  = Shot(shot_events.shot_1)

        # Test Case 1 - parent to child
        self.assertNotEqual(parent.id, child1.id)
        self.assertNotEqual(parent.id, child2.id)
        self.assertNotEqual(parent.id, child3.id)
        self.assertNotEqual(parent.id, child4.id)

        # Test Case 2 - Unlike instances
        self.assertNotEqual(child1.id, child2.id)
        self.assertNotEqual(child1.id, child3.id)
        self.assertNotEqual(child2.id, child3.id)
        self.assertNotEqual(child2.id, child4.id)
        self.assertNotEqual(child3.id, child4.id)

        # Test Case 3 - Like instances
        self.assertEqual(child1.id, child4.id)
        self.assertEqual(child4.id, child1.id)

        # Test Case 4 - Unlike classes
        self.assertNotEqual(child1.id, other.id)
        self.assertNotEqual(child2.id, other.id)
        self.assertNotEqual(child3.id, other.id)
        self.assertNotEqual(child4.id, other.id)

        # Test Case 5 - different eventid
        diff = Ping(ping_events.ping_different_event_id)
        self.assertEqual(child1.id, diff.id)

        # Test Case 6 - different eventidx
        diff = Ping(ping_events.ping_different_event_id_x)
        self.assertEqual(child1.id, diff.id)

        # Test Case 7 - different datetime
        diff = Ping(ping_events.ping_different_datetime)
        self.assertEqual(child1.id, diff.id)

        # Test Case 8 - different period
        diff = Ping(ping_events.ping_different_period)
        self.assertNotEqual(child1.id, diff.id)

        # Test Case 9 - different period time
        diff = Ping(ping_events.ping_different_period_time)
        self.assertEqual(child1.id, diff.id)

        # Test Case 10 - different period time remaining
        diff = Ping(ping_events.ping_different_period_time_remaining)
        self.assertNotEqual(child1.id, diff.id)

        # Test Case 11 - different shooter
        diff = Ping(ping_events.ping_different_shooter)
        self.assertNotEqual(child1.id, diff.id)

        # Test Case 12 - different goalie
        diff = Ping(ping_events.ping_different_goalie)
        self.assertNotEqual(child1.id, diff.id)

        # Test Case 13 - different goal post
        diff = Ping(ping_events.ping_different_goal_post)
        self.assertEqual(child1.id, diff.id)


    def test_shot_equality(self):
        """
        Test the equality operator for a Shot event.
        """
        parent = Event(shot_events.shot_1)
        child1 = Shot(shot_events.shot_1)
        child2 = Shot(shot_events.shot_2)
        child3 = Shot(shot_events.shot_3)
        child4 = Shot(shot_events.shot_1)
        other  = PeriodOfficial(shot_events.shot_1)

        # Test Case 1 - parent to child
        self.assertNotEqual(parent, child1)
        self.assertNotEqual(parent, child2)
        self.assertNotEqual(parent, child3)
        self.assertNotEqual(parent, child4)

        # Test Case 2 - Unlike instances
        self.assertNotEqual(child1, child2)
        self.assertNotEqual(child1, child3)
        self.assertNotEqual(child2, child3)
        self.assertNotEqual(child2, child4)
        self.assertNotEqual(child3, child4)

        # Test Case 3 - Like instances
        self.assertEqual(child1, child4)
        self.assertEqual(child4, child1)

        # Test Case 4 - Unlike classes
        self.assertNotEqual(child1, other)
        self.assertNotEqual(child2, other)
        self.assertNotEqual(child3, other)
        self.assertNotEqual(child4, other)

        # Test Case 5 - different eventid
        diff = Shot(shot_events.shot_different_event_id)
        self.assertEqual(child1, diff)

        # Test Case 6 - different eventidx
        diff = Shot(shot_events.shot_different_event_id_x)
        self.assertEqual(child1, diff)

        # Test Case 7 - different datetime
        diff = Shot(shot_events.shot_different_datetime)
        self.assertEqual(child1, diff)

        # Test Case 8 - different period
        diff = Shot(shot_events.shot_different_period)
        self.assertNotEqual(child1, diff)

        # Test Case 9 - different period time
        diff = Shot(shot_events.shot_different_period_time)
        self.assertEqual(child1, diff)

        # Test Case 10 - different period time remaining
        diff = Shot(shot_events.shot_different_period_time_remaining)
        self.assertNotEqual(child1, diff)

        # Test Case 11 - different shooter
        diff = Shot(shot_events.shot_different_shooter)
        self.assertNotEqual(child1, diff)

        # Test Case 12 - different goalie
        diff = Shot(shot_events.shot_different_goalie)
        self.assertNotEqual(child1, diff)


    def test_shot_id(self):
        """
        Test the ID property for a Shot event.
        """
        parent = Event(shot_events.shot_1)
        child1 = Shot(shot_events.shot_1)
        child2 = Shot(shot_events.shot_2)
        child3 = Shot(shot_events.shot_3)
        child4 = Shot(shot_events.shot_1)
        other  = PeriodOfficial(shot_events.shot_1)

        # Test Case 1 - parent to child
        self.assertNotEqual(parent.id, child1.id)
        self.assertNotEqual(parent.id, child2.id)
        self.assertNotEqual(parent.id, child3.id)
        self.assertNotEqual(parent.id, child4.id)

        # Test Case 2 - Unlike instances
        self.assertNotEqual(child1.id, child2.id)
        self.assertNotEqual(child1.id, child3.id)
        self.assertNotEqual(child2.id, child3.id)
        self.assertNotEqual(child2.id, child4.id)
        self.assertNotEqual(child3.id, child4.id)

        # Test Case 3 - Like instances
        self.assertEqual(child1.id, child4.id)
        self.assertEqual(child4.id, child1.id)

        # Test Case 4 - Unlike classes
        self.assertNotEqual(child1.id, other.id)
        self.assertNotEqual(child2.id, other.id)
        self.assertNotEqual(child3.id, other.id)
        self.assertNotEqual(child4.id, other.id)

        # Test Case 5 - different eventid
        diff = Shot(shot_events.shot_different_event_id)
        self.assertEqual(child1.id, diff.id)

        # Test Case 6 - different eventidx
        diff = Shot(shot_events.shot_different_event_id_x)
        self.assertEqual(child1.id, diff.id)

        # Test Case 7 - different datetime
        diff = Shot(shot_events.shot_different_datetime)
        self.assertEqual(child1.id, diff.id)

        # Test Case 8 - different period
        diff = Shot(shot_events.shot_different_period)
        self.assertNotEqual(child1.id, diff.id)

        # Test Case 9 - different period time
        diff = Shot(shot_events.shot_different_period_time)
        self.assertEqual(child1.id, diff.id)

        # Test Case 10 - different period time remaining
        diff = Shot(shot_events.shot_different_period_time_remaining)
        self.assertNotEqual(child1.id, diff.id)

        # Test Case 11 - different shooter
        diff = Shot(shot_events.shot_different_shooter)
        self.assertNotEqual(child1.id, diff.id)

        # Test Case 12 - different goalie
        diff = Shot(shot_events.shot_different_goalie)
        self.assertNotEqual(child1.id, diff.id)


    def test_stoppage_equality(self):
        """
        Test the equality operator for a Stoppage event.
        """
        parent = Event(stoppage_events.stoppage_1)
        child1 = Stoppage(stoppage_events.stoppage_1)
        child2 = Stoppage(stoppage_events.stoppage_2)
        child3 = Stoppage(stoppage_events.stoppage_3)
        child4 = Stoppage(stoppage_events.stoppage_1)
        other  = Shot(shot_events.shot_1)

        # Test Case 1 - parent to child
        self.assertNotEqual(parent, child1)
        self.assertNotEqual(parent, child2)
        self.assertNotEqual(parent, child3)
        self.assertNotEqual(parent, child4)

        # Test Case 2 - Unlike instances
        self.assertNotEqual(child1, child2)
        self.assertNotEqual(child1, child3)
        self.assertNotEqual(child2, child3)
        self.assertNotEqual(child2, child4)
        self.assertNotEqual(child3, child4)

        # Test Case 3 - Like instances
        self.assertEqual(child1, child4)
        self.assertEqual(child4, child1)

        # Test Case 4 - Unlike classes
        self.assertNotEqual(child1, other)
        self.assertNotEqual(child2, other)
        self.assertNotEqual(child3, other)
        self.assertNotEqual(child4, other)

        # Test Case 5 - different eventid
        diff = Stoppage(stoppage_events.stoppage_different_event_id)
        self.assertEqual(child1, diff)

        # Test Case 6 - different eventidx
        diff = Stoppage(stoppage_events.stoppage_different_event_id_x)
        self.assertEqual(child1, diff)

        # Test Case 7 - different datetime
        diff = Stoppage(stoppage_events.stoppage_different_datetime)
        self.assertEqual(child1, diff)

        # Test Case 8 - different period
        diff = Stoppage(stoppage_events.stoppage_different_period)
        self.assertNotEqual(child1, diff)

        # Test Case 9 - different period time
        diff = Stoppage(stoppage_events.stoppage_different_period_time)
        self.assertEqual(child1, diff)

        # Test Case 10 - different period time remaining
        diff = Stoppage(stoppage_events.stoppage_different_period_time_remaining)
        self.assertNotEqual(child1, diff)


    def test_stoppage_id(self):
        """
        Test the ID property for a Stoppage event.
        """
        parent = Event(stoppage_events.stoppage_1)
        child1 = Stoppage(stoppage_events.stoppage_1)
        child2 = Stoppage(stoppage_events.stoppage_2)
        child3 = Stoppage(stoppage_events.stoppage_3)
        child4 = Stoppage(stoppage_events.stoppage_1)
        other  = Shot(shot_events.shot_1)

        # Test Case 1 - parent to child
        self.assertNotEqual(parent.id, child1.id)
        self.assertNotEqual(parent.id, child2.id)
        self.assertNotEqual(parent.id, child3.id)
        self.assertNotEqual(parent.id, child4.id)

        # Test Case 2 - Unlike instances
        self.assertNotEqual(child1.id, child2.id)
        self.assertNotEqual(child1.id, child3.id)
        self.assertNotEqual(child2.id, child3.id)
        self.assertNotEqual(child2.id, child4.id)
        self.assertNotEqual(child3.id, child4.id)

        # Test Case 3 - Like instances
        self.assertEqual(child1.id, child4.id)
        self.assertEqual(child4.id, child1.id)

        # Test Case 4 - Unlike classes
        self.assertNotEqual(child1.id, other.id)
        self.assertNotEqual(child2.id, other.id)
        self.assertNotEqual(child3.id, other.id)
        self.assertNotEqual(child4.id, other.id)

        # Test Case 5 - different eventid
        diff = Stoppage(stoppage_events.stoppage_different_event_id)
        self.assertEqual(child1.id, diff.id)

        # Test Case 6 - different eventidx
        diff = Stoppage(stoppage_events.stoppage_different_event_id_x)
        self.assertEqual(child1.id, diff.id)

        # Test Case 7 - different datetime
        diff = Stoppage(stoppage_events.stoppage_different_datetime)
        self.assertEqual(child1.id, diff.id)

        # Test Case 8 - different period
        diff = Stoppage(stoppage_events.stoppage_different_period)
        self.assertNotEqual(child1.id, diff.id)

        # Test Case 9 - different period time
        diff = Stoppage(stoppage_events.stoppage_different_period_time)
        self.assertEqual(child1.id, diff.id)

        # Test Case 10 - different period time remaining
        diff = Stoppage(stoppage_events.stoppage_different_period_time_remaining)
        self.assertNotEqual(child1.id, diff.id)


    def test_takeaway_equality(self):
        """
        Test the equality operator for a Takeaway event.
        """
        parent = Event(takeaway_events.takeaway_1)
        child1 = Takeaway(takeaway_events.takeaway_1)
        child2 = Takeaway(takeaway_events.takeaway_2)
        child3 = Takeaway(takeaway_events.takeaway_3)
        child4 = Takeaway(takeaway_events.takeaway_1)
        other  = Shot(shot_events.shot_1)

        # Test Case 1 - parent to child
        self.assertNotEqual(parent, child1)
        self.assertNotEqual(parent, child2)
        self.assertNotEqual(parent, child3)
        self.assertNotEqual(parent, child4)

        # Test Case 2 - Unlike instances
        self.assertNotEqual(child1, child2)
        self.assertNotEqual(child1, child3)
        self.assertNotEqual(child2, child3)
        self.assertNotEqual(child2, child4)
        self.assertNotEqual(child3, child4)

        # Test Case 3 - Like instances
        self.assertEqual(child1, child4)
        self.assertEqual(child4, child1)

        # Test Case 4 - Unlike classes
        self.assertNotEqual(child1, other)
        self.assertNotEqual(child2, other)
        self.assertNotEqual(child3, other)
        self.assertNotEqual(child4, other)

        # Test Case 5 - different eventid
        diff = Takeaway(takeaway_events.takeaway_different_event_id)
        self.assertEqual(child1, diff)

        # Test Case 6 - different eventidx
        diff = Takeaway(takeaway_events.takeaway_different_event_id_x)
        self.assertEqual(child1, diff)

        # Test Case 7 - different datetime
        diff = Takeaway(takeaway_events.takeaway_different_datetime)
        self.assertEqual(child1, diff)

        # Test Case 8 - different period
        diff = Takeaway(takeaway_events.takeaway_different_period)
        self.assertNotEqual(child1, diff)

        # Test Case 9 - different period time
        diff = Takeaway(takeaway_events.takeaway_different_period_time)
        self.assertEqual(child1, diff)

        # Test Case 10 - different period time remaining
        diff = Takeaway(takeaway_events.takeaway_different_period_time_remaining)
        self.assertNotEqual(child1, diff)

        # Test Case 11 - different player
        diff = Takeaway(takeaway_events.takeaway_different_player)
        self.assertNotEqual(child1, diff)


    def test_takeaway_id(self):
        """
        Test the ID property for a Takeaway event.
        """
        parent = Event(takeaway_events.takeaway_1)
        child1 = Takeaway(takeaway_events.takeaway_1)
        child2 = Takeaway(takeaway_events.takeaway_2)
        child3 = Takeaway(takeaway_events.takeaway_3)
        child4 = Takeaway(takeaway_events.takeaway_1)
        other  = Shot(shot_events.shot_1)

        # Test Case 1 - parent to child
        self.assertNotEqual(parent.id, child1.id)
        self.assertNotEqual(parent.id, child2.id)
        self.assertNotEqual(parent.id, child3.id)
        self.assertNotEqual(parent.id, child4.id)

        # Test Case 2 - Unlike instances
        self.assertNotEqual(child1.id, child2.id)
        self.assertNotEqual(child1.id, child3.id)
        self.assertNotEqual(child2.id, child3.id)
        self.assertNotEqual(child2.id, child4.id)
        self.assertNotEqual(child3.id, child4.id)

        # Test Case 3 - Like instances
        self.assertEqual(child1.id, child4.id)
        self.assertEqual(child4.id, child1.id)

        # Test Case 4 - Unlike classes
        self.assertNotEqual(child1, other)
        self.assertNotEqual(child2, other)
        self.assertNotEqual(child3, other)
        self.assertNotEqual(child4, other)

        # Test Case 5 - different eventid
        diff = Takeaway(takeaway_events.takeaway_different_event_id)
        self.assertEqual(child1.id, diff.id)

        # Test Case 6 - different eventidx
        diff = Takeaway(takeaway_events.takeaway_different_event_id_x)
        self.assertEqual(child1.id, diff.id)

        # Test Case 7 - different datetime
        diff = Takeaway(takeaway_events.takeaway_different_datetime)
        self.assertEqual(child1.id, diff.id)

        # Test Case 8 - different period
        diff = Takeaway(takeaway_events.takeaway_different_period)
        self.assertNotEqual(child1.id, diff.id)

        # Test Case 9 - different period time
        diff = Takeaway(takeaway_events.takeaway_different_period_time)
        self.assertEqual(child1.id, diff.id)

        # Test Case 10 - different period time remaining
        diff = Takeaway(takeaway_events.takeaway_different_period_time_remaining)
        self.assertNotEqual(child1.id, diff.id)

        # Test Case 11 - different player
        diff = Takeaway(takeaway_events.takeaway_different_player)
        self.assertNotEqual(child1.id, diff.id)
