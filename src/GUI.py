# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, io):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1908, 1080)
        MainWindow.setStyleSheet("QLabel{background-color:navy}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 879, 1921, 151))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.blueButton = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.blueButton.setStyleSheet("#blueButton{background-color:blue}")
        self.blueButton.setObjectName("blueButton")
        self.horizontalLayout.addWidget(self.blueButton)
        self.redButton = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.redButton.setStyleSheet("#redButton{background-color:red}")
        self.redButton.setObjectName("redButton")
        self.horizontalLayout.addWidget(self.redButton)
        self.yellowButton = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.yellowButton.setStyleSheet("#yellowButton{background-color:yellow}")
        self.yellowButton.setObjectName("yellowButton")
        self.horizontalLayout.addWidget(self.yellowButton)
        self.greenButton = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.greenButton.setAutoFillBackground(False)
        self.greenButton.setStyleSheet("#greenButton{background-color:green}")
        self.greenButton.setObjectName("greenButton")
        self.horizontalLayout.addWidget(self.greenButton)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(1090, 100, 781, 671))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.messageBox1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.messageBox1.setObjectName("messageBox1")
        self.verticalLayout.addWidget(self.messageBox1)
        self.messageBox2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.messageBox2.setStyleSheet("QLabel {color: black}")
        self.messageBox2.setObjectName("messageBox2")
        self.verticalLayout.addWidget(self.messageBox2)
        self.messageBox3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.messageBox3.setObjectName("messageBox3")
        self.verticalLayout.addWidget(self.messageBox3)
        self.messageBox4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.messageBox4.setObjectName("messageBox4")
        self.verticalLayout.addWidget(self.messageBox4)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 180, 1021, 511))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/images/worldMap.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1908, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        io.comm.gpioButtonPressed.connect(self.clickHandler)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.blueButton.setText(_translate("MainWindow", "TextLabel"))
        self.redButton.setText(_translate("MainWindow", "TextLabel"))
        self.yellowButton.setText(_translate("MainWindow", "TextLabel"))
        self.greenButton.setText(_translate("MainWindow", "TextLabel"))
        self.messageBox1.setText(_translate("MainWindow", "TextLabel"))
        self.messageBox2.setText(_translate("MainWindow", "TextLabel"))
        self.messageBox3.setText(_translate("MainWindow", "TextLabel"))
        self.messageBox4.setText(_translate("MainWindow", "TextLabel"))

    def clickHandler(self, channel):
        print(channel)

import worldMap_rc

if __name__ == "__main__":
    import sys
    import ioInterface as i

    ioController = i.ioControl()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow, ioController)
    MainWindow.show()
    sys.exit(app.exec_())
