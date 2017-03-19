import requests
import xml.etree.ElementTree as etree
class SMS_Reciever:
    def __init__(self):
        self.REQUESTTARGET = "https://api.esendex.com/v1.0/inbox/messages"
        self.requestMethod = "GET"


    def getMessages(self):
        payload = ""
        headers = {
            'authorization': "Basic bS5jLmhhcnJpc0Bob3RtYWlsLmNvLnVrOm1jaGFja2ZhY2U=",
            'content-type': "application/xml",
            'cache-control': "no-cache",
            'postman-token': "47f80f72-7c47-8bb1-9537-5dd4fb1e2dfa"
            }

        self.response = requests.request(self.requestMethod, self.REQUESTTARGET, data=payload, headers=headers)

    def getMostRecentMessage(self):
        tree = etree.fromstring(self.response.text)

        number = tree[0][8][0].text
        message = tree[0][9].text
        print(message, number)
        return message,number

s = SMS_Reciever()
s.getMessages()
s.getMostRecentMessage()
