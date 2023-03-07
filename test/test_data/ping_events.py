"""
Test events for ping.
"""

ping_1 = {
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

ping_2 = {
    "players" : [ {
        "player" : {
        "id" : 8477476,
        "fullName" : "Artturi Lehkonen",
        "link" : "/api/v1/people/8477476"
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
        "eventCode" : "COL73",
        "eventTypeId" : "MISSED_SHOT",
        "description" : "Artturi Lehkonen Goalpost Jordan Binnington"
    },
    "about" : {
        "eventIdx" : 38,
        "eventId" : 73,
        "period" : 1,
        "periodType" : "REGULAR",
        "ordinalNum" : "1st",
        "periodTime" : "07:22",
        "periodTimeRemaining" : "12:38",
        "dateTime" : "2022-05-18T01:59:58Z",
        "goals" : {
        "away" : 1,
        "home" : 0
        }
    },
    "coordinates" : {
        "x" : -59.0,
        "y" : -18.0
    },
    "team" : {
        "id" : 21,
        "name" : "Colorado Avalanche",
        "link" : "/api/v1/teams/21",
        "triCode" : "COL"
    }
}

ping_3 = {
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

ping_different_event_id = {
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
        "eventId" : 666,
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

ping_different_event_id_x = {
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
        "eventIdx" : 666,
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

ping_different_datetime = {
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
        "dateTime" : "2022-05-18T05:55:39Z",
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

ping_different_period = {
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
        "period" : 3,
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

ping_different_period_time = {
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
        "periodTime" : "01:21",
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

ping_different_period_time_remaining = {
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
        "periodTimeRemaining" : "15:19",
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

ping_different_shooter = {
    "players" : [ {
        "player" : {
        "id" : 99,
        "fullName" : "Wayne Gretzky",
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

ping_different_goalie = {
    "players" : [ {
        "player" : {
        "id" : 8475172,
        "fullName" : "Nazem Kadri",
        "link" : "/api/v1/people/8475172"
        },
        "playerType" : "Shooter"
    }, {
        "player" : {
        "id" : 33,
        "fullName" : "Patrick Roy",
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

ping_different_goal_post = {
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
        "description" : "Nazem Kadri Hit Goalpost Jordan Binnington"
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
