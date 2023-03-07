"""
Test events for Blocked Shots.
"""

blocked_shot_1 = {
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

blocked_shot_2 = {
    "players" : [ {
        "player" : {
        "id" : 8475753,
        "fullName" : "Justin Faulk",
        "link" : "/api/v1/people/8475753"
        },
        "playerType" : "Blocker"
    }, {
        "player" : {
        "id" : 8479398,
        "fullName" : "Samuel Girard",
        "link" : "/api/v1/people/8479398"
        },
        "playerType" : "Shooter"
    } ],
    "result" : {
        "event" : "Blocked Shot",
        "eventCode" : "COL30",
        "eventTypeId" : "BLOCKED_SHOT",
        "description" : "Samuel Girard shot blocked shot by Justin Faulk"
    },
    "about" : {
        "eventIdx" : 83,
        "eventId" : 30,
        "period" : 1,
        "periodType" : "REGULAR",
        "ordinalNum" : "1st",
        "periodTime" : "18:32",
        "periodTimeRemaining" : "01:28",
        "dateTime" : "2022-05-18T02:20:04Z",
        "goals" : {
        "away" : 1,
        "home" : 0
        }
    },
    "coordinates" : {
        "x" : -67.0,
        "y" : -11.0
    },
    "team" : {
        "id" : 19,
        "name" : "St. Louis Blues",
        "link" : "/api/v1/teams/19",
        "triCode" : "STL"
    }
}

blocked_shot_3 = {
    "players" : [ {
        "player" : {
        "id" : 8475279,
        "fullName" : "Ben Chiarot",
        "link" : "/api/v1/people/8475279"
        },
        "playerType" : "Blocker"
    }, {
        "player" : {
        "id" : 8479984,
        "fullName" : "Cal Foote",
        "link" : "/api/v1/people/8479984"
        },
        "playerType" : "Shooter"
    } ],
    "result" : {
        "event" : "Blocked Shot",
        "eventCode" : "FLA158",
        "eventTypeId" : "BLOCKED_SHOT",
        "description" : "Cal Foote shot blocked shot by Ben Chiarot"
    },
    "about" : {
        "eventIdx" : 27,
        "eventId" : 158,
        "period" : 1,
        "periodType" : "REGULAR",
        "ordinalNum" : "1st",
        "periodTime" : "04:44",
        "periodTimeRemaining" : "15:16",
        "dateTime" : "2022-05-17T23:18:19Z",
        "goals" : {
        "away" : 0,
        "home" : 0
        }
    },
    "coordinates" : {
        "x" : 71.0,
        "y" : -13.0
    },
    "team" : {
        "id" : 13,
        "name" : "Florida Panthers",
        "link" : "/api/v1/teams/13",
        "triCode" : "FLA"
    }
}

blocked_shot_different_event_id = {
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
        "eventId": 666,
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

blocked_shot_different_event_id_x = {
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
        "eventIdx": 666,
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

blocked_shot_different_datetime = {
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
        "dateTime": "2022-04-10T17:42:12Z",
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

blocked_shot_different_period = {
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
        "period": 2,
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

blocked_shot_different_period_time = {
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
        "periodTime": "06:39",
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

blocked_shot_different_period_time_remaining = {
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
        "periodTimeRemaining": "12:21",
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

blocked_shot_different_shooter = {
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
                "id": 99,
                "fullName": "Wayne Gretzky",
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

blocked_shot_different_blocker = {
    "players": [
        {
            "player": {
                "id": 99,
                "fullName": "Wayne Gretzky",
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
