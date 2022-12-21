"""
Description:
    Test data for unit tests describing miscellaneous game events.
"""

null_event = {
    "players": [
        {"player": {"fullName": ""},
        "playerType": "Scorer"},
        {"player": {"fullName": ""},
        "playerType": "Assist"},
        {"player": {"fullName": ""},
        "playerType": "Assist"},
        {"player": {"fullName": ""},
        "playerType": "Goalie"},
        {"player": {"fullName": ""},
        "playerType": "Winner"},
        {"player": {"fullName": ""},
        "playerType": "Loser"},
        {"player": {"fullName": ""},
        "playerType": "Hitter"},
        {"player": {"fullName": ""},
        "playerType": "Hittee"},
        {"player": {"fullName": ""},
        "playerType": "Shooter"},
        {"player": {"fullName": ""},
        "playerType": "Blocker"},
        {"player": {"fullName": ""},
        "playerType": "PenaltyOn"},
        {"player": {"fullName": ""},
        "playerType": "DrewBy"},
        {"player": {"fullName": ""},
        "playerType": "PlayerID"},
        {"player": {"fullName": ""},
        "playerType": "Unknown"}
    ],
    "result": {
        "description": "",
        "secondaryType": "",
        "penaltySeverity": "",
        "penaltyMinutes": ""
    },
    "about": {
        "eventIdx": 3,
        "period": 1,
        "periodType": "REGULAR",
        "periodTimeRemaining": "20:00",
        "dateTime": "2022-04-10T17:41:12Z",
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
        "name": ""
    }
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

goalpost_data = {
    "players" : [ {
        "player" : {
        "id" : 8471699,
        "fullName" : "Andrew Cogliano",
        "link" : "/api/v1/people/8471699"
        },
        "playerType" : "Shooter"
    }, {
        "player" : {
        "id" : 8476412,
        "fullName" : "Jordan Binnington",
        "link" : "/api/v1/people/8476412"
        },
        "playerType" : "Unknown"
    } ],
    "result" : {
        "event" : "Missed Shot",
        "eventCode" : "COL740",
        "eventTypeId" : "MISSED_SHOT",
        "description" : "Andrew Cogliano Goalpost Jordan Binnington"
    },
    "about" : {
        "eventIdx" : 272,
        "eventId" : 740,
        "period" : 3,
        "periodType" : "REGULAR",
        "ordinalNum" : "3rd",
        "periodTime" : "08:29",
        "periodTimeRemaining" : "11:31",
        "dateTime" : "2022-05-18T03:49:32Z",
        "goals" : {
        "away" : 1,
        "home" : 2
        }
    },
    "coordinates" : {
        "x" : -80.0,
        "y" : -1.0
    },
    "team" : {
        "id" : 21,
        "name" : "Colorado Avalanche",
        "link" : "/api/v1/teams/21",
        "triCode" : "COL"
    }
}

crossbar_data = {
    "players" : [ {
        "player" : {
        "id" : 8475172,
        "fullName" : "Nazem Kadri",
        "link" : "/api/v1/people/8475172"
        },
        "playerType" : "Shooter"
    }, {
        "player" : {
        "id" : 8476412,
        "fullName" : "Jordan Binnington",
        "link" : "/api/v1/people/8476412"
        },
        "playerType" : "Unknown"
    } ],
    "result" : {
        "event" : "Missed Shot",
        "eventCode" : "COL66",
        "eventTypeId" : "MISSED_SHOT",
        "description" : "Nazem Kadri Hit Crossbar Jordan Binnington"
    },
    "about" : {
        "eventIdx" : 25,
        "eventId" : 66,
        "period" : 1,
        "periodType" : "REGULAR",
        "ordinalNum" : "1st",
        "periodTime" : "04:21",
        "periodTimeRemaining" : "15:39",
        "dateTime" : "2022-05-18T01:55:39Z",
        "goals" : {
        "away" : 0,
        "home" : 0
        }
    },
    "coordinates" : {
        "x" : -43.0,
        "y" : -36.0
    },
    "team" : {
        "id" : 21,
        "name" : "Colorado Avalanche",
        "link" : "/api/v1/teams/21",
        "triCode" : "COL"
    }
}
