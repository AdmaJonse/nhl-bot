"""
Description:
    Test data for unit tests describing goal events.
"""

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

goal_data_time_change = {
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
        "periodTime": "04:10",
        "periodTimeRemaining": "15:50",
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

goal_data_scorer_change = {
    "players": [
        {
            "player": {
                "id": 8474590,
                "fullName": "Adam Jones",
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

goal_data_shootout = {
    "players" : [ {
        "player" : {
        "id" : 8478542,
        "fullName" : "Evan Rodrigues",
        "link" : "/api/v1/people/8478542"
        },
        "playerType" : "Scorer",
        "seasonTotal" : 0
    }, {
        "player" : {
        "id" : 8478009,
        "fullName" : "Ilya Sorokin",
        "link" : "/api/v1/people/8478009"
        },
        "playerType" : "Goalie"
    } ],
    "result" : {
        "event" : "Goal",
        "eventCode" : "COL939",
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
    "coordinates" : {
        "x" : -82.0,
        "y" : 3.0
    },
    "team" : {
        "id" : 21,
        "name" : "Washington Capitals",
        "link" : "/api/v1/teams/21",
        "triCode" : "COL"
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

goal_data_no_assists = {
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

goal_data_one_assist = {
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

goal_data_two_assists = {
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
                "id": 8477839,
                "fullName": "Adam Jones",
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

goal_data_primary_assist_change = {
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
                "fullName": "Alex Ovechkin",
                "link": "/api/v1/people/8477839"
            },
            "playerType": "Assist",
            "seasonTotal": 20
        },
        {
            "player": {
                "id": 8477839,
                "fullName": "Adam Jones",
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

goal_data_secondary_assist_change = {
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
                "id": 8477839,
                "fullName": "Alex Ovechkin",
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

power_play_goal_data = {
    "players" : [ {
      "player" : {
        "id" : 8476468,
        "fullName" : "J.T. Miller",
        "link" : "/api/v1/people/8476468"
      },
      "playerType" : "Scorer",
      "seasonTotal" : 30
    }, {
      "player" : {
        "id" : 8480800,
        "fullName" : "Quinn Hughes",
        "link" : "/api/v1/people/8480800"
      },
      "playerType" : "Assist",
      "seasonTotal" : 54
    }, {
      "player" : {
        "id" : 8479406,
        "fullName" : "Filip Gustavsson",
        "link" : "/api/v1/people/8479406"
      },
      "playerType" : "Goalie"
    } ],
    "result" : {
      "event" : "Goal",
      "eventCode" : "VAN155",
      "eventTypeId" : "GOAL",
      "description" : "J.T. Miller (30) Snap Shot, assists: Quinn Hughes (54)",
      "secondaryType" : "Snap Shot",
      "strength" : {
        "code" : "PPG",
        "name" : "Power Play"
      },
      "gameWinningGoal" : False,
      "emptyNet" : False
    },
    "about" : {
      "eventIdx" : 17,
      "eventId" : 155,
      "period" : 1,
      "periodType" : "REGULAR",
      "ordinalNum" : "1st",
      "periodTime" : "01:55",
      "periodTimeRemaining" : "18:05",
      "dateTime" : "2022-04-20T02:11:33Z",
      "goals" : {
        "away" : 0,
        "home" : 1
      }
    },
    "coordinates" : {
      "x" : -52.0,
      "y" : -22.0
    },
    "team" : {
      "id" : 23,
      "name" : "Boston Bruins",
      "link" : "/api/v1/teams/23",
      "triCode" : "VAN"
    }
}

short_handed_goal_data = {
    "players" : [ {
      "player" : {
        "id" : 8476468,
        "fullName" : "J.T. Miller",
        "link" : "/api/v1/people/8476468"
      },
      "playerType" : "Scorer",
      "seasonTotal" : 30
    }, {
      "player" : {
        "id" : 8480800,
        "fullName" : "Quinn Hughes",
        "link" : "/api/v1/people/8480800"
      },
      "playerType" : "Assist",
      "seasonTotal" : 54
    }, {
      "player" : {
        "id" : 8479406,
        "fullName" : "Filip Gustavsson",
        "link" : "/api/v1/people/8479406"
      },
      "playerType" : "Goalie"
    } ],
    "result" : {
      "event" : "Goal",
      "eventCode" : "VAN155",
      "eventTypeId" : "GOAL",
      "description" : "J.T. Miller (30) Snap Shot, assists: Quinn Hughes (54)",
      "secondaryType" : "Snap Shot",
      "strength" : {
        "code" : "SHG",
        "name" : "Short Handed"
      },
      "gameWinningGoal" : False,
      "emptyNet" : False
    },
    "about" : {
      "eventIdx" : 17,
      "eventId" : 155,
      "period" : 1,
      "periodType" : "REGULAR",
      "ordinalNum" : "1st",
      "periodTime" : "01:55",
      "periodTimeRemaining" : "18:05",
      "dateTime" : "2022-04-20T02:11:33Z",
      "goals" : {
        "away" : 0,
        "home" : 1
      }
    },
    "coordinates" : {
      "x" : -52.0,
      "y" : -22.0
    },
    "team" : {
      "id" : 23,
      "name" : "Boston Bruins",
      "link" : "/api/v1/teams/23",
      "triCode" : "VAN"
    }
}

empty_net_goal_data = {
    "players" : [ {
      "player" : {
        "id" : 8476468,
        "fullName" : "J.T. Miller",
        "link" : "/api/v1/people/8476468"
      },
      "playerType" : "Scorer",
      "seasonTotal" : 30
    }, {
      "player" : {
        "id" : 8480800,
        "fullName" : "Quinn Hughes",
        "link" : "/api/v1/people/8480800"
      },
      "playerType" : "Assist",
      "seasonTotal" : 54
    }, {
      "player" : {
        "id" : 8479406,
        "fullName" : "Filip Gustavsson",
        "link" : "/api/v1/people/8479406"
      },
      "playerType" : "Goalie"
    } ],
    "result" : {
      "event" : "Goal",
      "eventCode" : "VAN155",
      "eventTypeId" : "GOAL",
      "description" : "J.T. Miller (30) Snap Shot, assists: Quinn Hughes (54)",
      "secondaryType" : "Snap Shot",
      "strength" : {
        "code" : "EVEN",
        "name" : "Even"
      },
      "gameWinningGoal" : False,
      "emptyNet" : True
    },
    "about" : {
      "eventIdx" : 17,
      "eventId" : 155,
      "period" : 1,
      "periodType" : "REGULAR",
      "ordinalNum" : "1st",
      "periodTime" : "01:55",
      "periodTimeRemaining" : "18:05",
      "dateTime" : "2022-04-20T02:11:33Z",
      "goals" : {
        "away" : 0,
        "home" : 1
      }
    },
    "coordinates" : {
      "x" : -52.0,
      "y" : -22.0
    },
    "team" : {
      "id" : 23,
      "name" : "Boston Bruins",
      "link" : "/api/v1/teams/23",
      "triCode" : "VAN"
    }
}

goal_1 = {
    "players" : [ {
        "player" : {
        "id" : 8477501,
        "fullName" : "Valeri Nichushkin",
        "link" : "/api/v1/people/8477501"
        },
        "playerType" : "Scorer",
        "seasonTotal" : 3
    }, {
        "player" : {
        "id" : 8477492,
        "fullName" : "Nathan MacKinnon",
        "link" : "/api/v1/people/8477492"
        },
        "playerType" : "Assist",
        "seasonTotal" : 2
    }, {
        "player" : {
        "id" : 8478420,
        "fullName" : "Mikko Rantanen",
        "link" : "/api/v1/people/8478420"
        },
        "playerType" : "Assist",
        "seasonTotal" : 6
    }, {
        "player" : {
        "id" : 8476412,
        "fullName" : "Jordan Binnington",
        "link" : "/api/v1/people/8476412"
        },
        "playerType" : "Goalie"
    } ],
    "result" : {
        "event" : "Goal",
        "eventCode" : "COL308",
        "eventTypeId" : "GOAL",
        "description" : "Valeri Nichushkin (3) Wrist Shot, assists: Nathan MacKinnon (2), Mikko Rantanen (6)",
        "secondaryType" : "Wrist Shot",
        "strength" : {
        "code" : "EVEN",
        "name" : "Even"
        },
        "gameWinningGoal" : False,
        "emptyNet" : False
    },
    "about" : {
        "eventIdx" : 116,
        "eventId" : 308,
        "period" : 2,
        "periodType" : "REGULAR",
        "ordinalNum" : "2nd",
        "periodTime" : "03:14",
        "periodTimeRemaining" : "16:46",
        "dateTime" : "2022-05-18T02:45:37Z",
        "goals" : {
        "away" : 1,
        "home" : 1
        }
    },
    "coordinates" : {
        "x" : 79.0,
        "y" : 2.0
    },
    "team" : {
        "id" : 21,
        "name" : "Colorado Avalanche",
        "link" : "/api/v1/teams/21",
        "triCode" : "COL"
    }
}

goal_2 = {
    "players" : [ {
        "player" : {
        "id" : 8475158,
        "fullName" : "Ryan O'Reilly",
        "link" : "/api/v1/people/8475158"
        },
        "playerType" : "Scorer",
        "seasonTotal" : 6
    }, {
        "player" : {
        "id" : 8475170,
        "fullName" : "Brayden Schenn",
        "link" : "/api/v1/people/8475170"
        },
        "playerType" : "Assist",
        "seasonTotal" : 4
    }, {
        "player" : {
        "id" : 8475311,
        "fullName" : "Darcy Kuemper",
        "link" : "/api/v1/people/8475311"
        },
        "playerType" : "Goalie"
    } ],
    "result" : {
        "event" : "Goal",
        "eventCode" : "COL72",
        "eventTypeId" : "GOAL",
        "description" : "Ryan O'Reilly (6) Backhand, assists: Brayden Schenn (4)",
        "secondaryType" : "Backhand",
        "strength" : {
        "code" : "EVEN",
        "name" : "Even"
        },
        "gameWinningGoal" : False,
        "emptyNet" : False
    },
    "about" : {
        "eventIdx" : 36,
        "eventId" : 72,
        "period" : 1,
        "periodType" : "REGULAR",
        "ordinalNum" : "1st",
        "periodTime" : "06:25",
        "periodTimeRemaining" : "13:35",
        "dateTime" : "2022-05-18T01:58:25Z",
        "goals" : {
        "away" : 1,
        "home" : 0
        }
    },
    "coordinates" : {
        "x" : 80.0,
        "y" : -6.0
    },
    "team" : {
        "id" : 19,
        "name" : "St. Louis Blues",
        "link" : "/api/v1/teams/19",
        "triCode" : "STL"
    }
}

goal_3 = {
    "players" : [ {
        "player" : {
        "id" : 8477407,
        "fullName" : "Anthony Duclair",
        "link" : "/api/v1/people/8477407"
        },
        "playerType" : "Scorer",
        "seasonTotal" : 1
    }, {
        "player" : {
        "id" : 8476456,
        "fullName" : "Jonathan Huberdeau",
        "link" : "/api/v1/people/8476456"
        },
        "playerType" : "Assist",
        "seasonTotal" : 3
    }, {
        "player" : {
        "id" : 8477986,
        "fullName" : "Brandon Montour",
        "link" : "/api/v1/people/8477986"
        },
        "playerType" : "Assist",
        "seasonTotal" : 3
    }, {
        "player" : {
        "id" : 8476883,
        "fullName" : "Andrei Vasilevskiy",
        "link" : "/api/v1/people/8476883"
        },
        "playerType" : "Goalie"
    } ],
    "result" : {
        "event" : "Goal",
        "eventCode" : "FLA174",
        "eventTypeId" : "GOAL",
        "description" : "Anthony Duclair (1) Wrist Shot, assists: Jonathan Huberdeau (3), Brandon Montour (3)",
        "secondaryType" : "Wrist Shot",
        "strength" : {
        "code" : "EVEN",
        "name" : "Even"
        },
        "gameWinningGoal" : False,
        "emptyNet" : False
    },
    "about" : {
        "eventIdx" : 78,
        "eventId" : 174,
        "period" : 1,
        "periodType" : "REGULAR",
        "ordinalNum" : "1st",
        "periodTime" : "14:01",
        "periodTimeRemaining" : "05:59",
        "dateTime" : "2022-05-17T23:34:54Z",
        "goals" : {
        "away" : 0,
        "home" : 1
        }
    },
    "coordinates" : {
        "x" : -83.0,
        "y" : -2.0
    },
    "team" : {
        "id" : 13,
        "name" : "Florida Panthers",
        "link" : "/api/v1/teams/13",
        "triCode" : "FLA"
    }
}

goal_different_event_id = {
    "players" : [ {
        "player" : {
        "id" : 8477501,
        "fullName" : "Valeri Nichushkin",
        "link" : "/api/v1/people/8477501"
        },
        "playerType" : "Scorer",
        "seasonTotal" : 3
    }, {
        "player" : {
        "id" : 8477492,
        "fullName" : "Nathan MacKinnon",
        "link" : "/api/v1/people/8477492"
        },
        "playerType" : "Assist",
        "seasonTotal" : 2
    }, {
        "player" : {
        "id" : 8478420,
        "fullName" : "Mikko Rantanen",
        "link" : "/api/v1/people/8478420"
        },
        "playerType" : "Assist",
        "seasonTotal" : 6
    }, {
        "player" : {
        "id" : 8476412,
        "fullName" : "Jordan Binnington",
        "link" : "/api/v1/people/8476412"
        },
        "playerType" : "Goalie"
    } ],
    "result" : {
        "event" : "Goal",
        "eventCode" : "COL308",
        "eventTypeId" : "GOAL",
        "description" : "Valeri Nichushkin (3) Wrist Shot, assists: Nathan MacKinnon (2), Mikko Rantanen (6)",
        "secondaryType" : "Wrist Shot",
        "strength" : {
        "code" : "EVEN",
        "name" : "Even"
        },
        "gameWinningGoal" : False,
        "emptyNet" : False
    },
    "about" : {
        "eventIdx" : 116,
        "eventId" : 666,
        "period" : 2,
        "periodType" : "REGULAR",
        "ordinalNum" : "2nd",
        "periodTime" : "03:14",
        "periodTimeRemaining" : "16:46",
        "dateTime" : "2022-05-18T02:45:37Z",
        "goals" : {
        "away" : 1,
        "home" : 1
        }
    },
    "coordinates" : {
        "x" : 79.0,
        "y" : 2.0
    },
    "team" : {
        "id" : 21,
        "name" : "Colorado Avalanche",
        "link" : "/api/v1/teams/21",
        "triCode" : "COL"
    }
}

goal_different_event_id_x = {
    "players" : [ {
        "player" : {
        "id" : 8477501,
        "fullName" : "Valeri Nichushkin",
        "link" : "/api/v1/people/8477501"
        },
        "playerType" : "Scorer",
        "seasonTotal" : 3
    }, {
        "player" : {
        "id" : 8477492,
        "fullName" : "Nathan MacKinnon",
        "link" : "/api/v1/people/8477492"
        },
        "playerType" : "Assist",
        "seasonTotal" : 2
    }, {
        "player" : {
        "id" : 8478420,
        "fullName" : "Mikko Rantanen",
        "link" : "/api/v1/people/8478420"
        },
        "playerType" : "Assist",
        "seasonTotal" : 6
    }, {
        "player" : {
        "id" : 8476412,
        "fullName" : "Jordan Binnington",
        "link" : "/api/v1/people/8476412"
        },
        "playerType" : "Goalie"
    } ],
    "result" : {
        "event" : "Goal",
        "eventCode" : "COL308",
        "eventTypeId" : "GOAL",
        "description" : "Valeri Nichushkin (3) Wrist Shot, assists: Nathan MacKinnon (2), Mikko Rantanen (6)",
        "secondaryType" : "Wrist Shot",
        "strength" : {
        "code" : "EVEN",
        "name" : "Even"
        },
        "gameWinningGoal" : False,
        "emptyNet" : False
    },
    "about" : {
        "eventIdx" : 666,
        "eventId" : 308,
        "period" : 2,
        "periodType" : "REGULAR",
        "ordinalNum" : "2nd",
        "periodTime" : "03:14",
        "periodTimeRemaining" : "16:46",
        "dateTime" : "2022-05-18T02:45:37Z",
        "goals" : {
        "away" : 1,
        "home" : 1
        }
    },
    "coordinates" : {
        "x" : 79.0,
        "y" : 2.0
    },
    "team" : {
        "id" : 21,
        "name" : "Colorado Avalanche",
        "link" : "/api/v1/teams/21",
        "triCode" : "COL"
    }
}

goal_different_datetime = {
    "players" : [ {
        "player" : {
        "id" : 8477501,
        "fullName" : "Valeri Nichushkin",
        "link" : "/api/v1/people/8477501"
        },
        "playerType" : "Scorer",
        "seasonTotal" : 3
    }, {
        "player" : {
        "id" : 8477492,
        "fullName" : "Nathan MacKinnon",
        "link" : "/api/v1/people/8477492"
        },
        "playerType" : "Assist",
        "seasonTotal" : 2
    }, {
        "player" : {
        "id" : 8478420,
        "fullName" : "Mikko Rantanen",
        "link" : "/api/v1/people/8478420"
        },
        "playerType" : "Assist",
        "seasonTotal" : 6
    }, {
        "player" : {
        "id" : 8476412,
        "fullName" : "Jordan Binnington",
        "link" : "/api/v1/people/8476412"
        },
        "playerType" : "Goalie"
    } ],
    "result" : {
        "event" : "Goal",
        "eventCode" : "COL308",
        "eventTypeId" : "GOAL",
        "description" : "Valeri Nichushkin (3) Wrist Shot, assists: Nathan MacKinnon (2), Mikko Rantanen (6)",
        "secondaryType" : "Wrist Shot",
        "strength" : {
        "code" : "EVEN",
        "name" : "Even"
        },
        "gameWinningGoal" : False,
        "emptyNet" : False
    },
    "about" : {
        "eventIdx" : 116,
        "eventId" : 308,
        "period" : 2,
        "periodType" : "REGULAR",
        "ordinalNum" : "2nd",
        "periodTime" : "03:14",
        "periodTimeRemaining" : "16:46",
        "dateTime" : "2022-05-18T02:41:37Z",
        "goals" : {
        "away" : 1,
        "home" : 1
        }
    },
    "coordinates" : {
        "x" : 79.0,
        "y" : 2.0
    },
    "team" : {
        "id" : 21,
        "name" : "Colorado Avalanche",
        "link" : "/api/v1/teams/21",
        "triCode" : "COL"
    }
}

goal_different_period = {
    "players" : [ {
        "player" : {
        "id" : 8477501,
        "fullName" : "Valeri Nichushkin",
        "link" : "/api/v1/people/8477501"
        },
        "playerType" : "Scorer",
        "seasonTotal" : 3
    }, {
        "player" : {
        "id" : 8477492,
        "fullName" : "Nathan MacKinnon",
        "link" : "/api/v1/people/8477492"
        },
        "playerType" : "Assist",
        "seasonTotal" : 2
    }, {
        "player" : {
        "id" : 8478420,
        "fullName" : "Mikko Rantanen",
        "link" : "/api/v1/people/8478420"
        },
        "playerType" : "Assist",
        "seasonTotal" : 6
    }, {
        "player" : {
        "id" : 8476412,
        "fullName" : "Jordan Binnington",
        "link" : "/api/v1/people/8476412"
        },
        "playerType" : "Goalie"
    } ],
    "result" : {
        "event" : "Goal",
        "eventCode" : "COL308",
        "eventTypeId" : "GOAL",
        "description" : "Valeri Nichushkin (3) Wrist Shot, assists: Nathan MacKinnon (2), Mikko Rantanen (6)",
        "secondaryType" : "Wrist Shot",
        "strength" : {
        "code" : "EVEN",
        "name" : "Even"
        },
        "gameWinningGoal" : False,
        "emptyNet" : False
    },
    "about" : {
        "eventIdx" : 116,
        "eventId" : 308,
        "period" : 3,
        "periodType" : "REGULAR",
        "ordinalNum" : "2nd",
        "periodTime" : "03:14",
        "periodTimeRemaining" : "16:46",
        "dateTime" : "2022-05-18T02:45:37Z",
        "goals" : {
        "away" : 1,
        "home" : 1
        }
    },
    "coordinates" : {
        "x" : 79.0,
        "y" : 2.0
    },
    "team" : {
        "id" : 21,
        "name" : "Colorado Avalanche",
        "link" : "/api/v1/teams/21",
        "triCode" : "COL"
    }
}

goal_different_period_time = {
    "players" : [ {
        "player" : {
        "id" : 8477501,
        "fullName" : "Valeri Nichushkin",
        "link" : "/api/v1/people/8477501"
        },
        "playerType" : "Scorer",
        "seasonTotal" : 3
    }, {
        "player" : {
        "id" : 8477492,
        "fullName" : "Nathan MacKinnon",
        "link" : "/api/v1/people/8477492"
        },
        "playerType" : "Assist",
        "seasonTotal" : 2
    }, {
        "player" : {
        "id" : 8478420,
        "fullName" : "Mikko Rantanen",
        "link" : "/api/v1/people/8478420"
        },
        "playerType" : "Assist",
        "seasonTotal" : 6
    }, {
        "player" : {
        "id" : 8476412,
        "fullName" : "Jordan Binnington",
        "link" : "/api/v1/people/8476412"
        },
        "playerType" : "Goalie"
    } ],
    "result" : {
        "event" : "Goal",
        "eventCode" : "COL308",
        "eventTypeId" : "GOAL",
        "description" : "Valeri Nichushkin (3) Wrist Shot, assists: Nathan MacKinnon (2), Mikko Rantanen (6)",
        "secondaryType" : "Wrist Shot",
        "strength" : {
        "code" : "EVEN",
        "name" : "Even"
        },
        "gameWinningGoal" : False,
        "emptyNet" : False
    },
    "about" : {
        "eventIdx" : 116,
        "eventId" : 308,
        "period" : 2,
        "periodType" : "REGULAR",
        "ordinalNum" : "2nd",
        "periodTime" : "03:12",
        "periodTimeRemaining" : "16:46",
        "dateTime" : "2022-05-18T02:45:37Z",
        "goals" : {
        "away" : 1,
        "home" : 1
        }
    },
    "coordinates" : {
        "x" : 79.0,
        "y" : 2.0
    },
    "team" : {
        "id" : 21,
        "name" : "Colorado Avalanche",
        "link" : "/api/v1/teams/21",
        "triCode" : "COL"
    }
}

goal_different_period_time_remaining = {
    "players" : [ {
        "player" : {
        "id" : 8477501,
        "fullName" : "Valeri Nichushkin",
        "link" : "/api/v1/people/8477501"
        },
        "playerType" : "Scorer",
        "seasonTotal" : 3
    }, {
        "player" : {
        "id" : 8477492,
        "fullName" : "Nathan MacKinnon",
        "link" : "/api/v1/people/8477492"
        },
        "playerType" : "Assist",
        "seasonTotal" : 2
    }, {
        "player" : {
        "id" : 8478420,
        "fullName" : "Mikko Rantanen",
        "link" : "/api/v1/people/8478420"
        },
        "playerType" : "Assist",
        "seasonTotal" : 6
    }, {
        "player" : {
        "id" : 8476412,
        "fullName" : "Jordan Binnington",
        "link" : "/api/v1/people/8476412"
        },
        "playerType" : "Goalie"
    } ],
    "result" : {
        "event" : "Goal",
        "eventCode" : "COL308",
        "eventTypeId" : "GOAL",
        "description" : "Valeri Nichushkin (3) Wrist Shot, assists: Nathan MacKinnon (2), Mikko Rantanen (6)",
        "secondaryType" : "Wrist Shot",
        "strength" : {
        "code" : "EVEN",
        "name" : "Even"
        },
        "gameWinningGoal" : False,
        "emptyNet" : False
    },
    "about" : {
        "eventIdx" : 116,
        "eventId" : 308,
        "period" : 2,
        "periodType" : "REGULAR",
        "ordinalNum" : "2nd",
        "periodTime" : "03:14",
        "periodTimeRemaining" : "16:26",
        "dateTime" : "2022-05-18T02:45:37Z",
        "goals" : {
        "away" : 1,
        "home" : 1
        }
    },
    "coordinates" : {
        "x" : 79.0,
        "y" : 2.0
    },
    "team" : {
        "id" : 21,
        "name" : "Colorado Avalanche",
        "link" : "/api/v1/teams/21",
        "triCode" : "COL"
    }
}

goal_different_scorer = {
    "players" : [ {
        "player" : {
        "id" : 99,
        "fullName" : "Wayne Gretzky",
        "link" : "/api/v1/people/8477501"
        },
        "playerType" : "Scorer",
        "seasonTotal" : 3
    }, {
        "player" : {
        "id" : 8477492,
        "fullName" : "Nathan MacKinnon",
        "link" : "/api/v1/people/8477492"
        },
        "playerType" : "Assist",
        "seasonTotal" : 2
    }, {
        "player" : {
        "id" : 8478420,
        "fullName" : "Mikko Rantanen",
        "link" : "/api/v1/people/8478420"
        },
        "playerType" : "Assist",
        "seasonTotal" : 6
    }, {
        "player" : {
        "id" : 8476412,
        "fullName" : "Jordan Binnington",
        "link" : "/api/v1/people/8476412"
        },
        "playerType" : "Goalie"
    } ],
    "result" : {
        "event" : "Goal",
        "eventCode" : "COL308",
        "eventTypeId" : "GOAL",
        "description" : "Valeri Nichushkin (3) Wrist Shot, assists: Nathan MacKinnon (2), Mikko Rantanen (6)",
        "secondaryType" : "Wrist Shot",
        "strength" : {
        "code" : "EVEN",
        "name" : "Even"
        },
        "gameWinningGoal" : False,
        "emptyNet" : False
    },
    "about" : {
        "eventIdx" : 116,
        "eventId" : 308,
        "period" : 2,
        "periodType" : "REGULAR",
        "ordinalNum" : "2nd",
        "periodTime" : "03:14",
        "periodTimeRemaining" : "16:46",
        "dateTime" : "2022-05-18T02:45:37Z",
        "goals" : {
        "away" : 1,
        "home" : 1
        }
    },
    "coordinates" : {
        "x" : 79.0,
        "y" : 2.0
    },
    "team" : {
        "id" : 21,
        "name" : "Colorado Avalanche",
        "link" : "/api/v1/teams/21",
        "triCode" : "COL"
    }
}

goal_different_primary_assist = {
    "players" : [ {
        "player" : {
        "id" : 8477501,
        "fullName" : "Valeri Nichushkin",
        "link" : "/api/v1/people/8477501"
        },
        "playerType" : "Scorer",
        "seasonTotal" : 3
    }, {
        "player" : {
        "id" : 99,
        "fullName" : "Wayne Gretzky",
        "link" : "/api/v1/people/8477492"
        },
        "playerType" : "Assist",
        "seasonTotal" : 2
    }, {
        "player" : {
        "id" : 8478420,
        "fullName" : "Mikko Rantanen",
        "link" : "/api/v1/people/8478420"
        },
        "playerType" : "Assist",
        "seasonTotal" : 6
    }, {
        "player" : {
        "id" : 8476412,
        "fullName" : "Jordan Binnington",
        "link" : "/api/v1/people/8476412"
        },
        "playerType" : "Goalie"
    } ],
    "result" : {
        "event" : "Goal",
        "eventCode" : "COL308",
        "eventTypeId" : "GOAL",
        "description" : "Valeri Nichushkin (3) Wrist Shot, assists: Nathan MacKinnon (2), Mikko Rantanen (6)",
        "secondaryType" : "Wrist Shot",
        "strength" : {
        "code" : "EVEN",
        "name" : "Even"
        },
        "gameWinningGoal" : False,
        "emptyNet" : False
    },
    "about" : {
        "eventIdx" : 116,
        "eventId" : 308,
        "period" : 2,
        "periodType" : "REGULAR",
        "ordinalNum" : "2nd",
        "periodTime" : "03:14",
        "periodTimeRemaining" : "16:46",
        "dateTime" : "2022-05-18T02:45:37Z",
        "goals" : {
        "away" : 1,
        "home" : 1
        }
    },
    "coordinates" : {
        "x" : 79.0,
        "y" : 2.0
    },
    "team" : {
        "id" : 21,
        "name" : "Colorado Avalanche",
        "link" : "/api/v1/teams/21",
        "triCode" : "COL"
    }
}

goal_different_secondary_assist = {
    "players" : [ {
        "player" : {
        "id" : 8477501,
        "fullName" : "Valeri Nichushkin",
        "link" : "/api/v1/people/8477501"
        },
        "playerType" : "Scorer",
        "seasonTotal" : 3
    }, {
        "player" : {
        "id" : 8477492,
        "fullName" : "Nathan MacKinnon",
        "link" : "/api/v1/people/8477492"
        },
        "playerType" : "Assist",
        "seasonTotal" : 2
    }, {
        "player" : {
        "id" : 99,
        "fullName" : "Wayne Gretzky",
        "link" : "/api/v1/people/8478420"
        },
        "playerType" : "Assist",
        "seasonTotal" : 6
    }, {
        "player" : {
        "id" : 8476412,
        "fullName" : "Jordan Binnington",
        "link" : "/api/v1/people/8476412"
        },
        "playerType" : "Goalie"
    } ],
    "result" : {
        "event" : "Goal",
        "eventCode" : "COL308",
        "eventTypeId" : "GOAL",
        "description" : "Valeri Nichushkin (3) Wrist Shot, assists: Nathan MacKinnon (2), Mikko Rantanen (6)",
        "secondaryType" : "Wrist Shot",
        "strength" : {
        "code" : "EVEN",
        "name" : "Even"
        },
        "gameWinningGoal" : False,
        "emptyNet" : False
    },
    "about" : {
        "eventIdx" : 116,
        "eventId" : 308,
        "period" : 2,
        "periodType" : "REGULAR",
        "ordinalNum" : "2nd",
        "periodTime" : "03:14",
        "periodTimeRemaining" : "16:46",
        "dateTime" : "2022-05-18T02:45:37Z",
        "goals" : {
        "away" : 1,
        "home" : 1
        }
    },
    "coordinates" : {
        "x" : 79.0,
        "y" : 2.0
    },
    "team" : {
        "id" : 21,
        "name" : "Colorado Avalanche",
        "link" : "/api/v1/teams/21",
        "triCode" : "COL"
    }
}

goal_different_goalie = {
    "players" : [ {
        "player" : {
        "id" : 8477501,
        "fullName" : "Valeri Nichushkin",
        "link" : "/api/v1/people/8477501"
        },
        "playerType" : "Scorer",
        "seasonTotal" : 3
    }, {
        "player" : {
        "id" : 8477492,
        "fullName" : "Nathan MacKinnon",
        "link" : "/api/v1/people/8477492"
        },
        "playerType" : "Assist",
        "seasonTotal" : 2
    }, {
        "player" : {
        "id" : 8478420,
        "fullName" : "Mikko Rantanen",
        "link" : "/api/v1/people/8478420"
        },
        "playerType" : "Assist",
        "seasonTotal" : 6
    }, {
        "player" : {
        "id" : 33,
        "fullName" : "Patrick Roy",
        "link" : "/api/v1/people/8476412"
        },
        "playerType" : "Goalie"
    } ],
    "result" : {
        "event" : "Goal",
        "eventCode" : "COL308",
        "eventTypeId" : "GOAL",
        "description" : "Valeri Nichushkin (3) Wrist Shot, assists: Nathan MacKinnon (2), Mikko Rantanen (6)",
        "secondaryType" : "Wrist Shot",
        "strength" : {
        "code" : "EVEN",
        "name" : "Even"
        },
        "gameWinningGoal" : False,
        "emptyNet" : False
    },
    "about" : {
        "eventIdx" : 116,
        "eventId" : 308,
        "period" : 2,
        "periodType" : "REGULAR",
        "ordinalNum" : "2nd",
        "periodTime" : "03:14",
        "periodTimeRemaining" : "16:46",
        "dateTime" : "2022-05-18T02:45:37Z",
        "goals" : {
        "away" : 1,
        "home" : 1
        }
    },
    "coordinates" : {
        "x" : 79.0,
        "y" : 2.0
    },
    "team" : {
        "id" : 21,
        "name" : "Colorado Avalanche",
        "link" : "/api/v1/teams/21",
        "triCode" : "COL"
    }
}

goal_different_strength = {
    "players" : [ {
        "player" : {
        "id" : 8477501,
        "fullName" : "Valeri Nichushkin",
        "link" : "/api/v1/people/8477501"
        },
        "playerType" : "Scorer",
        "seasonTotal" : 3
    }, {
        "player" : {
        "id" : 8477492,
        "fullName" : "Nathan MacKinnon",
        "link" : "/api/v1/people/8477492"
        },
        "playerType" : "Assist",
        "seasonTotal" : 2
    }, {
        "player" : {
        "id" : 8478420,
        "fullName" : "Mikko Rantanen",
        "link" : "/api/v1/people/8478420"
        },
        "playerType" : "Assist",
        "seasonTotal" : 6
    }, {
        "player" : {
        "id" : 8476412,
        "fullName" : "Jordan Binnington",
        "link" : "/api/v1/people/8476412"
        },
        "playerType" : "Goalie"
    } ],
    "result" : {
        "event" : "Goal",
        "eventCode" : "COL308",
        "eventTypeId" : "GOAL",
        "description" : "Valeri Nichushkin (3) Wrist Shot, assists: Nathan MacKinnon (2), Mikko Rantanen (6)",
        "secondaryType" : "Wrist Shot",
        "strength" : {
        "code" : "PP",
        "name" : "PP"
        },
        "gameWinningGoal" : False,
        "emptyNet" : False
    },
    "about" : {
        "eventIdx" : 116,
        "eventId" : 308,
        "period" : 2,
        "periodType" : "REGULAR",
        "ordinalNum" : "2nd",
        "periodTime" : "03:14",
        "periodTimeRemaining" : "16:46",
        "dateTime" : "2022-05-18T02:45:37Z",
        "goals" : {
        "away" : 1,
        "home" : 1
        }
    },
    "coordinates" : {
        "x" : 79.0,
        "y" : 2.0
    },
    "team" : {
        "id" : 21,
        "name" : "Colorado Avalanche",
        "link" : "/api/v1/teams/21",
        "triCode" : "COL"
    }
}

goal_different_empty_net = {
    "players" : [ {
        "player" : {
        "id" : 8477501,
        "fullName" : "Valeri Nichushkin",
        "link" : "/api/v1/people/8477501"
        },
        "playerType" : "Scorer",
        "seasonTotal" : 3
    }, {
        "player" : {
        "id" : 8477492,
        "fullName" : "Nathan MacKinnon",
        "link" : "/api/v1/people/8477492"
        },
        "playerType" : "Assist",
        "seasonTotal" : 2
    }, {
        "player" : {
        "id" : 8478420,
        "fullName" : "Mikko Rantanen",
        "link" : "/api/v1/people/8478420"
        },
        "playerType" : "Assist",
        "seasonTotal" : 6
    }, {
        "player" : {
        "id" : 8476412,
        "fullName" : "Jordan Binnington",
        "link" : "/api/v1/people/8476412"
        },
        "playerType" : "Goalie"
    } ],
    "result" : {
        "event" : "Goal",
        "eventCode" : "COL308",
        "eventTypeId" : "GOAL",
        "description" : "Valeri Nichushkin (3) Wrist Shot, assists: Nathan MacKinnon (2), Mikko Rantanen (6)",
        "secondaryType" : "Wrist Shot",
        "strength" : {
        "code" : "EVEN",
        "name" : "Even"
        },
        "gameWinningGoal" : False,
        "emptyNet" : True
    },
    "about" : {
        "eventIdx" : 116,
        "eventId" : 308,
        "period" : 2,
        "periodType" : "REGULAR",
        "ordinalNum" : "2nd",
        "periodTime" : "03:14",
        "periodTimeRemaining" : "16:46",
        "dateTime" : "2022-05-18T02:45:37Z",
        "goals" : {
        "away" : 1,
        "home" : 1
        }
    },
    "coordinates" : {
        "x" : 79.0,
        "y" : 2.0
    },
    "team" : {
        "id" : 21,
        "name" : "Colorado Avalanche",
        "link" : "/api/v1/teams/21",
        "triCode" : "COL"
    }
}

goal_different_team = {
    "players" : [ {
        "player" : {
        "id" : 8477501,
        "fullName" : "Valeri Nichushkin",
        "link" : "/api/v1/people/8477501"
        },
        "playerType" : "Scorer",
        "seasonTotal" : 3
    }, {
        "player" : {
        "id" : 8477492,
        "fullName" : "Nathan MacKinnon",
        "link" : "/api/v1/people/8477492"
        },
        "playerType" : "Assist",
        "seasonTotal" : 2
    }, {
        "player" : {
        "id" : 8478420,
        "fullName" : "Mikko Rantanen",
        "link" : "/api/v1/people/8478420"
        },
        "playerType" : "Assist",
        "seasonTotal" : 6
    }, {
        "player" : {
        "id" : 8476412,
        "fullName" : "Jordan Binnington",
        "link" : "/api/v1/people/8476412"
        },
        "playerType" : "Goalie"
    } ],
    "result" : {
        "event" : "Goal",
        "eventCode" : "COL308",
        "eventTypeId" : "GOAL",
        "description" : "Valeri Nichushkin (3) Wrist Shot, assists: Nathan MacKinnon (2), Mikko Rantanen (6)",
        "secondaryType" : "Wrist Shot",
        "strength" : {
        "code" : "EVEN",
        "name" : "Even"
        },
        "gameWinningGoal" : False,
        "emptyNet" : False
    },
    "about" : {
        "eventIdx" : 116,
        "eventId" : 308,
        "period" : 2,
        "periodType" : "REGULAR",
        "ordinalNum" : "2nd",
        "periodTime" : "03:14",
        "periodTimeRemaining" : "16:46",
        "dateTime" : "2022-05-18T02:45:37Z",
        "goals" : {
        "away" : 1,
        "home" : 1
        }
    },
    "coordinates" : {
        "x" : 79.0,
        "y" : 2.0
    },
    "team" : {
        "id" : 32,
        "name" : "Seattle Kraken",
        "link" : "/api/v1/teams/32",
        "triCode" : "SEA"
    }
}
