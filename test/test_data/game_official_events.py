"""
Test events for game official.
"""

game_official_1 = {
    "result" : {
        "event" : "Game Official",
        "eventCode" : "COL866",
        "eventTypeId" : "GAME_OFFICIAL",
        "description" : "Game Official"
    },
    "about" : {
        "eventIdx" : 388,
        "eventId" : 866,
        "period" : 4,
        "periodType" : "OVERTIME",
        "ordinalNum" : "OT",
        "periodTime" : "08:02",
        "periodTimeRemaining" : "11:58",
        "dateTime" : "2022-05-18T04:46:58Z",
        "goals" : {
        "away" : 2,
        "home" : 3
        }
    },
    "coordinates" : { }
}

game_official_2 = {
    "result" : {
        "event" : "Game Official",
        "eventCode" : "FLA1251",
        "eventTypeId" : "GAME_OFFICIAL",
        "description" : "Game Official"
    },
    "about" : {
        "eventIdx" : 350,
        "eventId" : 1251,
        "period" : 3,
        "periodType" : "REGULAR",
        "ordinalNum" : "3rd",
        "periodTime" : "20:00",
        "periodTimeRemaining" : "00:00",
        "dateTime" : "2022-05-18T10:46:32Z",
        "goals" : {
        "away" : 4,
        "home" : 1
        }
    },
    "coordinates" : { }
}

game_official_different_event_id = {
    "result" : {
        "event" : "Game Official",
        "eventCode" : "COL866",
        "eventTypeId" : "GAME_OFFICIAL",
        "description" : "Game Official"
    },
    "about" : {
        "eventIdx" : 388,
        "eventId" : 866,
        "period" : 4,
        "periodType" : "OVERTIME",
        "ordinalNum" : "OT",
        "periodTime" : "08:02",
        "periodTimeRemaining" : "11:58",
        "dateTime" : "2022-05-18T04:46:58Z",
        "goals" : {
        "away" : 2,
        "home" : 3
        }
    },
    "coordinates" : { }
}

game_official_different_event_id_x = {
    "result" : {
        "event" : "Game Official",
        "eventCode" : "COL866",
        "eventTypeId" : "GAME_OFFICIAL",
        "description" : "Game Official"
    },
    "about" : {
        "eventIdx" : 388,
        "eventId" : 866,
        "period" : 4,
        "periodType" : "OVERTIME",
        "ordinalNum" : "OT",
        "periodTime" : "08:02",
        "periodTimeRemaining" : "11:58",
        "dateTime" : "2022-05-18T04:46:58Z",
        "goals" : {
        "away" : 2,
        "home" : 3
        }
    },
    "coordinates" : { }
}

game_official_different_datetime = {
    "result" : {
        "event" : "Game Official",
        "eventCode" : "COL866",
        "eventTypeId" : "GAME_OFFICIAL",
        "description" : "Game Official"
    },
    "about" : {
        "eventIdx" : 388,
        "eventId" : 866,
        "period" : 4,
        "periodType" : "OVERTIME",
        "ordinalNum" : "OT",
        "periodTime" : "08:02",
        "periodTimeRemaining" : "11:58",
        "dateTime" : "2022-05-18T04:47:58Z",
        "goals" : {
        "away" : 2,
        "home" : 3
        }
    },
    "coordinates" : { }
}

game_official_different_period = {
    "result" : {
        "event" : "Game Official",
        "eventCode" : "COL866",
        "eventTypeId" : "GAME_OFFICIAL",
        "description" : "Game Official"
    },
    "about" : {
        "eventIdx" : 388,
        "eventId" : 866,
        "period" : 4,
        "periodType" : "OVERTIME",
        "ordinalNum" : "OT",
        "periodTime" : "08:02",
        "periodTimeRemaining" : "11:58",
        "dateTime" : "2022-05-18T04:46:58Z",
        "goals" : {
        "away" : 2,
        "home" : 3
        }
    },
    "coordinates" : { }
}

game_official_different_period_time = {
    "result" : {
        "event" : "Game Official",
        "eventCode" : "COL866",
        "eventTypeId" : "GAME_OFFICIAL",
        "description" : "Game Official"
    },
    "about" : {
        "eventIdx" : 388,
        "eventId" : 866,
        "period" : 4,
        "periodType" : "OVERTIME",
        "ordinalNum" : "OT",
        "periodTime" : "08:02",
        "periodTimeRemaining" : "11:58",
        "dateTime" : "2022-05-18T04:46:58Z",
        "goals" : {
        "away" : 2,
        "home" : 3
        }
    },
    "coordinates" : { }
}

game_official_different_period_time_remaining = {
    "result" : {
        "event" : "Game Official",
        "eventCode" : "COL866",
        "eventTypeId" : "GAME_OFFICIAL",
        "description" : "Game Official"
    },
    "about" : {
        "eventIdx" : 388,
        "eventId" : 866,
        "period" : 4,
        "periodType" : "OVERTIME",
        "ordinalNum" : "OT",
        "periodTime" : "08:02",
        "periodTimeRemaining" : "11:58",
        "dateTime" : "2022-05-18T04:46:58Z",
        "goals" : {
        "away" : 2,
        "home" : 3
        }
    },
    "coordinates" : { }
}
