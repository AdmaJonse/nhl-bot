"""
Test events for coach's challenge.
"""

challenge_1 = {
    "result" : {
        "event" : "Official Challenge",
        "eventCode" : "FLA674",
        "eventTypeId" : "CHALLENGE",
        "description" : "Coach's Challenge"
    },
    "about" : {
        "eventIdx" : 295,
        "eventId" : 674,
        "period" : 3,
        "periodType" : "REGULAR",
        "ordinalNum" : "3rd",
        "periodTime" : "11:51",
        "periodTimeRemaining" : "08:09",
        "dateTime" : "2022-05-18T01:27:12Z",
        "goals" : {
        "away" : 2,
        "home" : 1
        }
    },
    "coordinates" : { },
    "team" : {
        "id" : 14,
        "name" : "Tampa Bay Lightning",
        "link" : "/api/v1/teams/14",
        "triCode" : "TBL"
    }
}

challenge_2 = {
    "result" : {
      "event" : "Official Challenge",
      "eventCode" : "COL405",
      "eventTypeId" : "CHALLENGE",
      "description" : "Coach's Challenge"
    },
    "about" : {
      "eventIdx" : 105,
      "eventId" : 405,
      "period" : 2,
      "periodType" : "REGULAR",
      "ordinalNum" : "2nd",
      "periodTime" : "01:54",
      "periodTimeRemaining" : "18:06",
      "dateTime" : "2022-04-01T02:05:31Z",
      "goals" : {
        "away" : 0,
        "home" : 1
      }
    },
    "coordinates" : { },
    "team" : {
      "id" : 21,
      "name" : "Colorado Avalanche",
      "link" : "/api/v1/teams/21",
      "triCode" : "COL"
    }
}

challenge_different_event_id = {
    "result" : {
        "event" : "Official Challenge",
        "eventCode" : "FLA674",
        "eventTypeId" : "CHALLENGE",
        "description" : "Coach's Challenge"
    },
    "about" : {
        "eventIdx" : 295,
        "eventId" : 666,
        "period" : 3,
        "periodType" : "REGULAR",
        "ordinalNum" : "3rd",
        "periodTime" : "11:51",
        "periodTimeRemaining" : "08:09",
        "dateTime" : "2022-05-18T01:27:12Z",
        "goals" : {
        "away" : 2,
        "home" : 1
        }
    },
    "coordinates" : { },
    "team" : {
        "id" : 14,
        "name" : "Tampa Bay Lightning",
        "link" : "/api/v1/teams/14",
        "triCode" : "TBL"
    }
}

challenge_different_event_id_x = {
    "result" : {
        "event" : "Official Challenge",
        "eventCode" : "FLA674",
        "eventTypeId" : "CHALLENGE",
        "description" : "Coach's Challenge"
    },
    "about" : {
        "eventIdx" : 666,
        "eventId" : 674,
        "period" : 3,
        "periodType" : "REGULAR",
        "ordinalNum" : "3rd",
        "periodTime" : "11:51",
        "periodTimeRemaining" : "08:09",
        "dateTime" : "2022-05-18T01:27:12Z",
        "goals" : {
        "away" : 2,
        "home" : 1
        }
    },
    "coordinates" : { },
    "team" : {
        "id" : 14,
        "name" : "Tampa Bay Lightning",
        "link" : "/api/v1/teams/14",
        "triCode" : "TBL"
    }
}

challenge_different_datetime = {
    "result" : {
        "event" : "Official Challenge",
        "eventCode" : "FLA674",
        "eventTypeId" : "CHALLENGE",
        "description" : "Coach's Challenge"
    },
    "about" : {
        "eventIdx" : 295,
        "eventId" : 674,
        "period" : 3,
        "periodType" : "REGULAR",
        "ordinalNum" : "3rd",
        "periodTime" : "11:51",
        "periodTimeRemaining" : "08:09",
        "dateTime" : "2022-05-18T01:28:12Z",
        "goals" : {
        "away" : 2,
        "home" : 1
        }
    },
    "coordinates" : { },
    "team" : {
        "id" : 14,
        "name" : "Tampa Bay Lightning",
        "link" : "/api/v1/teams/14",
        "triCode" : "TBL"
    }
}

challenge_different_period = {
    "result" : {
        "event" : "Official Challenge",
        "eventCode" : "FLA674",
        "eventTypeId" : "CHALLENGE",
        "description" : "Coach's Challenge"
    },
    "about" : {
        "eventIdx" : 295,
        "eventId" : 674,
        "period" : 2,
        "periodType" : "REGULAR",
        "ordinalNum" : "3rd",
        "periodTime" : "11:51",
        "periodTimeRemaining" : "08:09",
        "dateTime" : "2022-05-18T01:27:12Z",
        "goals" : {
        "away" : 2,
        "home" : 1
        }
    },
    "coordinates" : { },
    "team" : {
        "id" : 14,
        "name" : "Tampa Bay Lightning",
        "link" : "/api/v1/teams/14",
        "triCode" : "TBL"
    }
}

challenge_different_period_time = {
    "result" : {
        "event" : "Official Challenge",
        "eventCode" : "FLA674",
        "eventTypeId" : "CHALLENGE",
        "description" : "Coach's Challenge"
    },
    "about" : {
        "eventIdx" : 295,
        "eventId" : 674,
        "period" : 3,
        "periodType" : "REGULAR",
        "ordinalNum" : "3rd",
        "periodTime" : "11:52",
        "periodTimeRemaining" : "08:09",
        "dateTime" : "2022-05-18T01:27:12Z",
        "goals" : {
        "away" : 2,
        "home" : 1
        }
    },
    "coordinates" : { },
    "team" : {
        "id" : 14,
        "name" : "Tampa Bay Lightning",
        "link" : "/api/v1/teams/14",
        "triCode" : "TBL"
    }
}

challenge_different_period_time_remaining = {
    "result" : {
        "event" : "Official Challenge",
        "eventCode" : "FLA674",
        "eventTypeId" : "CHALLENGE",
        "description" : "Coach's Challenge"
    },
    "about" : {
        "eventIdx" : 295,
        "eventId" : 674,
        "period" : 3,
        "periodType" : "REGULAR",
        "ordinalNum" : "3rd",
        "periodTime" : "11:51",
        "periodTimeRemaining" : "08:10",
        "dateTime" : "2022-05-18T01:27:12Z",
        "goals" : {
        "away" : 2,
        "home" : 1
        }
    },
    "coordinates" : { },
    "team" : {
        "id" : 14,
        "name" : "Tampa Bay Lightning",
        "link" : "/api/v1/teams/14",
        "triCode" : "TBL"
    }
}
