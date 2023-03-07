"""
Test events for giveaways.
"""

giveaway_1 = {
    "players" : [ {
        "player" : {
        "id" : 8475158,
        "fullName" : "Ryan O'Reilly",
        "link" : "/api/v1/people/8475158"
        },
        "playerType" : "PlayerID"
    } ],
    "result" : {
        "event" : "Giveaway",
        "eventCode" : "COL92",
        "eventTypeId" : "GIVEAWAY",
        "description" : "Giveaway by Ryan O'Reilly"
    },
    "about" : {
        "eventIdx" : 87,
        "eventId" : 92,
        "period" : 1,
        "periodType" : "REGULAR",
        "ordinalNum" : "1st",
        "periodTime" : "19:40",
        "periodTimeRemaining" : "00:20",
        "dateTime" : "2022-05-18T02:21:12Z",
        "goals" : {
        "away" : 1,
        "home" : 0
        }
    },
    "coordinates" : {
        "x" : 81.0,
        "y" : 32.0
    },
    "team" : {
        "id" : 19,
        "name" : "St. Louis Blues",
        "link" : "/api/v1/teams/19",
        "triCode" : "STL"
    }
}

giveaway_2 = {
    "players" : [ {
        "player" : {
        "id" : 8479398,
        "fullName" : "Samuel Girard",
        "link" : "/api/v1/people/8479398"
        },
        "playerType" : "PlayerID"
    } ],
    "result" : {
        "event" : "Giveaway",
        "eventCode" : "COL29",
        "eventTypeId" : "GIVEAWAY",
        "description" : "Giveaway by Samuel Girard"
    },
    "about" : {
        "eventIdx" : 80,
        "eventId" : 29,
        "period" : 1,
        "periodType" : "REGULAR",
        "ordinalNum" : "1st",
        "periodTime" : "18:02",
        "periodTimeRemaining" : "01:58",
        "dateTime" : "2022-05-18T02:19:34Z",
        "goals" : {
        "away" : 1,
        "home" : 0
        }
    },
    "coordinates" : {
        "x" : 98.0,
        "y" : -10.0
    },
    "team" : {
        "id" : 21,
        "name" : "Colorado Avalanche",
        "link" : "/api/v1/teams/21",
        "triCode" : "COL"
    }
}

giveaway_3 = {
    "players" : [ {
        "player" : {
        "id" : 8475462,
        "fullName" : "Radko Gudas",
        "link" : "/api/v1/people/8475462"
        },
        "playerType" : "PlayerID"
    } ],
    "result" : {
        "event" : "Giveaway",
        "eventCode" : "FLA123",
        "eventTypeId" : "GIVEAWAY",
        "description" : "Giveaway by Radko Gudas"
    },
    "about" : {
        "eventIdx" : 65,
        "eventId" : 123,
        "period" : 1,
        "periodType" : "REGULAR",
        "ordinalNum" : "1st",
        "periodTime" : "11:21",
        "periodTimeRemaining" : "08:39",
        "dateTime" : "2022-05-17T23:31:31Z",
        "goals" : {
        "away" : 0,
        "home" : 0
        }
    },
    "coordinates" : {
        "x" : 31.0,
        "y" : 40.0
    },
    "team" : {
        "id" : 13,
        "name" : "Florida Panthers",
        "link" : "/api/v1/teams/13",
        "triCode" : "FLA"
    }
}

giveaway_different_event_id = {
    "players" : [ {
        "player" : {
        "id" : 8475158,
        "fullName" : "Ryan O'Reilly",
        "link" : "/api/v1/people/8475158"
        },
        "playerType" : "PlayerID"
    } ],
    "result" : {
        "event" : "Giveaway",
        "eventCode" : "COL92",
        "eventTypeId" : "GIVEAWAY",
        "description" : "Giveaway by Ryan O'Reilly"
    },
    "about" : {
        "eventIdx" : 87,
        "eventId" : 666,
        "period" : 1,
        "periodType" : "REGULAR",
        "ordinalNum" : "1st",
        "periodTime" : "19:40",
        "periodTimeRemaining" : "00:20",
        "dateTime" : "2022-05-18T02:21:12Z",
        "goals" : {
        "away" : 1,
        "home" : 0
        }
    },
    "coordinates" : {
        "x" : 81.0,
        "y" : 32.0
    },
    "team" : {
        "id" : 19,
        "name" : "St. Louis Blues",
        "link" : "/api/v1/teams/19",
        "triCode" : "STL"
    }
}

giveaway_different_event_id_x = {
    "players" : [ {
        "player" : {
        "id" : 8475158,
        "fullName" : "Ryan O'Reilly",
        "link" : "/api/v1/people/8475158"
        },
        "playerType" : "PlayerID"
    } ],
    "result" : {
        "event" : "Giveaway",
        "eventCode" : "COL92",
        "eventTypeId" : "GIVEAWAY",
        "description" : "Giveaway by Ryan O'Reilly"
    },
    "about" : {
        "eventIdx" : 666,
        "eventId" : 92,
        "period" : 1,
        "periodType" : "REGULAR",
        "ordinalNum" : "1st",
        "periodTime" : "19:40",
        "periodTimeRemaining" : "00:20",
        "dateTime" : "2022-05-18T02:21:12Z",
        "goals" : {
        "away" : 1,
        "home" : 0
        }
    },
    "coordinates" : {
        "x" : 81.0,
        "y" : 32.0
    },
    "team" : {
        "id" : 19,
        "name" : "St. Louis Blues",
        "link" : "/api/v1/teams/19",
        "triCode" : "STL"
    }
}

giveaway_different_datetime = {
    "players" : [ {
        "player" : {
        "id" : 8475158,
        "fullName" : "Ryan O'Reilly",
        "link" : "/api/v1/people/8475158"
        },
        "playerType" : "PlayerID"
    } ],
    "result" : {
        "event" : "Giveaway",
        "eventCode" : "COL92",
        "eventTypeId" : "GIVEAWAY",
        "description" : "Giveaway by Ryan O'Reilly"
    },
    "about" : {
        "eventIdx" : 87,
        "eventId" : 92,
        "period" : 1,
        "periodType" : "REGULAR",
        "ordinalNum" : "1st",
        "periodTime" : "19:40",
        "periodTimeRemaining" : "00:20",
        "dateTime" : "2022-05-18T02:22:12Z",
        "goals" : {
        "away" : 1,
        "home" : 0
        }
    },
    "coordinates" : {
        "x" : 81.0,
        "y" : 32.0
    },
    "team" : {
        "id" : 19,
        "name" : "St. Louis Blues",
        "link" : "/api/v1/teams/19",
        "triCode" : "STL"
    }
}

giveaway_different_period = {
    "players" : [ {
        "player" : {
        "id" : 8475158,
        "fullName" : "Ryan O'Reilly",
        "link" : "/api/v1/people/8475158"
        },
        "playerType" : "PlayerID"
    } ],
    "result" : {
        "event" : "Giveaway",
        "eventCode" : "COL92",
        "eventTypeId" : "GIVEAWAY",
        "description" : "Giveaway by Ryan O'Reilly"
    },
    "about" : {
        "eventIdx" : 87,
        "eventId" : 92,
        "period" : 2,
        "periodType" : "REGULAR",
        "ordinalNum" : "1st",
        "periodTime" : "19:40",
        "periodTimeRemaining" : "00:20",
        "dateTime" : "2022-05-18T02:21:12Z",
        "goals" : {
        "away" : 1,
        "home" : 0
        }
    },
    "coordinates" : {
        "x" : 81.0,
        "y" : 32.0
    },
    "team" : {
        "id" : 19,
        "name" : "St. Louis Blues",
        "link" : "/api/v1/teams/19",
        "triCode" : "STL"
    }
}

giveaway_different_period_time = {
    "players" : [ {
        "player" : {
        "id" : 8475158,
        "fullName" : "Ryan O'Reilly",
        "link" : "/api/v1/people/8475158"
        },
        "playerType" : "PlayerID"
    } ],
    "result" : {
        "event" : "Giveaway",
        "eventCode" : "COL92",
        "eventTypeId" : "GIVEAWAY",
        "description" : "Giveaway by Ryan O'Reilly"
    },
    "about" : {
        "eventIdx" : 87,
        "eventId" : 92,
        "period" : 1,
        "periodType" : "REGULAR",
        "ordinalNum" : "1st",
        "periodTime" : "19:43",
        "periodTimeRemaining" : "00:20",
        "dateTime" : "2022-05-18T02:21:12Z",
        "goals" : {
        "away" : 1,
        "home" : 0
        }
    },
    "coordinates" : {
        "x" : 81.0,
        "y" : 32.0
    },
    "team" : {
        "id" : 19,
        "name" : "St. Louis Blues",
        "link" : "/api/v1/teams/19",
        "triCode" : "STL"
    }
}

giveaway_different_period_time_remaining = {
    "players" : [ {
        "player" : {
        "id" : 8475158,
        "fullName" : "Ryan O'Reilly",
        "link" : "/api/v1/people/8475158"
        },
        "playerType" : "PlayerID"
    } ],
    "result" : {
        "event" : "Giveaway",
        "eventCode" : "COL92",
        "eventTypeId" : "GIVEAWAY",
        "description" : "Giveaway by Ryan O'Reilly"
    },
    "about" : {
        "eventIdx" : 87,
        "eventId" : 92,
        "period" : 1,
        "periodType" : "REGULAR",
        "ordinalNum" : "1st",
        "periodTime" : "19:40",
        "periodTimeRemaining" : "00:23",
        "dateTime" : "2022-05-18T02:21:12Z",
        "goals" : {
        "away" : 1,
        "home" : 0
        }
    },
    "coordinates" : {
        "x" : 81.0,
        "y" : 32.0
    },
    "team" : {
        "id" : 19,
        "name" : "St. Louis Blues",
        "link" : "/api/v1/teams/19",
        "triCode" : "STL"
    }
}

giveaway_different_player = {
    "players" : [ {
        "player" : {
        "id" : 99,
        "fullName" : "Wayne Gretzky",
        "link" : "/api/v1/people/8475158"
        },
        "playerType" : "PlayerID"
    } ],
    "result" : {
        "event" : "Giveaway",
        "eventCode" : "COL92",
        "eventTypeId" : "GIVEAWAY",
        "description" : "Giveaway by Ryan O'Reilly"
    },
    "about" : {
        "eventIdx" : 87,
        "eventId" : 92,
        "period" : 1,
        "periodType" : "REGULAR",
        "ordinalNum" : "1st",
        "periodTime" : "19:40",
        "periodTimeRemaining" : "00:20",
        "dateTime" : "2022-05-18T02:21:12Z",
        "goals" : {
        "away" : 1,
        "home" : 0
        }
    },
    "coordinates" : {
        "x" : 81.0,
        "y" : 32.0
    },
    "team" : {
        "id" : 19,
        "name" : "St. Louis Blues",
        "link" : "/api/v1/teams/19",
        "triCode" : "STL"
    }
}
