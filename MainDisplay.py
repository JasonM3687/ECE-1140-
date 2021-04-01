# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TrainControllerDisplayPageUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from TrainDisplay import Ui_DisplayWindow
from EngineerControl import Ui_EngineerWindow
from TestUI import Ui_TestWindow
import trainModel
import time

class Ui_LoginWindow(object):
    #define static class variables
    speed = 0.0
    currentVelocity = 0
    temperature = 68
    nextStation = "NONE"
    headlightStatus = False
    cabinlightStatus = False
    doorStatus = False
    kp = 9000.0
    ki = 100.0
    faultStatus = "NONE"
    modeStatus = "MANUAL"
    engineStatus = False
    serviceBrake = False
    emergencyBrake = False
    intercom = False
    autoMode = False
    commanded = 30
    authority = 0
    speedLimit = 30
    power = 0
    startTime = time.time()
    beaconMessage = "NONE"
    announcement = "I Hate Trains"


    def setupUi1(self, LoginWindow1):
        self.LoginWindow=LoginWindow1
        self.LoginWindow.setObjectName("self.LoginWindow")
        self.LoginWindow.resize(514, 361)
        self.LoginWindow.setStyleSheet("background-color: rgb(240, 240, 180);")
        self.centralwidget = QtWidgets.QWidget(self.LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.usernameLabel = QtWidgets.QLabel(self.centralwidget)
        self.usernameLabel.setGeometry(QtCore.QRect(120, 120, 91, 21))
        self.usernameLabel.setStyleSheet("background-color: rgb(216, 216, 162);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.usernameLabel.setObjectName("usernameLabel")
        self.passwordLabel = QtWidgets.QLabel(self.centralwidget)
        self.passwordLabel.setGeometry(QtCore.QRect(120, 150, 81, 21))
        self.passwordLabel.setStyleSheet("background-color:rgb(216, 216, 162);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.passwordLabel.setObjectName("passwordLabel")
        self.loginLabel = QtWidgets.QLabel(self.centralwidget)
        self.loginLabel.setGeometry(QtCore.QRect(200, 30, 131, 61))
        self.loginLabel.setStyleSheet("font: 26pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(216, 216, 162)")
        self.loginLabel.setObjectName("loginLabel")
        self.loginButton = QtWidgets.QPushButton(self.centralwidget)
        self.loginButton.setGeometry(QtCore.QRect(280, 210, 61, 21))
        self.loginButton.setStyleSheet("background-color:rgb(216, 216, 162)")
        self.loginButton.setObjectName("loginButton")
        self.cancelButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancelButton.setGeometry(QtCore.QRect(190, 210, 61, 21))
        self.cancelButton.setStyleSheet("background-color:rgb(216, 216, 162)")
        self.cancelButton.setObjectName("cancelButton")
        self.usernameInput = QtWidgets.QLineEdit(self.centralwidget)
        self.usernameInput.setGeometry(QtCore.QRect(240, 110, 113, 31))
        self.usernameInput.setStyleSheet("background-color:rgb(216, 216, 162)")
        self.usernameInput.setText("")
        self.usernameInput.setAlignment(QtCore.Qt.AlignCenter)
        self.usernameInput.setObjectName("usernameInput")
        self.passwordInput = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordInput.setGeometry(QtCore.QRect(240, 140, 113, 31))
        self.passwordInput.setStyleSheet("background-color:rgb(216, 216, 162)")
        self.passwordInput.setText("")
        self.passwordInput.setAlignment(QtCore.Qt.AlignCenter)
        self.passwordInput.setObjectName("passwordInput")
        self.LoginWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self.LoginWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 514, 26))
        self.menubar.setObjectName("menubar")
        self.LoginWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self.LoginWindow)
        self.statusbar.setObjectName("statusbar")
        self.LoginWindow.setStatusBar(self.statusbar)

        self.retranslateUi1(self.LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(self.LoginWindow)

        #Login controls
        self.loginButton.clicked.connect(self.loginVerify)
        self.cancelButton.clicked.connect(self.usernameInput.clear)
        self.cancelButton.clicked.connect(self.passwordInput.clear)

    def retranslateUi1(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        self.LoginWindow.setWindowTitle(_translate("self.LoginWindow", "MainWindow"))
        self.usernameLabel.setText(_translate("self.LoginWindow", "Username:"))
        self.passwordLabel.setText(_translate("self.LoginWindow", "Password:"))
        self.loginLabel.setText(_translate("self.LoginWindow", "Log In"))
        self.loginButton.setText(_translate("self.LoginWindow", "Log In"))
        self.cancelButton.setText(_translate("self.LoginWindow", "Cancel"))

    
    #----------Functions for Train Model To recieve outputs------------------------------
    def getPower(self):
        return self.power

    def getHeadlightStatus(self):
        return self.headlightStatus

    def getCabinLightStatus(self):
        return self.cabinlightStatus

    def getDoorStatus(self):
        return self.doorStatus

    def getEBrake(self):
        return self.emergencyBrake

    def getServiceBrake(self):
        return self.serviceBrake

    def getKp(self):
        return self.kp
        
    def getAnnouncement(self):
        return self.announcement

    #-------------------------------------------------------------------------------------
    beans=0
    lastTime = 0.0
    timeChange = 0.0
    errSum = 0.0
    errSum2 = 0.0
    error = 0.0
    error2 = 0.0
    maxPower = 150000
    #Calculate power toi be sent to train controller
    def calcPower(self):
        #time since last calculation
        self.currentTime = time.time()
        self.timeChange = self.currentTime - self.startTime

        #Compute working error variables
        self.error = self.speed - self.currentVelocity
        if self.power < self.maxPower:
            self.errSum = self.errSum2 + (self.timeChange/2)*(self.error + self.error2)
        else:
            self.errSum = self.errSum2

        #Compute PID power output
        self.power = (self.kp * self.error) + (self.ki * self.errSum)

        self.startTime = self.currentTime
        self.error2 = self.error
        self.errSum2 = self.errSum

    def getTrainModelInputs(self):
        self.authority = self.trainMod.getAuthority(1)
        self.currentVelocity = self.trainMod.getVelocity(1)
        self.beaconMessage = self.trainMod.getBeacon(1)
        self.commanded = self.trainMod.getCommanded(1)
        self.displayUI.nextstationOutput.setText(self.beaconMessage)
        self.displayUI.actualSpeed.setText(str(self.currentVelocity/1.609344))


    #Create copy of display screen
    def driverWindow(self):
        self.LoginWindow.hide()
        self.DisplayWindow = QtWidgets.QMainWindow()
        self.displayUI = Ui_DisplayWindow()
        self.displayUI.setupUi(self.DisplayWindow)
        self.DisplayWindow.show()

        #Control links
        self.displayUI.speedInput.valueChanged.connect(self.speedControl)
        self.displayUI.temperatureInput.valueChanged.connect(self.tempControl)
        self.displayUI.headlightOnButton.clicked.connect(self.headlightControl1)
        self.displayUI.headlightOffButton.clicked.connect(self.headlightControl2)
        self.displayUI.cabinlightOnButton.clicked.connect(self.cabinlightControl1)
        self.displayUI.canbinlightOffButton.clicked.connect(self.cabinlightControl2)
        self.displayUI.doorOpenButton.clicked.connect(self.doorControl1)
        self.displayUI.doorCloseButton.clicked.connect(self.doorControl2)
        self.displayUI.engineOnButton.clicked.connect(self.engineControl1)
        self.displayUI.engineOffButton.clicked.connect(self.engineControl2)
        self.displayUI.logoutButton.clicked.connect(self.logoutControl1)
        self.displayUI.servicebrakeButton.pressed.connect(self.serviceBrakeControl)
        self.displayUI.emergencybrakeButton.pressed.connect(self.ebrakeControl)
        self.displayUI.announcementButton.pressed.connect(self.intercomControl)
        self.displayUI.automaticModeButton.pressed.connect(self.automaticControl)

        #Timer to refresh inputs every half second
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.getTrainModelInputs)
        self.timer.start(100)

        



    def engineerWindow(self):
        self.LoginWindow.hide()
        self.EngineerWindow = QtWidgets.QMainWindow()
        self.engineerUI = Ui_EngineerWindow()
        self.engineerUI.setupUi(self.EngineerWindow)
        self.EngineerWindow.show()

        #Control links
        self.engineerUI.logoutButton.clicked.connect(self.logoutControl2)
        self.engineerUI.kiInput.valueChanged.connect(self.kiControl)
        self.engineerUI.kpInput.valueChanged.connect(self.kpControl)

    def testWindow(self):
        self.LoginWindow.hide()
        self.TestWindow = QtWidgets.QMainWindow()
        self.testUI = Ui_TestWindow()
        self.testUI.setupUi(self.TestWindow)
        self.TestWindow.show()

        self.testUI.driverSpeedOutput.setText(str(self.speed))
        self.testUI.KpOutput.setText(str(self.kp))
        self.testUI.KiOutput.setText(str(self.ki))
        self.testUI.headlightOutput.setText(str(self.headlightStatus))
        self.testUI.cabinlightOutput.setText(str(self.cabinlightStatus))
        self.testUI.doorOutput.setText(str(self.doorStatus))

        self.testUI.CTCVelocityInput.setText(str(self.trainMod.getCommanded()))


        #Control Links
        self.testUI.backButton.clicked.connect(self.logoutControl3)
        self.testUI.CTCVelocityInput.returnPressed.connect(self.testRefresh)
        self.testUI.authorityInput.returnPressed.connect(self.testRefresh)
        self.testUI.faultStatusInput.returnPressed.connect(self.testRefresh)
        self.testUI.nextStationInput.returnPressed.connect(self.testRefresh)
        self.testUI.speedLimitInput.returnPressed.connect(self.testRefresh)

    #Set train speed to zero after e brake button is pressed
    def ebrakeControl(self):
        self.speed = 0
        if self.emergencyBrake == False:
            self.emergencyBrake = True
            while(self.currentVelocity>self.speed):
                self.calcPower()
                self.getTrainModelInputs()
        else:
            self.emergencyBrake = False

    def intercomControl(self):
        self.getTrainModelInputs()
        self.announcement = "We have arrived at " + self.beaconMessage + " station."
        print(self.announcement)

    def automaticControl(self):
        if self.autoMode == False:
            self.autoMode=True
            self.modeStatus = "AUTOMATIC"
            self.displayUI.modeOutput.setText(self.modeStatus)
            if self.CTCVelocity <= self.speedLimit:
                self.speed = self.CTCVelocity
                self.displayUI.speedInput.setValue(self.speed)
            else:
                self.speed = self.speedLimit
                self.displayUI.speedInput.setValue(self.speed)
        else:
            self.autoMode = False
            self.modeStatus = "MANUAL"
            self.displayUI.modeOutput.setText(self.modeStatus)

        if self.authority == 0:
            self.ebrakeControl()


    def testRefresh(self):
        self.CTCVelocity = int(self.testUI.CTCVelocityInput.text())
        self.authority = int(self.testUI.authorityInput.text())
        self.faultStatus = self.testUI.faultStatusInput.text()
        self.nextStation = self.testUI.nextStationInput.text()
        self.speedLimit = int(self.testUI.speedLimitInput.text())

    def serviceBrakeControl(self):
        if self.serviceBrake == False:
            self.serviceBrake = True
        else:
            self.serviceBrake = False
        while(self.serviceBrake == True and self.speed > 0):
            self.speed = self.speed - .0001
            self.calcPower()


    def kiControl(self):
        self.ki = self.engineerUI.kiInput.value()
        print(self.ki)

    def kpControl(self):
        self.kp = self.engineerUI.kpInput.value()
        print(self.kp)


    #Verify correct username and password
    def loginVerify(self):
        usernameDriver = "Driver"
        passwordDriver = "1234"
        usernameEngineer = "Engineer"
        passwordEngineer = "1234"
        usernameTest = "Test"
        passwordTest = "1234"
        if self.usernameInput.text() == usernameDriver and self.passwordInput.text() == passwordDriver:
            self.driverWindow()
        if self.usernameInput.text() == usernameEngineer and self.passwordInput.text() == passwordEngineer:
            self.engineerWindow()
        if self.usernameInput.text() == usernameTest and self.passwordInput.text() == passwordTest:
            self.testWindow()

    #Handle speed controls
    def speedControl(self):
        if self.autoMode == False:
            self.speed = self.displayUI.speedInput.value()
            if self.speed >= self.commanded:
                self.speed = self.commanded
                self.displayUI.speedInput.setValue(self.speed)
        self.calcPower()

    def tempControl(self):
        self.temperature = self.displayUI.temperatureInput.value()
        print(self.temperature)

    #Headlight off and on controls
    def headlightControl1(self):
        self.displayUI.headlightOnButton.setStyleSheet("background-color:rgb(0, 255, 0)")
        self.displayUI.headlightOffButton.setStyleSheet("background-color:rgb(216, 216, 162)")
        self.headlightStatus = True

    def headlightControl2(self):
        self.displayUI.headlightOffButton.setStyleSheet("background-color:rgb(0, 255, 0)")
        self.displayUI.headlightOnButton.setStyleSheet("background-color:rgb(216, 216, 162)")
        self.headlightStatus = False

    #Cabin light off and on controls
    def cabinlightControl1(self):
        self.displayUI.cabinlightOnButton.setStyleSheet("background-color:rgb(0, 255, 0)")
        self.displayUI.canbinlightOffButton.setStyleSheet("background-color:rgb(216, 216, 162)")
        self.cabinlightStatus = True

    def cabinlightControl2(self):
        self.displayUI.canbinlightOffButton.setStyleSheet("background-color:rgb(0, 255, 0)")
        self.displayUI.cabinlightOnButton.setStyleSheet("background-color:rgb(216, 216, 162)")
        self.cabinlightStatus = False

    #Door off and on controls
    def doorControl1(self):
        self.displayUI.doorOpenButton.setStyleSheet("background-color:rgb(0, 255, 0)")
        self.displayUI.doorCloseButton.setStyleSheet("background-color:rgb(216, 216, 162)")
        self.doorStatus = True

    def doorControl2(self):
        self.displayUI.doorCloseButton.setStyleSheet("background-color:rgb(0, 255, 0)")
        self.displayUI.doorOpenButton.setStyleSheet("background-color:rgb(216, 216, 162)")
        self.doorStatus = False

    #Engine off and on controls
    def engineControl1(self):
        self.displayUI.engineOnButton.setStyleSheet("background-color:rgb(0, 255, 0)")
        self.displayUI.engineOffButton.setStyleSheet("background-color:rgb(216, 216, 162)")
        self.engineStatus = True
        self.displayUI.nextstationOutput.setText(self.nextStation)
        self.displayUI.faultStatusOutput.setText(self.faultStatus)
        self.displayUI.modeOutput.setText(self.modeStatus)
        self.displayUI.kiInput.setText(str(self.ki))
        self.displayUI.kpInput.setText(str(self.kp))

    def engineControl2(self):
        #if self.speed == 0:
        self.displayUI.engineOffButton.setStyleSheet("background-color:rgb(0, 255, 0)")
        self.displayUI.engineOnButton.setStyleSheet("background-color:rgb(216, 216, 162)")
        self.engineStatus = False
        self.displayUI.nextstationOutput.setText("")
        self.displayUI.faultStatusOutput.setText("")
        self.displayUI.modeOutput.setText("")

    #deal with the logout button being pressed on each screen
    def logoutControl1(self):
        if self.engineStatus == False:
            self.DisplayWindow.hide()
            self.LoginWindow.show()

    def logoutControl2(self):
        if self.engineStatus == False:
            self.EngineerWindow.hide()
            self.LoginWindow.show()

    def logoutControl3(self):
        if self.engineStatus == False:
            self.TestWindow.hide()
            self.LoginWindow.show()

    def importTrain(self,obj):
        self.trainMod=obj
        



'''if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    self.LoginWindow = QtWidgets.QMainWindow()
    TrainWindow = QtWidgets.QMainWindow()
    loginUI = Ui_self.LoginWindow()
    loginUI.setupUi1(self.LoginWindow)
    trainMod = Ui_MainWindow()
    trainMod.setupUi(TrainWindow)
    self.LoginWindow.show()
    TrainWindow.show()
    sys.exit(app.exec_())'''
