"""
Test events for game ends.
"""

game_end_1 = {
    "result" : {
        "event" : "Game End",
        "eventCode" : "COL865",
        "eventTypeId" : "GAME_END",
        "description" : "Game End"
    },
    "about" : {
        "eventIdx" : 387,
        "eventId" : 865,
        "period" : 4,
        "periodType" : "OVERTIME",
        "ordinalNum" : "OT",
        "periodTime" : "08:02",
        "periodTimeRemaining" : "11:58",
        "dateTime" : "2022-05-18T04:38:08Z",
        "goals" : {
            "away" : 2,
            "home" : 3
        }
    },
    "coordinates" : { }
}

game_end_2 = {
    "result" : {
        "event" : "Game End",
        "eventCode" : "FLA692",
        "eventTypeId" : "GAME_END",
        "description" : "Game End"
    },
    "about" : {
        "eventIdx" : 349,
        "eventId" : 692,
        "period" : 3,
        "periodType" : "REGULAR",
        "ordinalNum" : "3rd",
        "periodTime" : "20:00",
        "periodTimeRemaining" : "00:00",
        "dateTime" : "2022-05-18T01:50:34Z",
        "goals" : {
            "away" : 4,
            "home" : 1
        }
    },
    "coordinates" : { }
}

game_end_different_event_id = {
    "result" : {
        "event" : "Game End",
        "eventCode" : "COL865",
        "eventTypeId" : "GAME_END",
        "description" : "Game End"
    },
    "about" : {
        "eventIdx" : 387,
        "eventId" : 666,
        "period" : 4,
        "periodType" : "OVERTIME",
        "ordinalNum" : "OT",
        "periodTime" : "08:02",
        "periodTimeRemaining" : "11:58",
        "dateTime" : "2022-05-18T04:38:08Z",
        "goals" : {
            "away" : 2,
            "home" : 3
        }
    },
    "coordinates" : { }
}

game_end_different_event_id_x = {
    "result" : {
        "event" : "Game End",
        "eventCode" : "COL865",
        "eventTypeId" : "GAME_END",
        "description" : "Game End"
    },
    "about" : {
        "eventIdx" : 666,
        "eventId" : 865,
        "period" : 4,
        "periodType" : "OVERTIME",
        "ordinalNum" : "OT",
        "periodTime" : "08:02",
        "periodTimeRemaining" : "11:58",
        "dateTime" : "2022-05-18T04:38:08Z",
        "goals" : {
            "away" : 2,
            "home" : 3
        }
    },
    "coordinates" : { }
}

game_end_different_datetime = {
    "result" : {
        "event" : "Game End",
        "eventCode" : "COL865",
        "eventTypeId" : "GAME_END",
        "description" : "Game End"
    },
    "about" : {
        "eventIdx" : 387,
        "eventId" : 865,
        "period" : 4,
        "periodType" : "OVERTIME",
        "ordinalNum" : "OT",
        "periodTime" : "08:02",
        "periodTimeRemaining" : "11:58",
        "dateTime" : "2022-05-18T04:39:08Z",
        "goals" : {
            "away" : 2,
            "home" : 3
        }
    },
    "coordinates" : { }
}

game_end_different_period = {
    "result" : {
        "event" : "Game End",
        "eventCode" : "COL865",
        "eventTypeId" : "GAME_END",
        "description" : "Game End"
    },
    "about" : {
        "eventIdx" : 387,
        "eventId" : 865,
        "period" : 3,
        "periodType" : "OVERTIME",
        "ordinalNum" : "OT",
        "periodTime" : "08:02",
        "periodTimeRemaining" : "11:58",
        "dateTime" : "2022-05-18T04:38:08Z",
        "goals" : {
            "away" : 2,
            "home" : 3
        }
    },
    "coordinates" : { }
}

game_end_different_period_time = {
    "result" : {
        "event" : "Game End",
        "eventCode" : "COL865",
        "eventTypeId" : "GAME_END",
        "description" : "Game End"
    },
    "about" : {
        "eventIdx" : 387,
        "eventId" : 865,
        "period" : 4,
        "periodType" : "OVERTIME",
        "ordinalNum" : "OT",
        "periodTime" : "08:01",
        "periodTimeRemaining" : "11:58",
        "dateTime" : "2022-05-18T04:38:08Z",
        "goals" : {
            "away" : 2,
            "home" : 3
        }
    },
    "coordinates" : { }
}

game_end_different_period_time_remaining = {
    "result" : {
        "event" : "Game End",
        "eventCode" : "COL865",
        "eventTypeId" : "GAME_END",
        "description" : "Game End"
    },
    "about" : {
        "eventIdx" : 387,
        "eventId" : 865,
        "period" : 4,
        "periodType" : "OVERTIME",
        "ordinalNum" : "OT",
        "periodTime" : "08:02",
        "periodTimeRemaining" : "11:59",
        "dateTime" : "2022-05-18T04:38:08Z",
        "goals" : {
            "away" : 2,
            "home" : 3
        }
    },
    "coordinates" : { }
}
