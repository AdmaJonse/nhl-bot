"""
Test events for period official.
"""

period_official_1 = {
    "result" : {
        "event" : "Period Official",
        "eventCode" : "FLA691",
        "eventTypeId" : "PERIOD_OFFICIAL",
        "description" : "Period Official"
    },
    "about" : {
        "eventIdx" : 348,
        "eventId" : 691,
        "period" : 3,
        "periodType" : "REGULAR",
        "ordinalNum" : "3rd",
        "periodTime" : "20:00",
        "periodTimeRemaining" : "00:00",
        "dateTime" : "2022-05-18T01:50:29Z",
        "goals" : {
        "away" : 4,
        "home" : 1
        }
    },
    "coordinates" : { }
}

period_official_2 = {
    "result" : {
        "event" : "Period Official",
        "eventCode" : "FLA651",
        "eventTypeId" : "PERIOD_OFFICIAL",
        "description" : "Period Official"
    },
    "about" : {
        "eventIdx" : 232,
        "eventId" : 651,
        "period" : 2,
        "periodType" : "REGULAR",
        "ordinalNum" : "2nd",
        "periodTime" : "20:00",
        "periodTimeRemaining" : "00:00",
        "dateTime" : "2022-05-18T00:58:06Z",
        "goals" : {
        "away" : 1,
        "home" : 1
        }
    },
    "coordinates" : { }
}

period_official_3 = {
    "result" : {
        "event" : "Period Official",
        "eventCode" : "COL35",
        "eventTypeId" : "PERIOD_OFFICIAL",
        "description" : "Period Official"
    },
    "about" : {
        "eventIdx" : 93,
        "eventId" : 35,
        "period" : 1,
        "periodType" : "REGULAR",
        "ordinalNum" : "1st",
        "periodTime" : "20:00",
        "periodTimeRemaining" : "00:00",
        "dateTime" : "2022-05-18T02:38:52Z",
        "goals" : {
        "away" : 1,
        "home" : 0
        }
    },
    "coordinates" : { }
}

period_official_different_event_id = {
    "result" : {
        "event" : "Period Official",
        "eventCode" : "FLA691",
        "eventTypeId" : "PERIOD_OFFICIAL",
        "description" : "Period Official"
    },
    "about" : {
        "eventIdx" : 348,
        "eventId" : 666,
        "period" : 3,
        "periodType" : "REGULAR",
        "ordinalNum" : "3rd",
        "periodTime" : "20:00",
        "periodTimeRemaining" : "00:00",
        "dateTime" : "2022-05-18T01:50:29Z",
        "goals" : {
        "away" : 4,
        "home" : 1
        }
    },
    "coordinates" : { }
}

period_official_different_event_id_x = {
    "result" : {
        "event" : "Period Official",
        "eventCode" : "FLA691",
        "eventTypeId" : "PERIOD_OFFICIAL",
        "description" : "Period Official"
    },
    "about" : {
        "eventIdx" : 666,
        "eventId" : 691,
        "period" : 3,
        "periodType" : "REGULAR",
        "ordinalNum" : "3rd",
        "periodTime" : "20:00",
        "periodTimeRemaining" : "00:00",
        "dateTime" : "2022-05-18T01:50:29Z",
        "goals" : {
        "away" : 4,
        "home" : 1
        }
    },
    "coordinates" : { }
}

period_official_different_datetime = {
    "result" : {
        "event" : "Period Official",
        "eventCode" : "FLA691",
        "eventTypeId" : "PERIOD_OFFICIAL",
        "description" : "Period Official"
    },
    "about" : {
        "eventIdx" : 348,
        "eventId" : 691,
        "period" : 3,
        "periodType" : "REGULAR",
        "ordinalNum" : "3rd",
        "periodTime" : "20:00",
        "periodTimeRemaining" : "00:00",
        "dateTime" : "2022-05-18T01:10:29Z",
        "goals" : {
        "away" : 4,
        "home" : 1
        }
    },
    "coordinates" : { }
}

period_official_different_period = {
    "result" : {
        "event" : "Period Official",
        "eventCode" : "FLA691",
        "eventTypeId" : "PERIOD_OFFICIAL",
        "description" : "Period Official"
    },
    "about" : {
        "eventIdx" : 348,
        "eventId" : 691,
        "period" : 2,
        "periodType" : "REGULAR",
        "ordinalNum" : "3rd",
        "periodTime" : "20:00",
        "periodTimeRemaining" : "00:00",
        "dateTime" : "2022-05-18T01:50:29Z",
        "goals" : {
        "away" : 4,
        "home" : 1
        }
    },
    "coordinates" : { }
}

period_official_different_period_time = {
    "result" : {
        "event" : "Period Official",
        "eventCode" : "FLA691",
        "eventTypeId" : "PERIOD_OFFICIAL",
        "description" : "Period Official"
    },
    "about" : {
        "eventIdx" : 348,
        "eventId" : 691,
        "period" : 3,
        "periodType" : "REGULAR",
        "ordinalNum" : "3rd",
        "periodTime" : "20:20",
        "periodTimeRemaining" : "00:00",
        "dateTime" : "2022-05-18T01:50:29Z",
        "goals" : {
        "away" : 4,
        "home" : 1
        }
    },
    "coordinates" : { }
}

period_official_different_period_time_remaining = {
    "result" : {
        "event" : "Period Official",
        "eventCode" : "FLA691",
        "eventTypeId" : "PERIOD_OFFICIAL",
        "description" : "Period Official"
    },
    "about" : {
        "eventIdx" : 348,
        "eventId" : 691,
        "period" : 3,
        "periodType" : "REGULAR",
        "ordinalNum" : "3rd",
        "periodTime" : "20:00",
        "periodTimeRemaining" : "00:01",
        "dateTime" : "2022-05-18T01:50:29Z",
        "goals" : {
        "away" : 4,
        "home" : 1
        }
    },
    "coordinates" : { }
}
