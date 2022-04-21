"""
Description:
    Test data for unit tests describing period events.
"""

period_ready_data = {
    "result": {
        "event": "Period Ready",
        "eventCode": "WSH5",
        "eventTypeId": "PERIOD_READY",
        "description": "Period Ready"
    },
    "about": {
        "eventIdx": 1,
        "eventId": 5,
        "period": 1,
        "periodType": "REGULAR",
        "ordinalNum": "1st",
        "periodTime": "00:00",
        "periodTimeRemaining": "20:00",
        "dateTime": "2022-04-10T17:32:15Z",
        "goals": {
            "away": 0,
            "home": 0
        }
    },
    "coordinates": {}
}

period_start_data = {
    "result": {
        "event": "Period Start",
        "eventCode": "WSH504",
        "eventTypeId": "PERIOD_START",
        "description": "Period Start"
    },
    "about": {
        "eventIdx": 124,
        "eventId": 504,
        "period": 2,
        "periodType": "REGULAR",
        "ordinalNum": "2nd",
        "periodTime": "00:00",
        "periodTimeRemaining": "20:00",
        "dateTime": "2022-04-10T18:28:48Z",
        "goals": {
            "away": 0,
            "home": 0
        }
    },
    "coordinates": {}
}

period_end_data = {
    "result": {
        "event": "Period End",
        "eventCode": "WSH261",
        "eventTypeId": "PERIOD_END",
        "description": "End of 1st Period"
    },
    "about": {
        "eventIdx": 121,
        "eventId": 261,
        "period": 1,
        "periodType": "REGULAR",
        "ordinalNum": "1st",
        "periodTime": "20:00",
        "periodTimeRemaining": "00:00",
        "dateTime": "2022-04-10T18:10:01Z",
        "goals": {
            "away": 0,
            "home": 0
        }
    },
    "coordinates": {}
}

period_official_data = {
    "result": {
        "event": "Period Official",
        "eventCode": "WSH264",
        "eventTypeId": "PERIOD_OFFICIAL",
        "description": "Period Official"
    },
    "about": {
        "eventIdx": 122,
        "eventId": 264,
        "period": 1,
        "periodType": "REGULAR",
        "ordinalNum": "1st",
        "periodTime": "20:00",
        "periodTimeRemaining": "00:00",
        "dateTime": "2022-04-10T18:26:05Z",
        "goals": {
            "away": 0,
            "home": 0
        }
    },
    "coordinates": {}
}
