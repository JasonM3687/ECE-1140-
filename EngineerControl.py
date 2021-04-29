# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EngineerControl.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EngineerWindow(object):
    def setupUi(self, EngineerWindow):
        EngineerWindow.setObjectName("EngineerWindow")
        EngineerWindow.resize(385, 251)
        EngineerWindow.setStyleSheet("background-color: rgb(240, 240, 180);")
        self.centralwidget = QtWidgets.QWidget(EngineerWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.controllerLabel = QtWidgets.QLabel(self.centralwidget)
        self.controllerLabel.setGeometry(QtCore.QRect(30, 10, 201, 61))
        self.controllerLabel.setStyleSheet("font: 26pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(216, 216, 162)")
        self.controllerLabel.setObjectName("controllerLabel")
        self.trainNumLabel = QtWidgets.QLabel(self.centralwidget)
        self.trainNumLabel.setGeometry(QtCore.QRect(60, 100, 111, 31))
        self.trainNumLabel.setStyleSheet("background-color: rgb(216, 216, 162);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.trainNumLabel.setObjectName("trainNumLabel")
        self.trainNumOutput = QtWidgets.QLineEdit(self.centralwidget)
        self.trainNumOutput.setGeometry(QtCore.QRect(240, 100, 41, 31))
        self.trainNumOutput.setStyleSheet("background-color:rgb(216, 216, 162)")
        self.trainNumOutput.setText("")
        self.trainNumOutput.setAlignment(QtCore.Qt.AlignCenter)
        self.trainNumOutput.setObjectName("trainNumOutput")
        self.kpLabel = QtWidgets.QLabel(self.centralwidget)
        self.kpLabel.setGeometry(QtCore.QRect(40, 150, 41, 31))
        self.kpLabel.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"background-color:rgb(216, 216, 162)")
        self.kpLabel.setObjectName("kpLabel")
        self.kpInput = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.kpInput.setGeometry(QtCore.QRect(90, 150, 81, 31))
        self.kpInput.setTabletTracking(False)
        self.kpInput.setStyleSheet("background-color: rgb(240, 240, 180);")
        self.kpInput.setMaximum(10000)
        self.kpInput.setAlignment(QtCore.Qt.AlignCenter)
        self.kpInput.setObjectName("kpInput")
        self.kiLabel = QtWidgets.QLabel(self.centralwidget)
        self.kiLabel.setGeometry(QtCore.QRect(220, 150, 31, 31))
        self.kiLabel.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"background-color:rgb(216, 216, 162)")
        self.kiLabel.setObjectName("kiLabel")
        self.kiInput = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.kiInput.setGeometry(QtCore.QRect(260, 150, 81, 31))
        self.kiInput.setTabletTracking(False)
        self.kiInput.setMaximum(10000)
        self.kiInput.setStyleSheet("background-color: rgb(240, 240, 180);")
        self.kiInput.setAlignment(QtCore.Qt.AlignCenter)
        self.kiInput.setObjectName("kiInput")
        self.logoutButton = QtWidgets.QPushButton(self.centralwidget)
        self.logoutButton.setGeometry(QtCore.QRect(270, 30, 93, 28))
        self.logoutButton.setStyleSheet("background-color:rgb(216, 216, 162)")
        self.logoutButton.setObjectName("logoutButton")
        EngineerWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(EngineerWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 385, 26))
        self.menubar.setObjectName("menubar")
        EngineerWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(EngineerWindow)
        self.statusbar.setObjectName("statusbar")
        EngineerWindow.setStatusBar(self.statusbar)

        self.retranslateUi(EngineerWindow)
        QtCore.QMetaObject.connectSlotsByName(EngineerWindow)

    def retranslateUi(self, EngineerWindow):
        _translate = QtCore.QCoreApplication.translate
        EngineerWindow.setWindowTitle(_translate("EngineerWindow", "MainWindow"))
        self.controllerLabel.setText(_translate("EngineerWindow", "Controller:"))
        self.trainNumLabel.setText(_translate("EngineerWindow", "Train Number:"))
        self.kpLabel.setText(_translate("EngineerWindow", "Kp:"))
        self.kiLabel.setText(_translate("EngineerWindow", "Ki:"))
        self.logoutButton.setText(_translate("EngineerWindow", "Logout"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EngineerWindow = QtWidgets.QMainWindow()
    ui = Ui_EngineerWindow()
    ui.setupUi(EngineerWindow)
    EngineerWindow.show()
    sys.exit(app.exec_())