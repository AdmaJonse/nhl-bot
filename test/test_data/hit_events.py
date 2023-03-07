"""
Test events for hits.
"""

hit_1 = {
    "players" : [ {
        "player" : {
        "id" : 8475279,
        "fullName" : "Ben Chiarot",
        "link" : "/api/v1/people/8475279"
        },
        "playerType" : "Hitter"
    }, {
        "player" : {
        "id" : 8479525,
        "fullName" : "Ross Colton",
        "link" : "/api/v1/people/8479525"
        },
        "playerType" : "Hittee"
    } ],
    "result" : {
        "event" : "Hit",
        "eventCode" : "FLA43",
        "eventTypeId" : "HIT",
        "description" : "Ben Chiarot hit Ross Colton"
    },
    "about" : {
        "eventIdx" : 80,
        "eventId" : 43,
        "period" : 1,
        "periodType" : "REGULAR",
        "ordinalNum" : "1st",
        "periodTime" : "14:10",
        "periodTimeRemaining" : "05:50",
        "dateTime" : "2022-05-17T23:35:51Z",
        "goals" : {
        "away" : 0,
        "home" : 1
        }
    },
    "coordinates" : {
        "x" : 99.0,
        "y" : -22.0
    },
    "team" : {
        "id" : 13,
        "name" : "Florida Panthers",
        "link" : "/api/v1/teams/13",
        "triCode" : "FLA"
    }
}

hit_2 = {
    "players" : [ {
        "player" : {
        "id" : 8477476,
        "fullName" : "Artturi Lehkonen",
        "link" : "/api/v1/people/8477476"
        },
        "playerType" : "Hitter"
    }, {
        "player" : {
        "id" : 8475765,
        "fullName" : "Vladimir Tarasenko",
        "link" : "/api/v1/people/8475765"
        },
        "playerType" : "Hittee"
    } ],
    "result" : {
        "event" : "Hit",
        "eventCode" : "COL186",
        "eventTypeId" : "HIT",
        "description" : "Artturi Lehkonen hit Vladimir Tarasenko"
    },
    "about" : {
        "eventIdx" : 124,
        "eventId" : 186,
        "period" : 2,
        "periodType" : "REGULAR",
        "ordinalNum" : "2nd",
        "periodTime" : "04:23",
        "periodTimeRemaining" : "15:37",
        "dateTime" : "2022-05-18T02:48:04Z",
        "goals" : {
        "away" : 1,
        "home" : 1
        }
    },
    "coordinates" : {
        "x" : 86.0,
        "y" : 38.0
    },
    "team" : {
        "id" : 21,
        "name" : "Colorado Avalanche",
        "link" : "/api/v1/teams/21",
        "triCode" : "COL"
    }
}

hit_3 = {
    "players" : [ {
        "player" : {
        "id" : 8476312,
        "fullName" : "Josh Manson",
        "link" : "/api/v1/people/8476312"
        },
        "playerType" : "Hitter"
    }, {
        "player" : {
        "id" : 8480023,
        "fullName" : "Robert Thomas",
        "link" : "/api/v1/people/8480023"
        },
        "playerType" : "Hittee"
    } ],
    "result" : {
        "event" : "Hit",
        "eventCode" : "COL187",
        "eventTypeId" : "HIT",
        "description" : "Josh Manson hit Robert Thomas"
    },
    "about" : {
        "eventIdx" : 126,
        "eventId" : 187,
        "period" : 2,
        "periodType" : "REGULAR",
        "ordinalNum" : "2nd",
        "periodTime" : "04:33",
        "periodTimeRemaining" : "15:27",
        "dateTime" : "2022-05-18T02:48:14Z",
        "goals" : {
        "away" : 1,
        "home" : 1
        }
    },
    "coordinates" : {
        "x" : -6.0,
        "y" : 6.0
    },
    "team" : {
        "id" : 21,
        "name" : "Colorado Avalanche",
        "link" : "/api/v1/teams/21",
        "triCode" : "COL"
    }
}

hit_different_event_id = {
    "players" : [ {
        "player" : {
        "id" : 8475279,
        "fullName" : "Ben Chiarot",
        "link" : "/api/v1/people/8475279"
        },
        "playerType" : "Hitter"
    }, {
        "player" : {
        "id" : 8479525,
        "fullName" : "Ross Colton",
        "link" : "/api/v1/people/8479525"
        },
        "playerType" : "Hittee"
    } ],
    "result" : {
        "event" : "Hit",
        "eventCode" : "FLA43",
        "eventTypeId" : "HIT",
        "description" : "Ben Chiarot hit Ross Colton"
    },
    "about" : {
        "eventIdx" : 80,
        "eventId" : 666,
        "period" : 1,
        "periodType" : "REGULAR",
        "ordinalNum" : "1st",
        "periodTime" : "14:10",
        "periodTimeRemaining" : "05:50",
        "dateTime" : "2022-05-17T23:35:51Z",
        "goals" : {
        "away" : 0,
        "home" : 1
        }
    },
    "coordinates" : {
        "x" : 99.0,
        "y" : -22.0
    },
    "team" : {
        "id" : 13,
        "name" : "Florida Panthers",
        "link" : "/api/v1/teams/13",
        "triCode" : "FLA"
    }
}

hit_different_event_id_x = {
    "players" : [ {
        "player" : {
        "id" : 8475279,
        "fullName" : "Ben Chiarot",
        "link" : "/api/v1/people/8475279"
        },
        "playerType" : "Hitter"
    }, {
        "player" : {
        "id" : 8479525,
        "fullName" : "Ross Colton",
        "link" : "/api/v1/people/8479525"
        },
        "playerType" : "Hittee"
    } ],
    "result" : {
        "event" : "Hit",
        "eventCode" : "FLA43",
        "eventTypeId" : "HIT",
        "description" : "Ben Chiarot hit Ross Colton"
    },
    "about" : {
        "eventIdx" : 666,
        "eventId" : 43,
        "period" : 1,
        "periodType" : "REGULAR",
        "ordinalNum" : "1st",
        "periodTime" : "14:10",
        "periodTimeRemaining" : "05:50",
        "dateTime" : "2022-05-17T23:35:51Z",
        "goals" : {
        "away" : 0,
        "home" : 1
        }
    },
    "coordinates" : {
        "x" : 99.0,
        "y" : -22.0
    },
    "team" : {
        "id" : 13,
        "name" : "Florida Panthers",
        "link" : "/api/v1/teams/13",
        "triCode" : "FLA"
    }
}

hit_different_datetime = {
    "players" : [ {
        "player" : {
        "id" : 8475279,
        "fullName" : "Ben Chiarot",
        "link" : "/api/v1/people/8475279"
        },
        "playerType" : "Hitter"
    }, {
        "player" : {
        "id" : 8479525,
        "fullName" : "Ross Colton",
        "link" : "/api/v1/people/8479525"
        },
        "playerType" : "Hittee"
    } ],
    "result" : {
        "event" : "Hit",
        "eventCode" : "FLA43",
        "eventTypeId" : "HIT",
        "description" : "Ben Chiarot hit Ross Colton"
    },
    "about" : {
        "eventIdx" : 80,
        "eventId" : 43,
        "period" : 1,
        "periodType" : "REGULAR",
        "ordinalNum" : "1st",
        "periodTime" : "14:10",
        "periodTimeRemaining" : "05:50",
        "dateTime" : "2022-05-17T22:35:51Z",
        "goals" : {
        "away" : 0,
        "home" : 1
        }
    },
    "coordinates" : {
        "x" : 99.0,
        "y" : -22.0
    },
    "team" : {
        "id" : 13,
        "name" : "Florida Panthers",
        "link" : "/api/v1/teams/13",
        "triCode" : "FLA"
    }
}

hit_different_period = {
    "players" : [ {
        "player" : {
        "id" : 8475279,
        "fullName" : "Ben Chiarot",
        "link" : "/api/v1/people/8475279"
        },
        "playerType" : "Hitter"
    }, {
        "player" : {
        "id" : 8479525,
        "fullName" : "Ross Colton",
        "link" : "/api/v1/people/8479525"
        },
        "playerType" : "Hittee"
    } ],
    "result" : {
        "event" : "Hit",
        "eventCode" : "FLA43",
        "eventTypeId" : "HIT",
        "description" : "Ben Chiarot hit Ross Colton"
    },
    "about" : {
        "eventIdx" : 80,
        "eventId" : 43,
        "period" : 4,
        "periodType" : "REGULAR",
        "ordinalNum" : "1st",
        "periodTime" : "14:10",
        "periodTimeRemaining" : "05:50",
        "dateTime" : "2022-05-17T23:35:51Z",
        "goals" : {
        "away" : 0,
        "home" : 1
        }
    },
    "coordinates" : {
        "x" : 99.0,
        "y" : -22.0
    },
    "team" : {
        "id" : 13,
        "name" : "Florida Panthers",
        "link" : "/api/v1/teams/13",
        "triCode" : "FLA"
    }
}

hit_different_period_time = {
    "players" : [ {
        "player" : {
        "id" : 8475279,
        "fullName" : "Ben Chiarot",
        "link" : "/api/v1/people/8475279"
        },
        "playerType" : "Hitter"
    }, {
        "player" : {
        "id" : 8479525,
        "fullName" : "Ross Colton",
        "link" : "/api/v1/people/8479525"
        },
        "playerType" : "Hittee"
    } ],
    "result" : {
        "event" : "Hit",
        "eventCode" : "FLA43",
        "eventTypeId" : "HIT",
        "description" : "Ben Chiarot hit Ross Colton"
    },
    "about" : {
        "eventIdx" : 80,
        "eventId" : 43,
        "period" : 1,
        "periodType" : "REGULAR",
        "ordinalNum" : "1st",
        "periodTime" : "13:10",
        "periodTimeRemaining" : "05:50",
        "dateTime" : "2022-05-17T23:35:51Z",
        "goals" : {
        "away" : 0,
        "home" : 1
        }
    },
    "coordinates" : {
        "x" : 99.0,
        "y" : -22.0
    },
    "team" : {
        "id" : 13,
        "name" : "Florida Panthers",
        "link" : "/api/v1/teams/13",
        "triCode" : "FLA"
    }
}

hit_different_period_time_remaining = {
    "players" : [ {
        "player" : {
        "id" : 8475279,
        "fullName" : "Ben Chiarot",
        "link" : "/api/v1/people/8475279"
        },
        "playerType" : "Hitter"
    }, {
        "player" : {
        "id" : 8479525,
        "fullName" : "Ross Colton",
        "link" : "/api/v1/people/8479525"
        },
        "playerType" : "Hittee"
    } ],
    "result" : {
        "event" : "Hit",
        "eventCode" : "FLA43",
        "eventTypeId" : "HIT",
        "description" : "Ben Chiarot hit Ross Colton"
    },
    "about" : {
        "eventIdx" : 80,
        "eventId" : 43,
        "period" : 1,
        "periodType" : "REGULAR",
        "ordinalNum" : "1st",
        "periodTime" : "14:10",
        "periodTimeRemaining" : "05:30",
        "dateTime" : "2022-05-17T23:35:51Z",
        "goals" : {
        "away" : 0,
        "home" : 1
        }
    },
    "coordinates" : {
        "x" : 99.0,
        "y" : -22.0
    },
    "team" : {
        "id" : 13,
        "name" : "Florida Panthers",
        "link" : "/api/v1/teams/13",
        "triCode" : "FLA"
    }
}

hit_different_hitter = {
    "players" : [ {
        "player" : {
        "id" : 99,
        "fullName" : "Wayne Gretzky",
        "link" : "/api/v1/people/8475279"
        },
        "playerType" : "Hitter"
    }, {
        "player" : {
        "id" : 8479525,
        "fullName" : "Ross Colton",
        "link" : "/api/v1/people/8479525"
        },
        "playerType" : "Hittee"
    } ],
    "result" : {
        "event" : "Hit",
        "eventCode" : "FLA43",
        "eventTypeId" : "HIT",
        "description" : "Ben Chiarot hit Ross Colton"
    },
    "about" : {
        "eventIdx" : 80,
        "eventId" : 43,
        "period" : 1,
        "periodType" : "REGULAR",
        "ordinalNum" : "1st",
        "periodTime" : "14:10",
        "periodTimeRemaining" : "05:50",
        "dateTime" : "2022-05-17T23:35:51Z",
        "goals" : {
        "away" : 0,
        "home" : 1
        }
    },
    "coordinates" : {
        "x" : 99.0,
        "y" : -22.0
    },
    "team" : {
        "id" : 13,
        "name" : "Florida Panthers",
        "link" : "/api/v1/teams/13",
        "triCode" : "FLA"
    }
}

hit_different_hittee = {
    "players" : [ {
        "player" : {
        "id" : 8475279,
        "fullName" : "Ben Chiarot",
        "link" : "/api/v1/people/8475279"
        },
        "playerType" : "Hitter"
    }, {
        "player" : {
        "id" : 99,
        "fullName" : "Gretzky",
        "link" : "/api/v1/people/8479525"
        },
        "playerType" : "Hittee"
    } ],
    "result" : {
        "event" : "Hit",
        "eventCode" : "FLA43",
        "eventTypeId" : "HIT",
        "description" : "Ben Chiarot hit Ross Colton"
    },
    "about" : {
        "eventIdx" : 80,
        "eventId" : 43,
        "period" : 1,
        "periodType" : "REGULAR",
        "ordinalNum" : "1st",
        "periodTime" : "14:10",
        "periodTimeRemaining" : "05:50",
        "dateTime" : "2022-05-17T23:35:51Z",
        "goals" : {
        "away" : 0,
        "home" : 1
        }
    },
    "coordinates" : {
        "x" : 99.0,
        "y" : -22.0
    },
    "team" : {
        "id" : 13,
        "name" : "Florida Panthers",
        "link" : "/api/v1/teams/13",
        "triCode" : "FLA"
    }
}
