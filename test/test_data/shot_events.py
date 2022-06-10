"""
TODO
"""

shot_1 = {
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
        "playerType" : "Goalie"
    } ],
    "result" : {
        "event" : "Shot",
        "eventCode" : "COL741",
        "eventTypeId" : "SHOT",
        "description" : "Nazem Kadri Wrist Shot saved by Jordan Binnington",
        "secondaryType" : "Wrist Shot"
    },
    "about" : {
        "eventIdx" : 275,
        "eventId" : 741,
        "period" : 3,
        "periodType" : "REGULAR",
        "ordinalNum" : "3rd",
        "periodTime" : "09:31",
        "periodTimeRemaining" : "10:29",
        "dateTime" : "2022-05-18T03:50:34Z",
        "goals" : {
        "away" : 1,
        "home" : 2
        }
    },
    "coordinates" : {
        "x" : -78.0,
        "y" : -8.0
    },
    "team" : {
        "id" : 21,
        "name" : "Colorado Avalanche",
        "link" : "/api/v1/teams/21",
        "triCode" : "COL"
    }
}

shot_2 = {
    "players" : [ {
        "player" : {
        "id" : 8477407,
        "fullName" : "Anthony Duclair",
        "link" : "/api/v1/people/8477407"
        },
        "playerType" : "Shooter"
    }, {
        "player" : {
        "id" : 8476883,
        "fullName" : "Andrei Vasilevskiy",
        "link" : "/api/v1/people/8476883"
        },
        "playerType" : "Goalie"
    } ],
    "result" : {
        "event" : "Shot",
        "eventCode" : "FLA178",
        "eventTypeId" : "SHOT",
        "description" : "Anthony Duclair Slap Shot saved by Andrei Vasilevskiy",
        "secondaryType" : "Slap Shot"
    },
    "about" : {
        "eventIdx" : 94,
        "eventId" : 178,
        "period" : 1,
        "periodType" : "REGULAR",
        "ordinalNum" : "1st",
        "periodTime" : "16:56",
        "periodTimeRemaining" : "03:04",
        "dateTime" : "2022-05-17T23:41:00Z",
        "goals" : {
        "away" : 0,
        "home" : 1
        }
    },
    "coordinates" : {
        "x" : -45.0,
        "y" : -7.0
    },
    "team" : {
        "id" : 13,
        "name" : "Florida Panthers",
        "link" : "/api/v1/teams/13",
        "triCode" : "FLA"
    }
}

shot_3 = {
    "players" : [ {
        "player" : {
        "id" : 8480069,
        "fullName" : "Cale Makar",
        "link" : "/api/v1/people/8480069"
        },
        "playerType" : "Shooter"
    }, {
        "player" : {
        "id" : 8476412,
        "fullName" : "Jordan Binnington",
        "link" : "/api/v1/people/8476412"
        },
        "playerType" : "Goalie"
    } ],
    "result" : {
        "event" : "Shot",
        "eventCode" : "COL744",
        "eventTypeId" : "SHOT",
        "description" : "Cale Makar Wrist Shot saved by Jordan Binnington",
        "secondaryType" : "Wrist Shot"
    },
    "about" : {
        "eventIdx" : 281,
        "eventId" : 744,
        "period" : 3,
        "periodType" : "REGULAR",
        "ordinalNum" : "3rd",
        "periodTime" : "09:43",
        "periodTimeRemaining" : "10:17",
        "dateTime" : "2022-05-18T03:52:08Z",
        "goals" : {
        "away" : 1,
        "home" : 2
        }
    },
    "coordinates" : {
        "x" : -35.0,
        "y" : 0.0
    },
    "team" : {
        "id" : 21,
        "name" : "Colorado Avalanche",
        "link" : "/api/v1/teams/21",
        "triCode" : "COL"
    }
}

shot_different_event_id = {
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
        "playerType" : "Goalie"
    } ],
    "result" : {
        "event" : "Shot",
        "eventCode" : "COL741",
        "eventTypeId" : "SHOT",
        "description" : "Nazem Kadri Wrist Shot saved by Jordan Binnington",
        "secondaryType" : "Wrist Shot"
    },
    "about" : {
        "eventIdx" : 275,
        "eventId" : 666,
        "period" : 3,
        "periodType" : "REGULAR",
        "ordinalNum" : "3rd",
        "periodTime" : "09:31",
        "periodTimeRemaining" : "10:29",
        "dateTime" : "2022-05-18T03:50:34Z",
        "goals" : {
        "away" : 1,
        "home" : 2
        }
    },
    "coordinates" : {
        "x" : -78.0,
        "y" : -8.0
    },
    "team" : {
        "id" : 21,
        "name" : "Colorado Avalanche",
        "link" : "/api/v1/teams/21",
        "triCode" : "COL"
    }
}

shot_different_event_id_x = {
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
        "playerType" : "Goalie"
    } ],
    "result" : {
        "event" : "Shot",
        "eventCode" : "COL741",
        "eventTypeId" : "SHOT",
        "description" : "Nazem Kadri Wrist Shot saved by Jordan Binnington",
        "secondaryType" : "Wrist Shot"
    },
    "about" : {
        "eventIdx" : 666,
        "eventId" : 741,
        "period" : 3,
        "periodType" : "REGULAR",
        "ordinalNum" : "3rd",
        "periodTime" : "09:31",
        "periodTimeRemaining" : "10:29",
        "dateTime" : "2022-05-18T03:50:34Z",
        "goals" : {
        "away" : 1,
        "home" : 2
        }
    },
    "coordinates" : {
        "x" : -78.0,
        "y" : -8.0
    },
    "team" : {
        "id" : 21,
        "name" : "Colorado Avalanche",
        "link" : "/api/v1/teams/21",
        "triCode" : "COL"
    }
}

shot_different_datetime = {
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
        "playerType" : "Goalie"
    } ],
    "result" : {
        "event" : "Shot",
        "eventCode" : "COL741",
        "eventTypeId" : "SHOT",
        "description" : "Nazem Kadri Wrist Shot saved by Jordan Binnington",
        "secondaryType" : "Wrist Shot"
    },
    "about" : {
        "eventIdx" : 275,
        "eventId" : 741,
        "period" : 3,
        "periodType" : "REGULAR",
        "ordinalNum" : "3rd",
        "periodTime" : "09:31",
        "periodTimeRemaining" : "10:29",
        "dateTime" : "2022-05-18T13:50:34Z",
        "goals" : {
        "away" : 1,
        "home" : 2
        }
    },
    "coordinates" : {
        "x" : -78.0,
        "y" : -8.0
    },
    "team" : {
        "id" : 21,
        "name" : "Colorado Avalanche",
        "link" : "/api/v1/teams/21",
        "triCode" : "COL"
    }
}

shot_different_period = {
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
        "playerType" : "Goalie"
    } ],
    "result" : {
        "event" : "Shot",
        "eventCode" : "COL741",
        "eventTypeId" : "SHOT",
        "description" : "Nazem Kadri Wrist Shot saved by Jordan Binnington",
        "secondaryType" : "Wrist Shot"
    },
    "about" : {
        "eventIdx" : 275,
        "eventId" : 741,
        "period" : 1,
        "periodType" : "REGULAR",
        "ordinalNum" : "3rd",
        "periodTime" : "09:31",
        "periodTimeRemaining" : "10:29",
        "dateTime" : "2022-05-18T03:50:34Z",
        "goals" : {
        "away" : 1,
        "home" : 2
        }
    },
    "coordinates" : {
        "x" : -78.0,
        "y" : -8.0
    },
    "team" : {
        "id" : 21,
        "name" : "Colorado Avalanche",
        "link" : "/api/v1/teams/21",
        "triCode" : "COL"
    }
}

shot_different_period_time = {
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
        "playerType" : "Goalie"
    } ],
    "result" : {
        "event" : "Shot",
        "eventCode" : "COL741",
        "eventTypeId" : "SHOT",
        "description" : "Nazem Kadri Wrist Shot saved by Jordan Binnington",
        "secondaryType" : "Wrist Shot"
    },
    "about" : {
        "eventIdx" : 275,
        "eventId" : 741,
        "period" : 3,
        "periodType" : "REGULAR",
        "ordinalNum" : "3rd",
        "periodTime" : "09:21",
        "periodTimeRemaining" : "10:29",
        "dateTime" : "2022-05-18T03:50:34Z",
        "goals" : {
        "away" : 1,
        "home" : 2
        }
    },
    "coordinates" : {
        "x" : -78.0,
        "y" : -8.0
    },
    "team" : {
        "id" : 21,
        "name" : "Colorado Avalanche",
        "link" : "/api/v1/teams/21",
        "triCode" : "COL"
    }
}

shot_different_period_time_remaining = {
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
        "playerType" : "Goalie"
    } ],
    "result" : {
        "event" : "Shot",
        "eventCode" : "COL741",
        "eventTypeId" : "SHOT",
        "description" : "Nazem Kadri Wrist Shot saved by Jordan Binnington",
        "secondaryType" : "Wrist Shot"
    },
    "about" : {
        "eventIdx" : 275,
        "eventId" : 741,
        "period" : 3,
        "periodType" : "REGULAR",
        "ordinalNum" : "3rd",
        "periodTime" : "09:31",
        "periodTimeRemaining" : "10:19",
        "dateTime" : "2022-05-18T03:50:34Z",
        "goals" : {
        "away" : 1,
        "home" : 2
        }
    },
    "coordinates" : {
        "x" : -78.0,
        "y" : -8.0
    },
    "team" : {
        "id" : 21,
        "name" : "Colorado Avalanche",
        "link" : "/api/v1/teams/21",
        "triCode" : "COL"
    }
}

shot_different_shooter = {
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
        "playerType" : "Goalie"
    } ],
    "result" : {
        "event" : "Shot",
        "eventCode" : "COL741",
        "eventTypeId" : "SHOT",
        "description" : "Nazem Kadri Wrist Shot saved by Jordan Binnington",
        "secondaryType" : "Wrist Shot"
    },
    "about" : {
        "eventIdx" : 275,
        "eventId" : 741,
        "period" : 3,
        "periodType" : "REGULAR",
        "ordinalNum" : "3rd",
        "periodTime" : "09:31",
        "periodTimeRemaining" : "10:29",
        "dateTime" : "2022-05-18T03:50:34Z",
        "goals" : {
        "away" : 1,
        "home" : 2
        }
    },
    "coordinates" : {
        "x" : -78.0,
        "y" : -8.0
    },
    "team" : {
        "id" : 21,
        "name" : "Colorado Avalanche",
        "link" : "/api/v1/teams/21",
        "triCode" : "COL"
    }
}

shot_different_goalie = {
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
        "playerType" : "Goalie"
    } ],
    "result" : {
        "event" : "Shot",
        "eventCode" : "COL741",
        "eventTypeId" : "SHOT",
        "description" : "Nazem Kadri Wrist Shot saved by Jordan Binnington",
        "secondaryType" : "Wrist Shot"
    },
    "about" : {
        "eventIdx" : 275,
        "eventId" : 741,
        "period" : 3,
        "periodType" : "REGULAR",
        "ordinalNum" : "3rd",
        "periodTime" : "09:31",
        "periodTimeRemaining" : "10:29",
        "dateTime" : "2022-05-18T03:50:34Z",
        "goals" : {
        "away" : 1,
        "home" : 2
        }
    },
    "coordinates" : {
        "x" : -78.0,
        "y" : -8.0
    },
    "team" : {
        "id" : 21,
        "name" : "Colorado Avalanche",
        "link" : "/api/v1/teams/21",
        "triCode" : "COL"
    }
}