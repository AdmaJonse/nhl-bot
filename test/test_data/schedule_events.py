"""
Description:
    Test data for unit tests describing the NHL schedule.
"""

valid_schedule_data = {
    "copyright" : "",
    "totalItems" : 1,
    "totalEvents" : 0,
    "totalGames" : 1,
    "totalMatches" : 0,
    "metaData" : {
        "timeStamp" : "20220412_013822"
    },
    "wait" : 10,
    "dates" : [ {
        "date" : "2022-04-11",
        "totalItems" : 1,
        "totalEvents" : 0,
        "totalGames" : 1,
        "totalMatches" : 0,
        "games" : [ {
        "gamePk" : 2021021162,
        "link" : "/api/v1/game/2021021162/feed/live",
        "gameType" : "R",
        "season" : "20212022",
        "gameDate" : "2022-04-11T23:00:00Z",
        "status" : {
            "abstractGameState" : "Final",
            "codedGameState" : "6",
            "detailedState" : "Final",
            "statusCode" : "6",
            "startTimeTBD" : False
        },
        "teams" : {
        },
        "venue" : {
            "name" : "Centre Bell",
            "link" : "/api/v1/venues/null"
        },
        "content" : {
            "link" : "/api/v1/game/2021021162/content"
        }
        } ],
        "events" : [ ],
        "matches" : [ ]
    } ]
}

invalid_schedule_data = {
    "copyright" : "",
    "totalItems" : 0,
    "totalEvents" : 0,
    "totalGames" : 0,
    "totalMatches" : 0,
    "metaData" : {
        "timeStamp" : "20220412_013745"
    },
    "wait" : 10,
    "dates" : [ ]
}
