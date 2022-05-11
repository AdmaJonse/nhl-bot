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
