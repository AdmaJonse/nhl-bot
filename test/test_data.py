#################################################
# Game Data
#################################################

game_data = {
    "gameData": {
        "datetime": {
            "dateTime": "2022-04-10T17:30:00Z",
            "endDateTime": "2022-04-10T20:12:25Z"
        },
        "about": {
            "periodTimeRemaining": "20:00",
            "ordinalNum": "1st"
        },
        "teams": {
            "away": {
                "name": "Boston Bruins",
                "abbreviation": "BOS",
                "teamName": "Bruins",
                "locationName": "Boston"
            },
            "home": {
                "name": "Washington Capitals",
                "venue": {
                    "name": "Capital One Arena"
                },
                "abbreviation": "WSH",
                "teamName": "Capitals",
                "locationName": "Washington"
            }
        }
    },
    "liveData": {
        "linescore": {
            "teams": {
                "home": {
                    "team": {
                        "id": 15,
                        "name": "Washington Capitals",
                        "link": "/api/v1/teams/15",
                        "abbreviation": "WSH",
                        "triCode": "WSH"
                    },
                    "goals": 4,
                    "shotsOnGoal": 33,
                    "goaliePulled": False,
                    "numSkaters": 5,
                    "powerPlay": False
                },
                "away": {
                    "team": {
                        "id": 6,
                        "name": "Boston Bruins",
                        "link": "/api/v1/teams/6",
                        "abbreviation": "BOS",
                        "triCode": "BOS"
                    },
                    "goals": 2,
                    "shotsOnGoal": 30,
                    "goaliePulled": False,
                    "numSkaters": 5,
                    "powerPlay": False
                }
            }
        }
    }
}

#################################################
# Game Events
#################################################

game_scheduled_data = {
    "result": {
        "event": "Game Scheduled",
        "eventCode": "WSH1",
        "eventTypeId": "GAME_SCHEDULED",
        "description": "Game Scheduled"
    },
    "about": {
        "eventIdx": 0,
        "eventId": 1,
        "period": 1,
        "periodType": "REGULAR",
        "ordinalNum": "1st",
        "periodTime": "00:00",
        "periodTimeRemaining": "20:00",
        "dateTime": "2022-04-10T16:56:39Z",
        "goals": {
            "away": 0,
            "home": 0
        }
    },
    "coordinates": {}
}

game_end_data = {
    "result": {
        "event": "Game End",
        "eventCode": "WSH915",
        "eventTypeId": "GAME_END",
        "description": "Game End"
    },
    "about": {
        "eventIdx": 384,
        "eventId": 915,
        "period": 3,
        "periodType": "REGULAR",
        "ordinalNum": "3rd",
        "periodTime": "20:00",
        "periodTimeRemaining": "00:00",
        "dateTime": "2022-04-10T20:12:25Z",
        "goals": {
            "away": 2,
            "home": 4
        }
    },
    "coordinates": {}
}

game_official_data = {
    "result": {
        "event": "Game Official",
        "eventCode": "WSH916",
        "eventTypeId": "GAME_OFFICIAL",
        "description": "Game Official"
    },
    "about": {
        "eventIdx": 385,
        "eventId": 916,
        "period": 3,
        "periodType": "REGULAR",
        "ordinalNum": "3rd",
        "periodTime": "20:00",
        "periodTimeRemaining": "00:00",
        "dateTime": "2022-04-10T21:27:01Z",
        "goals": {
            "away": 2,
            "home": 4
        }
    },
    "coordinates": {}
}

faceoff_data = {
    "players": [
        {
            "player": {
                "id": 8474189,
                "fullName": "Lars Eller",
                "link": "/api/v1/people/8474189"
            },
            "playerType": "Winner"
        },
        {
            "player": {
                "id": 8475745,
                "fullName": "Charlie Coyle",
                "link": "/api/v1/people/8475745"
            },
            "playerType": "Loser"
        }
    ],
    "result": {
        "event": "Faceoff",
        "eventCode": "WSH9",
        "eventTypeId": "FACEOFF",
        "description": "Lars Eller faceoff won against Charlie Coyle"
    },
    "about": {
        "eventIdx": 3,
        "eventId": 9,
        "period": 1,
        "periodType": "REGULAR",
        "ordinalNum": "1st",
        "periodTime": "00:00",
        "periodTimeRemaining": "20:00",
        "dateTime": "2022-04-10T17:33:32Z",
        "goals": {
            "away": 0,
            "home": 0
        }
    },
    "coordinates": {
        "x": 0.0,
        "y": 0.0
    },
    "team": {
        "id": 15,
        "name": "Washington Capitals",
        "link": "/api/v1/teams/15",
        "triCode": "WSH"
    }
}

stoppage_data = {
    "result": {
        "event": "Stoppage",
        "eventCode": "WSH152",
        "eventTypeId": "STOP",
        "description": "Puck in Netting"
    },
    "about": {
        "eventIdx": 6,
        "eventId": 152,
        "period": 1,
        "periodType": "REGULAR",
        "ordinalNum": "1st",
        "periodTime": "00:41",
        "periodTimeRemaining": "19:19",
        "dateTime": "2022-04-10T17:34:13Z",
        "goals": {
            "away": 0,
            "home": 0
        }
    },
    "coordinates": {}
}

shot_data = {
    "players": [
        {
            "player": {
                "id": 8475744,
                "fullName": "Evgeny Kuznetsov",
                "link": "/api/v1/people/8475744"
            },
            "playerType": "Shooter"
        },
        {
            "player": {
                "id": 8476999,
                "fullName": "Linus Ullmark",
                "link": "/api/v1/people/8476999"
            },
            "playerType": "Goalie"
        }
    ],
    "result": {
        "event": "Shot",
        "eventCode": "WSH755",
        "eventTypeId": "SHOT",
        "description": "Evgeny Kuznetsov Wrist Shot saved by Linus Ullmark",
        "secondaryType": "Wrist Shot"
    },
    "about": {
        "eventIdx": 12,
        "eventId": 755,
        "period": 1,
        "periodType": "REGULAR",
        "ordinalNum": "1st",
        "periodTime": "01:46",
        "periodTimeRemaining": "18:14",
        "dateTime": "2022-04-10T17:35:55Z",
        "goals": {
            "away": 0,
            "home": 0
        }
    },
    "coordinates": {
        "x": -85.0,
        "y": -26.0
    },
    "team": {
        "id": 15,
        "name": "Washington Capitals",
        "link": "/api/v1/teams/15",
        "triCode": "WSH"
    }
}

hit_data = {
    "players": [
        {
            "player": {
                "id": 8471214,
                "fullName": "Alex Ovechkin",
                "link": "/api/v1/people/8471214"
            },
            "playerType": "Hitter"
        },
        {
            "player": {
                "id": 8477508,
                "fullName": "Curtis Lazar",
                "link": "/api/v1/people/8477508"
            },
            "playerType": "Hittee"
        }
    ],
    "result": {
        "event": "Hit",
        "eventCode": "WSH158",
        "eventTypeId": "HIT",
        "description": "Alex Ovechkin hit Curtis Lazar"
    },
    "about": {
        "eventIdx": 15,
        "eventId": 158,
        "period": 1,
        "periodType": "REGULAR",
        "ordinalNum": "1st",
        "periodTime": "02:05",
        "periodTimeRemaining": "17:55",
        "dateTime": "2022-04-10T17:36:40Z",
        "goals": {
            "away": 0,
            "home": 0
        }
    },
    "coordinates": {
        "x": -95.0,
        "y": -3.0
    },
    "team": {
        "id": 15,
        "name": "Washington Capitals",
        "link": "/api/v1/teams/15",
        "triCode": "WSH"
    }
}

blocked_shot_data = {
    "players": [
        {
            "player": {
                "id": 8474602,
                "fullName": "Justin Schultz",
                "link": "/api/v1/people/8474602"
            },
            "playerType": "Blocker"
        },
        {
            "player": {
                "id": 8477931,
                "fullName": "Tomas Nosek",
                "link": "/api/v1/people/8477931"
            },
            "playerType": "Shooter"
        }
    ],
    "result": {
        "event": "Blocked Shot",
        "eventCode": "WSH19",
        "eventTypeId": "BLOCKED_SHOT",
        "description": "Tomas Nosek shot blocked shot by Justin Schultz"
    },
    "about": {
        "eventIdx": 31,
        "eventId": 19,
        "period": 1,
        "periodType": "REGULAR",
        "ordinalNum": "1st",
        "periodTime": "05:39",
        "periodTimeRemaining": "14:21",
        "dateTime": "2022-04-10T17:41:12Z",
        "goals": {
            "away": 0,
            "home": 0
        }
    },
    "coordinates": {
        "x": 77.0,
        "y": 19.0
    },
    "team": {
        "id": 15,
        "name": "Washington Capitals",
        "link": "/api/v1/teams/15",
        "triCode": "WSH"
    }
}

giveaway_data = {
    "players": [
        {
            "player": {
                "id": 8478443,
                "fullName": "Brandon Carlo",
                "link": "/api/v1/people/8478443"
            },
            "playerType": "PlayerID"
        }
    ],
    "result": {
        "event": "Giveaway",
        "eventCode": "WSH163",
        "eventTypeId": "GIVEAWAY",
        "description": "Giveaway by Brandon Carlo"
    },
    "about": {
        "eventIdx": 24,
        "eventId": 163,
        "period": 1,
        "periodType": "REGULAR",
        "ordinalNum": "1st",
        "periodTime": "03:38",
        "periodTimeRemaining": "16:22",
        "dateTime": "2022-04-10T17:38:40Z",
        "goals": {
            "away": 0,
            "home": 0
        }
    },
    "coordinates": {
        "x": -98.0,
        "y": -5.0
    },
    "team": {
        "id": 6,
        "name": "Boston Bruins",
        "link": "/api/v1/teams/6",
        "triCode": "BOS"
    }
}

takeaway_data = {
    "players": [
        {
            "player": {
                "id": 8475728,
                "fullName": "Johan Larsson",
                "link": "/api/v1/people/8475728"
            },
            "playerType": "PlayerID"
        }
    ],
    "result": {
        "event": "Takeaway",
        "eventCode": "WSH153",
        "eventTypeId": "TAKEAWAY",
        "description": "Takeaway by Johan Larsson"
    },
    "about": {
        "eventIdx": 8,
        "eventId": 153,
        "period": 1,
        "periodType": "REGULAR",
        "ordinalNum": "1st",
        "periodTime": "01:06",
        "periodTimeRemaining": "18:54",
        "dateTime": "2022-04-10T17:35:15Z",
        "goals": {
            "away": 0,
            "home": 0
        }
    },
    "coordinates": {
        "x": -12.0,
        "y": -36.0
    },
    "team": {
        "id": 15,
        "name": "Washington Capitals",
        "link": "/api/v1/teams/15",
        "triCode": "WSH"
    }
}

missed_shot_data = {
    "players": [
        {
            "player": {
                "id": 8479325,
                "fullName": "Charlie McAvoy",
                "link": "/api/v1/people/8479325"
            },
            "playerType": "Shooter"
        },
        {
            "player": {
                "id": 8477970,
                "fullName": "Vitek Vanecek",
                "link": "/api/v1/people/8477970"
            },
            "playerType": "Unknown"
        }
    ],
    "result": {
        "event": "Missed Shot",
        "eventCode": "WSH14",
        "eventTypeId": "MISSED_SHOT",
        "description": "Charlie McAvoy Wide of Net Vitek Vanecek"
    },
    "about": {
        "eventIdx": 17,
        "eventId": 14,
        "period": 1,
        "periodType": "REGULAR",
        "ordinalNum": "1st",
        "periodTime": "02:21",
        "periodTimeRemaining": "17:39",
        "dateTime": "2022-04-10T17:36:56Z",
        "goals": {
            "away": 0,
            "home": 0
        }
    },
    "coordinates": {
        "x": 34.0,
        "y": -31.0
    },
    "team": {
        "id": 6,
        "name": "Boston Bruins",
        "link": "/api/v1/teams/6",
        "triCode": "BOS"
    }
}

penalty_data = {
    "players": [
        {
            "player": {
                "id": 8475343,
                "fullName": "Nic Dowd",
                "link": "/api/v1/people/8475343"
            },
            "playerType": "PenaltyOn"
        },
        {
            "player": {
                "id": 8477384,
                "fullName": "Josh Brown",
                "link": "/api/v1/people/8477384"
            },
            "playerType": "DrewBy"
        }
    ],
    "result": {
        "event": "Penalty",
        "eventCode": "WSH86",
        "eventTypeId": "PENALTY",
        "description": "Nic Dowd Hi-sticking against Josh Brown",
        "secondaryType": "Hi-sticking",
        "penaltySeverity": "Minor",
        "penaltyMinutes": 2
    },
    "about": {
        "eventIdx": 77,
        "eventId": 86,
        "period": 1,
        "periodType": "REGULAR",
        "ordinalNum": "1st",
        "periodTime": "11:47",
        "periodTimeRemaining": "08:13",
        "dateTime": "2022-04-10T17:57:07Z",
        "goals": {
            "away": 0,
            "home": 0
        }
    },
    "coordinates": {
        "x": -97.0,
        "y": 19.0
    },
    "team": {
        "id": 15,
        "name": "Washington Capitals",
        "link": "/api/v1/teams/15",
        "triCode": "WSH"
    }
}

penalty_data_no_taker = {
    "players": [
        {
            "player": {
                "id": 8477384,
                "fullName": "Josh Brown",
                "link": "/api/v1/people/8477384"
            },
            "playerType": "DrewBy"
        }
    ],
    "result": {
        "event": "Penalty",
        "eventCode": "WSH86",
        "eventTypeId": "PENALTY",
        "description": "Nic Dowd Hi-sticking against Josh Brown",
        "secondaryType": "Hi-sticking",
        "penaltySeverity": "Minor",
        "penaltyMinutes": 2
    },
    "about": {
        "eventIdx": 77,
        "eventId": 86,
        "period": 1,
        "periodType": "REGULAR",
        "ordinalNum": "1st",
        "periodTime": "11:47",
        "periodTimeRemaining": "08:13",
        "dateTime": "2022-04-10T17:57:07Z",
        "goals": {
            "away": 0,
            "home": 0
        }
    },
    "coordinates": {
        "x": -97.0,
        "y": 19.0
    },
    "team": {
        "id": 15,
        "name": "Washington Capitals",
        "link": "/api/v1/teams/15",
        "triCode": "WSH"
    }
}

penalty_shot_data = {
    "players" : [ {
      "player" : {
        "id" : 8475455,
        "fullName" : "Brenden Dillon",
        "link" : "/api/v1/people/8475455"
      },
      "playerType" : "PenaltyOn"
    }, {
      "player" : {
        "id" : 8477456,
        "fullName" : "J.T. Compher",
        "link" : "/api/v1/people/8477456"
      },
      "playerType" : "DrewBy"
    } ],
    "result" : {
      "event" : "Penalty",
      "eventCode" : "WPG287",
      "eventTypeId" : "PENALTY",
      "description" : "Brenden Dillon PS - Hooking on breakaway against J.T. Compher",
      "secondaryType" : "PS - Hooking on breakaway",
      "penaltySeverity" : "Penalty Shot",
      "penaltyMinutes" : 0
    },
    "about" : {
      "eventIdx" : 212,
      "eventId" : 287,
      "period" : 2,
      "periodType" : "REGULAR",
      "ordinalNum" : "2nd",
      "periodTime" : "17:18",
      "periodTimeRemaining" : "02:42",
      "dateTime" : "2022-04-09T01:34:36Z",
      "goals" : {
        "away" : 3,
        "home" : 2
      }
    },
    "coordinates" : {
      "x" : -75.0,
      "y" : 0.0
    },
    "team" : {
      "id" : 52,
      "name" : "Boston Bruins",
      "link" : "/api/v1/teams/52",
      "triCode" : "WPG"
    }
}

period_ready_data = {
    "result": {
        "event": "Period Ready",
        "eventCode": "WSH5",
        "eventTypeId": "PERIOD_READY",
        "description": "Period Ready"
    },
    "about": {
        "eventIdx": 1,
        "eventId": 5,
        "period": 1,
        "periodType": "REGULAR",
        "ordinalNum": "1st",
        "periodTime": "00:00",
        "periodTimeRemaining": "20:00",
        "dateTime": "2022-04-10T17:32:15Z",
        "goals": {
            "away": 0,
            "home": 0
        }
    },
    "coordinates": {}
}

period_start_data = {
    "result": {
        "event": "Period Start",
        "eventCode": "WSH504",
        "eventTypeId": "PERIOD_START",
        "description": "Period Start"
    },
    "about": {
        "eventIdx": 124,
        "eventId": 504,
        "period": 2,
        "periodType": "REGULAR",
        "ordinalNum": "2nd",
        "periodTime": "00:00",
        "periodTimeRemaining": "20:00",
        "dateTime": "2022-04-10T18:28:48Z",
        "goals": {
            "away": 0,
            "home": 0
        }
    },
    "coordinates": {}
}

period_end_data = {
    "result": {
        "event": "Period End",
        "eventCode": "WSH261",
        "eventTypeId": "PERIOD_END",
        "description": "End of 1st Period"
    },
    "about": {
        "eventIdx": 121,
        "eventId": 261,
        "period": 1,
        "periodType": "REGULAR",
        "ordinalNum": "1st",
        "periodTime": "20:00",
        "periodTimeRemaining": "00:00",
        "dateTime": "2022-04-10T18:10:01Z",
        "goals": {
            "away": 0,
            "home": 0
        }
    },
    "coordinates": {}
}

period_official_data = {
    "result": {
        "event": "Period Official",
        "eventCode": "WSH264",
        "eventTypeId": "PERIOD_OFFICIAL",
        "description": "Period Official"
    },
    "about": {
        "eventIdx": 122,
        "eventId": 264,
        "period": 1,
        "periodType": "REGULAR",
        "ordinalNum": "1st",
        "periodTime": "20:00",
        "periodTimeRemaining": "00:00",
        "dateTime": "2022-04-10T18:26:05Z",
        "goals": {
            "away": 0,
            "home": 0
        }
    },
    "coordinates": {}
}

goal_data = {
    "players": [
        {
            "player": {
                "id": 8474590,
                "fullName": "John Carlson",
                "link": "/api/v1/people/8474590"
            },
            "playerType": "Scorer",
            "seasonTotal": 14
        },
        {
            "player": {
                "id": 8477839,
                "fullName": "Conor Sheary",
                "link": "/api/v1/people/8477839"
            },
            "playerType": "Assist",
            "seasonTotal": 20
        },
        {
            "player": {
                "id": 8476999,
                "fullName": "Linus Ullmark",
                "link": "/api/v1/people/8476999"
            },
            "playerType": "Goalie"
        }
    ],
    "result": {
        "event": "Goal",
        "eventCode": "WSH278",
        "eventTypeId": "GOAL",
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

goal_data_no_scorer = {
    "players": [
        {
            "player": {
                "id": 8477839,
                "fullName": "Conor Sheary",
                "link": "/api/v1/people/8477839"
            },
            "playerType": "Assist",
            "seasonTotal": 20
        },
        {
            "player": {
                "id": 8476999,
                "fullName": "Linus Ullmark",
                "link": "/api/v1/people/8476999"
            },
            "playerType": "Goalie"
        }
    ],
    "result": {
        "event": "Goal",
        "eventCode": "WSH278",
        "eventTypeId": "GOAL",
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

challenge_data = {
    "result" : {
      "event" : "Official Challenge",
      "eventCode" : "COL405",
      "eventTypeId" : "CHALLENGE",
      "description" : "Coach's Challenge"
    },
    "about" : {
      "eventIdx" : 105,
      "eventId" : 405,
      "period" : 2,
      "periodType" : "REGULAR",
      "ordinalNum" : "2nd",
      "periodTime" : "01:54",
      "periodTimeRemaining" : "18:06",
      "dateTime" : "2022-04-01T02:05:31Z",
      "goals" : {
        "away" : 0,
        "home" : 1
      }
    },
    "coordinates" : { },
    "team" : {
      "id" : 28,
      "name" : "Boston Bruins",
      "link" : "/api/v1/teams/28",
      "triCode" : "BOS"
    }
}

#################################################
# Schedule Data
#################################################

valid_schedule_data = {
    "copyright" : "NHL and the NHL Shield are registered trademarks of the National Hockey League. NHL and NHL team marks are the property of the NHL and its teams. © NHL 2022. All Rights Reserved.",
    "totalItems" : 1,
    "totalEvents" : 0,
    "totalGames" : 1,
    "totalMatches" : 0,
    "metaData" : {
        "timeStamp" : "20220412_013822"
    },
    "wait" : 10,
    "dates" : [ {
        "date" : "2022-04-11",
        "totalItems" : 1,
        "totalEvents" : 0,
        "totalGames" : 1,
        "totalMatches" : 0,
        "games" : [ {
        "gamePk" : 2021021162,
        "link" : "/api/v1/game/2021021162/feed/live",
        "gameType" : "R",
        "season" : "20212022",
        "gameDate" : "2022-04-11T23:00:00Z",
        "status" : {
            "abstractGameState" : "Final",
            "codedGameState" : "6",
            "detailedState" : "Final",
            "statusCode" : "6",
            "startTimeTBD" : False
        },
        "teams" : {
            "away" : {
            "leagueRecord" : {
                "wins" : 35,
                "losses" : 28,
                "ot" : 11,
                "type" : "league"
            },
            "score" : 4,
            "team" : {
                "id" : 52,
                "name" : "Winnipeg Jets",
                "link" : "/api/v1/teams/52"
            }
            },
            "home" : {
            "leagueRecord" : {
                "wins" : 20,
                "losses" : 42,
                "ot" : 11,
                "type" : "league"
            },
            "score" : 2,
            "team" : {
                "id" : 8,
                "name" : "Montréal Canadiens",
                "link" : "/api/v1/teams/8"
            }
            }
        },
        "venue" : {
            "name" : "Centre Bell",
            "link" : "/api/v1/venues/null"
        },
        "content" : {
            "link" : "/api/v1/game/2021021162/content"
        }
        } ],
        "events" : [ ],
        "matches" : [ ]
    } ]
}


invalid_schedule_data = {
    "copyright" : "NHL and the NHL Shield are registered trademarks of the National Hockey League. NHL and NHL team marks are the property of the NHL and its teams. © NHL 2022. All Rights Reserved.",
    "totalItems" : 0,
    "totalEvents" : 0,
    "totalGames" : 0,
    "totalMatches" : 0,
    "metaData" : {
        "timeStamp" : "20220412_013745"
    },
    "wait" : 10,
    "dates" : [ ]
}