import requests
import json
class getCalendar:
    def __init__(self):
        self.REQUESTTARGET = "https://api.cronofy.com/v1/events"

    def getEvents(self):
        querystring = {"tzid":"Etc/UTC"}

        headers = {
            'authorization': "Bearer NTz4oKbCrxN0ZJpv_7511dedIzX7ebXS",
            'cache-control': "no-cache",
            'postman-token': "7b2733ab-9d3c-bc60-a7a5-22210c1046d8"
            }

        self.response = requests.request("GET", self.REQUESTTARGET, headers=headers, params=querystring)

        return self.response.text
    def parseJSON(self):
        parsed_json = json.loads(self.response.text)
        events = []
        print(len(parsed_json["events"]))
        for i in range(len(parsed_json["events"])):
            allevents = parsed_json["events"][i]
            events.append([allevents["start"],allevents["calendar_id"]])
        return events

C = getCalendar()
C.getEvents()
C.parseJSON()
