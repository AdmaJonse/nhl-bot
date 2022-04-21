"""
Description:
    Test data for unit tests describing game events.
"""

game_data = {
    "gameData": {
        "datetime": {
            "dateTime": "2022-04-10T17:30:00Z",
            "endDateTime": "2022-04-10T20:12:25Z"
        },
        "about": {
            "periodTimeRemaining": "20:00",
            "ordinalNum": "1st"
        },
        "teams": {
            "away": {
                "name": "Boston Bruins",
                "abbreviation": "BOS",
                "teamName": "Bruins",
                "locationName": "Boston"
            },
            "home": {
                "name": "Washington Capitals",
                "venue": {
                    "name": "Capital One Arena"
                },
                "abbreviation": "WSH",
                "teamName": "Capitals",
                "locationName": "Washington"
            }
        }
    },
    "liveData": {
        "linescore": {
            "teams": {
                "home": {
                    "team": {
                        "id": 15,
                        "name": "Washington Capitals",
                        "link": "/api/v1/teams/15",
                        "abbreviation": "WSH",
                        "triCode": "WSH"
                    },
                    "goals": 4,
                    "shotsOnGoal": 33,
                    "goaliePulled": False,
                    "numSkaters": 5,
                    "powerPlay": False
                },
                "away": {
                    "team": {
                        "id": 6,
                        "name": "Boston Bruins",
                        "link": "/api/v1/teams/6",
                        "abbreviation": "BOS",
                        "triCode": "BOS"
                    },
                    "goals": 2,
                    "shotsOnGoal": 30,
                    "goaliePulled": False,
                    "numSkaters": 5,
                    "powerPlay": False
                }
            }
        }
    }
}

game_scheduled_data = {
    "result": {
        "event": "Game Scheduled",
        "eventCode": "WSH1",
        "eventTypeId": "GAME_SCHEDULED",
        "description": "Game Scheduled"
    },
    "about": {
        "eventIdx": 0,
        "eventId": 1,
        "period": 1,
        "periodType": "REGULAR",
        "ordinalNum": "1st",
        "periodTime": "00:00",
        "periodTimeRemaining": "20:00",
        "dateTime": "2022-04-10T16:56:39Z",
        "goals": {
            "away": 0,
            "home": 0
        }
    },
    "coordinates": {}
}

game_end_data = {
    "result": {
        "event": "Game End",
        "eventCode": "WSH915",
        "eventTypeId": "GAME_END",
        "description": "Game End"
    },
    "about": {
        "eventIdx": 384,
        "eventId": 915,
        "period": 3,
        "periodType": "REGULAR",
        "ordinalNum": "3rd",
        "periodTime": "20:00",
        "periodTimeRemaining": "00:00",
        "dateTime": "2022-04-10T20:12:25Z",
        "goals": {
            "away": 2,
            "home": 4
        }
    },
    "coordinates": {}
}

game_official_data = {
    "result": {
        "event": "Game Official",
        "eventCode": "WSH916",
        "eventTypeId": "GAME_OFFICIAL",
        "description": "Game Official"
    },
    "about": {
        "eventIdx": 385,
        "eventId": 916,
        "period": 3,
        "periodType": "REGULAR",
        "ordinalNum": "3rd",
        "periodTime": "20:00",
        "periodTimeRemaining": "00:00",
        "dateTime": "2022-04-10T21:27:01Z",
        "goals": {
            "away": 2,
            "home": 4
        }
    },
    "coordinates": {}
}
