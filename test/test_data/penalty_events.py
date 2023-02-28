"""
Test data for unit tests describing penalty events.
"""

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

penalty_1 = {
    "players" : [ {
        "player" : {
        "id" : 8474151,
        "fullName" : "Ryan McDonagh",
        "link" : "/api/v1/people/8474151"
        },
        "playerType" : "PenaltyOn"
    }, {
        "player" : {
        "id" : 8477493,
        "fullName" : "Aleksander Barkov",
        "link" : "/api/v1/people/8477493"
        },
        "playerType" : "DrewBy"
    } ],
    "result" : {
        "event" : "Penalty",
        "eventCode" : "FLA497",
        "eventTypeId" : "PENALTY",
        "description" : "Ryan McDonagh Holding the stick against Aleksander Barkov",
        "secondaryType" : "Holding the stick",
        "penaltySeverity" : "Minor",
        "penaltyMinutes" : 2
    },
    "about" : {
        "eventIdx" : 121,
        "eventId" : 497,
        "period" : 2,
        "periodType" : "REGULAR",
        "ordinalNum" : "2nd",
        "periodTime" : "00:59",
        "periodTimeRemaining" : "19:01",
        "dateTime" : "2022-05-18T00:07:12Z",
        "goals" : {
        "away" : 0,
        "home" : 1
        }
    },
    "coordinates" : {
        "x" : 96.0,
        "y" : -16.0
    },
    "team" : {
        "id" : 14,
        "name" : "Tampa Bay Lightning",
        "link" : "/api/v1/teams/14",
        "triCode" : "TBL"
    }
}

penalty_2 = {
    "players" : [ {
        "player" : {
        "id" : 8477407,
        "fullName" : "Anthony Duclair",
        "link" : "/api/v1/people/8477407"
        },
        "playerType" : "PenaltyOn"
    }, {
        "player" : {
        "id" : 8479542,
        "fullName" : "Brandon Hagel",
        "link" : "/api/v1/people/8479542"
        },
        "playerType" : "DrewBy"
    } ],
    "result" : {
        "event" : "Penalty",
        "eventCode" : "FLA27",
        "eventTypeId" : "PENALTY",
        "description" : "Anthony Duclair Hi-sticking against Brandon Hagel",
        "secondaryType" : "Hi-sticking",
        "penaltySeverity" : "Minor",
        "penaltyMinutes" : 2
    },
    "about" : {
        "eventIdx" : 44,
        "eventId" : 27,
        "period" : 1,
        "periodType" : "REGULAR",
        "ordinalNum" : "1st",
        "periodTime" : "07:30",
        "periodTimeRemaining" : "12:30",
        "dateTime" : "2022-05-17T23:21:28Z",
        "goals" : {
        "away" : 0,
        "home" : 0
        }
    },
    "coordinates" : {
        "x" : 59.0,
        "y" : -25.0
    },
    "team" : {
        "id" : 13,
        "name" : "Florida Panthers",
        "link" : "/api/v1/teams/13",
        "triCode" : "FLA"
    }
}

penalty_3 = {
    "players" : [ {
        "player" : {
        "id" : 8477964,
        "fullName" : "Ivan Barbashev",
        "link" : "/api/v1/people/8477964"
        },
        "playerType" : "PenaltyOn"
    }, {
        "player" : {
        "id" : 8477444,
        "fullName" : "Andre Burakovsky",
        "link" : "/api/v1/people/8477444"
        },
        "playerType" : "DrewBy"
    } ],
    "result" : {
        "event" : "Penalty",
        "eventCode" : "COL698",
        "eventTypeId" : "PENALTY",
        "description" : "Ivan Barbashev Hooking against Andre Burakovsky",
        "secondaryType" : "Hooking",
        "penaltySeverity" : "Minor",
        "penaltyMinutes" : 2
    },
    "about" : {
        "eventIdx" : 187,
        "eventId" : 698,
        "period" : 2,
        "periodType" : "REGULAR",
        "ordinalNum" : "2nd",
        "periodTime" : "13:37",
        "periodTimeRemaining" : "06:23",
        "dateTime" : "2022-05-18T03:06:10Z",
        "goals" : {
        "away" : 1,
        "home" : 2
        }
    },
    "coordinates" : {
        "x" : 65.0,
        "y" : 1.0
    },
    "team" : {
        "id" : 19,
        "name" : "St. Louis Blues",
        "link" : "/api/v1/teams/19",
        "triCode" : "STL"
    }
}

penalty_different_event_id = {
    "players" : [ {
        "player" : {
        "id" : 8474151,
        "fullName" : "Ryan McDonagh",
        "link" : "/api/v1/people/8474151"
        },
        "playerType" : "PenaltyOn"
    }, {
        "player" : {
        "id" : 8477493,
        "fullName" : "Aleksander Barkov",
        "link" : "/api/v1/people/8477493"
        },
        "playerType" : "DrewBy"
    } ],
    "result" : {
        "event" : "Penalty",
        "eventCode" : "FLA497",
        "eventTypeId" : "PENALTY",
        "description" : "Ryan McDonagh Holding the stick against Aleksander Barkov",
        "secondaryType" : "Holding the stick",
        "penaltySeverity" : "Minor",
        "penaltyMinutes" : 2
    },
    "about" : {
        "eventIdx" : 121,
        "eventId" : 666,
        "period" : 2,
        "periodType" : "REGULAR",
        "ordinalNum" : "2nd",
        "periodTime" : "00:59",
        "periodTimeRemaining" : "19:01",
        "dateTime" : "2022-05-18T00:07:12Z",
        "goals" : {
        "away" : 0,
        "home" : 1
        }
    },
    "coordinates" : {
        "x" : 96.0,
        "y" : -16.0
    },
    "team" : {
        "id" : 14,
        "name" : "Tampa Bay Lightning",
        "link" : "/api/v1/teams/14",
        "triCode" : "TBL"
    }
}

penalty_different_event_id_x = {
    "players" : [ {
        "player" : {
        "id" : 8474151,
        "fullName" : "Ryan McDonagh",
        "link" : "/api/v1/people/8474151"
        },
        "playerType" : "PenaltyOn"
    }, {
        "player" : {
        "id" : 8477493,
        "fullName" : "Aleksander Barkov",
        "link" : "/api/v1/people/8477493"
        },
        "playerType" : "DrewBy"
    } ],
    "result" : {
        "event" : "Penalty",
        "eventCode" : "FLA497",
        "eventTypeId" : "PENALTY",
        "description" : "Ryan McDonagh Holding the stick against Aleksander Barkov",
        "secondaryType" : "Holding the stick",
        "penaltySeverity" : "Minor",
        "penaltyMinutes" : 2
    },
    "about" : {
        "eventIdx" : 666,
        "eventId" : 497,
        "period" : 2,
        "periodType" : "REGULAR",
        "ordinalNum" : "2nd",
        "periodTime" : "00:59",
        "periodTimeRemaining" : "19:01",
        "dateTime" : "2022-05-18T00:07:12Z",
        "goals" : {
        "away" : 0,
        "home" : 1
        }
    },
    "coordinates" : {
        "x" : 96.0,
        "y" : -16.0
    },
    "team" : {
        "id" : 14,
        "name" : "Tampa Bay Lightning",
        "link" : "/api/v1/teams/14",
        "triCode" : "TBL"
    }
}

penalty_different_datetime = {
    "players" : [ {
        "player" : {
        "id" : 8474151,
        "fullName" : "Ryan McDonagh",
        "link" : "/api/v1/people/8474151"
        },
        "playerType" : "PenaltyOn"
    }, {
        "player" : {
        "id" : 8477493,
        "fullName" : "Aleksander Barkov",
        "link" : "/api/v1/people/8477493"
        },
        "playerType" : "DrewBy"
    } ],
    "result" : {
        "event" : "Penalty",
        "eventCode" : "FLA497",
        "eventTypeId" : "PENALTY",
        "description" : "Ryan McDonagh Holding the stick against Aleksander Barkov",
        "secondaryType" : "Holding the stick",
        "penaltySeverity" : "Minor",
        "penaltyMinutes" : 2
    },
    "about" : {
        "eventIdx" : 121,
        "eventId" : 497,
        "period" : 2,
        "periodType" : "REGULAR",
        "ordinalNum" : "2nd",
        "periodTime" : "00:59",
        "periodTimeRemaining" : "19:01",
        "dateTime" : "2022-05-18T00:07:32Z",
        "goals" : {
        "away" : 0,
        "home" : 1
        }
    },
    "coordinates" : {
        "x" : 96.0,
        "y" : -16.0
    },
    "team" : {
        "id" : 14,
        "name" : "Tampa Bay Lightning",
        "link" : "/api/v1/teams/14",
        "triCode" : "TBL"
    }
}

penalty_different_period = {
    "players" : [ {
        "player" : {
        "id" : 8474151,
        "fullName" : "Ryan McDonagh",
        "link" : "/api/v1/people/8474151"
        },
        "playerType" : "PenaltyOn"
    }, {
        "player" : {
        "id" : 8477493,
        "fullName" : "Aleksander Barkov",
        "link" : "/api/v1/people/8477493"
        },
        "playerType" : "DrewBy"
    } ],
    "result" : {
        "event" : "Penalty",
        "eventCode" : "FLA497",
        "eventTypeId" : "PENALTY",
        "description" : "Ryan McDonagh Holding the stick against Aleksander Barkov",
        "secondaryType" : "Holding the stick",
        "penaltySeverity" : "Minor",
        "penaltyMinutes" : 2
    },
    "about" : {
        "eventIdx" : 121,
        "eventId" : 497,
        "period" : 3,
        "periodType" : "REGULAR",
        "ordinalNum" : "2nd",
        "periodTime" : "00:59",
        "periodTimeRemaining" : "19:01",
        "dateTime" : "2022-05-18T00:07:12Z",
        "goals" : {
        "away" : 0,
        "home" : 1
        }
    },
    "coordinates" : {
        "x" : 96.0,
        "y" : -16.0
    },
    "team" : {
        "id" : 14,
        "name" : "Tampa Bay Lightning",
        "link" : "/api/v1/teams/14",
        "triCode" : "TBL"
    }
}

penalty_different_period_time = {
    "players" : [ {
        "player" : {
        "id" : 8474151,
        "fullName" : "Ryan McDonagh",
        "link" : "/api/v1/people/8474151"
        },
        "playerType" : "PenaltyOn"
    }, {
        "player" : {
        "id" : 8477493,
        "fullName" : "Aleksander Barkov",
        "link" : "/api/v1/people/8477493"
        },
        "playerType" : "DrewBy"
    } ],
    "result" : {
        "event" : "Penalty",
        "eventCode" : "FLA497",
        "eventTypeId" : "PENALTY",
        "description" : "Ryan McDonagh Holding the stick against Aleksander Barkov",
        "secondaryType" : "Holding the stick",
        "penaltySeverity" : "Minor",
        "penaltyMinutes" : 2
    },
    "about" : {
        "eventIdx" : 121,
        "eventId" : 497,
        "period" : 2,
        "periodType" : "REGULAR",
        "ordinalNum" : "2nd",
        "periodTime" : "00:52",
        "periodTimeRemaining" : "19:01",
        "dateTime" : "2022-05-18T00:07:12Z",
        "goals" : {
        "away" : 0,
        "home" : 1
        }
    },
    "coordinates" : {
        "x" : 96.0,
        "y" : -16.0
    },
    "team" : {
        "id" : 14,
        "name" : "Tampa Bay Lightning",
        "link" : "/api/v1/teams/14",
        "triCode" : "TBL"
    }
}

penalty_different_period_time_remaining = {
    "players" : [ {
        "player" : {
        "id" : 8474151,
        "fullName" : "Ryan McDonagh",
        "link" : "/api/v1/people/8474151"
        },
        "playerType" : "PenaltyOn"
    }, {
        "player" : {
        "id" : 8477493,
        "fullName" : "Aleksander Barkov",
        "link" : "/api/v1/people/8477493"
        },
        "playerType" : "DrewBy"
    } ],
    "result" : {
        "event" : "Penalty",
        "eventCode" : "FLA497",
        "eventTypeId" : "PENALTY",
        "description" : "Ryan McDonagh Holding the stick against Aleksander Barkov",
        "secondaryType" : "Holding the stick",
        "penaltySeverity" : "Minor",
        "penaltyMinutes" : 2
    },
    "about" : {
        "eventIdx" : 121,
        "eventId" : 497,
        "period" : 2,
        "periodType" : "REGULAR",
        "ordinalNum" : "2nd",
        "periodTime" : "00:59",
        "periodTimeRemaining" : "19:02",
        "dateTime" : "2022-05-18T00:07:12Z",
        "goals" : {
        "away" : 0,
        "home" : 1
        }
    },
    "coordinates" : {
        "x" : 96.0,
        "y" : -16.0
    },
    "team" : {
        "id" : 14,
        "name" : "Tampa Bay Lightning",
        "link" : "/api/v1/teams/14",
        "triCode" : "TBL"
    }
}

penalty_different_taker = {
    "players" : [ {
        "player" : {
        "id" : 99,
        "fullName" : "Wayne Gretzky",
        "link" : "/api/v1/people/8474151"
        },
        "playerType" : "PenaltyOn"
    }, {
        "player" : {
        "id" : 8477493,
        "fullName" : "Aleksander Barkov",
        "link" : "/api/v1/people/8477493"
        },
        "playerType" : "DrewBy"
    } ],
    "result" : {
        "event" : "Penalty",
        "eventCode" : "FLA497",
        "eventTypeId" : "PENALTY",
        "description" : "Ryan McDonagh Holding the stick against Aleksander Barkov",
        "secondaryType" : "Holding the stick",
        "penaltySeverity" : "Minor",
        "penaltyMinutes" : 2
    },
    "about" : {
        "eventIdx" : 121,
        "eventId" : 497,
        "period" : 2,
        "periodType" : "REGULAR",
        "ordinalNum" : "2nd",
        "periodTime" : "00:59",
        "periodTimeRemaining" : "19:01",
        "dateTime" : "2022-05-18T00:07:12Z",
        "goals" : {
        "away" : 0,
        "home" : 1
        }
    },
    "coordinates" : {
        "x" : 96.0,
        "y" : -16.0
    },
    "team" : {
        "id" : 14,
        "name" : "Tampa Bay Lightning",
        "link" : "/api/v1/teams/14",
        "triCode" : "TBL"
    }
}

penalty_different_drawn_by = {
    "players" : [ {
        "player" : {
        "id" : 8474151,
        "fullName" : "Ryan McDonagh",
        "link" : "/api/v1/people/8474151"
        },
        "playerType" : "PenaltyOn"
    }, {
        "player" : {
        "id" : 99,
        "fullName" : "Wayne Gretzky",
        "link" : "/api/v1/people/8477493"
        },
        "playerType" : "DrewBy"
    } ],
    "result" : {
        "event" : "Penalty",
        "eventCode" : "FLA497",
        "eventTypeId" : "PENALTY",
        "description" : "Ryan McDonagh Holding the stick against Aleksander Barkov",
        "secondaryType" : "Holding the stick",
        "penaltySeverity" : "Minor",
        "penaltyMinutes" : 2
    },
    "about" : {
        "eventIdx" : 121,
        "eventId" : 497,
        "period" : 2,
        "periodType" : "REGULAR",
        "ordinalNum" : "2nd",
        "periodTime" : "00:59",
        "periodTimeRemaining" : "19:01",
        "dateTime" : "2022-05-18T00:07:12Z",
        "goals" : {
        "away" : 0,
        "home" : 1
        }
    },
    "coordinates" : {
        "x" : 96.0,
        "y" : -16.0
    },
    "team" : {
        "id" : 14,
        "name" : "Tampa Bay Lightning",
        "link" : "/api/v1/teams/14",
        "triCode" : "TBL"
    }
}

penalty_different_reason = {
    "players" : [ {
        "player" : {
        "id" : 8474151,
        "fullName" : "Ryan McDonagh",
        "link" : "/api/v1/people/8474151"
        },
        "playerType" : "PenaltyOn"
    }, {
        "player" : {
        "id" : 8477493,
        "fullName" : "Aleksander Barkov",
        "link" : "/api/v1/people/8477493"
        },
        "playerType" : "DrewBy"
    } ],
    "result" : {
        "event" : "Penalty",
        "eventCode" : "FLA497",
        "eventTypeId" : "PENALTY",
        "description" : "Ryan McDonagh Holding the stick against Aleksander Barkov",
        "secondaryType" : "Tripping",
        "penaltySeverity" : "Minor",
        "penaltyMinutes" : 2
    },
    "about" : {
        "eventIdx" : 121,
        "eventId" : 497,
        "period" : 2,
        "periodType" : "REGULAR",
        "ordinalNum" : "2nd",
        "periodTime" : "00:59",
        "periodTimeRemaining" : "19:01",
        "dateTime" : "2022-05-18T00:07:12Z",
        "goals" : {
        "away" : 0,
        "home" : 1
        }
    },
    "coordinates" : {
        "x" : 96.0,
        "y" : -16.0
    },
    "team" : {
        "id" : 14,
        "name" : "Tampa Bay Lightning",
        "link" : "/api/v1/teams/14",
        "triCode" : "TBL"
    }
}

penalty_different_severity = {
    "players" : [ {
        "player" : {
        "id" : 8474151,
        "fullName" : "Ryan McDonagh",
        "link" : "/api/v1/people/8474151"
        },
        "playerType" : "PenaltyOn"
    }, {
        "player" : {
        "id" : 8477493,
        "fullName" : "Aleksander Barkov",
        "link" : "/api/v1/people/8477493"
        },
        "playerType" : "DrewBy"
    } ],
    "result" : {
        "event" : "Penalty",
        "eventCode" : "FLA497",
        "eventTypeId" : "PENALTY",
        "description" : "Ryan McDonagh Holding the stick against Aleksander Barkov",
        "secondaryType" : "Holding the stick",
        "penaltySeverity" : "Major",
        "penaltyMinutes" : 2
    },
    "about" : {
        "eventIdx" : 121,
        "eventId" : 497,
        "period" : 2,
        "periodType" : "REGULAR",
        "ordinalNum" : "2nd",
        "periodTime" : "00:59",
        "periodTimeRemaining" : "19:01",
        "dateTime" : "2022-05-18T00:07:12Z",
        "goals" : {
        "away" : 0,
        "home" : 1
        }
    },
    "coordinates" : {
        "x" : 96.0,
        "y" : -16.0
    },
    "team" : {
        "id" : 14,
        "name" : "Tampa Bay Lightning",
        "link" : "/api/v1/teams/14",
        "triCode" : "TBL"
    }
}

penalty_different_minutes = {
    "players" : [ {
        "player" : {
        "id" : 8474151,
        "fullName" : "Ryan McDonagh",
        "link" : "/api/v1/people/8474151"
        },
        "playerType" : "PenaltyOn"
    }, {
        "player" : {
        "id" : 8477493,
        "fullName" : "Aleksander Barkov",
        "link" : "/api/v1/people/8477493"
        },
        "playerType" : "DrewBy"
    } ],
    "result" : {
        "event" : "Penalty",
        "eventCode" : "FLA497",
        "eventTypeId" : "PENALTY",
        "description" : "Ryan McDonagh Holding the stick against Aleksander Barkov",
        "secondaryType" : "Holding the stick",
        "penaltySeverity" : "Minor",
        "penaltyMinutes" : 4
    },
    "about" : {
        "eventIdx" : 121,
        "eventId" : 497,
        "period" : 2,
        "periodType" : "REGULAR",
        "ordinalNum" : "2nd",
        "periodTime" : "00:59",
        "periodTimeRemaining" : "19:01",
        "dateTime" : "2022-05-18T00:07:12Z",
        "goals" : {
        "away" : 0,
        "home" : 1
        }
    },
    "coordinates" : {
        "x" : 96.0,
        "y" : -16.0
    },
    "team" : {
        "id" : 14,
        "name" : "Tampa Bay Lightning",
        "link" : "/api/v1/teams/14",
        "triCode" : "TBL"
    }
}
