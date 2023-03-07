"""
Test events for penalty shots.
"""

penalty_shot_1 = {
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

penalty_shot_2 = {
    "players" : [ {
        "player" : {
        "id" : 8474884,
        "fullName" : "Mike Hoffman",
        "link" : "/api/v1/people/8474884"
        },
        "playerType" : "PenaltyOn"
    }, {
        "player" : {
        "id" : 8475287,
        "fullName" : "Erik Haula",
        "link" : "/api/v1/people/8475287"
        },
        "playerType" : "DrewBy"
    } ],
    "result" : {
        "event" : "Penalty",
        "eventCode" : "MTL50",
        "eventTypeId" : "PENALTY",
        "description" : "Mike Hoffman PS - Slash on breakaway against Erik Haula",
        "secondaryType" : "PS - Slash on breakaway",
        "penaltySeverity" : "Penalty Shot",
        "penaltyMinutes" : 0
    },
    "about" : {
        "eventIdx" : 111,
        "eventId" : 50,
        "period" : 1,
        "periodType" : "REGULAR",
        "ordinalNum" : "1st",
        "periodTime" : "18:03",
        "periodTimeRemaining" : "01:57",
        "dateTime" : "2022-04-25T00:01:41Z",
        "goals" : {
        "away" : 1,
        "home" : 0
        }
    },
    "coordinates" : {
        "x" : 56.0,
        "y" : 1.0
    },
    "team" : {
        "id" : 8,
        "name" : "Montréal Canadiens",
        "link" : "/api/v1/teams/8",
        "triCode" : "MTL"
    }
}

penalty_shot_3 = {
    "players" : [ {
        "player" : {
        "id" : 8479388,
        "fullName" : "Riley Stillman",
        "link" : "/api/v1/people/8479388"
        },
        "playerType" : "PenaltyOn"
    }, {
        "player" : {
        "id" : 8477955,
        "fullName" : "Jared McCann",
        "link" : "/api/v1/people/8477955"
        },
        "playerType" : "DrewBy"
    } ],
    "result" : {
        "event" : "Penalty",
        "eventCode" : "SEA612",
        "eventTypeId" : "PENALTY",
        "description" : "Riley Stillman PS - Tripping on breakaway against Jared McCann",
        "secondaryType" : "PS - Tripping on breakaway",
        "penaltySeverity" : "Penalty Shot",
        "penaltyMinutes" : 0
    },
    "about" : {
        "eventIdx" : 232,
        "eventId" : 612,
        "period" : 3,
        "periodType" : "REGULAR",
        "ordinalNum" : "3rd",
        "periodTime" : "13:34",
        "periodTimeRemaining" : "06:26",
        "dateTime" : "2022-01-18T00:17:29Z",
        "goals" : {
        "away" : 2,
        "home" : 2
        }
    },
    "coordinates" : {
        "x" : 76.0,
        "y" : -1.0
    },
    "team" : {
        "id" : 16,
        "name" : "Chicago Blackhawks",
        "link" : "/api/v1/teams/16",
        "triCode" : "CHI"
    }
}

penalty_shot_different_event_id = {
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
      "eventId" : 666,
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

penalty_shot_different_event_id_x = {
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
      "eventIdx" : 666,
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

penalty_shot_different_datetime = {
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
      "dateTime" : "2022-04-09T01:36:36Z",
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

penalty_shot_different_period = {
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
      "period" : 3,
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

penalty_shot_different_period_time = {
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
      "periodTime" : "17:12",
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

penalty_shot_different_period_time_remaining = {
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
      "periodTimeRemaining" : "02:22",
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

penalty_shot_different_taker = {
    "players" : [ {
      "player" : {
        "id" : 99,
        "fullName" : "Wayne Gretzky",
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

penalty_shot_different_drawn_by = {
    "players" : [ {
      "player" : {
        "id" : 8475455,
        "fullName" : "Brenden Dillon",
        "link" : "/api/v1/people/8475455"
      },
      "playerType" : "PenaltyOn"
    }, {
      "player" : {
        "id" : 99,
        "fullName" : "Wayne Gretzky",
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

penalty_shot_different_reason = {
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
      "secondaryType" : "PS - Tripping on breakaway",
      "penaltySeverity" : "Penalty Shot",
      "penaltyMinutes" : 0
    },
    "about" : {
      "eventIdx" : 212,
      "eventId" : 666,
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
