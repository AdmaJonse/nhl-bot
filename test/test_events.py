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
from test.test_data import shot_events

from src import event_factory
from src.game_data import GameData

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
from src.events.shootout_end import ShootoutEnd
from src.events.stoppage import Stoppage
from src.events.takeaway import Takeaway


class TestEvents(unittest.TestCase):
    """
    Description:
        Unit tests for the generator class.
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
                "periodType": "REGULAR",
                "periodTimeRemaining": "20:00",
                "dateTime": "2022-04-10T17:41:12Z",
                "goals": {
                    "home": 0,
                    "away": 0
                }
            }
        }
        expected = GameScheduled(data)
        actual   = event_factory.create(game_events.game_scheduled_data)
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
                "periodType": "REGULAR",
                "periodTimeRemaining": "00:00",
                "dateTime": "2022-04-10T17:41:12Z",
                "goals": {
                    "home": 2,
                    "away": 4
                }
            }
        }
        expected = GameEnd(data)
        actual   = event_factory.create(game_events.game_end_data)
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
                "periodType": "REGULAR",
                "periodTimeRemaining": "00:00",
                "dateTime": "2022-04-10T17:41:12Z",
                "goals": {
                    "home": 2,
                    "away": 4
                }
            }
        }
        expected = GameOfficial(data)
        actual   = event_factory.create(game_events.game_official_data)
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
                "periodType": "REGULAR",
                "periodTimeRemaining": "20:00",
                "dateTime": "2022-04-10T17:41:12Z",
                "goals": {
                    "home": 0,
                    "away": 0
                }
            }
        }
        expected = Faceoff(data)
        actual   = event_factory.create(miscellaneous_events.faceoff_data)
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
                "periodType": "REGULAR",
                "periodTimeRemaining": "19:19",
                "dateTime": "2022-04-10T17:41:12Z",
                "goals": {
                    "home": 0,
                    "away": 0
                }
            }
        }
        expected = Stoppage(data)
        actual   = event_factory.create(miscellaneous_events.stoppage_data)
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
                "periodType": "REGULAR",
                "periodTimeRemaining": "18:14",
                "dateTime": "2022-04-10T17:41:12Z",
                "goals": {
                    "home": 0,
                    "away": 0
                }
            },
            "team" : {
                "name" : "Washington Capitals"
            }
        }
        expected = Shot(data)
        actual   = event_factory.create(miscellaneous_events.shot_data)
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
                "periodType": "REGULAR",
                "periodTimeRemaining": "17:55",
                "dateTime": "2022-04-10T17:41:12Z",
                "goals": {
                    "home": 0,
                    "away": 0
                }
            }
        }
        expected = Hit(data)
        actual   = event_factory.create(miscellaneous_events.hit_data)
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
                "periodType": "REGULAR",
                "periodTimeRemaining": "14:21",
                "dateTime": "2022-04-10T17:41:12Z",
                "goals": {
                    "home": 0,
                    "away": 0
                }
            }
        }
        expected = BlockedShot(data)
        actual   = event_factory.create(miscellaneous_events.blocked_shot_data)
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
                "periodType": "REGULAR",
                "periodTimeRemaining": "16:22",
                "dateTime": "2022-04-10T17:41:12Z",
                "goals": {
                    "home": 0,
                    "away": 0
                }
            }
        }
        expected = Giveaway(data)
        actual   = event_factory.create(miscellaneous_events.giveaway_data)
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
                "periodType": "REGULAR",
                "periodTimeRemaining": "18:54",
                "dateTime": "2022-04-10T17:41:12Z",
                "goals": {
                    "home": 0,
                    "away": 0
                }
            }
        }
        expected = Takeaway(data)
        actual   = event_factory.create(miscellaneous_events.takeaway_data)
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
                "periodType": "REGULAR",
                "periodTimeRemaining": "17:39",
                "dateTime": "2022-04-10T17:41:12Z",
                "goals": {
                    "home": 0,
                    "away": 0
                }
            }
        }
        expected = MissedShot(data)
        actual   = event_factory.create(miscellaneous_events.missed_shot_data)
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
                "periodType": "REGULAR",
                "periodTimeRemaining": "08:13",
                "dateTime": "2022-04-10T17:41:12Z",
                "goals": {
                    "home": 0,
                    "away": 0
                }
            },
            "team" : {
                "name" : "Florida Panthers"
            }
        }
        expected = Penalty(data)
        actual   = event_factory.create(penalty_events.penalty_data)
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
                "periodType": "REGULAR",
                "periodTimeRemaining": "02:42",
                "dateTime": "2022-04-10T17:41:12Z",
                "goals": {
                    "home": 3,
                    "away": 2
                }
            },
            "team" : {
                "name" : "Florida Panthers"
            }
        }
        expected = PenaltyShot(data)
        actual   = event_factory.create(penalty_events.penalty_shot_data)
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
                "periodType": "REGULAR",
                "periodTimeRemaining": "20:00",
                "dateTime": "2022-04-10T17:41:12Z",
                "goals": {
                    "home": 0,
                    "away": 0
                }
            }
        }
        expected = PeriodReady(data)
        actual   = event_factory.create(period_events.period_ready_data)
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
                "periodType": "REGULAR",
                "periodTimeRemaining": "20:00",
                "dateTime": "2022-04-10T17:41:12Z",
                "goals": {
                    "home": 0,
                    "away": 0
                }
            }
        }
        expected = PeriodStart(data)
        actual   = event_factory.create(period_events.period_start_data)
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
                "periodType": "REGULAR",
                "periodTimeRemaining": "00:00",
                "dateTime": "2022-04-10T17:41:12Z",
                "goals": {
                    "home": 0,
                    "away": 0
                }
            }
        }
        expected = PeriodEnd(data)
        actual   = event_factory.create(period_events.period_end_data)
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
                "periodType": "REGULAR",
                "periodTimeRemaining": "00:00",
                "dateTime": "2022-04-10T17:41:12Z",
                "goals": {
                    "home": 0,
                    "away": 0
                }
            }
        }
        expected = PeriodOfficial(data)
        actual   = event_factory.create(period_events.period_official_data)
        self.assertEqual(expected, actual)


    def test_shootout_end(self):
        """
        Description:
            Test the constructor of a Shootout End event.
        """
        data = {
            "result": {"description": "Shootout Complete"},
            "about": {
                "eventIdx": 122,
                "period": 5,
                "periodType": "SHOOTOUT",
                "periodTimeRemaining": "00:00",
                "dateTime": "2022-04-10T17:41:12Z",
                "goals": {
                    "home": 0,
                    "away": 0
                }
            }
        }
        expected = ShootoutEnd(data)
        actual   = event_factory.create(period_events.shootout_end_data)
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
                 "playerType": "Goalie"}],
            "result": {
                "event": "Goal",
                "description": "John Carlson (14) Slap Shot, assists: Conor Sheary (20)",
                "secondaryType": "Slap Shot",
                "strength": {
                    "code": "EVEN",
                    "name": "Even"
                },
                "gameWinningGoal": False,
                "emptyNet": False
            },
            "about": {
                "eventIdx": 155,
                "eventId": 278,
                "period": 2,
                "periodType": "REGULAR",
                "ordinalNum": "2nd",
                "periodTime": "04:11",
                "periodTimeRemaining": "15:49",
                "dateTime": "2022-04-10T18:36:23Z",
                "goals": {
                    "away": 0,
                    "home": 1
                }
            },
            "coordinates": {
                "x": 45.0,
                "y": -25.0
            },
            "team": {
                "id": 15,
                "name": "Washington Capitals",
                "link": "/api/v1/teams/15",
                "triCode": "WSH"
            }
        }
        expected = Goal(data)
        actual   = event_factory.create(goal_events.goal_data_two_assists)
        self.assertEqual(expected, actual)


    def test_shootout_goal(self):
        """
        Description:
            Test the constructor of a Goal event for a shootout goal.
        """
        data = {
            "players" : [ {
            "player" : {
                "fullName" : "Evan Rodrigues"
            },
            "playerType" : "Scorer"
            }, {
            "player" : {
                "fullName" : "Ilya Sorokin"
            },
            "playerType" : "Goalie"
            } ],
            "result" : {
            "event" : "Goal",
            "eventTypeId" : "GOAL",
            "description" : "Evan Rodrigues - Wrist Shot",
            "secondaryType" : "Wrist Shot",
            "strength" : {
                "code" : "EVEN",
                "name" : "Even"
            },
            "gameWinningGoal" : False
            },
            "about" : {
            "eventIdx" : 369,
            "eventId" : 939,
            "period" : 5,
            "periodType" : "SHOOTOUT",
            "ordinalNum" : "SO",
            "periodTime" : "00:00",
            "periodTimeRemaining" : "00:00",
            "dateTime" : "2022-12-20T04:49:31Z",
            "goals" : {
                "away" : 0,
                "home" : 0
            }
            },
            "team" : {
            "name" : "Washington Capitals"
            }
        }
        expected = Goal(data)
        actual   = event_factory.create(goal_events.goal_data_shootout)
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
                "periodType": "REGULAR",
                "periodTimeRemaining": "18:06",
                "dateTime": "2022-04-10T17:41:12Z",
                "goals": {
                    "home": 0,
                    "away": 1
                }
            },
            "team" : {
                "name" : "Florida Panthers"
            }
        }
        expected = Challenge(data)
        actual   = event_factory.create(miscellaneous_events.challenge_data)
        self.assertEqual(expected, actual)

    #################################################
    # Event Posts
    #################################################

    def test_game_scheduled_post(self):
        """
        Description:
            Test the expected output of a game scheduled event.
        """
        event     = event_factory.create(game_events.game_scheduled_data)
        game_data = GameData(game_events.game_data)
        actual    = event.get_post(game_data)
        expected  = None
        self.assertEqual(expected, actual)


    def test_game_end_post(self):
        """
        Description:
            Test the expected output of a game end event.
        """
        event     = event_factory.create(game_events.game_end_data)
        game_data = GameData(game_events.game_data)
        actual    = event.get_post(game_data)
        expected  = "\nThe game is over. Washington wins!\n\nFinal:\nWashington: 4\nBoston: 2\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)


    def test_game_official_post(self):
        """
        Description:
            Test the expected output of a game official event.
        """
        event     = event_factory.create(game_events.game_official_data)
        game_data = GameData(game_events.game_data)
        actual    = event.get_post(game_data)
        expected  = None
        self.assertEqual(expected, actual)


    def test_faceoff_post(self):
        """
        Description:
            Test the expected output of a faceoff event.
        """
        event     = event_factory.create(miscellaneous_events.faceoff_data)
        game_data = GameData(game_events.game_data)
        actual    = event.get_post(game_data)
        expected  = None
        self.assertEqual(expected, actual)


    def test_stoppage_post(self):
        """
        Description:
            Test the expected output of a stoppage event.
        """
        event     = event_factory.create(miscellaneous_events.stoppage_data)
        game_data = GameData(game_events.game_data)
        actual    = event.get_post(game_data)
        expected  = None
        self.assertEqual(expected, actual)


    def test_shot_post(self):
        """
        Description:
            Test the expected output of a shot event.
        """
        event     = event_factory.create(miscellaneous_events.shot_data)
        game_data = GameData(game_events.game_data)
        actual    = event.get_post(game_data)
        expected  = None
        self.assertEqual(expected, actual)


    def test_hit_post(self):
        """
        Description:
            Test the expected output of a hit event.
        """
        event     = event_factory.create(miscellaneous_events.hit_data)
        game_data = GameData(game_events.game_data)
        actual    = event.get_post(game_data)
        expected  = None
        self.assertEqual(expected, actual)


    def test_blocked_shot_post(self):
        """
        Description:
            Test the expected output of a blocked shot event.
        """
        event     = event_factory.create(miscellaneous_events.blocked_shot_data)
        game_data = GameData(game_events.game_data)
        actual    = event.get_post(game_data)
        expected  = None
        self.assertEqual(expected, actual)


    def test_giveaway_post(self):
        """
        Description:
            Test the expected output of a giveaway event.
        """
        event     = event_factory.create(miscellaneous_events.giveaway_data)
        game_data = GameData(game_events.game_data)
        actual    = event.get_post(game_data)
        expected  = None
        self.assertEqual(expected, actual)


    def test_takeaway_post(self):
        """
        Description:
            Test the expected output of a takeaway event.
        """
        event     = event_factory.create(miscellaneous_events.takeaway_data)
        game_data = GameData(game_events.game_data)
        actual    = event.get_post(game_data)
        expected  = None
        self.assertEqual(expected, actual)


    def test_missed_shot_post(self):
        """
        Description:
            Test the expected output of a missed shot event.
        """
        event     = event_factory.create(miscellaneous_events.missed_shot_data)
        game_data = GameData(game_events.game_data)
        actual    = event.get_post(game_data)
        expected  = None
        self.assertEqual(expected, actual)


    def test_penalty_post(self):
        """
        Description:
            Test the expected output of a penalty event.
        """
        event     = event_factory.create(penalty_events.penalty_data)
        game_data = GameData(game_events.game_data)
        actual    = event.get_post(game_data)
        expected  = "\nThere is a penalty on Washington.\n\nNic Dowd will serve a 2 minute minor for hi-sticking.\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)


    def test_penalty_no_taker_post(self):
        """
        Description:
            Test the expected output of a penalty event when no
            penalty taker is present in the event data.
        """
        event     = event_factory.create(penalty_events.penalty_data_no_taker)
        expected  = None
        self.assertEqual(expected, event)


    def test_penalty_shot_post(self):
        """
        Description:
            Test the expected output of a penalty shot event.
        """
        event     = event_factory.create(penalty_events.penalty_shot_data)
        game_data = GameData(game_events.game_data)
        actual    = event.get_post(game_data)
        expected  = "\nThat's a penalty shot for Washington!\n\nThe infraction is against Brenden Dillon for hooking on breakaway.\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)


    def test_period_ready_post(self):
        """
        Description:
            Test the expected output of a period ready event.
        """
        event     = event_factory.create(period_events.period_ready_data)
        game_data = GameData(game_events.game_data)
        actual    = event.get_post(game_data)
        expected  = None
        self.assertEqual(expected, actual)


    def test_period_start_post(self):
        """
        Description:
            Test the expected output of a period start event.
        """
        event     = event_factory.create(period_events.period_start_data)
        game_data = GameData(game_events.game_data)
        actual    = event.get_post(game_data)
        expected  = "\nThe second period is starting at Capital One Arena.\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)


    def test_period_end_post(self):
        """
        Description:
            Test the expected output of a period end event.
        """
        event     = event_factory.create(period_events.period_end_data)
        game_data = GameData(game_events.game_data)
        actual    = event.get_post(game_data)
        expected  = "\nThe first period is over at Capital One Arena.\n\nGoals\nWashington: 0\nBoston: 0\n\nShots on Goal\nWashington: 33\nBoston: 30\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)


    def test_period_official_post(self):
        """
        Description:
            Test the expected output of a period official event.
        """
        event     = event_factory.create(period_events.period_official_data)
        game_data = GameData(game_events.game_data)
        actual    = event.get_post(game_data)
        expected  = None
        self.assertEqual(expected, actual)


    def test_shootout_end_post(self):
        """
        Description:
            Test the expected output of a shootout end event.
        """
        event     = event_factory.create(period_events.shootout_end_data)
        game_data = GameData(game_events.game_data)
        actual    = event.get_post(game_data)
        expected  = None
        self.assertEqual(expected, actual)


    def test_goal_post(self):
        """
        Description:
            Test the expected output of a goal event.
        """
        event     = event_factory.create(goal_events.goal_data)
        game_data = GameData(game_events.game_data)
        actual    = event.get_post(game_data)
        expected  = "\nWashington goal!\n\nScored by John Carlson with 15:49 remaining in the 2nd period.\n\nAssisted by Conor Sheary.\n\nWashington: 1\nBoston: 0\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)


    def test_goal_no_scorer_post(self):
        """
        Description:
            Test the expected output of a goal event when no scorer is present
            in the event data.
        """
        event    = event_factory.create(goal_events.goal_data_no_scorer)
        expected = None
        self.assertEqual(expected, event)


    def test_power_play_goal_post(self):
        """
        Description:
            Test the expected output of a power play goal event.
        """
        event     = event_factory.create(goal_events.power_play_goal_data)
        game_data = GameData(game_events.game_data)
        actual    = event.get_post(game_data)
        expected  = "\nPower play goal for Boston!\n\nScored by J.T. Miller with 18:05 remaining in the 1st period.\n\nAssisted by Quinn Hughes.\n\nWashington: 1\nBoston: 0\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)


    def test_short_handed_goal_post(self):
        """
        Description:
            Test the expected output of a short-handed goal event.
        """
        event     = event_factory.create(goal_events.short_handed_goal_data)
        game_data = GameData(game_events.game_data)
        actual    = event.get_post(game_data)
        expected  = "\nShort-handed goal for Boston!\n\nScored by J.T. Miller with 18:05 remaining in the 1st period.\n\nAssisted by Quinn Hughes.\n\nWashington: 1\nBoston: 0\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)


    def test_empty_net_goal_post(self):
        """
        Description:
            Test the expected output of an empty net goal event.
        """
        event     = event_factory.create(goal_events.empty_net_goal_data)
        game_data = GameData(game_events.game_data)
        actual    = event.get_post(game_data)
        expected  = "\nEmpty net goal for Boston!\n\nScored by J.T. Miller with 18:05 remaining in the 1st period.\n\nAssisted by Quinn Hughes.\n\nWashington: 1\nBoston: 0\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)


    def test_challenge_post(self):
        """
        Description:
            Test the expected output of a coach's challenge event.
        """
        event     = event_factory.create(miscellaneous_events.challenge_data)
        game_data = GameData(game_events.game_data)
        actual    = event.get_post(game_data)
        expected  = "\nBoston is challenging the ruling on the play.\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)


    def test_goalpost_post(self):
        """
        Description:
            Test the expected output of a ping event.
        """
        event     = event_factory.create(miscellaneous_events.goalpost_data)
        game_data = GameData(game_events.game_data)
        actual    = event.get_post(game_data)
        expected  = "\nPing!\n\nAndrew Cogliano's shot on Jordan Binnington hit the post.\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)


    def test_crossbar_post(self):
        """
        Description:
            Test the expected output of a ping event.
        """
        event     = event_factory.create(miscellaneous_events.crossbar_data)
        game_data = GameData(game_events.game_data)
        actual    = event.get_post(game_data)
        expected  = "\nPing!\n\nNazem Kadri's shot on Jordan Binnington hit the crossbar.\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)


    def test_shootout_goal_post(self):
        """
        Description:
            Test the expected output of a shootout goal event.
        """
        event     = event_factory.create(goal_events.goal_data_shootout)
        game_data = GameData(game_events.game_data)
        actual    = event.get_post(game_data)
        expected  = "\nWashington goal!\n\nEvan Rodrigues scores against Ilya Sorokin in the shootout.\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)


    def test_shootout_miss_post(self):
        """
        Description:
            Test the expected output of a shootout miss event.
        """
        event     = event_factory.create(shot_events.shootout_miss_data)
        game_data = GameData(game_events.game_data)
        actual    = event.get_post(game_data)
        expected  = "\nWashington miss.\n\nThe shootout attempt by Simon Holmstrom missed the net.\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)


    def test_shootout_save_post(self):
        """
        Description:
            Test the expected output of a shootout save event.
        """
        event     = event_factory.create(shot_events.shootout_save_data)
        game_data = GameData(game_events.game_data)
        actual    = event.get_post(game_data)
        expected  = "\nWashington miss.\n\nAlexandar Georgiev stopped the shootout attempt by Mathew Barzal.\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)
