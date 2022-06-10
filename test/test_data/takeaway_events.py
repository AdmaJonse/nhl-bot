"""
TODO
"""

takeaway_1 = {
    "players" : [ {
        "player" : {
        "id" : 8477409,
        "fullName" : "Carter Verhaeghe",
        "link" : "/api/v1/people/8477409"
        },
        "playerType" : "PlayerID"
    } ],
    "result" : {
        "event" : "Takeaway",
        "eventCode" : "FLA436",
        "eventTypeId" : "TAKEAWAY",
        "description" : "Takeaway by Carter Verhaeghe"
    },
    "about" : {
        "eventIdx" : 263,
        "eventId" : 436,
        "period" : 3,
        "periodType" : "REGULAR",
        "ordinalNum" : "3rd",
        "periodTime" : "04:58",
        "periodTimeRemaining" : "15:02",
        "dateTime" : "2022-05-18T01:12:35Z",
        "goals" : {
        "away" : 2,
        "home" : 1
        }
    },
    "coordinates" : {
        "x" : 45.0,
        "y" : -20.0
    },
    "team" : {
        "id" : 13,
        "name" : "Florida Panthers",
        "link" : "/api/v1/teams/13",
        "triCode" : "FLA"
    }
}

takeaway_2 = {
    "players" : [ {
        "player" : {
        "id" : 8474151,
        "fullName" : "Ryan McDonagh",
        "link" : "/api/v1/people/8474151"
        },
        "playerType" : "PlayerID"
    } ],
    "result" : {
        "event" : "Takeaway",
        "eventCode" : "FLA417",
        "eventTypeId" : "TAKEAWAY",
        "description" : "Takeaway by Ryan McDonagh"
    },
    "about" : {
        "eventIdx" : 203,
        "eventId" : 417,
        "period" : 2,
        "periodType" : "REGULAR",
        "ordinalNum" : "2nd",
        "periodTime" : "13:44",
        "periodTimeRemaining" : "06:16",
        "dateTime" : "2022-05-18T00:33:46Z",
        "goals" : {
        "away" : 0,
        "home" : 1
        }
    },
    "coordinates" : {
        "x" : 55.0,
        "y" : -36.0
    },
    "team" : {
        "id" : 14,
        "name" : "Tampa Bay Lightning",
        "link" : "/api/v1/teams/14",
        "triCode" : "TBL"
    }
}

takeaway_3 = {
    "players" : [ {
        "player" : {
        "id" : 8477402,
        "fullName" : "Pavel Buchnevich",
        "link" : "/api/v1/people/8477402"
        },
        "playerType" : "PlayerID"
    } ],
    "result" : {
        "event" : "Takeaway",
        "eventCode" : "COL363",
        "eventTypeId" : "TAKEAWAY",
        "description" : "Takeaway by Pavel Buchnevich"
    },
    "about" : {
        "eventIdx" : 128,
        "eventId" : 363,
        "period" : 2,
        "periodType" : "REGULAR",
        "ordinalNum" : "2nd",
        "periodTime" : "04:39",
        "periodTimeRemaining" : "15:21",
        "dateTime" : "2022-05-18T02:48:20Z",
        "goals" : {
        "away" : 1,
        "home" : 1
        }
    },
    "coordinates" : {
        "x" : 45.0,
        "y" : 39.0
    },
    "team" : {
        "id" : 19,
        "name" : "St. Louis Blues",
        "link" : "/api/v1/teams/19",
        "triCode" : "STL"
    }
}

takeaway_different_event_id = {
    "players" : [ {
        "player" : {
        "id" : 8477409,
        "fullName" : "Carter Verhaeghe",
        "link" : "/api/v1/people/8477409"
        },
        "playerType" : "PlayerID"
    } ],
    "result" : {
        "event" : "Takeaway",
        "eventCode" : "FLA436",
        "eventTypeId" : "TAKEAWAY",
        "description" : "Takeaway by Carter Verhaeghe"
    },
    "about" : {
        "eventIdx" : 263,
        "eventId" : 666,
        "period" : 3,
        "periodType" : "REGULAR",
        "ordinalNum" : "3rd",
        "periodTime" : "04:58",
        "periodTimeRemaining" : "15:02",
        "dateTime" : "2022-05-18T01:12:35Z",
        "goals" : {
        "away" : 2,
        "home" : 1
        }
    },
    "coordinates" : {
        "x" : 45.0,
        "y" : -20.0
    },
    "team" : {
        "id" : 13,
        "name" : "Florida Panthers",
        "link" : "/api/v1/teams/13",
        "triCode" : "FLA"
    }
}

takeaway_different_event_id_x = {
    "players" : [ {
        "player" : {
        "id" : 8477409,
        "fullName" : "Carter Verhaeghe",
        "link" : "/api/v1/people/8477409"
        },
        "playerType" : "PlayerID"
    } ],
    "result" : {
        "event" : "Takeaway",
        "eventCode" : "FLA436",
        "eventTypeId" : "TAKEAWAY",
        "description" : "Takeaway by Carter Verhaeghe"
    },
    "about" : {
        "eventIdx" : 666,
        "eventId" : 436,
        "period" : 3,
        "periodType" : "REGULAR",
        "ordinalNum" : "3rd",
        "periodTime" : "04:58",
        "periodTimeRemaining" : "15:02",
        "dateTime" : "2022-05-18T01:12:35Z",
        "goals" : {
        "away" : 2,
        "home" : 1
        }
    },
    "coordinates" : {
        "x" : 45.0,
        "y" : -20.0
    },
    "team" : {
        "id" : 13,
        "name" : "Florida Panthers",
        "link" : "/api/v1/teams/13",
        "triCode" : "FLA"
    }
}

takeaway_different_datetime = {
    "players" : [ {
        "player" : {
        "id" : 8477409,
        "fullName" : "Carter Verhaeghe",
        "link" : "/api/v1/people/8477409"
        },
        "playerType" : "PlayerID"
    } ],
    "result" : {
        "event" : "Takeaway",
        "eventCode" : "FLA436",
        "eventTypeId" : "TAKEAWAY",
        "description" : "Takeaway by Carter Verhaeghe"
    },
    "about" : {
        "eventIdx" : 263,
        "eventId" : 436,
        "period" : 3,
        "periodType" : "REGULAR",
        "ordinalNum" : "3rd",
        "periodTime" : "04:58",
        "periodTimeRemaining" : "15:02",
        "dateTime" : "2022-05-18T01:11:35Z",
        "goals" : {
        "away" : 2,
        "home" : 1
        }
    },
    "coordinates" : {
        "x" : 45.0,
        "y" : -20.0
    },
    "team" : {
        "id" : 13,
        "name" : "Florida Panthers",
        "link" : "/api/v1/teams/13",
        "triCode" : "FLA"
    }
}

takeaway_different_period = {
    "players" : [ {
        "player" : {
        "id" : 8477409,
        "fullName" : "Carter Verhaeghe",
        "link" : "/api/v1/people/8477409"
        },
        "playerType" : "PlayerID"
    } ],
    "result" : {
        "event" : "Takeaway",
        "eventCode" : "FLA436",
        "eventTypeId" : "TAKEAWAY",
        "description" : "Takeaway by Carter Verhaeghe"
    },
    "about" : {
        "eventIdx" : 263,
        "eventId" : 436,
        "period" : 2,
        "periodType" : "REGULAR",
        "ordinalNum" : "3rd",
        "periodTime" : "04:58",
        "periodTimeRemaining" : "15:02",
        "dateTime" : "2022-05-18T01:12:35Z",
        "goals" : {
        "away" : 2,
        "home" : 1
        }
    },
    "coordinates" : {
        "x" : 45.0,
        "y" : -20.0
    },
    "team" : {
        "id" : 13,
        "name" : "Florida Panthers",
        "link" : "/api/v1/teams/13",
        "triCode" : "FLA"
    }
}

takeaway_different_period_time = {
    "players" : [ {
        "player" : {
        "id" : 8477409,
        "fullName" : "Carter Verhaeghe",
        "link" : "/api/v1/people/8477409"
        },
        "playerType" : "PlayerID"
    } ],
    "result" : {
        "event" : "Takeaway",
        "eventCode" : "FLA436",
        "eventTypeId" : "TAKEAWAY",
        "description" : "Takeaway by Carter Verhaeghe"
    },
    "about" : {
        "eventIdx" : 263,
        "eventId" : 436,
        "period" : 3,
        "periodType" : "REGULAR",
        "ordinalNum" : "3rd",
        "periodTime" : "04:38",
        "periodTimeRemaining" : "15:02",
        "dateTime" : "2022-05-18T01:12:35Z",
        "goals" : {
        "away" : 2,
        "home" : 1
        }
    },
    "coordinates" : {
        "x" : 45.0,
        "y" : -20.0
    },
    "team" : {
        "id" : 13,
        "name" : "Florida Panthers",
        "link" : "/api/v1/teams/13",
        "triCode" : "FLA"
    }
}

takeaway_different_period_time_remaining = {
    "players" : [ {
        "player" : {
        "id" : 8477409,
        "fullName" : "Carter Verhaeghe",
        "link" : "/api/v1/people/8477409"
        },
        "playerType" : "PlayerID"
    } ],
    "result" : {
        "event" : "Takeaway",
        "eventCode" : "FLA436",
        "eventTypeId" : "TAKEAWAY",
        "description" : "Takeaway by Carter Verhaeghe"
    },
    "about" : {
        "eventIdx" : 263,
        "eventId" : 436,
        "period" : 3,
        "periodType" : "REGULAR",
        "ordinalNum" : "3rd",
        "periodTime" : "04:58",
        "periodTimeRemaining" : "15:03",
        "dateTime" : "2022-05-18T01:12:35Z",
        "goals" : {
        "away" : 2,
        "home" : 1
        }
    },
    "coordinates" : {
        "x" : 45.0,
        "y" : -20.0
    },
    "team" : {
        "id" : 13,
        "name" : "Florida Panthers",
        "link" : "/api/v1/teams/13",
        "triCode" : "FLA"
    }
}

takeaway_different_player = {
    "players" : [ {
        "player" : {
        "id" : 99,
        "fullName" : "Wayne Gretzky",
        "link" : "/api/v1/people/8477409"
        },
        "playerType" : "PlayerID"
    } ],
    "result" : {
        "event" : "Takeaway",
        "eventCode" : "FLA436",
        "eventTypeId" : "TAKEAWAY",
        "description" : "Takeaway by Carter Verhaeghe"
    },
    "about" : {
        "eventIdx" : 263,
        "eventId" : 436,
        "period" : 3,
        "periodType" : "REGULAR",
        "ordinalNum" : "3rd",
        "periodTime" : "04:58",
        "periodTimeRemaining" : "15:02",
        "dateTime" : "2022-05-18T01:12:35Z",
        "goals" : {
        "away" : 2,
        "home" : 1
        }
    },
    "coordinates" : {
        "x" : 45.0,
        "y" : -20.0
    },
    "team" : {
        "id" : 13,
        "name" : "Florida Panthers",
        "link" : "/api/v1/teams/13",
        "triCode" : "FLA"
    }
}
