"""
TODO
"""

period_ready_1 = {
    "result" : {
        "event" : "Period Ready",
        "eventCode" : "COL36",
        "eventTypeId" : "PERIOD_READY",
        "description" : "Period Ready"
    },
    "about" : {
        "eventIdx" : 94,
        "eventId" : 36,
        "period" : 2,
        "periodType" : "REGULAR",
        "ordinalNum" : "2nd",
        "periodTime" : "00:00",
        "periodTimeRemaining" : "20:00",
        "dateTime" : "2022-05-18T02:38:57Z",
        "goals" : {
        "away" : 1,
        "home" : 0
        }
    },
    "coordinates" : { }
}

period_ready_2 = {
    "result" : {
        "event" : "Period Ready",
        "eventCode" : "COL548",
        "eventTypeId" : "PERIOD_READY",
        "description" : "Period Ready"
    },
    "about" : {
        "eventIdx" : 337,
        "eventId" : 548,
        "period" : 4,
        "periodType" : "OVERTIME",
        "ordinalNum" : "OT",
        "periodTime" : "00:00",
        "periodTimeRemaining" : "20:00",
        "dateTime" : "2022-05-18T04:22:47Z",
        "goals" : {
        "away" : 2,
        "home" : 2
        }
    },
    "coordinates" : { }
}

period_ready_3 = {
    "result" : {
        "event" : "Period Ready",
        "eventCode" : "FLA261",
        "eventTypeId" : "PERIOD_READY",
        "description" : "Period Ready"
    },
    "about" : {
        "eventIdx" : 114,
        "eventId" : 261,
        "period" : 3,
        "periodType" : "REGULAR",
        "ordinalNum" : "2nd",
        "periodTime" : "00:00",
        "periodTimeRemaining" : "20:00",
        "dateTime" : "2022-05-18T00:05:03Z",
        "goals" : {
        "away" : 0,
        "home" : 1
        }
    },
    "coordinates" : { }
}

period_ready_different_event_id = {
    "result" : {
        "event" : "Period Ready",
        "eventCode" : "COL36",
        "eventTypeId" : "PERIOD_READY",
        "description" : "Period Ready"
    },
    "about" : {
        "eventIdx" : 94,
        "eventId" : 666,
        "period" : 2,
        "periodType" : "REGULAR",
        "ordinalNum" : "2nd",
        "periodTime" : "00:00",
        "periodTimeRemaining" : "20:00",
        "dateTime" : "2022-05-18T02:38:57Z",
        "goals" : {
        "away" : 1,
        "home" : 0
        }
    },
    "coordinates" : { }
}

period_ready_different_event_id_x = {
    "result" : {
        "event" : "Period Ready",
        "eventCode" : "COL36",
        "eventTypeId" : "PERIOD_READY",
        "description" : "Period Ready"
    },
    "about" : {
        "eventIdx" : 666,
        "eventId" : 36,
        "period" : 2,
        "periodType" : "REGULAR",
        "ordinalNum" : "2nd",
        "periodTime" : "00:00",
        "periodTimeRemaining" : "20:00",
        "dateTime" : "2022-05-18T02:38:57Z",
        "goals" : {
        "away" : 1,
        "home" : 0
        }
    },
    "coordinates" : { }
}

period_ready_different_datetime = {
    "result" : {
        "event" : "Period Ready",
        "eventCode" : "COL36",
        "eventTypeId" : "PERIOD_READY",
        "description" : "Period Ready"
    },
    "about" : {
        "eventIdx" : 94,
        "eventId" : 36,
        "period" : 2,
        "periodType" : "REGULAR",
        "ordinalNum" : "2nd",
        "periodTime" : "00:00",
        "periodTimeRemaining" : "20:00",
        "dateTime" : "2022-05-18T02:18:57Z",
        "goals" : {
        "away" : 1,
        "home" : 0
        }
    },
    "coordinates" : { }
}

period_ready_different_period = {
    "result" : {
        "event" : "Period Ready",
        "eventCode" : "COL36",
        "eventTypeId" : "PERIOD_READY",
        "description" : "Period Ready"
    },
    "about" : {
        "eventIdx" : 94,
        "eventId" : 36,
        "period" : 1,
        "periodType" : "REGULAR",
        "ordinalNum" : "2nd",
        "periodTime" : "00:00",
        "periodTimeRemaining" : "20:00",
        "dateTime" : "2022-05-18T02:38:57Z",
        "goals" : {
        "away" : 1,
        "home" : 0
        }
    },
    "coordinates" : { }
}

period_ready_different_period_time = {
    "result" : {
        "event" : "Period Ready",
        "eventCode" : "COL36",
        "eventTypeId" : "PERIOD_READY",
        "description" : "Period Ready"
    },
    "about" : {
        "eventIdx" : 94,
        "eventId" : 36,
        "period" : 2,
        "periodType" : "REGULAR",
        "ordinalNum" : "2nd",
        "periodTime" : "00:01",
        "periodTimeRemaining" : "20:00",
        "dateTime" : "2022-05-18T02:38:57Z",
        "goals" : {
        "away" : 1,
        "home" : 0
        }
    },
    "coordinates" : { }
}

period_ready_different_period_time_remaining = {
    "result" : {
        "event" : "Period Ready",
        "eventCode" : "COL36",
        "eventTypeId" : "PERIOD_READY",
        "description" : "Period Ready"
    },
    "about" : {
        "eventIdx" : 94,
        "eventId" : 36,
        "period" : 2,
        "periodType" : "REGULAR",
        "ordinalNum" : "2nd",
        "periodTime" : "00:00",
        "periodTimeRemaining" : "21:00",
        "dateTime" : "2022-05-18T02:38:57Z",
        "goals" : {
        "away" : 1,
        "home" : 0
        }
    },
    "coordinates" : { }
}
