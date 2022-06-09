"""
TODO
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
from test.test_data import shot_events

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
from src.events.shot import Shot

class TestEquality(unittest.TestCase):
    """
    Description:
        Unit tests for the generator class.
    """

    def test_blocked_shot_equality(self):
        """Test the equality operator for a BlockedShot event."""
        parent = Event(blocked_shot_events.blocked_shot_1)
        child1 = BlockedShot(blocked_shot_events.blocked_shot_1)
        child2 = BlockedShot(blocked_shot_events.blocked_shot_2)
        child3 = BlockedShot(blocked_shot_events.blocked_shot_3)
        child4 = BlockedShot(blocked_shot_events.blocked_shot_1)
        other  = Shot(shot_events.shot_event_1)

        # Test Case 1 - parent is not equivalent to child
        self.assertNotEqual(parent, child1)
        self.assertNotEqual(parent, child2)
        self.assertNotEqual(parent, child3)
        self.assertNotEqual(parent, child4)

        # Test Case 2 - Unlike instances are not equivalent
        self.assertNotEqual(child1, child2)
        self.assertNotEqual(child1, child3)
        self.assertNotEqual(child2, child3)
        self.assertNotEqual(child2, child4)
        self.assertNotEqual(child3, child4)

        # Test Case 3 - Like instances are equivalent
        self.assertEqual(child1, child4)
        self.assertEqual(child4, child1)

        # Test Case 4 - Unlike classes are not equivalent
        self.assertNotEqual(child1, other)
        self.assertNotEqual(child2, other)
        self.assertNotEqual(child3, other)
        self.assertNotEqual(child4, other)

        # Test Case 5 - different eventid is still equivalent
        diff = BlockedShot(blocked_shot_events.blocked_shot_different_event_id)
        self.assertEqual(child1, diff)

        # Test Case 6 - different eventidx is still equivalent
        diff = BlockedShot(blocked_shot_events.blocked_shot_different_event_id_x)
        self.assertEqual(child1, diff)

        # Test Case 7 - different datetime is still equivalent
        diff = BlockedShot(blocked_shot_events.blocked_shot_different_datetime)
        self.assertEqual(child1, diff)

        # Test Case 8 - different period is not equivalent
        diff = BlockedShot(blocked_shot_events.blocked_shot_different_period)
        self.assertNotEqual(child1, diff)

        # Test Case 9 - different periodtime is still equivalent
        diff = BlockedShot(blocked_shot_events.blocked_shot_different_period_time)
        self.assertEqual(child1, diff)

        # Test Case 10 - different periodtime_remaining is not equivalent
        diff = BlockedShot(blocked_shot_events.blocked_shot_different_period_time_remaining)
        self.assertNotEqual(child1, diff)

        # Test Case 11 - different shooter is not equivalent
        diff = BlockedShot(blocked_shot_events.blocked_shot_different_shooter)
        self.assertNotEqual(child1, diff)

        # Test Case 12 - different blocker is not equivalent
        diff = BlockedShot(blocked_shot_events.blocked_shot_different_blocker)
        self.assertNotEqual(child1, diff)


    def test_blocked_shot_id(self):
        """Test the ID property for a BlockedShot event."""
        parent = Event(blocked_shot_events.blocked_shot_1)
        child1 = BlockedShot(blocked_shot_events.blocked_shot_1)
        child2 = BlockedShot(blocked_shot_events.blocked_shot_2)
        child3 = BlockedShot(blocked_shot_events.blocked_shot_3)
        child4 = BlockedShot(blocked_shot_events.blocked_shot_1)
        other  = Shot(shot_events.shot_event_1)

        # Test Case 1 - parent is not equivalent to child
        self.assertNotEqual(parent.id, child1.id)
        self.assertNotEqual(parent.id, child2.id)
        self.assertNotEqual(parent.id, child3.id)
        self.assertNotEqual(parent.id, child4.id)

        # Test Case 2 - Unlike instances are not equivalent
        self.assertNotEqual(child1.id, child2.id)
        self.assertNotEqual(child1.id, child3.id)
        self.assertNotEqual(child2.id, child3.id)
        self.assertNotEqual(child2.id, child4.id)
        self.assertNotEqual(child3.id, child4.id)

        # Test Case 3 - Like instances are equivalent
        self.assertEqual(child1.id, child4.id)
        self.assertEqual(child4.id, child1.id)

        # Test Case 4 - Unlike classes are not equivalent
        self.assertNotEqual(child1.id, other.id)
        self.assertNotEqual(child2.id, other.id)
        self.assertNotEqual(child3.id, other.id)
        self.assertNotEqual(child4.id, other.id)

        # Test Case 5 - different eventid is still equivalent
        diff = BlockedShot(blocked_shot_events.blocked_shot_different_event_id)
        self.assertEqual(child1.id, diff.id)

        # Test Case 6 - different eventidx is still equivalent
        diff = BlockedShot(blocked_shot_events.blocked_shot_different_event_id_x)
        self.assertEqual(child1.id, diff.id)

        # Test Case 7 - different datetime is not equivalent
        diff = BlockedShot(blocked_shot_events.blocked_shot_different_datetime)
        self.assertNotEqual(child1.id, diff.id)

        # Test Case 8 - different period is still equivalent
        diff = BlockedShot(blocked_shot_events.blocked_shot_different_period)
        self.assertEqual(child1.id, diff.id)

        # Test Case 9 - different periodtime is still equivalent
        diff = BlockedShot(blocked_shot_events.blocked_shot_different_period_time)
        self.assertEqual(child1.id, diff.id)

        # Test Case 10 - different periodtime_remaining is still equivalent
        diff = BlockedShot(blocked_shot_events.blocked_shot_different_period_time_remaining)
        self.assertEqual(child1.id, diff.id)

        # Test Case 11 - different shooter is still equivalent
        diff = BlockedShot(blocked_shot_events.blocked_shot_different_shooter)
        self.assertEqual(child1.id, diff.id)

        # Test Case 12 - different blocker is still equivalent
        diff = BlockedShot(blocked_shot_events.blocked_shot_different_blocker)
        self.assertEqual(child1.id, diff.id)


    def test_challenge_equality(self):
        """Test the equality operator for a Challenge event."""
        parent = Event(challenge_events.challenge_1)
        child1 = Challenge(challenge_events.challenge_1)
        child2 = Challenge(challenge_events.challenge_2)
        child3 = Challenge(challenge_events.challenge_1)
        other  = Shot(shot_events.shot_event_1)

        # Test Case 1 - parent is not equivalent to child
        self.assertNotEqual(parent, child1)
        self.assertNotEqual(parent, child2)

        # Test Case 2 - Unlike instances are not equivalent
        self.assertNotEqual(child1, child2)

        # Test Case 3 - Like instances are equivalent
        self.assertEqual(child1, child3)
        self.assertEqual(child3, child1)

        # Test Case 4 - Unlike classes are not equivalent
        self.assertNotEqual(child1, other)
        self.assertNotEqual(child2, other)
        self.assertNotEqual(child3, other)

        # Test Case 5 - different eventid is still equivalent
        diff = Challenge(challenge_events.challenge_different_event_id)
        self.assertEqual(child1, diff)

        # Test Case 6 - different eventidx is still equivalent
        diff = Challenge(challenge_events.challenge_different_event_id_x)
        self.assertEqual(child1, diff)

        # Test Case 7 - different datetime is still equivalent
        diff = Challenge(challenge_events.challenge_different_datetime)
        self.assertEqual(child1, diff)

        # Test Case 8 - different period is not equivalent
        diff = Challenge(challenge_events.challenge_different_period)
        self.assertNotEqual(child1, diff)

        # Test Case 9 - different periodtime is still equivalent
        diff = Challenge(challenge_events.challenge_different_period_time)
        self.assertEqual(child1, diff)

        # Test Case 10 - different periodtime_remaining is not equivalent
        diff = Challenge(challenge_events.challenge_different_period_time_remaining)
        self.assertNotEqual(child1, diff)


    def test_challenge_id(self):
        """Test the ID property for a Challenge event."""
        parent = Event(challenge_events.challenge_1)
        child1 = Challenge(challenge_events.challenge_1)
        child2 = Challenge(challenge_events.challenge_2)
        child3 = Challenge(challenge_events.challenge_1)
        other  = Shot(shot_events.shot_event_1)

        # Test Case 1 - parent is not equivalent to child
        self.assertNotEqual(parent.id, child1.id)
        self.assertNotEqual(parent.id, child2.id)

        # Test Case 2 - Unlike instances are not equivalent
        self.assertNotEqual(child1.id, child2.id)

        # Test Case 3 - Like instances are equivalent
        self.assertEqual(child1.id, child3.id)
        self.assertEqual(child3.id, child1.id)

        # Test Case 4 - Unlike classes are not equivalent
        self.assertNotEqual(child1.id, other.id)
        self.assertNotEqual(child2.id, other.id)
        self.assertNotEqual(child3.id, other.id)

        # Test Case 5 - different eventid is still equivalent
        diff = Challenge(challenge_events.challenge_different_event_id)
        self.assertEqual(child1.id, diff.id)

        # Test Case 6 - different eventidx is still equivalent
        diff = Challenge(challenge_events.challenge_different_event_id_x)
        self.assertEqual(child1.id, diff.id)

        # Test Case 7 - different datetime is not equivalent
        diff = Challenge(challenge_events.challenge_different_datetime)
        self.assertNotEqual(child1.id, diff.id)

        # Test Case 8 - different period is still equivalent
        diff = Challenge(challenge_events.challenge_different_period)
        self.assertEqual(child1.id, diff.id)

        # Test Case 9 - different periodtime is still equivalent
        diff = Challenge(challenge_events.challenge_different_period_time)
        self.assertEqual(child1.id, diff.id)

        # Test Case 10 - different periodtime_remaining is still equivalent
        diff = Challenge(challenge_events.challenge_different_period_time_remaining)
        self.assertEqual(child1.id, diff.id)


    def test_faceoff_equality(self):
        """Test the equality operator for a Faceoff event."""
        parent = Event(faceoff_events.faceoff_1)
        child1 = Faceoff(faceoff_events.faceoff_1)
        child2 = Faceoff(faceoff_events.faceoff_2)
        child3 = Faceoff(faceoff_events.faceoff_3)
        child4 = Faceoff(faceoff_events.faceoff_1)
        other  = Shot(shot_events.shot_event_1)

        # Test Case 1 - parent is not equivalent to child
        self.assertNotEqual(parent, child1)
        self.assertNotEqual(parent, child2)
        self.assertNotEqual(parent, child3)
        self.assertNotEqual(parent, child4)

        # Test Case 2 - Unlike instances are not equivalent
        self.assertNotEqual(child1, child2)
        self.assertNotEqual(child1, child3)
        self.assertNotEqual(child2, child3)
        self.assertNotEqual(child2, child4)
        self.assertNotEqual(child3, child4)

        # Test Case 3 - Like instances are equivalent
        self.assertEqual(child1, child4)
        self.assertEqual(child4, child1)

        # Test Case 4 - Unlike classes are not equivalent
        self.assertNotEqual(child1, other)
        self.assertNotEqual(child2, other)
        self.assertNotEqual(child3, other)
        self.assertNotEqual(child4, other)

        # Test Case 5 - different eventid is still equivalent
        diff = Faceoff(faceoff_events.faceoff_different_event_id)
        self.assertEqual(child1, diff)

        # Test Case 6 - different eventidx is still equivalent
        diff = Faceoff(faceoff_events.faceoff_different_event_id_x)
        self.assertEqual(child1, diff)

        # Test Case 7 - different datetime is still equivalent
        diff = Faceoff(faceoff_events.faceoff_different_datetime)
        self.assertEqual(child1, diff)

        # Test Case 8 - different period is not equivalent
        diff = Faceoff(faceoff_events.faceoff_different_period)
        self.assertNotEqual(child1, diff)

        # Test Case 9 - different periodtime is still equivalent
        diff = Faceoff(faceoff_events.faceoff_different_period_time)
        self.assertEqual(child1, diff)

        # Test Case 10 - different periodtime_remaining is not equivalent
        diff = Faceoff(faceoff_events.faceoff_different_period_time_remaining)
        self.assertNotEqual(child1, diff)

        # Test Case 11 - different winner is not equivalent
        diff = Faceoff(faceoff_events.faceoff_different_winner)
        self.assertNotEqual(child1, diff)

        # Test Case 12 - different loser is not equivalent
        diff = Faceoff(faceoff_events.faceoff_different_loser)
        self.assertNotEqual(child1, diff)


    def test_faceoff_id(self):
        """Test the ID property for a Faceoff event."""
        parent = Event(faceoff_events.faceoff_1)
        child1 = Faceoff(faceoff_events.faceoff_1)
        child2 = Faceoff(faceoff_events.faceoff_2)
        child3 = Faceoff(faceoff_events.faceoff_3)
        child4 = Faceoff(faceoff_events.faceoff_1)
        other  = Shot(shot_events.shot_event_1)

        # Test Case 1 - parent is not equivalent to child
        self.assertNotEqual(parent.id, child1.id)
        self.assertNotEqual(parent.id, child2.id)
        self.assertNotEqual(parent.id, child3.id)
        self.assertNotEqual(parent.id, child4.id)

        # Test Case 2 - Unlike instances are not equivalent
        self.assertNotEqual(child1.id, child2.id)
        self.assertNotEqual(child1.id, child3.id)
        self.assertNotEqual(child2.id, child3.id)
        self.assertNotEqual(child2.id, child4.id)
        self.assertNotEqual(child3.id, child4.id)

        # Test Case 3 - Like instances are equivalent
        self.assertEqual(child1.id, child4.id)
        self.assertEqual(child4.id, child1.id)

        # Test Case 4 - Unlike classes are not equivalent
        self.assertNotEqual(child1.id, other.id)
        self.assertNotEqual(child2.id, other.id)
        self.assertNotEqual(child3.id, other.id)
        self.assertNotEqual(child4.id, other.id)

        # Test Case 5 - different eventid is still equivalent
        diff = Faceoff(faceoff_events.faceoff_different_event_id)
        self.assertEqual(child1.id, diff.id)

        # Test Case 6 - different eventidx is still equivalent
        diff = Faceoff(faceoff_events.faceoff_different_event_id_x)
        self.assertEqual(child1.id, diff.id)

        # Test Case 7 - different datetime is not equivalent
        diff = Faceoff(faceoff_events.faceoff_different_datetime)
        self.assertNotEqual(child1.id, diff.id)

        # Test Case 8 - different period is still equivalent
        diff = Faceoff(faceoff_events.faceoff_different_period)
        self.assertEqual(child1.id, diff.id)

        # Test Case 9 - different periodtime is still equivalent
        diff = Faceoff(faceoff_events.faceoff_different_period_time)
        self.assertEqual(child1.id, diff.id)

        # Test Case 10 - different periodtime_remaining is still equivalent
        diff = Faceoff(faceoff_events.faceoff_different_period_time_remaining)
        self.assertEqual(child1.id, diff.id)

        # Test Case 11 - different winner is still equivalent
        diff = Faceoff(faceoff_events.faceoff_different_winner)
        self.assertEqual(child1.id, diff.id)

        # Test Case 12 - different loser is still equivalent
        diff = Faceoff(faceoff_events.faceoff_different_loser)
        self.assertEqual(child1.id, diff.id)


    def test_game_end_equality(self):
        """Test the equality operator for a GameEnd event."""
        parent = Event(faceoff_events.faceoff_1)
        child1 = GameEnd(game_end_events.game_end_1)
        child2 = GameEnd(game_end_events.game_end_2)
        child3 = GameEnd(game_end_events.game_end_1)
        other  = Shot(shot_events.shot_event_1)

        # Test Case 1 - parent is not equivalent to child
        self.assertNotEqual(parent, child1)
        self.assertNotEqual(parent, child2)
        self.assertNotEqual(parent, child3)

        # Test Case 2 - Unlike instances are equivalent
        self.assertEqual(child1, child2)
        self.assertEqual(child2, child3)

        # Test Case 3 - Like instances are equivalent
        self.assertEqual(child1, child3)
        self.assertEqual(child3, child1)

        # Test Case 4 - Unlike classes are not equivalent
        self.assertNotEqual(child1, other)
        self.assertNotEqual(child2, other)
        self.assertNotEqual(child3, other)

        # Test Case 5 - different eventid is still equivalent
        diff = GameEnd(game_end_events.game_end_different_event_id)
        self.assertEqual(child1, diff)

        # Test Case 6 - different eventidx is still equivalent
        diff = GameEnd(game_end_events.game_end_different_event_id_x)
        self.assertEqual(child1, diff)

        # Test Case 7 - different datetime is still equivalent
        diff = GameEnd(game_end_events.game_end_different_datetime)
        self.assertEqual(child1, diff)

        # Test Case 8 - different period is still equivalent
        diff = GameEnd(game_end_events.game_end_different_period)
        self.assertEqual(child1, diff)

        # Test Case 9 - different periodtime is still equivalent
        diff = GameEnd(game_end_events.game_end_different_period_time)
        self.assertEqual(child1, diff)

        # Test Case 10 - different periodtime_remaining is still equivalent
        diff = GameEnd(game_end_events.game_end_different_period_time_remaining)
        self.assertEqual(child1, diff)


    def test_game_end_id(self):
        """Test the ID property for a GameEnd event."""

        parent = Event(faceoff_events.faceoff_1)
        child1 = GameEnd(game_end_events.game_end_1)
        child2 = GameEnd(game_end_events.game_end_2)
        child3 = GameEnd(game_end_events.game_end_1)
        other  = Shot(shot_events.shot_event_1)

        # Test Case 1 - parent is not equivalent to child
        self.assertNotEqual(parent.id, child1.id)
        self.assertNotEqual(parent.id, child2.id)
        self.assertNotEqual(parent.id, child3.id)

        # Test Case 2 - Unlike instances are not equivalent
        self.assertNotEqual(child1.id, child2.id)
        self.assertNotEqual(child2.id, child3.id)

        # Test Case 3 - Like instances are equivalent
        self.assertEqual(child1.id, child3.id)
        self.assertEqual(child3.id, child1.id)

        # Test Case 4 - Unlike classes are not equivalent
        self.assertNotEqual(child1.id, other.id)
        self.assertNotEqual(child2.id, other.id)
        self.assertNotEqual(child3.id, other.id)

        # Test Case 5 - different eventid is still equivalent
        diff = GameEnd(game_end_events.game_end_different_event_id)
        self.assertEqual(child1.id, diff.id)

        # Test Case 6 - different eventidx is still equivalent
        diff = GameEnd(game_end_events.game_end_different_event_id_x)
        self.assertEqual(child1.id, diff.id)

        # Test Case 7 - different datetime is still equivalent
        diff = GameEnd(game_end_events.game_end_different_datetime)
        self.assertNotEqual(child1.id, diff.id)

        # Test Case 8 - different period is still equivalent
        diff = GameEnd(game_end_events.game_end_different_period)
        self.assertEqual(child1.id, diff.id)

        # Test Case 9 - different periodtime is still equivalent
        diff = GameEnd(game_end_events.game_end_different_period_time)
        self.assertEqual(child1.id, diff.id)

        # Test Case 10 - different periodtime_remaining is still equivalent
        diff = GameEnd(game_end_events.game_end_different_period_time_remaining)
        self.assertEqual(child1.id, diff.id)


    def test_game_official_equality(self):
        """Test the equality operator for a GameOfficial event."""
        parent = Event(faceoff_events.faceoff_1)
        child1 = GameOfficial(game_official_events.game_official_1)
        child2 = GameOfficial(game_official_events.game_official_2)
        child3 = GameOfficial(game_official_events.game_official_1)
        other  = Shot(shot_events.shot_event_1)

        # Test Case 1 - parent is not equivalent to child
        self.assertNotEqual(parent, child1)
        self.assertNotEqual(parent, child2)
        self.assertNotEqual(parent, child3)

        # Test Case 2 - Unlike instances are equivalent
        self.assertEqual(child1, child2)
        self.assertEqual(child2, child3)

        # Test Case 3 - Like instances are equivalent
        self.assertEqual(child1, child3)
        self.assertEqual(child3, child1)

        # Test Case 4 - Unlike classes are not equivalent
        self.assertNotEqual(child1, other)
        self.assertNotEqual(child2, other)
        self.assertNotEqual(child3, other)

        # Test Case 5 - different eventid is still equivalent
        diff = GameOfficial(game_official_events.game_official_different_event_id)
        self.assertEqual(child1, diff)

        # Test Case 6 - different eventidx is still equivalent
        diff = GameOfficial(game_official_events.game_official_different_event_id_x)
        self.assertEqual(child1, diff)

        # Test Case 7 - different datetime is still equivalent
        diff = GameOfficial(game_official_events.game_official_different_datetime)
        self.assertEqual(child1, diff)

        # Test Case 8 - different period is still equivalent
        diff = GameOfficial(game_official_events.game_official_different_period)
        self.assertEqual(child1, diff)

        # Test Case 9 - different periodtime is still equivalent
        diff = GameOfficial(game_official_events.game_official_different_period_time)
        self.assertEqual(child1, diff)

        # Test Case 10 - different periodtime_remaining is still equivalent
        diff = GameOfficial(game_official_events.game_official_different_period_time_remaining)
        self.assertEqual(child1, diff)


    def test_game_official_id(self):
        """Test the ID property for a GameOfficial event."""

        parent = Event(faceoff_events.faceoff_1)
        child1 = GameOfficial(game_official_events.game_official_1)
        child2 = GameOfficial(game_official_events.game_official_2)
        child3 = GameOfficial(game_official_events.game_official_1)
        other  = Shot(shot_events.shot_event_1)

        # Test Case 1 - parent is not equivalent to child
        self.assertNotEqual(parent.id, child1.id)
        self.assertNotEqual(parent.id, child2.id)
        self.assertNotEqual(parent.id, child3.id)

        # Test Case 2 - Unlike instances are not equivalent
        self.assertNotEqual(child1.id, child2.id)
        self.assertNotEqual(child2.id, child3.id)

        # Test Case 3 - Like instances are equivalent
        self.assertEqual(child1.id, child3.id)
        self.assertEqual(child3.id, child1.id)

        # Test Case 4 - Unlike classes are not equivalent
        self.assertNotEqual(child1.id, other.id)
        self.assertNotEqual(child2.id, other.id)
        self.assertNotEqual(child3.id, other.id)

        # Test Case 5 - different eventid is still equivalent
        diff = GameOfficial(game_official_events.game_official_different_event_id)
        self.assertEqual(child1.id, diff.id)

        # Test Case 6 - different eventidx is still equivalent
        diff = GameOfficial(game_official_events.game_official_different_event_id_x)
        self.assertEqual(child1.id, diff.id)

        # Test Case 7 - different datetime is not equivalent
        diff = GameOfficial(game_official_events.game_official_different_datetime)
        self.assertNotEqual(child1.id, diff.id)

        # Test Case 8 - different period is still equivalent
        diff = GameOfficial(game_official_events.game_official_different_period)
        self.assertEqual(child1.id, diff.id)

        # Test Case 9 - different periodtime is still equivalent
        diff = GameOfficial(game_official_events.game_official_different_period_time)
        self.assertEqual(child1.id, diff.id)

        # Test Case 10 - different periodtime_remaining is still equivalent
        diff = GameOfficial(game_official_events.game_official_different_period_time_remaining)
        self.assertEqual(child1.id, diff.id)


    def test_game_scheduled_equality(self):
        """Test the equality operator for a GameScheduled event."""
        parent = Event(faceoff_events.faceoff_1)
        child1 = GameScheduled(game_scheduled_events.game_scheduled_1)
        child2 = GameScheduled(game_scheduled_events.game_scheduled_2)
        child3 = GameScheduled(game_scheduled_events.game_scheduled_1)
        other  = Shot(shot_events.shot_event_1)

        # Test Case 1 - parent is not equivalent to child
        self.assertNotEqual(parent, child1)
        self.assertNotEqual(parent, child2)
        self.assertNotEqual(parent, child3)

        # Test Case 2 - Unlike instances are equivalent
        self.assertEqual(child1, child2)
        self.assertEqual(child2, child3)

        # Test Case 3 - Like instances are equivalent
        self.assertEqual(child1, child3)
        self.assertEqual(child3, child1)

        # Test Case 4 - Unlike classes are not equivalent
        self.assertNotEqual(child1, other)
        self.assertNotEqual(child2, other)
        self.assertNotEqual(child3, other)

        # Test Case 5 - different eventid is still equivalent
        diff = GameScheduled(game_scheduled_events.game_scheduled_different_event_id)
        self.assertEqual(child1, diff)

        # Test Case 6 - different eventidx is still equivalent
        diff = GameScheduled(game_scheduled_events.game_scheduled_different_event_id_x)
        self.assertEqual(child1, diff)

        # Test Case 7 - different datetime is still equivalent
        diff = GameScheduled(game_scheduled_events.game_scheduled_different_datetime)
        self.assertEqual(child1, diff)

        # Test Case 8 - different period is still equivalent
        diff = GameScheduled(game_scheduled_events.game_scheduled_different_period)
        self.assertEqual(child1, diff)

        # Test Case 9 - different periodtime is still equivalent
        diff = GameScheduled(game_scheduled_events.game_scheduled_different_period_time)
        self.assertEqual(child1, diff)

        # Test Case 10 - different periodtime_remaining is still equivalent
        diff = GameScheduled(game_scheduled_events.game_scheduled_different_period_time_remaining)
        self.assertEqual(child1, diff)


    def test_game_scheduled_id(self):
        """Test the ID property for a GameOfficial event."""

        parent = Event(faceoff_events.faceoff_1)
        child1 = GameScheduled(game_scheduled_events.game_scheduled_1)
        child2 = GameScheduled(game_scheduled_events.game_scheduled_2)
        child3 = GameScheduled(game_scheduled_events.game_scheduled_1)
        other  = Shot(shot_events.shot_event_1)

        # Test Case 1 - parent is not equivalent to child
        self.assertNotEqual(parent.id, child1.id)
        self.assertNotEqual(parent.id, child2.id)
        self.assertNotEqual(parent.id, child3.id)

        # Test Case 2 - Unlike instances are not equivalent
        self.assertNotEqual(child1.id, child2.id)
        self.assertNotEqual(child2.id, child3.id)

        # Test Case 3 - Like instances are equivalent
        self.assertEqual(child1.id, child3.id)
        self.assertEqual(child3.id, child1.id)

        # Test Case 4 - Unlike classes are not equivalent
        self.assertNotEqual(child1.id, other.id)
        self.assertNotEqual(child2.id, other.id)
        self.assertNotEqual(child3.id, other.id)

        # Test Case 5 - different eventid is still equivalent
        diff = GameScheduled(game_scheduled_events.game_scheduled_different_event_id)
        self.assertEqual(child1.id, diff.id)

        # Test Case 6 - different eventidx is still equivalent
        diff = GameScheduled(game_scheduled_events.game_scheduled_different_event_id_x)
        self.assertEqual(child1.id, diff.id)

        # Test Case 7 - different datetime is not equivalent
        diff = GameScheduled(game_scheduled_events.game_scheduled_different_datetime)
        self.assertNotEqual(child1.id, diff.id)

        # Test Case 8 - different period is still equivalent
        diff = GameScheduled(game_scheduled_events.game_scheduled_different_period)
        self.assertEqual(child1.id, diff.id)

        # Test Case 9 - different periodtime is still equivalent
        diff = GameScheduled(game_scheduled_events.game_scheduled_different_period_time)
        self.assertEqual(child1.id, diff.id)

        # Test Case 10 - different periodtime_remaining is still equivalent
        diff = GameScheduled(game_scheduled_events.game_scheduled_different_period_time_remaining)
        self.assertEqual(child1.id, diff.id)


    def test_giveaway_equality(self):
        """Test the equality operator for a Giveaway event."""
        parent = Event(giveaway_events.giveaway_1)
        child1 = Giveaway(giveaway_events.giveaway_1)
        child2 = Giveaway(giveaway_events.giveaway_2)
        child3 = Giveaway(giveaway_events.giveaway_3)
        child4 = Giveaway(giveaway_events.giveaway_1)
        other  = Shot(shot_events.shot_event_1)

        # Test Case 1 - parent is not equivalent to child
        self.assertNotEqual(parent, child1)
        self.assertNotEqual(parent, child2)
        self.assertNotEqual(parent, child3)
        self.assertNotEqual(parent, child4)

        # Test Case 2 - Unlike instances are not equivalent
        self.assertNotEqual(child1, child2)
        self.assertNotEqual(child1, child3)
        self.assertNotEqual(child2, child3)
        self.assertNotEqual(child2, child4)
        self.assertNotEqual(child3, child4)

        # Test Case 3 - Like instances are equivalent
        self.assertEqual(child1, child4)
        self.assertEqual(child4, child1)

        # Test Case 4 - Unlike classes are not equivalent
        self.assertNotEqual(child1, other)
        self.assertNotEqual(child2, other)
        self.assertNotEqual(child3, other)
        self.assertNotEqual(child4, other)

        # Test Case 5 - different eventid is still equivalent
        diff = Giveaway(giveaway_events.giveaway_different_event_id)
        self.assertEqual(child1, diff)

        # Test Case 6 - different eventidx is still equivalent
        diff = Giveaway(giveaway_events.giveaway_different_event_id_x)
        self.assertEqual(child1, diff)

        # Test Case 7 - different datetime is still equivalent
        diff = Giveaway(giveaway_events.giveaway_different_datetime)
        self.assertEqual(child1, diff)

        # Test Case 8 - different period is not equivalent
        diff = Giveaway(giveaway_events.giveaway_different_period)
        self.assertNotEqual(child1, diff)

        # Test Case 9 - different periodtime is still equivalent
        diff = Giveaway(giveaway_events.giveaway_different_period_time)
        self.assertEqual(child1, diff)

        # Test Case 10 - different periodtime_remaining is not equivalent
        diff = Giveaway(giveaway_events.giveaway_different_period_time_remaining)
        self.assertNotEqual(child1, diff)

        # Test Case 11 - different player is not equivalent
        diff = Giveaway(giveaway_events.giveaway_different_player)
        self.assertNotEqual(child1, diff)


    def test_giveaway_id(self):
        """Test the ID property for a Giveaway event."""
        parent = Event(giveaway_events.giveaway_1)
        child1 = Giveaway(giveaway_events.giveaway_1)
        child2 = Giveaway(giveaway_events.giveaway_2)
        child3 = Giveaway(giveaway_events.giveaway_3)
        child4 = Giveaway(giveaway_events.giveaway_1)
        other  = Shot(shot_events.shot_event_1)

        # Test Case 1 - parent is not equivalent to child
        self.assertNotEqual(parent.id, child1.id)
        self.assertNotEqual(parent.id, child2.id)
        self.assertNotEqual(parent.id, child3.id)
        self.assertNotEqual(parent.id, child4.id)

        # Test Case 2 - Unlike instances are not equivalent
        self.assertNotEqual(child1.id, child2.id)
        self.assertNotEqual(child1.id, child3.id)
        self.assertNotEqual(child2.id, child3.id)
        self.assertNotEqual(child2.id, child4.id)
        self.assertNotEqual(child3.id, child4.id)

        # Test Case 3 - Like instances are equivalent
        self.assertEqual(child1.id, child4.id)
        self.assertEqual(child4.id, child1.id)

        # Test Case 4 - Unlike classes are not equivalent
        self.assertNotEqual(child1.id, other.id)
        self.assertNotEqual(child2.id, other.id)
        self.assertNotEqual(child3.id, other.id)
        self.assertNotEqual(child4.id, other.id)

        # Test Case 5 - different eventid is still equivalent
        diff = Giveaway(giveaway_events.giveaway_different_event_id)
        self.assertEqual(child1.id, diff.id)

        # Test Case 6 - different eventidx is still equivalent
        diff = Giveaway(giveaway_events.giveaway_different_event_id_x)
        self.assertEqual(child1.id, diff.id)

        # Test Case 7 - different datetime is not equivalent
        diff = Giveaway(giveaway_events.giveaway_different_datetime)
        self.assertNotEqual(child1.id, diff.id)

        # Test Case 8 - different period is still equivalent
        diff = Giveaway(giveaway_events.giveaway_different_period)
        self.assertEqual(child1.id, diff.id)

        # Test Case 9 - different periodtime is still equivalent
        diff = Giveaway(giveaway_events.giveaway_different_period_time)
        self.assertEqual(child1.id, diff.id)

        # Test Case 10 - different periodtime_remaining is still equivalent
        diff = Giveaway(giveaway_events.giveaway_different_period_time_remaining)
        self.assertEqual(child1.id, diff.id)

        # Test Case 11 - different player is still equivalent
        diff = Giveaway(giveaway_events.giveaway_different_player)
        self.assertEqual(child1.id, diff.id)


    def test_goal_equality(self):
        """Test the equality operator for a Goal event."""
        parent = Event(giveaway_events.giveaway_1)
        child1 = Goal(goal_events.goal_1)
        child2 = Goal(goal_events.goal_2)
        child3 = Goal(goal_events.goal_3)
        child4 = Goal(goal_events.goal_1)
        other  = Shot(shot_events.shot_event_1)

        # Test Case 1 - parent is not equivalent to child
        self.assertNotEqual(parent, child1)
        self.assertNotEqual(parent, child2)
        self.assertNotEqual(parent, child3)
        self.assertNotEqual(parent, child4)

        # Test Case 2 - Unlike instances are not equivalent
        self.assertNotEqual(child1, child2)
        self.assertNotEqual(child1, child3)
        self.assertNotEqual(child2, child3)
        self.assertNotEqual(child2, child4)
        self.assertNotEqual(child3, child4)

        # Test Case 3 - Like instances are equivalent
        self.assertEqual(child1, child4)
        self.assertEqual(child4, child1)

        # Test Case 4 - Unlike classes are not equivalent
        self.assertNotEqual(child1, other)
        self.assertNotEqual(child2, other)
        self.assertNotEqual(child3, other)
        self.assertNotEqual(child4, other)

        # Test Case 5 - different eventid is still equivalent
        diff = Goal(goal_events.goal_different_event_id)
        self.assertEqual(child1, diff)

        # Test Case 6 - different eventidx is still equivalent
        diff = Goal(goal_events.goal_different_event_id_x)
        self.assertEqual(child1, diff)

        # Test Case 7 - different datetime is still equivalent
        diff = Goal(goal_events.goal_different_datetime)
        self.assertEqual(child1, diff)

        # Test Case 8 - different period is not equivalent
        diff = Goal(goal_events.goal_different_period)
        self.assertNotEqual(child1, diff)

        # Test Case 9 - different periodtime is still equivalent
        diff = Goal(goal_events.goal_different_period_time)
        self.assertEqual(child1, diff)

        # Test Case 10 - different periodtime_remaining is not equivalent
        diff = Goal(goal_events.goal_different_period_time_remaining)
        self.assertNotEqual(child1, diff)

        # Test Case 11 - different scorer is not equivalent
        diff = Goal(goal_events.goal_different_scorer)
        self.assertNotEqual(child1, diff)

        # Test Case 12 - different primary assist is not equivalent
        diff = Goal(goal_events.goal_different_primary_assist)
        self.assertNotEqual(child1, diff)

        # Test Case 13 - different secondary assist is not equivalent
        diff = Goal(goal_events.goal_different_secondary_assist)
        self.assertNotEqual(child1, diff)

        # Test Case 14 - different goalie is not equivalent
        diff = Goal(goal_events.goal_different_goalie)
        self.assertNotEqual(child1, diff)

        # Test Case 15 - different strength is not equivalent
        diff = Goal(goal_events.goal_different_strength)
        self.assertNotEqual(child1, diff)

        # Test Case 16 - different empty net is not equivalent
        diff = Goal(goal_events.goal_different_empty_net)
        self.assertNotEqual(child1, diff)

        # Test Case 17 - different team is not equivalent
        diff = Goal(goal_events.goal_different_team)
        self.assertNotEqual(child1, diff)


    def test_goal_id(self):
        """Test the ID property for a Goal event."""
        parent = Event(giveaway_events.giveaway_1)
        child1 = Goal(goal_events.goal_1)
        child2 = Goal(goal_events.goal_2)
        child3 = Goal(goal_events.goal_3)
        child4 = Goal(goal_events.goal_1)
        other  = Shot(shot_events.shot_event_1)

        # Test Case 1 - parent is not equivalent to child
        self.assertNotEqual(parent.id, child1.id)
        self.assertNotEqual(parent.id, child2.id)
        self.assertNotEqual(parent.id, child3.id)
        self.assertNotEqual(parent.id, child4.id)

        # Test Case 2 - Unlike instances are not equivalent
        self.assertNotEqual(child1.id, child2.id)
        self.assertNotEqual(child1.id, child3.id)
        self.assertNotEqual(child2.id, child3.id)
        self.assertNotEqual(child2.id, child4.id)
        self.assertNotEqual(child3.id, child4.id)

        # Test Case 3 - Like instances are equivalent
        self.assertEqual(child1.id, child4.id)
        self.assertEqual(child4.id, child1.id)

        # Test Case 4 - Unlike classes are not equivalent
        self.assertNotEqual(child1.id, other.id)
        self.assertNotEqual(child2.id, other.id)
        self.assertNotEqual(child3.id, other.id)
        self.assertNotEqual(child4.id, other.id)

        # Test Case 5 - different eventid is still equivalent
        diff = Goal(goal_events.goal_different_event_id)
        self.assertEqual(child1.id, diff.id)

        # Test Case 6 - different eventidx is still equivalent
        diff = Goal(goal_events.goal_different_event_id_x)
        self.assertEqual(child1.id, diff.id)

        # Test Case 7 - different datetime is not equivalent
        diff = Goal(goal_events.goal_different_datetime)
        self.assertNotEqual(child1.id, diff.id)

        # Test Case 8 - different period is still equivalent
        diff = Goal(goal_events.goal_different_period)
        self.assertEqual(child1.id, diff.id)

        # Test Case 9 - different periodtime is still equivalent
        diff = Goal(goal_events.goal_different_period_time)
        self.assertEqual(child1.id, diff.id)

        # Test Case 10 - different period time remaining is still equivalent
        diff = Goal(goal_events.goal_different_period_time_remaining)
        self.assertEqual(child1.id, diff.id)

        # Test Case 11 - different scorer is still equivalent
        diff = Goal(goal_events.goal_different_scorer)
        self.assertEqual(child1.id, diff.id)

        # Test Case 12 - different primary assist is still equivalent
        diff = Goal(goal_events.goal_different_primary_assist)
        self.assertEqual(child1.id, diff.id)

        # Test Case 13 - different secondary assist is still equivalent
        diff = Goal(goal_events.goal_different_secondary_assist)
        self.assertEqual(child1.id, diff.id)

        # Test Case 14 - different goalie is still equivalent
        diff = Goal(goal_events.goal_different_goalie)
        self.assertEqual(child1.id, diff.id)

        # Test Case 15 - different strength is still equivalent
        diff = Goal(goal_events.goal_different_strength)
        self.assertEqual(child1.id, diff.id)

        # Test Case 16 - different empty net is still equivalent
        diff = Goal(goal_events.goal_different_empty_net)
        self.assertEqual(child1.id, diff.id)

        # Test Case 17 - different team is still equivalent
        diff = Goal(goal_events.goal_different_team)
        self.assertEqual(child1.id, diff.id)


    def test_hit_equality(self):
        """Test the equality operator for a Hit event."""
        parent = Event(hit_events.hit_1)
        child1 = Hit(hit_events.hit_1)
        child2 = Hit(hit_events.hit_2)
        child3 = Hit(hit_events.hit_3)
        child4 = Hit(hit_events.hit_1)
        other  = Shot(shot_events.shot_event_1)

        # Test Case 1 - parent is not equivalent to child
        self.assertNotEqual(parent, child1)
        self.assertNotEqual(parent, child2)
        self.assertNotEqual(parent, child3)
        self.assertNotEqual(parent, child4)

        # Test Case 2 - Unlike instances are not equivalent
        self.assertNotEqual(child1, child2)
        self.assertNotEqual(child1, child3)
        self.assertNotEqual(child2, child3)
        self.assertNotEqual(child2, child4)
        self.assertNotEqual(child3, child4)

        # Test Case 3 - Like instances are equivalent
        self.assertEqual(child1, child4)
        self.assertEqual(child4, child1)

        # Test Case 4 - Unlike classes are not equivalent
        self.assertNotEqual(child1, other)
        self.assertNotEqual(child2, other)
        self.assertNotEqual(child3, other)
        self.assertNotEqual(child4, other)

        # Test Case 5 - different eventid is still equivalent
        diff = Hit(hit_events.hit_different_event_id)
        self.assertEqual(child1, diff)

        # Test Case 6 - different eventidx is still equivalent
        diff = Hit(hit_events.hit_different_event_id_x)
        self.assertEqual(child1, diff)

        # Test Case 7 - different datetime is still equivalent
        diff = Hit(hit_events.hit_different_datetime)
        self.assertEqual(child1, diff)

        # Test Case 8 - different period is not equivalent
        diff = Hit(hit_events.hit_different_period)
        self.assertNotEqual(child1, diff)

        # Test Case 9 - different periodtime is still equivalent
        diff = Hit(hit_events.hit_different_period_time)
        self.assertEqual(child1, diff)

        # Test Case 10 - different periodtime_remaining is not equivalent
        diff = Hit(hit_events.hit_different_period_time_remaining)
        self.assertNotEqual(child1, diff)

        # Test Case 11 - different hitter is not equivalent
        diff = Hit(hit_events.hit_different_hitter)
        self.assertNotEqual(child1, diff)

        # Test Case 12 - different hittee is not equivalent
        diff = Hit(hit_events.hit_different_hittee)
        self.assertNotEqual(child1, diff)


    def test_hit_id(self):
        """Test the property ID for a Hit event."""
        parent = Event(hit_events.hit_1)
        child1 = Hit(hit_events.hit_1)
        child2 = Hit(hit_events.hit_2)
        child3 = Hit(hit_events.hit_3)
        child4 = Hit(hit_events.hit_1)
        other  = Shot(shot_events.shot_event_1)

        # Test Case 1 - parent is not equivalent to child
        self.assertNotEqual(parent.id, child1.id)
        self.assertNotEqual(parent.id, child2.id)
        self.assertNotEqual(parent.id, child3.id)
        self.assertNotEqual(parent.id, child4.id)

        # Test Case 2 - Unlike instances are not equivalent
        self.assertNotEqual(child1.id, child2.id)
        self.assertNotEqual(child1.id, child3.id)
        self.assertNotEqual(child2.id, child3.id)
        self.assertNotEqual(child2.id, child4.id)
        self.assertNotEqual(child3.id, child4.id)

        # Test Case 3 - Like instances are equivalent
        self.assertEqual(child1.id, child4.id)
        self.assertEqual(child4.id, child1.id)

        # Test Case 4 - Unlike classes are not equivalent
        self.assertNotEqual(child1.id, other.id)
        self.assertNotEqual(child2.id, other.id)
        self.assertNotEqual(child3.id, other.id)
        self.assertNotEqual(child4.id, other.id)

        # Test Case 5 - different eventid is still equivalent
        diff = Hit(hit_events.hit_different_event_id)
        self.assertEqual(child1.id, diff.id)

        # Test Case 6 - different eventidx is still equivalent
        diff = Hit(hit_events.hit_different_event_id_x)
        self.assertEqual(child1.id, diff.id)

        # Test Case 7 - different datetime is not equivalent
        diff = Hit(hit_events.hit_different_datetime)
        self.assertNotEqual(child1.id, diff.id)

        # Test Case 8 - different period is still equivalent
        diff = Hit(hit_events.hit_different_period)
        self.assertEqual(child1.id, diff.id)

        # Test Case 9 - different periodtime is still equivalent
        diff = Hit(hit_events.hit_different_period_time)
        self.assertEqual(child1.id, diff.id)

        # Test Case 10 - different periodtime_remaining is still equivalent
        diff = Hit(hit_events.hit_different_period_time_remaining)
        self.assertEqual(child1.id, diff.id)

        # Test Case 11 - different hitter is still equivalent
        diff = Hit(hit_events.hit_different_hitter)
        self.assertEqual(child1.id, diff.id)

        # Test Case 12 - different hittee is still equivalent
        diff = Hit(hit_events.hit_different_hittee)
        self.assertEqual(child1.id, diff.id)


    def test_missed_shot_equality(self):
        """Test the equality operator for a MissedShot event."""
        parent = Event(missed_shot_events.missed_shot_1)
        child1 = MissedShot(missed_shot_events.missed_shot_1)
        child2 = MissedShot(missed_shot_events.missed_shot_2)
        child3 = MissedShot(missed_shot_events.missed_shot_3)
        child4 = MissedShot(missed_shot_events.missed_shot_1)
        other  = Shot(shot_events.shot_event_1)

        # Test Case 1 - parent is not equivalent to child
        self.assertNotEqual(parent, child1)
        self.assertNotEqual(parent, child2)
        self.assertNotEqual(parent, child3)
        self.assertNotEqual(parent, child4)

        # Test Case 2 - Unlike instances are not equivalent
        self.assertNotEqual(child1, child2)
        self.assertNotEqual(child1, child3)
        self.assertNotEqual(child2, child3)
        self.assertNotEqual(child2, child4)
        self.assertNotEqual(child3, child4)

        # Test Case 3 - Like instances are equivalent
        self.assertEqual(child1, child4)
        self.assertEqual(child4, child1)

        # Test Case 4 - Unlike classes are not equivalent
        self.assertNotEqual(child1, other)
        self.assertNotEqual(child2, other)
        self.assertNotEqual(child3, other)
        self.assertNotEqual(child4, other)

        # Test Case 5 - different eventid is still equivalent
        diff = MissedShot(missed_shot_events.missed_shot_different_event_id)
        self.assertEqual(child1, diff)

        # Test Case 6 - different eventidx is still equivalent
        diff = MissedShot(missed_shot_events.missed_shot_different_event_id_x)
        self.assertEqual(child1, diff)

        # Test Case 7 - different datetime is still equivalent
        diff = MissedShot(missed_shot_events.missed_shot_different_datetime)
        self.assertEqual(child1, diff)

        # Test Case 8 - different period is not equivalent
        diff = MissedShot(missed_shot_events.missed_shot_different_period)
        self.assertNotEqual(child1, diff)

        # Test Case 9 - different periodtime is still equivalent
        diff = MissedShot(missed_shot_events.missed_shot_different_period_time)
        self.assertEqual(child1, diff)

        # Test Case 10 - different periodtime_remaining is not equivalent
        diff = MissedShot(missed_shot_events.missed_shot_different_period_time_remaining)
        self.assertNotEqual(child1, diff)

        # Test Case 11 - different shooter is not equivalent
        diff = MissedShot(missed_shot_events.missed_shot_different_shooter)
        self.assertNotEqual(child1, diff)

        # Test Case 12 - different goalie is not equivalent
        diff = MissedShot(missed_shot_events.missed_shot_different_goalie)
        self.assertNotEqual(child1, diff)


    def test_missed_shot_id(self):
        """Test the ID property for a MissedShot event."""
        parent = Event(missed_shot_events.missed_shot_1)
        child1 = MissedShot(missed_shot_events.missed_shot_1)
        child2 = MissedShot(missed_shot_events.missed_shot_2)
        child3 = MissedShot(missed_shot_events.missed_shot_3)
        child4 = MissedShot(missed_shot_events.missed_shot_1)
        other  = Shot(shot_events.shot_event_1)

        # Test Case 1 - parent is not equivalent to child
        self.assertNotEqual(parent.id, child1.id)
        self.assertNotEqual(parent.id, child2.id)
        self.assertNotEqual(parent.id, child3.id)
        self.assertNotEqual(parent.id, child4.id)

        # Test Case 2 - Unlike instances are not equivalent
        self.assertNotEqual(child1.id, child2.id)
        self.assertNotEqual(child1.id, child3.id)
        self.assertNotEqual(child2.id, child3.id)
        self.assertNotEqual(child2.id, child4.id)
        self.assertNotEqual(child3.id, child4.id)

        # Test Case 3 - Like instances are equivalent
        self.assertEqual(child1.id, child4.id)
        self.assertEqual(child4.id, child1.id)

        # Test Case 4 - Unlike classes are not equivalent
        self.assertNotEqual(child1.id, other.id)
        self.assertNotEqual(child2.id, other.id)
        self.assertNotEqual(child3.id, other.id)
        self.assertNotEqual(child4.id, other.id)

        # Test Case 5 - different eventid is still equivalent
        diff = MissedShot(missed_shot_events.missed_shot_different_event_id)
        self.assertEqual(child1.id, diff.id)

        # Test Case 6 - different eventidx is still equivalent
        diff = MissedShot(missed_shot_events.missed_shot_different_event_id_x)
        self.assertEqual(child1.id, diff.id)

        # Test Case 7 - different datetime is not equivalent
        diff = MissedShot(missed_shot_events.missed_shot_different_datetime)
        self.assertNotEqual(child1.id, diff.id)

        # Test Case 8 - different period is still equivalent
        diff = MissedShot(missed_shot_events.missed_shot_different_period)
        self.assertEqual(child1.id, diff.id)

        # Test Case 9 - different periodtime is still equivalent
        diff = MissedShot(missed_shot_events.missed_shot_different_period_time)
        self.assertEqual(child1.id, diff.id)

        # Test Case 10 - different periodtime_remaining is still equivalent
        diff = MissedShot(missed_shot_events.missed_shot_different_period_time_remaining)
        self.assertEqual(child1.id, diff.id)

        # Test Case 11 - different shooter is still equivalent
        diff = MissedShot(missed_shot_events.missed_shot_different_shooter)
        self.assertEqual(child1.id, diff.id)

        # Test Case 12 - different goalie is still equivalent
        diff = MissedShot(missed_shot_events.missed_shot_different_goalie)
        self.assertEqual(child1.id, diff.id)


    def test_penalty_shot_equality(self):
        """Test the equality operator for a PenaltyShot event."""
        parent = Event(penalty_shot_events.penalty_shot_1)
        child1 = PenaltyShot(penalty_shot_events.penalty_shot_1)
        child2 = PenaltyShot(penalty_shot_events.penalty_shot_2)
        child3 = PenaltyShot(penalty_shot_events.penalty_shot_3)
        child4 = PenaltyShot(penalty_shot_events.penalty_shot_1)
        other  = Shot(shot_events.shot_event_1)

        # Test Case 1 - parent is not equivalent to child
        self.assertNotEqual(parent, child1)
        self.assertNotEqual(parent, child2)
        self.assertNotEqual(parent, child3)
        self.assertNotEqual(parent, child4)

        # Test Case 2 - Unlike instances are not equivalent
        self.assertNotEqual(child1, child2)
        self.assertNotEqual(child1, child3)
        self.assertNotEqual(child2, child3)
        self.assertNotEqual(child2, child4)
        self.assertNotEqual(child3, child4)

        # Test Case 3 - Like instances are equivalent
        self.assertEqual(child1, child4)
        self.assertEqual(child4, child1)

        # Test Case 4 - Unlike classes are not equivalent
        self.assertNotEqual(child1, other)
        self.assertNotEqual(child2, other)
        self.assertNotEqual(child3, other)
        self.assertNotEqual(child4, other)

        # Test Case 5 - different eventid is still equivalent
        diff = PenaltyShot(penalty_shot_events.penalty_shot_different_event_id)
        self.assertEqual(child1, diff)

        # Test Case 6 - different eventidx is still equivalent
        diff = PenaltyShot(penalty_shot_events.penalty_shot_different_event_id_x)
        self.assertEqual(child1, diff)

        # Test Case 7 - different datetime is still equivalent
        diff = PenaltyShot(penalty_shot_events.penalty_shot_different_datetime)
        self.assertEqual(child1, diff)

        # Test Case 8 - different period is not equivalent
        diff = PenaltyShot(penalty_shot_events.penalty_shot_different_period)
        self.assertNotEqual(child1, diff)

        # Test Case 9 - different periodtime is still equivalent
        diff = PenaltyShot(penalty_shot_events.penalty_shot_different_period_time)
        self.assertEqual(child1, diff)

        # Test Case 10 - different periodtime_remaining is not equivalent
        diff = PenaltyShot(penalty_shot_events.penalty_shot_different_period_time_remaining)
        self.assertNotEqual(child1, diff)

        # Test Case 11 - different taker is not equivalent
        diff = PenaltyShot(penalty_shot_events.penalty_shot_different_taker)
        self.assertNotEqual(child1, diff)

        # Test Case 12 - different drawn by is not equivalent
        diff = PenaltyShot(penalty_shot_events.penalty_shot_different_drawn_by)
        self.assertNotEqual(child1, diff)

        # Test Case 13 - different reason is not equivalent
        diff = PenaltyShot(penalty_shot_events.penalty_shot_different_reason)
        self.assertNotEqual(child1, diff)


    def test_penalty_shot_id(self):
        """Test the ID property for a PenaltyShot event."""
        parent = Event(penalty_shot_events.penalty_shot_1)
        child1 = PenaltyShot(penalty_shot_events.penalty_shot_1)
        child2 = PenaltyShot(penalty_shot_events.penalty_shot_2)
        child3 = PenaltyShot(penalty_shot_events.penalty_shot_3)
        child4 = PenaltyShot(penalty_shot_events.penalty_shot_1)
        other  = Shot(shot_events.shot_event_1)

        # Test Case 1 - parent is not equivalent to child
        self.assertNotEqual(parent.id, child1.id)
        self.assertNotEqual(parent.id, child2.id)
        self.assertNotEqual(parent.id, child3.id)
        self.assertNotEqual(parent.id, child4.id)

        # Test Case 2 - Unlike instances are not equivalent
        self.assertNotEqual(child1.id, child2.id)
        self.assertNotEqual(child1.id, child3.id)
        self.assertNotEqual(child2.id, child3.id)
        self.assertNotEqual(child2.id, child4.id)
        self.assertNotEqual(child3.id, child4.id)

        # Test Case 3 - Like instances are equivalent
        self.assertEqual(child1.id, child4.id)
        self.assertEqual(child4.id, child1.id)

        # Test Case 4 - Unlike classes are not equivalent
        self.assertNotEqual(child1.id, other.id)
        self.assertNotEqual(child2.id, other.id)
        self.assertNotEqual(child3.id, other.id)
        self.assertNotEqual(child4.id, other.id)

        # Test Case 5 - different eventid is still equivalent
        diff = PenaltyShot(penalty_shot_events.penalty_shot_different_event_id)
        self.assertEqual(child1.id, diff.id)

        # Test Case 6 - different eventidx is still equivalent
        diff = PenaltyShot(penalty_shot_events.penalty_shot_different_event_id_x)
        self.assertEqual(child1.id, diff.id)

        # Test Case 7 - different datetime is not equivalent
        diff = PenaltyShot(penalty_shot_events.penalty_shot_different_datetime)
        self.assertNotEqual(child1.id, diff.id)

        # Test Case 8 - different period is still equivalent
        diff = PenaltyShot(penalty_shot_events.penalty_shot_different_period)
        self.assertEqual(child1.id, diff.id)

        # Test Case 9 - different periodtime is still equivalent
        diff = PenaltyShot(penalty_shot_events.penalty_shot_different_period_time)
        self.assertEqual(child1.id, diff.id)

        # Test Case 10 - different periodtime_remaining is still equivalent
        diff = PenaltyShot(penalty_shot_events.penalty_shot_different_period_time_remaining)
        self.assertEqual(child1.id, diff.id)

        # Test Case 11 - different taker is still equivalent
        diff = PenaltyShot(penalty_shot_events.penalty_shot_different_taker)
        self.assertEqual(child1.id, diff.id)

        # Test Case 12 - different drawn by is still equivalent
        diff = PenaltyShot(penalty_shot_events.penalty_shot_different_drawn_by)
        self.assertEqual(child1.id, diff.id)


    def test_penalty_equality(self):
        """Test the equality operator for a Penalty event."""
        parent = Event(penalty_shot_events.penalty_shot_1)
        child1 = Penalty(penalty_events.penalty_1)
        child2 = Penalty(penalty_events.penalty_2)
        child3 = Penalty(penalty_events.penalty_3)
        child4 = Penalty(penalty_events.penalty_1)
        other  = Shot(shot_events.shot_event_1)

        # Test Case 1 - parent is not equivalent to child
        self.assertNotEqual(parent, child1)
        self.assertNotEqual(parent, child2)
        self.assertNotEqual(parent, child3)
        self.assertNotEqual(parent, child4)

        # Test Case 2 - Unlike instances are not equivalent
        self.assertNotEqual(child1, child2)
        self.assertNotEqual(child1, child3)
        self.assertNotEqual(child2, child3)
        self.assertNotEqual(child2, child4)
        self.assertNotEqual(child3, child4)

        # Test Case 3 - Like instances are equivalent
        self.assertEqual(child1, child4)
        self.assertEqual(child4, child1)

        # Test Case 4 - Unlike classes are not equivalent
        self.assertNotEqual(child1, other)
        self.assertNotEqual(child2, other)
        self.assertNotEqual(child3, other)
        self.assertNotEqual(child4, other)

        # Test Case 5 - different eventid is still equivalent
        diff = Penalty(penalty_events.penalty_different_event_id)
        self.assertEqual(child1, diff)

        # Test Case 6 - different eventidx is still equivalent
        diff = Penalty(penalty_events.penalty_different_event_id_x)
        self.assertEqual(child1, diff)

        # Test Case 7 - different datetime is still equivalent
        diff = Penalty(penalty_events.penalty_different_datetime)
        self.assertEqual(child1, diff)

        # Test Case 8 - different period is not equivalent
        diff = Penalty(penalty_events.penalty_different_period)
        self.assertNotEqual(child1, diff)

        # Test Case 9 - different periodtime is still equivalent
        diff = Penalty(penalty_events.penalty_different_period_time)
        self.assertEqual(child1, diff)

        # Test Case 10 - different periodtime_remaining is not equivalent
        diff = Penalty(penalty_events.penalty_different_period_time_remaining)
        self.assertNotEqual(child1, diff)

        # Test Case 11 - different taker is not equivalent
        diff = Penalty(penalty_events.penalty_different_taker)
        self.assertNotEqual(child1, diff)

        # Test Case 12 - different drawn by is not equivalent
        diff = Penalty(penalty_events.penalty_different_drawn_by)
        self.assertNotEqual(child1, diff)

        # Test Case 13 - different reason is not equivalent
        diff = Penalty(penalty_events.penalty_different_reason)
        self.assertNotEqual(child1, diff)

        # Test Case 14 - different severity is not equivalent
        diff = Penalty(penalty_events.penalty_different_severity)
        self.assertNotEqual(child1, diff)

        # Test Case 15 - different minutes is not equivalent
        diff = Penalty(penalty_events.penalty_different_minutes)
        self.assertNotEqual(child1, diff)


    def test_penalty_id(self):
        """Test the ID property for a Penalty event."""
        parent = Event(penalty_shot_events.penalty_shot_1)
        child1 = Penalty(penalty_events.penalty_1)
        child2 = Penalty(penalty_events.penalty_2)
        child3 = Penalty(penalty_events.penalty_3)
        child4 = Penalty(penalty_events.penalty_1)
        other  = Shot(shot_events.shot_event_1)

        # Test Case 1 - parent is not equivalent to child
        self.assertNotEqual(parent.id, child1.id)
        self.assertNotEqual(parent.id, child2.id)
        self.assertNotEqual(parent.id, child3.id)
        self.assertNotEqual(parent.id, child4.id)

        # Test Case 2 - Unlike instances are not equivalent
        self.assertNotEqual(child1.id, child2.id)
        self.assertNotEqual(child1.id, child3.id)
        self.assertNotEqual(child2.id, child3.id)
        self.assertNotEqual(child2.id, child4.id)
        self.assertNotEqual(child3.id, child4.id)

        # Test Case 3 - Like instances are equivalent
        self.assertEqual(child1.id, child4.id)
        self.assertEqual(child4.id, child1.id)

        # Test Case 4 - Unlike classes are not equivalent
        self.assertNotEqual(child1.id, other.id)
        self.assertNotEqual(child2.id, other.id)
        self.assertNotEqual(child3.id, other.id)
        self.assertNotEqual(child4.id, other.id)

        # Test Case 5 - different eventid is still equivalent
        diff = Penalty(penalty_events.penalty_different_event_id)
        self.assertEqual(child1.id, diff.id)

        # Test Case 6 - different eventidx is still equivalent
        diff = Penalty(penalty_events.penalty_different_event_id_x)
        self.assertEqual(child1.id, diff.id)

        # Test Case 7 - different datetime is not equivalent
        diff = Penalty(penalty_events.penalty_different_datetime)
        self.assertNotEqual(child1.id, diff.id)

        # Test Case 8 - different period is still equivalent
        diff = Penalty(penalty_events.penalty_different_period)
        self.assertEqual(child1.id, diff.id)

        # Test Case 9 - different periodtime is still equivalent
        diff = Penalty(penalty_events.penalty_different_period_time)
        self.assertEqual(child1.id, diff.id)

        # Test Case 10 - different periodtime_remaining is still equivalent
        diff = Penalty(penalty_events.penalty_different_period_time_remaining)
        self.assertEqual(child1.id, diff.id)

        # Test Case 11 - different taker is still equivalent
        diff = Penalty(penalty_events.penalty_different_taker)
        self.assertEqual(child1.id, diff.id)

        # Test Case 12 - different drawn by is still equivalent
        diff = Penalty(penalty_events.penalty_different_drawn_by)
        self.assertEqual(child1.id, diff.id)

        # Test Case 13 - different reason is still equivalent
        diff = Penalty(penalty_events.penalty_different_reason)
        self.assertEqual(child1.id, diff.id)

        # Test Case 14 - different severity is still equivalent
        diff = Penalty(penalty_events.penalty_different_severity)
        self.assertEqual(child1.id, diff.id)

        # Test Case 15 - different minutes is still equivalent
        diff = Penalty(penalty_events.penalty_different_minutes)
        self.assertEqual(child1.id, diff.id)
