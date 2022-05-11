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
from src import events


class TestPrinter(unittest.TestCase):
    """
    Description:
        Unit tests for the Printer class.
    """

    def test_game_scheduled(self):
        """
        Description:
            Test the constructor of a game scheduled event.
        """
        data = {
            "result": {"description": "Game Scheduled"},
            "about": {
                "eventIdx": 0,
                "period": 1,
                "periodTimeRemaining": "20:00",
                "goals": {
                    "home": 0,
                    "away": 0
                }
            }
        }
        expected = events.GameScheduled(data)
        actual   = events.to_event(game_events.game_scheduled_data)
        self.assertEqual(expected, actual)


    def test_game_end(self):
        """
        Description:
            Test the constructor of a game end event.
        """
        data = {
            "result": {"description": "Game End"},
            "about": {
                "eventIdx": 384,
                "period": 3,
                "periodTimeRemaining": "00:00",
                "goals": {
                    "home": 2,
                    "away": 4
                }
            }
        }
        expected = events.GameEnd(data)
        actual   = events.to_event(game_events.game_end_data)
        self.assertEqual(expected, actual)


    def test_game_official(self):
        """
        Description:
            Test the constructor of a game official event.
        """
        data = {
            "result": {"description": "Game Official"},
            "about": {
                "eventIdx": 385,
                "period": 3,
                "periodTimeRemaining": "00:00",
                "goals": {
                    "home": 2,
                    "away": 4
                }
            }
        }
        expected = events.GameOfficial(data)
        actual   = events.to_event(game_events.game_official_data)
        self.assertEqual(expected, actual)


    def test_faceoff(self):
        """
        Description:
            Test the constructor of a faceoff event.
        """
        data = {
            "players": [
                {"player": {"fullName": "Lars Eller"},
                 "playerType": "Winner"},
                {"player": {"fullName": "Charlie Coyle"},
                 "playerType": "Loser"}
            ],
            "result": {"description": "Faceoff"},
            "about": {
                "eventIdx": 3,
                "period": 1,
                "periodTimeRemaining": "20:00",
                "goals": {
                    "home": 0,
                    "away": 0
                }
            }
        }
        expected = events.Faceoff(data)
        actual   = events.to_event(miscellaneous_events.faceoff_data)
        self.assertEqual(expected, actual)


    def test_stoppage(self):
        """
        Description:
            Test the constructor of a stoppage event.
        """
        data = {
            "result": {"description": "Puck in Netting"},
            "about": {
                "eventIdx": 6,
                "period": 1,
                "periodTimeRemaining": "19:19",
                "goals": {
                    "home": 0,
                    "away": 0
                }
            }
        }
        expected = events.Stoppage(data)
        actual   = events.to_event(miscellaneous_events.stoppage_data)
        self.assertEqual(expected, actual)


    def test_shot(self):
        """
        Description:
            Test the constructor of a shot event.
        """
        data = {
            "players": [
                {"player": {"fullName": "Evgeny Kuznetsov"},
                 "playerType": "Shooter"},
                {"player": {"fullName": "Linus Ullmark"},
                 "playerType": "Goalie"}
            ],
            "result": {"description": "Evgeny Kuznetsov Wrist Shot saved by Linus Ullmark"},
            "about": {
                "eventIdx": 12,
                "period": 1,
                "periodTimeRemaining": "18:14",
                "goals": {
                    "home": 0,
                    "away": 0
                }
            }
        }
        expected = events.Shot(data)
        actual   = events.to_event(miscellaneous_events.shot_data)
        self.assertEqual(expected, actual)


    def test_hit(self):
        """
        Description:
            Test the constructor of a hit event.
        """
        data = {
            "players": [
                {"player": {"fullName": "Alex Ovechkin"},
                 "playerType": "Hitter"},
                {"player": {"fullName": "Curtis Lazar"},
                 "playerType": "Hittee"}
            ],
            "result": {"description": "Alex Ovechkin hit Curtis Lazar"},
            "about": {
                "eventIdx": 15,
                "period": 1,
                "periodTimeRemaining": "17:55",
                "goals": {
                    "home": 0,
                    "away": 0
                }
            }
        }
        expected = events.Hit(data)
        actual   = events.to_event(miscellaneous_events.hit_data)
        self.assertEqual(expected, actual)


    def test_blocked_shot(self):
        """
        Description:
            Test the constructor of a blocked shot event.
        """
        data = {
            "players": [
                {"player": {"fullName": "Justin Schultz"},
                 "playerType": "Blocker"},
                {"player": {"fullName": "Tomas Nosek"},
                 "playerType": "Shooter"}
            ],
            "result": {"description": "Tomas Nosek shot blocked shot by Justin Schultz"},
            "about": {
                "eventIdx": 31,
                "period": 1,
                "periodTimeRemaining": "14:21",
                "goals": {
                    "home": 0,
                    "away": 0
                }
            }
        }
        expected = events.BlockedShot(data)
        actual   = events.to_event(miscellaneous_events.blocked_shot_data)
        self.assertEqual(expected, actual)


    def test_giveaway(self):
        """
        Description:
            Test the constructor of a giveaway event.
        """
        data = {
            "players": [
                {"player": {"fullName": "Brandon Carlo"},
                 "playerType": "PlayerID"}
            ],
            "result": {"description": "Giveaway by Brandon Carlo"},
            "about": {
                "eventIdx": 24,
                "period": 1,
                "periodTimeRemaining": "16:22",
                "goals": {
                    "home": 0,
                    "away": 0
                }
            }
        }
        expected = events.Giveaway(data)
        actual   = events.to_event(miscellaneous_events.giveaway_data)
        self.assertEqual(expected, actual)


    def test_takeaway(self):
        """
        Description:
            Test the constructor of a takeaway event.
        """
        data = {
            "players": [
                {"player": {"fullName": "Johan Larsson"},
                 "playerType": "PlayerID"}
            ],
            "result": {"description": "Takeaway by Johan Larsson"},
            "about": {
                "eventIdx": 8,
                "period": 1,
                "periodTimeRemaining": "18:54",
                "goals": {
                    "home": 0,
                    "away": 0
                }
            }
        }
        expected = events.Takeaway(data)
        actual   = events.to_event(miscellaneous_events.takeaway_data)
        self.assertEqual(expected, actual)


    def test_missed_shot(self):
        """
        Description:
            Test the constructor of a missed shot event.
        """
        data = {
            "players": [
                {"player": {"fullName": "Charlie McAvoy"},
                 "playerType": "Shooter"},
                {"player": {"fullName": "Vitek Vanecek"},
                 "playerType": "Unknown"}
            ],
            "result": {"description": "Charlie McAvoy Wide of Net Vitek Vanecek"},
            "about": {
                "eventIdx": 17,
                "period": 1,
                "periodTimeRemaining": "17:39",
                "goals": {
                    "home": 0,
                    "away": 0
                }
            }
        }
        expected = events.MissedShot(data)
        actual   = events.to_event(miscellaneous_events.missed_shot_data)
        self.assertEqual(expected, actual)


    def test_penalty(self):
        """
        Description:
            Test the constructor of a Penalty event.
        """
        data = {
            "players": [
                {"player": {"fullName": "Nic Dowd"},
                 "playerType": "PenaltyOn"},
                {"player": {"fullName": "Josh Brown"},
                 "playerType": "DrewBy"}
            ],
            "result": {
                "description": "Nic Dowd Hi-sticking against Josh Brown",
                "secondaryType": "Hi-sticking",
                "penaltySeverity": "Minor",
                "penaltyMinutes": 2
            },
            "about": {
                "eventIdx": 77,
                "period": 1,
                "periodTimeRemaining": "08:13",
                "goals": {
                    "home": 0,
                    "away": 0
                }
            }
        }
        expected = events.Penalty(data)
        actual   = events.to_event(penalty_events.penalty_data)
        self.assertEqual(expected, actual)


    def test_penalty_shot(self):
        """
        Description:
            Test the constructor of a Penalty Shot event.
        """
        data = {
            "players": [
                {"player": {"fullName": "Brenden Dillon"},
                 "playerType": "PenaltyOn"},
                {"player": {"fullName": "J.T. Compher"},
                 "playerType": "DrewBy"}
            ],
            "result": {
                "description": "Brenden Dillon PS - Hooking on breakaway against J.T. Compher",
                "secondaryType": "PS - Hooking on breakaway",
                "penaltySeverity": "Penalty Shot",
                "penaltyMinutes": 0
            },
            "about": {
                "eventIdx": 212,
                "period": 2,
                "periodTimeRemaining": "02:42",
                "goals": {
                    "home": 3,
                    "away": 2
                }
            }
        }
        expected = events.PenaltyShot(data)
        actual   = events.to_event(penalty_events.penalty_shot_data)
        self.assertEqual(expected, actual)


    def test_period_ready(self):
        """
        Description:
            Test the constructor of a Period Ready event.
        """
        data = {
            "result": {"description": "Period Ready"},
            "about": {
                "eventIdx": 1,
                "period": 1,
                "periodTimeRemaining": "20:00",
                "goals": {
                    "home": 0,
                    "away": 0
                }
            }
        }
        expected = events.PeriodReady(data)
        actual   = events.to_event(period_events.period_ready_data)
        self.assertEqual(expected, actual)


    def test_period_start(self):
        """
        Description:
            Test the constructor of a Period Start event.
        """
        data = {
            "result": {"description": "Period Start"},
            "about": {
                "eventIdx": 124,
                "period": 2,
                "periodTimeRemaining": "20:00",
                "goals": {
                    "home": 0,
                    "away": 0
                }
            }
        }
        expected = events.PeriodStart(data)
        actual   = events.to_event(period_events.period_start_data)
        self.assertEqual(expected, actual)


    def test_period_end(self):
        """
        Description:
            Test the constructor of a Period End event.
        """
        data = {
            "result": {"description": "End of 1st Period"},
            "about": {
                "eventIdx": 121,
                "period": 1,
                "periodTimeRemaining": "00:00",
                "goals": {
                    "home": 0,
                    "away": 0
                }
            }
        }
        expected = events.PeriodEnd(data)
        actual   = events.to_event(period_events.period_end_data)
        self.assertEqual(expected, actual)


    def test_period_official(self):
        """
        Description:
            Test the constructor of a Period Official event.
        """
        data = {
            "result": {"description": "Period Official"},
            "about": {
                "eventIdx": 122,
                "period": 1,
                "periodTimeRemaining": "00:00",
                "goals": {
                    "home": 0,
                    "away": 0
                }
            }
        }
        expected = events.PeriodOfficial(data)
        actual   = events.to_event(period_events.period_official_data)
        self.assertEqual(expected, actual)


    def test_goal(self):
        """
        Description:
            Test the constructor of a Goal event.
        """
        data = {
            "players": [
                {"player": {"fullName": "John Carlson"},
                 "playerType": "Scorer"},
                {"player": {"fullName": "Conor Sheary"},
                 "playerType": "Assist"},
                {"player": {"fullName": "Adam Jones"},
                 "playerType": "Assist"},
                {"player": {"fullName": "Linus Ullmark"},
                 "playerType": "Goalie"}
            ],
            "result": {"description": "John Carlson (14) Slap Shot, assists: Conor Sheary (20), Adam Jones (999)"},
            "about": {
                "eventIdx": 155,
                "period": 1,
                "periodTimeRemaining": "15:49",
                "goals": {
                    "home": 0,
                    "away": 1
                }
            }
        }
        expected = events.Goal(data)
        actual   = events.to_event(goal_events.goal_data_two_assists)
        self.assertEqual(expected, actual)


    def test_challenge(self):
        """
        Description:
            Test the constructor of a challenge event.
        """
        data = {
            "result": {"description": "Coach's Challenge"},
            "about": {
                "eventIdx": 105,
                "period": 2,
                "periodTimeRemaining": "18:06",
                "goals": {
                    "home": 0,
                    "away": 1
                }
            }
        }
        expected = events.Challenge(data)
        actual   = events.to_event(miscellaneous_events.challenge_data)
        self.assertEqual(expected, actual)
