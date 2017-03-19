#!/usr/bin/env python

import RPi.GPIO as gpio
from PyQt5.QtCore import pyqtSignal, QObject


#Pin Val, Button Colour, Button Ref
PINS = [[3, "BLUE", 1], [5, "RED", 2], [7, "YELLOW", 3], [8, "GREEN", 4], [10, "WHITE", 5], [11, "BLACK", 6], [12, "PURPLE", 7]]

class ioComm(QObject):
    gpioButtonPressed = pyqtSignal(int)

class ioControl():
    def __init__(self):
        self.comm = ioComm()

    def ioConfigure(self):
        gpio.setmode(gpio.BOARD)
        for i in PINS:
            gpio.setup(i[0], gpio.IN, pull_up_down = gpio.PUD_DOWN)
            gpio.add_event_detect(i[0], gpio.RISING, callback=self.ioButtonCallback,bouncetime=200)
           
#self.comm.gpioButtonPressed.connect(self.test)

    def ioGetStates(self):
        for i in PINS:
            if gpio.input(i[0]):
                return i[2]
        return 0

    def ioButtonCallback(self, channel):
        #print("CALLBACK")
        self.comm.gpioButtonPressed.emit(channel)

    def test(self):
        print("TEST")

