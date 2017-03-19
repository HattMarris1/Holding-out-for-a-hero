#!/usr/bin/env python

import RPi.GPIO as gpio
from PyQt5.QtCore import pyqtSignal, QObject


#Pin Val, Button Colour, Button Ref
PINS = [[3, "BLUE", 1], [5, "RED", 2], [7, "YELLOW", 3], [8, "GREEN", 4], [10, "WHITE", 5], [11, "BLACK", 6], [12, "PURPLE", 7]]

class ioComm(QObject):
    gpioButtonPressed = pyqtSignal()

class ioControl():
    def __init__(self):
        self.comm = ioComm(int)

    def ioConfigure():
        gpio.setmode(gpio.board)
        for i in PINS:
            gpio.setup(i[0], gpio.INPUT, pull_up_down = gpio.PUD_DOWN)
            gpio.add_event_detect(i[0], gpio.RISING, callback=ioControl.ioButtonCallback)


    def ioGetStates():
        for i in PINS:
            if gpio.input(i[0]):
                return i[2]
        return 0

    def ioButtonCallback(self, channel):
        self.comm.gpioButtonPressed.emit(channel)