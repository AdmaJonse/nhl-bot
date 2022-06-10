"""
TODO
"""

stoppage_1 = {
    "result" : {
        "event" : "Stoppage",
        "eventCode" : "COL9",
        "eventTypeId" : "STOP",
        "description" : "Goalie Stopped"
    },
    "about" : {
        "eventIdx" : 7,
        "eventId" : 9,
        "period" : 1,
        "periodType" : "REGULAR",
        "ordinalNum" : "1st",
        "periodTime" : "01:18",
        "periodTimeRemaining" : "18:42",
        "dateTime" : "2022-05-18T01:51:36Z",
        "goals" : {
        "away" : 0,
        "home" : 0
        }
    },
    "coordinates" : { }
}

stoppage_2 = {
    "result" : {
        "event" : "Stoppage",
        "eventCode" : "COL22",
        "eventTypeId" : "STOP",
        "description" : "Icing"
    },
    "about" : {
        "eventIdx" : 60,
        "eventId" : 22,
        "period" : 1,
        "periodType" : "REGULAR",
        "ordinalNum" : "1st",
        "periodTime" : "13:30",
        "periodTimeRemaining" : "06:30",
        "dateTime" : "2022-05-18T02:06:35Z",
        "goals" : {
        "away" : 1,
        "home" : 0
        }
    },
    "coordinates" : { }
}

stoppage_3 = {
    "result" : {
        "event" : "Stoppage",
        "eventCode" : "FLA654",
        "eventTypeId" : "STOP",
        "description" : "Goalie Stopped"
    },
    "about" : {
        "eventIdx" : 239,
        "eventId" : 654,
        "period" : 3,
        "periodType" : "REGULAR",
        "ordinalNum" : "3rd",
        "periodTime" : "01:30",
        "periodTimeRemaining" : "18:30",
        "dateTime" : "2022-05-18T01:05:53Z",
        "goals" : {
        "away" : 1,
        "home" : 1
        }
    },
    "coordinates" : { }
}

stoppage_different_event_id = {
    "result" : {
        "event" : "Stoppage",
        "eventCode" : "COL9",
        "eventTypeId" : "STOP",
        "description" : "Goalie Stopped"
    },
    "about" : {
        "eventIdx" : 7,
        "eventId" : 666,
        "period" : 1,
        "periodType" : "REGULAR",
        "ordinalNum" : "1st",
        "periodTime" : "01:18",
        "periodTimeRemaining" : "18:42",
        "dateTime" : "2022-05-18T01:51:36Z",
        "goals" : {
        "away" : 0,
        "home" : 0
        }
    },
    "coordinates" : { }
}

stoppage_different_event_id_x = {
    "result" : {
        "event" : "Stoppage",
        "eventCode" : "COL9",
        "eventTypeId" : "STOP",
        "description" : "Goalie Stopped"
    },
    "about" : {
        "eventIdx" : 666,
        "eventId" : 9,
        "period" : 1,
        "periodType" : "REGULAR",
        "ordinalNum" : "1st",
        "periodTime" : "01:18",
        "periodTimeRemaining" : "18:42",
        "dateTime" : "2022-05-18T01:51:36Z",
        "goals" : {
        "away" : 0,
        "home" : 0
        }
    },
    "coordinates" : { }
}

stoppage_different_datetime = {
    "result" : {
        "event" : "Stoppage",
        "eventCode" : "COL9",
        "eventTypeId" : "STOP",
        "description" : "Goalie Stopped"
    },
    "about" : {
        "eventIdx" : 7,
        "eventId" : 9,
        "period" : 1,
        "periodType" : "REGULAR",
        "ordinalNum" : "1st",
        "periodTime" : "01:18",
        "periodTimeRemaining" : "18:42",
        "dateTime" : "2022-05-18T21:51:36Z",
        "goals" : {
        "away" : 0,
        "home" : 0
        }
    },
    "coordinates" : { }
}

stoppage_different_period = {
    "result" : {
        "event" : "Stoppage",
        "eventCode" : "COL9",
        "eventTypeId" : "STOP",
        "description" : "Goalie Stopped"
    },
    "about" : {
        "eventIdx" : 7,
        "eventId" : 9,
        "period" : 2,
        "periodType" : "REGULAR",
        "ordinalNum" : "1st",
        "periodTime" : "01:18",
        "periodTimeRemaining" : "18:42",
        "dateTime" : "2022-05-18T01:51:36Z",
        "goals" : {
        "away" : 0,
        "home" : 0
        }
    },
    "coordinates" : { }
}

stoppage_different_period_time = {
    "result" : {
        "event" : "Stoppage",
        "eventCode" : "COL9",
        "eventTypeId" : "STOP",
        "description" : "Goalie Stopped"
    },
    "about" : {
        "eventIdx" : 7,
        "eventId" : 9,
        "period" : 1,
        "periodType" : "REGULAR",
        "ordinalNum" : "1st",
        "periodTime" : "01:28",
        "periodTimeRemaining" : "18:42",
        "dateTime" : "2022-05-18T01:51:36Z",
        "goals" : {
        "away" : 0,
        "home" : 0
        }
    },
    "coordinates" : { }
}

stoppage_different_period_time_remaining = {
    "result" : {
        "event" : "Stoppage",
        "eventCode" : "COL9",
        "eventTypeId" : "STOP",
        "description" : "Goalie Stopped"
    },
    "about" : {
        "eventIdx" : 7,
        "eventId" : 9,
        "period" : 1,
        "periodType" : "REGULAR",
        "ordinalNum" : "1st",
        "periodTime" : "01:18",
        "periodTimeRemaining" : "18:22",
        "dateTime" : "2022-05-18T01:51:36Z",
        "goals" : {
        "away" : 0,
        "home" : 0
        }
    },
    "coordinates" : { }
}