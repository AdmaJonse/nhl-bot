"""
TODO
"""

period_end_1 = {
    "result" : {
        "event" : "Period End",
        "eventCode" : "COL514",
        "eventTypeId" : "PERIOD_END",
        "description" : "End of 2nd Period"
    },
    "about" : {
        "eventIdx" : 226,
        "eventId" : 514,
        "period" : 2,
        "periodType" : "REGULAR",
        "ordinalNum" : "2nd",
        "periodTime" : "20:00",
        "periodTimeRemaining" : "00:00",
        "dateTime" : "2022-05-18T03:17:48Z",
        "goals" : {
        "away" : 1,
        "home" : 2
        }
    },
    "coordinates" : { }
}

period_end_2 = {
    "result" : {
        "event" : "Period End",
        "eventCode" : "COL32",
        "eventTypeId" : "PERIOD_END",
        "description" : "End of 1st Period"
    },
    "about" : {
        "eventIdx" : 92,
        "eventId" : 32,
        "period" : 1,
        "periodType" : "REGULAR",
        "ordinalNum" : "1st",
        "periodTime" : "20:00",
        "periodTimeRemaining" : "00:00",
        "dateTime" : "2022-05-18T02:22:03Z",
        "goals" : {
        "away" : 1,
        "home" : 0
        }
    },
    "coordinates" : { }
}

period_end_3 = {
    "result" : {
        "event" : "Period End",
        "eventCode" : "FLA688",
        "eventTypeId" : "PERIOD_END",
        "description" : "End of 3rd Period"
    },
    "about" : {
        "eventIdx" : 347,
        "eventId" : 688,
        "period" : 3,
        "periodType" : "REGULAR",
        "ordinalNum" : "3rd",
        "periodTime" : "20:00",
        "periodTimeRemaining" : "00:00",
        "dateTime" : "2022-05-18T01:50:23Z",
        "goals" : {
        "away" : 4,
        "home" : 1
        }
    },
    "coordinates" : { }
}

period_end_different_event_id = {
    "result" : {
        "event" : "Period End",
        "eventCode" : "COL514",
        "eventTypeId" : "PERIOD_END",
        "description" : "End of 2nd Period"
    },
    "about" : {
        "eventIdx" : 226,
        "eventId" : 666,
        "period" : 2,
        "periodType" : "REGULAR",
        "ordinalNum" : "2nd",
        "periodTime" : "20:00",
        "periodTimeRemaining" : "00:00",
        "dateTime" : "2022-05-18T03:17:48Z",
        "goals" : {
        "away" : 1,
        "home" : 2
        }
    },
    "coordinates" : { }
}

period_end_different_event_id_x = {
    "result" : {
        "event" : "Period End",
        "eventCode" : "COL514",
        "eventTypeId" : "PERIOD_END",
        "description" : "End of 2nd Period"
    },
    "about" : {
        "eventIdx" : 666,
        "eventId" : 514,
        "period" : 2,
        "periodType" : "REGULAR",
        "ordinalNum" : "2nd",
        "periodTime" : "20:00",
        "periodTimeRemaining" : "00:00",
        "dateTime" : "2022-05-18T03:17:48Z",
        "goals" : {
        "away" : 1,
        "home" : 2
        }
    },
    "coordinates" : { }
}

period_end_different_datetime = {
    "result" : {
        "event" : "Period End",
        "eventCode" : "COL514",
        "eventTypeId" : "PERIOD_END",
        "description" : "End of 2nd Period"
    },
    "about" : {
        "eventIdx" : 226,
        "eventId" : 514,
        "period" : 2,
        "periodType" : "REGULAR",
        "ordinalNum" : "2nd",
        "periodTime" : "20:00",
        "periodTimeRemaining" : "00:00",
        "dateTime" : "2022-05-18T03:16:48Z",
        "goals" : {
        "away" : 1,
        "home" : 2
        }
    },
    "coordinates" : { }
}

period_end_different_period = {
    "result" : {
        "event" : "Period End",
        "eventCode" : "COL514",
        "eventTypeId" : "PERIOD_END",
        "description" : "End of 2nd Period"
    },
    "about" : {
        "eventIdx" : 226,
        "eventId" : 514,
        "period" : 3,
        "periodType" : "REGULAR",
        "ordinalNum" : "2nd",
        "periodTime" : "20:00",
        "periodTimeRemaining" : "00:00",
        "dateTime" : "2022-05-18T03:17:48Z",
        "goals" : {
        "away" : 1,
        "home" : 2
        }
    },
    "coordinates" : { }
}

period_end_different_period_time = {
    "result" : {
        "event" : "Period End",
        "eventCode" : "COL514",
        "eventTypeId" : "PERIOD_END",
        "description" : "End of 2nd Period"
    },
    "about" : {
        "eventIdx" : 226,
        "eventId" : 514,
        "period" : 2,
        "periodType" : "REGULAR",
        "ordinalNum" : "2nd",
        "periodTime" : "19:00",
        "periodTimeRemaining" : "00:00",
        "dateTime" : "2022-05-18T03:17:48Z",
        "goals" : {
        "away" : 1,
        "home" : 2
        }
    },
    "coordinates" : { }
}

period_end_different_period_time_remaining = {
    "result" : {
        "event" : "Period End",
        "eventCode" : "COL514",
        "eventTypeId" : "PERIOD_END",
        "description" : "End of 2nd Period"
    },
    "about" : {
        "eventIdx" : 226,
        "eventId" : 514,
        "period" : 2,
        "periodType" : "REGULAR",
        "ordinalNum" : "2nd",
        "periodTime" : "20:00",
        "periodTimeRemaining" : "01:00",
        "dateTime" : "2022-05-18T03:17:48Z",
        "goals" : {
        "away" : 1,
        "home" : 2
        }
    },
    "coordinates" : { }
}
