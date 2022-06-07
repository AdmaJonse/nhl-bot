"""
TODO
"""

game_scheduled_1 = {
    "result" : {
        "event" : "Game Scheduled",
        "eventCode" : "COL1",
        "eventTypeId" : "GAME_SCHEDULED",
        "description" : "Game Scheduled"
    },
    "about" : {
        "eventIdx" : 0,
        "eventId" : 1,
        "period" : 1,
        "periodType" : "REGULAR",
        "ordinalNum" : "1st",
        "periodTime" : "00:00",
        "periodTimeRemaining" : "20:00",
        "dateTime" : "2022-05-18T01:06:28Z",
        "goals" : {
        "away" : 0,
        "home" : 0
        }
    },
    "coordinates" : { }
}

game_scheduled_2 = {
    "result" : {
        "event" : "Game Scheduled",
        "eventCode" : "FLA1",
        "eventTypeId" : "GAME_SCHEDULED",
        "description" : "Game Scheduled"
    },
    "about" : {
        "eventIdx" : 0,
        "eventId" : 1,
        "period" : 1,
        "periodType" : "REGULAR",
        "ordinalNum" : "1st",
        "periodTime" : "00:00",
        "periodTimeRemaining" : "20:00",
        "dateTime" : "2022-05-17T22:14:26Z",
        "goals" : {
        "away" : 0,
        "home" : 0
        }
    },
    "coordinates" : { }
}

game_scheduled_different_event_id = {
    "result" : {
        "event" : "Game Scheduled",
        "eventCode" : "COL1",
        "eventTypeId" : "GAME_SCHEDULED",
        "description" : "Game Scheduled"
    },
    "about" : {
        "eventIdx" : 0,
        "eventId" : 100,
        "period" : 1,
        "periodType" : "REGULAR",
        "ordinalNum" : "1st",
        "periodTime" : "00:00",
        "periodTimeRemaining" : "20:00",
        "dateTime" : "2022-05-18T01:06:28Z",
        "goals" : {
        "away" : 0,
        "home" : 0
        }
    },
    "coordinates" : { }
}

game_scheduled_different_event_id_x = {
    "result" : {
        "event" : "Game Scheduled",
        "eventCode" : "COL1",
        "eventTypeId" : "GAME_SCHEDULED",
        "description" : "Game Scheduled"
    },
    "about" : {
        "eventIdx" : 100,
        "eventId" : 1,
        "period" : 1,
        "periodType" : "REGULAR",
        "ordinalNum" : "1st",
        "periodTime" : "00:00",
        "periodTimeRemaining" : "20:00",
        "dateTime" : "2022-05-18T01:06:28Z",
        "goals" : {
        "away" : 0,
        "home" : 0
        }
    },
    "coordinates" : { }
}

game_scheduled_different_datetime = {
    "result" : {
        "event" : "Game Scheduled",
        "eventCode" : "COL1",
        "eventTypeId" : "GAME_SCHEDULED",
        "description" : "Game Scheduled"
    },
    "about" : {
        "eventIdx" : 0,
        "eventId" : 1,
        "period" : 1,
        "periodType" : "REGULAR",
        "ordinalNum" : "1st",
        "periodTime" : "00:00",
        "periodTimeRemaining" : "20:00",
        "dateTime" : "2022-05-18T01:05:28Z",
        "goals" : {
        "away" : 0,
        "home" : 0
        }
    },
    "coordinates" : { }
}

game_scheduled_different_period = {
    "result" : {
        "event" : "Game Scheduled",
        "eventCode" : "COL1",
        "eventTypeId" : "GAME_SCHEDULED",
        "description" : "Game Scheduled"
    },
    "about" : {
        "eventIdx" : 0,
        "eventId" : 1,
        "period" : 3,
        "periodType" : "REGULAR",
        "ordinalNum" : "1st",
        "periodTime" : "00:00",
        "periodTimeRemaining" : "20:00",
        "dateTime" : "2022-05-18T01:06:28Z",
        "goals" : {
        "away" : 0,
        "home" : 0
        }
    },
    "coordinates" : { }
}

game_scheduled_different_period_time = {
    "result" : {
        "event" : "Game Scheduled",
        "eventCode" : "COL1",
        "eventTypeId" : "GAME_SCHEDULED",
        "description" : "Game Scheduled"
    },
    "about" : {
        "eventIdx" : 0,
        "eventId" : 1,
        "period" : 1,
        "periodType" : "REGULAR",
        "ordinalNum" : "1st",
        "periodTime" : "00:01",
        "periodTimeRemaining" : "20:00",
        "dateTime" : "2022-05-18T01:06:28Z",
        "goals" : {
        "away" : 0,
        "home" : 0
        }
    },
    "coordinates" : { }
}

game_scheduled_different_period_time_remaining = {
    "result" : {
        "event" : "Game Scheduled",
        "eventCode" : "COL1",
        "eventTypeId" : "GAME_SCHEDULED",
        "description" : "Game Scheduled"
    },
    "about" : {
        "eventIdx" : 0,
        "eventId" : 1,
        "period" : 1,
        "periodType" : "REGULAR",
        "ordinalNum" : "1st",
        "periodTime" : "00:00",
        "periodTimeRemaining" : "19:00",
        "dateTime" : "2022-05-18T01:06:28Z",
        "goals" : {
        "away" : 0,
        "home" : 0
        }
    },
    "coordinates" : { }
}
