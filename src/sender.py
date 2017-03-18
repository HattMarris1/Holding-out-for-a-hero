#import http

class SMS_Sender:
    def __init__(self, acc, pwd):
        self.MESSAGE_TARGET = "https://api.esendex.com/v1.0/messagedispatcher"
        self.requestMethod = "POST"
        self.account = acc
        self.password = pwd

    def send_message(self, messageBody, tar):
        #expects message string and target phone number
        return None

    def create_XML_Message(self, messageBody, tar):
        #takes a message string and target phone number and builds the full request ready to post
        return None

    def checkResponse(self, response, expected):
        #takes a HTTP response and ensures it matches the desired response code
        return None

