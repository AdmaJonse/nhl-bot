"""
Description:
    Test data for unit tests describing penalty events.
"""

penalty_data = {
    "players": [
        {
            "player": {
                "id": 8475343,
                "fullName": "Nic Dowd",
                "link": "/api/v1/people/8475343"
            },
            "playerType": "PenaltyOn"
        },
        {
            "player": {
                "id": 8477384,
                "fullName": "Josh Brown",
                "link": "/api/v1/people/8477384"
            },
            "playerType": "DrewBy"
        }
    ],
    "result": {
        "event": "Penalty",
        "eventCode": "WSH86",
        "eventTypeId": "PENALTY",
        "description": "Nic Dowd Hi-sticking against Josh Brown",
        "secondaryType": "Hi-sticking",
        "penaltySeverity": "Minor",
        "penaltyMinutes": 2
    },
    "about": {
        "eventIdx": 77,
        "eventId": 86,
        "period": 1,
        "periodType": "REGULAR",
        "ordinalNum": "1st",
        "periodTime": "11:47",
        "periodTimeRemaining": "08:13",
        "dateTime": "2022-04-10T17:57:07Z",
        "goals": {
            "away": 0,
            "home": 0
        }
    },
    "coordinates": {
        "x": -97.0,
        "y": 19.0
    },
    "team": {
        "id": 15,
        "name": "Washington Capitals",
        "link": "/api/v1/teams/15",
        "triCode": "WSH"
    }
}

penalty_data_no_taker = {
    "players": [
        {
            "player": {
                "id": 8477384,
                "fullName": "Josh Brown",
                "link": "/api/v1/people/8477384"
            },
            "playerType": "DrewBy"
        }
    ],
    "result": {
        "event": "Penalty",
        "eventCode": "WSH86",
        "eventTypeId": "PENALTY",
        "description": "Nic Dowd Hi-sticking against Josh Brown",
        "secondaryType": "Hi-sticking",
        "penaltySeverity": "Minor",
        "penaltyMinutes": 2
    },
    "about": {
        "eventIdx": 77,
        "eventId": 86,
        "period": 1,
        "periodType": "REGULAR",
        "ordinalNum": "1st",
        "periodTime": "11:47",
        "periodTimeRemaining": "08:13",
        "dateTime": "2022-04-10T17:57:07Z",
        "goals": {
            "away": 0,
            "home": 0
        }
    },
    "coordinates": {
        "x": -97.0,
        "y": 19.0
    },
    "team": {
        "id": 15,
        "name": "Washington Capitals",
        "link": "/api/v1/teams/15",
        "triCode": "WSH"
    }
}

penalty_shot_data = {
    "players" : [ {
      "player" : {
        "id" : 8475455,
        "fullName" : "Brenden Dillon",
        "link" : "/api/v1/people/8475455"
      },
      "playerType" : "PenaltyOn"
    }, {
      "player" : {
        "id" : 8477456,
        "fullName" : "J.T. Compher",
        "link" : "/api/v1/people/8477456"
      },
      "playerType" : "DrewBy"
    } ],
    "result" : {
      "event" : "Penalty",
      "eventCode" : "WPG287",
      "eventTypeId" : "PENALTY",
      "description" : "Brenden Dillon PS - Hooking on breakaway against J.T. Compher",
      "secondaryType" : "PS - Hooking on breakaway",
      "penaltySeverity" : "Penalty Shot",
      "penaltyMinutes" : 0
    },
    "about" : {
      "eventIdx" : 212,
      "eventId" : 287,
      "period" : 2,
      "periodType" : "REGULAR",
      "ordinalNum" : "2nd",
      "periodTime" : "17:18",
      "periodTimeRemaining" : "02:42",
      "dateTime" : "2022-04-09T01:34:36Z",
      "goals" : {
        "away" : 3,
        "home" : 2
      }
    },
    "coordinates" : {
      "x" : -75.0,
      "y" : 0.0
    },
    "team" : {
      "id" : 52,
      "name" : "Boston Bruins",
      "link" : "/api/v1/teams/52",
      "triCode" : "WPG"
    }
}
