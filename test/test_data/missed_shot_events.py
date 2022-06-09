"""
TODO
"""

missed_shot_1 = {
    "players" : [ {
        "player" : {
        "id" : 8475765,
        "fullName" : "Vladimir Tarasenko",
        "link" : "/api/v1/people/8475765"
        },
        "playerType" : "Shooter"
    }, {
        "player" : {
        "id" : 8475311,
        "fullName" : "Darcy Kuemper",
        "link" : "/api/v1/people/8475311"
        },
        "playerType" : "Unknown"
    } ],
    "result" : {
        "event" : "Missed Shot",
        "eventCode" : "COL315",
        "eventTypeId" : "MISSED_SHOT",
        "description" : "Vladimir Tarasenko Wide of Net Darcy Kuemper"
    },
    "about" : {
        "eventIdx" : 127,
        "eventId" : 315,
        "period" : 2,
        "periodType" : "REGULAR",
        "ordinalNum" : "2nd",
        "periodTime" : "04:37",
        "periodTimeRemaining" : "15:23",
        "dateTime" : "2022-05-18T02:48:18Z",
        "goals" : {
        "away" : 1,
        "home" : 1
        }
    },
    "coordinates" : {
        "x" : -76.0,
        "y" : -9.0
    },
    "team" : {
        "id" : 19,
        "name" : "St. Louis Blues",
        "link" : "/api/v1/teams/19",
        "triCode" : "STL"
    }
}

missed_shot_2 = {
    "players" : [ {
        "player" : {
        "id" : 8479398,
        "fullName" : "Samuel Girard",
        "link" : "/api/v1/people/8479398"
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
        "eventCode" : "COL312",
        "eventTypeId" : "MISSED_SHOT",
        "description" : "Samuel Girard Wide of Net Jordan Binnington"
    },
    "about" : {
        "eventIdx" : 123,
        "eventId" : 312,
        "period" : 2,
        "periodType" : "REGULAR",
        "ordinalNum" : "2nd",
        "periodTime" : "04:14",
        "periodTimeRemaining" : "15:46",
        "dateTime" : "2022-05-18T02:47:55Z",
        "goals" : {
        "away" : 1,
        "home" : 1
        }
    },
    "coordinates" : {
        "x" : 38.0,
        "y" : 6.0
    },
    "team" : {
        "id" : 21,
        "name" : "Colorado Avalanche",
        "link" : "/api/v1/teams/21",
        "triCode" : "COL"
    }
}

missed_shot_3 = {
    "players" : [ {
        "player" : {
        "id" : 8471887,
        "fullName" : "Patric Hornqvist",
        "link" : "/api/v1/people/8471887"
        },
        "playerType" : "Shooter"
    }, {
        "player" : {
        "id" : 8476883,
        "fullName" : "Andrei Vasilevskiy",
        "link" : "/api/v1/people/8476883"
        },
        "playerType" : "Unknown"
    } ],
    "result" : {
        "event" : "Missed Shot",
        "eventCode" : "FLA171",
        "eventTypeId" : "MISSED_SHOT",
        "description" : "Patric Hornqvist Wide of Net Andrei Vasilevskiy"
    },
    "about" : {
        "eventIdx" : 74,
        "eventId" : 171,
        "period" : 1,
        "periodType" : "REGULAR",
        "ordinalNum" : "1st",
        "periodTime" : "13:05",
        "periodTimeRemaining" : "06:55",
        "dateTime" : "2022-05-17T23:33:57Z",
        "goals" : {
        "away" : 0,
        "home" : 0
        }
    },
    "coordinates" : {
        "x" : -80.0,
        "y" : 4.0
    },
    "team" : {
        "id" : 13,
        "name" : "Florida Panthers",
        "link" : "/api/v1/teams/13",
        "triCode" : "FLA"
    }
}

missed_shot_different_event_id = {
    "players" : [ {
        "player" : {
        "id" : 8475765,
        "fullName" : "Vladimir Tarasenko",
        "link" : "/api/v1/people/8475765"
        },
        "playerType" : "Shooter"
    }, {
        "player" : {
        "id" : 8475311,
        "fullName" : "Darcy Kuemper",
        "link" : "/api/v1/people/8475311"
        },
        "playerType" : "Unknown"
    } ],
    "result" : {
        "event" : "Missed Shot",
        "eventCode" : "COL315",
        "eventTypeId" : "MISSED_SHOT",
        "description" : "Vladimir Tarasenko Wide of Net Darcy Kuemper"
    },
    "about" : {
        "eventIdx" : 127,
        "eventId" : 666,
        "period" : 2,
        "periodType" : "REGULAR",
        "ordinalNum" : "2nd",
        "periodTime" : "04:37",
        "periodTimeRemaining" : "15:23",
        "dateTime" : "2022-05-18T02:48:18Z",
        "goals" : {
        "away" : 1,
        "home" : 1
        }
    },
    "coordinates" : {
        "x" : -76.0,
        "y" : -9.0
    },
    "team" : {
        "id" : 19,
        "name" : "St. Louis Blues",
        "link" : "/api/v1/teams/19",
        "triCode" : "STL"
    }
}

missed_shot_different_event_id_x = {
    "players" : [ {
        "player" : {
        "id" : 8475765,
        "fullName" : "Vladimir Tarasenko",
        "link" : "/api/v1/people/8475765"
        },
        "playerType" : "Shooter"
    }, {
        "player" : {
        "id" : 8475311,
        "fullName" : "Darcy Kuemper",
        "link" : "/api/v1/people/8475311"
        },
        "playerType" : "Unknown"
    } ],
    "result" : {
        "event" : "Missed Shot",
        "eventCode" : "COL315",
        "eventTypeId" : "MISSED_SHOT",
        "description" : "Vladimir Tarasenko Wide of Net Darcy Kuemper"
    },
    "about" : {
        "eventIdx" : 666,
        "eventId" : 315,
        "period" : 2,
        "periodType" : "REGULAR",
        "ordinalNum" : "2nd",
        "periodTime" : "04:37",
        "periodTimeRemaining" : "15:23",
        "dateTime" : "2022-05-18T02:48:18Z",
        "goals" : {
        "away" : 1,
        "home" : 1
        }
    },
    "coordinates" : {
        "x" : -76.0,
        "y" : -9.0
    },
    "team" : {
        "id" : 19,
        "name" : "St. Louis Blues",
        "link" : "/api/v1/teams/19",
        "triCode" : "STL"
    }
}

missed_shot_different_datetime = {
    "players" : [ {
        "player" : {
        "id" : 8475765,
        "fullName" : "Vladimir Tarasenko",
        "link" : "/api/v1/people/8475765"
        },
        "playerType" : "Shooter"
    }, {
        "player" : {
        "id" : 8475311,
        "fullName" : "Darcy Kuemper",
        "link" : "/api/v1/people/8475311"
        },
        "playerType" : "Unknown"
    } ],
    "result" : {
        "event" : "Missed Shot",
        "eventCode" : "COL315",
        "eventTypeId" : "MISSED_SHOT",
        "description" : "Vladimir Tarasenko Wide of Net Darcy Kuemper"
    },
    "about" : {
        "eventIdx" : 127,
        "eventId" : 315,
        "period" : 2,
        "periodType" : "REGULAR",
        "ordinalNum" : "2nd",
        "periodTime" : "04:37",
        "periodTimeRemaining" : "15:23",
        "dateTime" : "2022-05-18T12:48:18Z",
        "goals" : {
        "away" : 1,
        "home" : 1
        }
    },
    "coordinates" : {
        "x" : -76.0,
        "y" : -9.0
    },
    "team" : {
        "id" : 19,
        "name" : "St. Louis Blues",
        "link" : "/api/v1/teams/19",
        "triCode" : "STL"
    }
}

missed_shot_different_period = {
    "players" : [ {
        "player" : {
        "id" : 8475765,
        "fullName" : "Vladimir Tarasenko",
        "link" : "/api/v1/people/8475765"
        },
        "playerType" : "Shooter"
    }, {
        "player" : {
        "id" : 8475311,
        "fullName" : "Darcy Kuemper",
        "link" : "/api/v1/people/8475311"
        },
        "playerType" : "Unknown"
    } ],
    "result" : {
        "event" : "Missed Shot",
        "eventCode" : "COL315",
        "eventTypeId" : "MISSED_SHOT",
        "description" : "Vladimir Tarasenko Wide of Net Darcy Kuemper"
    },
    "about" : {
        "eventIdx" : 127,
        "eventId" : 315,
        "period" : 3,
        "periodType" : "REGULAR",
        "ordinalNum" : "2nd",
        "periodTime" : "04:37",
        "periodTimeRemaining" : "15:23",
        "dateTime" : "2022-05-18T02:48:18Z",
        "goals" : {
        "away" : 1,
        "home" : 1
        }
    },
    "coordinates" : {
        "x" : -76.0,
        "y" : -9.0
    },
    "team" : {
        "id" : 19,
        "name" : "St. Louis Blues",
        "link" : "/api/v1/teams/19",
        "triCode" : "STL"
    }
}

missed_shot_different_period_time = {
    "players" : [ {
        "player" : {
        "id" : 8475765,
        "fullName" : "Vladimir Tarasenko",
        "link" : "/api/v1/people/8475765"
        },
        "playerType" : "Shooter"
    }, {
        "player" : {
        "id" : 8475311,
        "fullName" : "Darcy Kuemper",
        "link" : "/api/v1/people/8475311"
        },
        "playerType" : "Unknown"
    } ],
    "result" : {
        "event" : "Missed Shot",
        "eventCode" : "COL315",
        "eventTypeId" : "MISSED_SHOT",
        "description" : "Vladimir Tarasenko Wide of Net Darcy Kuemper"
    },
    "about" : {
        "eventIdx" : 127,
        "eventId" : 315,
        "period" : 2,
        "periodType" : "REGULAR",
        "ordinalNum" : "2nd",
        "periodTime" : "04:33",
        "periodTimeRemaining" : "15:23",
        "dateTime" : "2022-05-18T02:48:18Z",
        "goals" : {
        "away" : 1,
        "home" : 1
        }
    },
    "coordinates" : {
        "x" : -76.0,
        "y" : -9.0
    },
    "team" : {
        "id" : 19,
        "name" : "St. Louis Blues",
        "link" : "/api/v1/teams/19",
        "triCode" : "STL"
    }
}

missed_shot_different_period_time_remaining = {
    "players" : [ {
        "player" : {
        "id" : 8475765,
        "fullName" : "Vladimir Tarasenko",
        "link" : "/api/v1/people/8475765"
        },
        "playerType" : "Shooter"
    }, {
        "player" : {
        "id" : 8475311,
        "fullName" : "Darcy Kuemper",
        "link" : "/api/v1/people/8475311"
        },
        "playerType" : "Unknown"
    } ],
    "result" : {
        "event" : "Missed Shot",
        "eventCode" : "COL315",
        "eventTypeId" : "MISSED_SHOT",
        "description" : "Vladimir Tarasenko Wide of Net Darcy Kuemper"
    },
    "about" : {
        "eventIdx" : 127,
        "eventId" : 315,
        "period" : 2,
        "periodType" : "REGULAR",
        "ordinalNum" : "2nd",
        "periodTime" : "04:37",
        "periodTimeRemaining" : "15:24",
        "dateTime" : "2022-05-18T02:48:18Z",
        "goals" : {
        "away" : 1,
        "home" : 1
        }
    },
    "coordinates" : {
        "x" : -76.0,
        "y" : -9.0
    },
    "team" : {
        "id" : 19,
        "name" : "St. Louis Blues",
        "link" : "/api/v1/teams/19",
        "triCode" : "STL"
    }
}

missed_shot_different_shooter = {
    "players" : [ {
        "player" : {
        "id" : 99,
        "fullName" : "Wayne Gretzky",
        "link" : "/api/v1/people/8475765"
        },
        "playerType" : "Shooter"
    }, {
        "player" : {
        "id" : 8475311,
        "fullName" : "Darcy Kuemper",
        "link" : "/api/v1/people/8475311"
        },
        "playerType" : "Unknown"
    } ],
    "result" : {
        "event" : "Missed Shot",
        "eventCode" : "COL315",
        "eventTypeId" : "MISSED_SHOT",
        "description" : "Vladimir Tarasenko Wide of Net Darcy Kuemper"
    },
    "about" : {
        "eventIdx" : 127,
        "eventId" : 315,
        "period" : 2,
        "periodType" : "REGULAR",
        "ordinalNum" : "2nd",
        "periodTime" : "04:37",
        "periodTimeRemaining" : "15:23",
        "dateTime" : "2022-05-18T02:48:18Z",
        "goals" : {
        "away" : 1,
        "home" : 1
        }
    },
    "coordinates" : {
        "x" : -76.0,
        "y" : -9.0
    },
    "team" : {
        "id" : 19,
        "name" : "St. Louis Blues",
        "link" : "/api/v1/teams/19",
        "triCode" : "STL"
    }
}

missed_shot_different_goalie = {
    "players" : [ {
        "player" : {
        "id" : 8475765,
        "fullName" : "Vladimir Tarasenko",
        "link" : "/api/v1/people/8475765"
        },
        "playerType" : "Shooter"
    }, {
        "player" : {
        "id" : 33,
        "fullName" : "Patrick Roy",
        "link" : "/api/v1/people/8475311"
        },
        "playerType" : "Unknown"
    } ],
    "result" : {
        "event" : "Missed Shot",
        "eventCode" : "COL315",
        "eventTypeId" : "MISSED_SHOT",
        "description" : "Vladimir Tarasenko Wide of Net Darcy Kuemper"
    },
    "about" : {
        "eventIdx" : 127,
        "eventId" : 315,
        "period" : 2,
        "periodType" : "REGULAR",
        "ordinalNum" : "2nd",
        "periodTime" : "04:37",
        "periodTimeRemaining" : "15:23",
        "dateTime" : "2022-05-18T02:48:18Z",
        "goals" : {
        "away" : 1,
        "home" : 1
        }
    },
    "coordinates" : {
        "x" : -76.0,
        "y" : -9.0
    },
    "team" : {
        "id" : 19,
        "name" : "St. Louis Blues",
        "link" : "/api/v1/teams/19",
        "triCode" : "STL"
    }
}