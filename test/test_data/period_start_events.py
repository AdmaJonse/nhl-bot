"""
Test events for period start.
"""

period_start_1 = {
    "result" : {
        "event" : "Period Start",
        "eventCode" : "FLA262",
        "eventTypeId" : "PERIOD_START",
        "description" : "Period Start"
    },
    "about" : {
        "eventIdx" : 115,
        "eventId" : 262,
        "period" : 2,
        "periodType" : "REGULAR",
        "ordinalNum" : "2nd",
        "periodTime" : "00:00",
        "periodTimeRemaining" : "20:00",
        "dateTime" : "2022-05-18T00:05:32Z",
        "goals" : {
        "away" : 0,
        "home" : 1
        }
    },
    "coordinates" : { }
}

period_start_2 = {
    "result" : {
        "event" : "Period Start",
        "eventCode" : "FLA653",
        "eventTypeId" : "PERIOD_START",
        "description" : "Period Start"
    },
    "about" : {
        "eventIdx" : 234,
        "eventId" : 653,
        "period" : 3,
        "periodType" : "REGULAR",
        "ordinalNum" : "3rd",
        "periodTime" : "00:00",
        "periodTimeRemaining" : "20:00",
        "dateTime" : "2022-05-18T01:04:23Z",
        "goals" : {
        "away" : 1,
        "home" : 1
        }
    },
    "coordinates" : { }
}

period_start_3 = {
    "result" : {
        "event" : "Period Start",
        "eventCode" : "COL715",
        "eventTypeId" : "PERIOD_START",
        "description" : "Period Start"
    },
    "about" : {
        "eventIdx" : 229,
        "eventId" : 715,
        "period" : 1,
        "periodType" : "REGULAR",
        "ordinalNum" : "3rd",
        "periodTime" : "00:00",
        "periodTimeRemaining" : "20:00",
        "dateTime" : "2022-05-18T03:36:35Z",
        "goals" : {
        "away" : 1,
        "home" : 2
        }
    },
    "coordinates" : { }
}

period_start_different_event_id = {
    "result" : {
        "event" : "Period Start",
        "eventCode" : "FLA262",
        "eventTypeId" : "PERIOD_START",
        "description" : "Period Start"
    },
    "about" : {
        "eventIdx" : 115,
        "eventId" : 666,
        "period" : 2,
        "periodType" : "REGULAR",
        "ordinalNum" : "2nd",
        "periodTime" : "00:00",
        "periodTimeRemaining" : "20:00",
        "dateTime" : "2022-05-18T00:05:32Z",
        "goals" : {
        "away" : 0,
        "home" : 1
        }
    },
    "coordinates" : { }
}

period_start_different_event_id_x = {
    "result" : {
        "event" : "Period Start",
        "eventCode" : "FLA262",
        "eventTypeId" : "PERIOD_START",
        "description" : "Period Start"
    },
    "about" : {
        "eventIdx" : 666,
        "eventId" : 262,
        "period" : 2,
        "periodType" : "REGULAR",
        "ordinalNum" : "2nd",
        "periodTime" : "00:00",
        "periodTimeRemaining" : "20:00",
        "dateTime" : "2022-05-18T00:05:32Z",
        "goals" : {
        "away" : 0,
        "home" : 1
        }
    },
    "coordinates" : { }
}

period_start_different_datetime = {
    "result" : {
        "event" : "Period Start",
        "eventCode" : "FLA262",
        "eventTypeId" : "PERIOD_START",
        "description" : "Period Start"
    },
    "about" : {
        "eventIdx" : 115,
        "eventId" : 262,
        "period" : 2,
        "periodType" : "REGULAR",
        "ordinalNum" : "2nd",
        "periodTime" : "00:00",
        "periodTimeRemaining" : "20:00",
        "dateTime" : "2022-05-18T00:15:32Z",
        "goals" : {
        "away" : 0,
        "home" : 1
        }
    },
    "coordinates" : { }
}

period_start_different_period = {
    "result" : {
        "event" : "Period Start",
        "eventCode" : "FLA262",
        "eventTypeId" : "PERIOD_START",
        "description" : "Period Start"
    },
    "about" : {
        "eventIdx" : 115,
        "eventId" : 262,
        "period" : 3,
        "periodType" : "REGULAR",
        "ordinalNum" : "2nd",
        "periodTime" : "00:00",
        "periodTimeRemaining" : "20:00",
        "dateTime" : "2022-05-18T00:05:32Z",
        "goals" : {
        "away" : 0,
        "home" : 1
        }
    },
    "coordinates" : { }
}

period_start_different_period_time = {
    "result" : {
        "event" : "Period Start",
        "eventCode" : "FLA262",
        "eventTypeId" : "PERIOD_START",
        "description" : "Period Start"
    },
    "about" : {
        "eventIdx" : 115,
        "eventId" : 262,
        "period" : 2,
        "periodType" : "REGULAR",
        "ordinalNum" : "2nd",
        "periodTime" : "00:10",
        "periodTimeRemaining" : "20:00",
        "dateTime" : "2022-05-18T00:05:32Z",
        "goals" : {
        "away" : 0,
        "home" : 1
        }
    },
    "coordinates" : { }
}

period_start_different_period_time_remaining = {
    "result" : {
        "event" : "Period Start",
        "eventCode" : "FLA262",
        "eventTypeId" : "PERIOD_START",
        "description" : "Period Start"
    },
    "about" : {
        "eventIdx" : 115,
        "eventId" : 262,
        "period" : 2,
        "periodType" : "REGULAR",
        "ordinalNum" : "2nd",
        "periodTime" : "00:00",
        "periodTimeRemaining" : "20:01",
        "dateTime" : "2022-05-18T00:05:32Z",
        "goals" : {
        "away" : 0,
        "home" : 1
        }
    },
    "coordinates" : { }
}
