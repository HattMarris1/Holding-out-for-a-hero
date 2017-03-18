import requests

class SMS_Sender:
    def __init__(self, acc):
        self.MESSAGE_TARGET = "https://api.esendex.com/v1.0/messagedispatcher"
        self.requestMethod = "POST"
        self.account = acc

    def send_message(self, messageBody, tar):
        #expects message string and target phone number

        payload = create_XML_Message(messageBody,tar)
        headers = {
            'authorization': "Basic bS5jLmhhcnJpc0Bob3RtYWlsLmNvLnVrOm1jaGFja2ZhY2U=",
            'content-type': "application/xml",
            'cache-control': "no-cache",
            'postman-token': "afb5ff75-c9d6-8d6f-7901-6bd646c04457"
            }

        response = requests.request(self.requestMethod, self.MESSAGE_TARGET, data=payload, headers=headers)

        print(response.text)
        return None

    def create_XML_Message(self, messageBody, tar):
        #takes a message string and target phone number and builds the full request ready to post
        theMessage = "<?xml version='1.0' encoding='UTF-8'?>  \r\n<messages>  \r\n    <accountreference>EX0226395</accountreference>\r\n    <message>\r\n        <to>"\
        + tar + "</to>\r\n        <body>" + messageBody + "</body>\r\n    </message>  \r\n</messages>"
        return theMessage

    def checkResponse(self, response, expected):
        #takes a HTTP response and ensures it matches the desired response code

        return None

Sender = SMS_Sender("bS5jLmhhcnJpc0Bob3RtYWlsLmNvLnVrOm1jaGFja2ZhY2U")
print(Sender.create_XML_Message("Emergency","07531661956"))
