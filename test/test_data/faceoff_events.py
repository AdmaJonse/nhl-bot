"""
TODO
"""

faceoff_1 = {
    "players" : [ {
        "player" : {
        "id" : 8475158,
        "fullName" : "Ryan O'Reilly",
        "link" : "/api/v1/people/8475158"
        },
        "playerType" : "Winner"
    }, {
        "player" : {
        "id" : 8477492,
        "fullName" : "Nathan MacKinnon",
        "link" : "/api/v1/people/8477492"
        },
        "playerType" : "Loser"
    } ],
    "result" : {
        "event" : "Faceoff",
        "eventCode" : "COL52",
        "eventTypeId" : "FACEOFF",
        "description" : "Ryan O'Reilly faceoff won against Nathan MacKinnon"
    },
    "about" : {
        "eventIdx" : 3,
        "eventId" : 52,
        "period" : 1,
        "periodType" : "REGULAR",
        "ordinalNum" : "1st",
        "periodTime" : "00:00",
        "periodTimeRemaining" : "20:00",
        "dateTime" : "2022-05-18T01:50:19Z",
        "goals" : {
        "away" : 0,
        "home" : 0
        }
    },
    "coordinates" : {
        "x" : 0.0,
        "y" : 0.0
    },
    "team" : {
        "id" : 19,
        "name" : "St. Louis Blues",
        "link" : "/api/v1/teams/19",
        "triCode" : "STL"
    }
}

faceoff_2 = {
    "players" : [ {
        "player" : {
        "id" : 8480023,
        "fullName" : "Robert Thomas",
        "link" : "/api/v1/people/8480023"
        },
        "playerType" : "Winner"
    }, {
        "player" : {
        "id" : 8471794,
        "fullName" : "Darren Helm",
        "link" : "/api/v1/people/8471794"
        },
        "playerType" : "Loser"
    } ],
    "result" : {
        "event" : "Faceoff",
        "eventCode" : "COL976",
        "eventTypeId" : "FACEOFF",
        "description" : "Robert Thomas faceoff won against Darren Helm"
    },
    "about" : {
        "eventIdx" : 356,
        "eventId" : 976,
        "period" : 4,
        "periodType" : "OVERTIME",
        "ordinalNum" : "OT",
        "periodTime" : "03:20",
        "periodTimeRemaining" : "16:40",
        "dateTime" : "2022-05-18T04:29:26Z",
        "goals" : {
        "away" : 2,
        "home" : 2
        }
    },
    "coordinates" : {
        "x" : 20.0,
        "y" : 22.0
    },
    "team" : {
        "id" : 19,
        "name" : "St. Louis Blues",
        "link" : "/api/v1/teams/19",
        "triCode" : "STL"
    }
}

faceoff_3 = {
    "players" : [ {
        "player" : {
        "id" : 8473512,
        "fullName" : "Claude Giroux",
        "link" : "/api/v1/people/8473512"
        },
        "playerType" : "Winner"
    }, {
        "player" : {
        "id" : 8478519,
        "fullName" : "Anthony Cirelli",
        "link" : "/api/v1/people/8478519"
        },
        "playerType" : "Loser"
    } ],
    "result" : {
        "event" : "Faceoff",
        "eventCode" : "FLA124",
        "eventTypeId" : "FACEOFF",
        "description" : "Claude Giroux faceoff won against Anthony Cirelli"
    },
    "about" : {
        "eventIdx" : 68,
        "eventId" : 124,
        "period" : 1,
        "periodType" : "REGULAR",
        "ordinalNum" : "1st",
        "periodTime" : "11:26",
        "periodTimeRemaining" : "08:34",
        "dateTime" : "2022-05-17T23:32:18Z",
        "goals" : {
        "away" : 0,
        "home" : 0
        }
    },
    "coordinates" : {
        "x" : 69.0,
        "y" : 22.0
    },
    "team" : {
        "id" : 13,
        "name" : "Florida Panthers",
        "link" : "/api/v1/teams/13",
        "triCode" : "FLA"
    }
}

faceoff_different_event_id = {
    "players" : [ {
        "player" : {
        "id" : 8475158,
        "fullName" : "Ryan O'Reilly",
        "link" : "/api/v1/people/8475158"
        },
        "playerType" : "Winner"
    }, {
        "player" : {
        "id" : 8477492,
        "fullName" : "Nathan MacKinnon",
        "link" : "/api/v1/people/8477492"
        },
        "playerType" : "Loser"
    } ],
    "result" : {
        "event" : "Faceoff",
        "eventCode" : "COL52",
        "eventTypeId" : "FACEOFF",
        "description" : "Ryan O'Reilly faceoff won against Nathan MacKinnon"
    },
    "about" : {
        "eventIdx" : 3,
        "eventId" : 666,
        "period" : 1,
        "periodType" : "REGULAR",
        "ordinalNum" : "1st",
        "periodTime" : "00:00",
        "periodTimeRemaining" : "20:00",
        "dateTime" : "2022-05-18T01:50:19Z",
        "goals" : {
        "away" : 0,
        "home" : 0
        }
    },
    "coordinates" : {
        "x" : 0.0,
        "y" : 0.0
    },
    "team" : {
        "id" : 19,
        "name" : "St. Louis Blues",
        "link" : "/api/v1/teams/19",
        "triCode" : "STL"
    }
}

faceoff_different_event_id_x = {
    "players" : [ {
        "player" : {
        "id" : 8475158,
        "fullName" : "Ryan O'Reilly",
        "link" : "/api/v1/people/8475158"
        },
        "playerType" : "Winner"
    }, {
        "player" : {
        "id" : 8477492,
        "fullName" : "Nathan MacKinnon",
        "link" : "/api/v1/people/8477492"
        },
        "playerType" : "Loser"
    } ],
    "result" : {
        "event" : "Faceoff",
        "eventCode" : "COL52",
        "eventTypeId" : "FACEOFF",
        "description" : "Ryan O'Reilly faceoff won against Nathan MacKinnon"
    },
    "about" : {
        "eventIdx" : 666,
        "eventId" : 52,
        "period" : 1,
        "periodType" : "REGULAR",
        "ordinalNum" : "1st",
        "periodTime" : "00:00",
        "periodTimeRemaining" : "20:00",
        "dateTime" : "2022-05-18T01:50:19Z",
        "goals" : {
        "away" : 0,
        "home" : 0
        }
    },
    "coordinates" : {
        "x" : 0.0,
        "y" : 0.0
    },
    "team" : {
        "id" : 19,
        "name" : "St. Louis Blues",
        "link" : "/api/v1/teams/19",
        "triCode" : "STL"
    }
}

faceoff_different_datetime = {
    "players" : [ {
        "player" : {
        "id" : 8475158,
        "fullName" : "Ryan O'Reilly",
        "link" : "/api/v1/people/8475158"
        },
        "playerType" : "Winner"
    }, {
        "player" : {
        "id" : 8477492,
        "fullName" : "Nathan MacKinnon",
        "link" : "/api/v1/people/8477492"
        },
        "playerType" : "Loser"
    } ],
    "result" : {
        "event" : "Faceoff",
        "eventCode" : "COL52",
        "eventTypeId" : "FACEOFF",
        "description" : "Ryan O'Reilly faceoff won against Nathan MacKinnon"
    },
    "about" : {
        "eventIdx" : 3,
        "eventId" : 52,
        "period" : 1,
        "periodType" : "REGULAR",
        "ordinalNum" : "1st",
        "periodTime" : "00:00",
        "periodTimeRemaining" : "20:00",
        "dateTime" : "2022-05-18T02:50:19Z",
        "goals" : {
        "away" : 0,
        "home" : 0
        }
    },
    "coordinates" : {
        "x" : 0.0,
        "y" : 0.0
    },
    "team" : {
        "id" : 19,
        "name" : "St. Louis Blues",
        "link" : "/api/v1/teams/19",
        "triCode" : "STL"
    }
}

faceoff_different_period = {
    "players" : [ {
        "player" : {
        "id" : 8475158,
        "fullName" : "Ryan O'Reilly",
        "link" : "/api/v1/people/8475158"
        },
        "playerType" : "Winner"
    }, {
        "player" : {
        "id" : 8477492,
        "fullName" : "Nathan MacKinnon",
        "link" : "/api/v1/people/8477492"
        },
        "playerType" : "Loser"
    } ],
    "result" : {
        "event" : "Faceoff",
        "eventCode" : "COL52",
        "eventTypeId" : "FACEOFF",
        "description" : "Ryan O'Reilly faceoff won against Nathan MacKinnon"
    },
    "about" : {
        "eventIdx" : 3,
        "eventId" : 52,
        "period" : 3,
        "periodType" : "REGULAR",
        "ordinalNum" : "1st",
        "periodTime" : "00:00",
        "periodTimeRemaining" : "20:00",
        "dateTime" : "2022-05-18T01:50:19Z",
        "goals" : {
        "away" : 0,
        "home" : 0
        }
    },
    "coordinates" : {
        "x" : 0.0,
        "y" : 0.0
    },
    "team" : {
        "id" : 19,
        "name" : "St. Louis Blues",
        "link" : "/api/v1/teams/19",
        "triCode" : "STL"
    }
}

faceoff_different_period_time = {
    "players" : [ {
        "player" : {
        "id" : 8475158,
        "fullName" : "Ryan O'Reilly",
        "link" : "/api/v1/people/8475158"
        },
        "playerType" : "Winner"
    }, {
        "player" : {
        "id" : 8477492,
        "fullName" : "Nathan MacKinnon",
        "link" : "/api/v1/people/8477492"
        },
        "playerType" : "Loser"
    } ],
    "result" : {
        "event" : "Faceoff",
        "eventCode" : "COL52",
        "eventTypeId" : "FACEOFF",
        "description" : "Ryan O'Reilly faceoff won against Nathan MacKinnon"
    },
    "about" : {
        "eventIdx" : 3,
        "eventId" : 52,
        "period" : 1,
        "periodType" : "REGULAR",
        "ordinalNum" : "1st",
        "periodTime" : "01:00",
        "periodTimeRemaining" : "20:00",
        "dateTime" : "2022-05-18T01:50:19Z",
        "goals" : {
        "away" : 0,
        "home" : 0
        }
    },
    "coordinates" : {
        "x" : 0.0,
        "y" : 0.0
    },
    "team" : {
        "id" : 19,
        "name" : "St. Louis Blues",
        "link" : "/api/v1/teams/19",
        "triCode" : "STL"
    }
}

faceoff_different_period_time_remaining = {
    "players" : [ {
        "player" : {
        "id" : 8475158,
        "fullName" : "Ryan O'Reilly",
        "link" : "/api/v1/people/8475158"
        },
        "playerType" : "Winner"
    }, {
        "player" : {
        "id" : 8477492,
        "fullName" : "Nathan MacKinnon",
        "link" : "/api/v1/people/8477492"
        },
        "playerType" : "Loser"
    } ],
    "result" : {
        "event" : "Faceoff",
        "eventCode" : "COL52",
        "eventTypeId" : "FACEOFF",
        "description" : "Ryan O'Reilly faceoff won against Nathan MacKinnon"
    },
    "about" : {
        "eventIdx" : 3,
        "eventId" : 52,
        "period" : 1,
        "periodType" : "REGULAR",
        "ordinalNum" : "1st",
        "periodTime" : "00:00",
        "periodTimeRemaining" : "19:00",
        "dateTime" : "2022-05-18T01:50:19Z",
        "goals" : {
        "away" : 0,
        "home" : 0
        }
    },
    "coordinates" : {
        "x" : 0.0,
        "y" : 0.0
    },
    "team" : {
        "id" : 19,
        "name" : "St. Louis Blues",
        "link" : "/api/v1/teams/19",
        "triCode" : "STL"
    }
}

faceoff_different_winner = {
    "players" : [ {
        "player" : {
        "id" : 99,
        "fullName" : "Wayne Gretzky",
        "link" : "/api/v1/people/8475158"
        },
        "playerType" : "Winner"
    }, {
        "player" : {
        "id" : 8477492,
        "fullName" : "Nathan MacKinnon",
        "link" : "/api/v1/people/8477492"
        },
        "playerType" : "Loser"
    } ],
    "result" : {
        "event" : "Faceoff",
        "eventCode" : "COL52",
        "eventTypeId" : "FACEOFF",
        "description" : "Ryan O'Reilly faceoff won against Nathan MacKinnon"
    },
    "about" : {
        "eventIdx" : 3,
        "eventId" : 52,
        "period" : 1,
        "periodType" : "REGULAR",
        "ordinalNum" : "1st",
        "periodTime" : "00:00",
        "periodTimeRemaining" : "20:00",
        "dateTime" : "2022-05-18T01:50:19Z",
        "goals" : {
        "away" : 0,
        "home" : 0
        }
    },
    "coordinates" : {
        "x" : 0.0,
        "y" : 0.0
    },
    "team" : {
        "id" : 19,
        "name" : "St. Louis Blues",
        "link" : "/api/v1/teams/19",
        "triCode" : "STL"
    }
}

faceoff_different_loser = {
    "players" : [ {
        "player" : {
        "id" : 8475158,
        "fullName" : "Ryan O'Reilly",
        "link" : "/api/v1/people/8475158"
        },
        "playerType" : "Winner"
    }, {
        "player" : {
        "id" : 99,
        "fullName" : "Wayne Gretzky",
        "link" : "/api/v1/people/8477492"
        },
        "playerType" : "Loser"
    } ],
    "result" : {
        "event" : "Faceoff",
        "eventCode" : "COL52",
        "eventTypeId" : "FACEOFF",
        "description" : "Ryan O'Reilly faceoff won against Nathan MacKinnon"
    },
    "about" : {
        "eventIdx" : 3,
        "eventId" : 52,
        "period" : 1,
        "periodType" : "REGULAR",
        "ordinalNum" : "1st",
        "periodTime" : "00:00",
        "periodTimeRemaining" : "20:00",
        "dateTime" : "2022-05-18T01:50:19Z",
        "goals" : {
        "away" : 0,
        "home" : 0
        }
    },
    "coordinates" : {
        "x" : 0.0,
        "y" : 0.0
    },
    "team" : {
        "id" : 19,
        "name" : "St. Louis Blues",
        "link" : "/api/v1/teams/19",
        "triCode" : "STL"
    }
}
