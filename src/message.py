import xml.etree.ElementTree as etree

class Message:
    def __init__(self, senderNum, timeRec, message):
        self.senderNumber = senderNum
        self.timeRecieved - timeRec
        self.messageSummary - message

    def parseXML(self, message):
        self.xmlTree = etree.fromString(message)
        self.root = self.xmlTree.getRoot()

