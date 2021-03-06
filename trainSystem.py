import trainModel
import SWTrackControllerNew
import trackModel
import t1_updated
from tkinter import Tk
import MainDisplay
from PyQt5 import QtWidgets

if __name__=='__main__':
    import sys
    
    trackApp=QtWidgets.QApplication(sys.argv)
    trackWindow=QtWidgets.QMainWindow()
    track=trackModel.trackModel()
    track.setupUi(trackWindow)
    track.importTrack()
    
    trainCApp=QtWidgets.QApplication(sys.argv)
    trainCWindow=QtWidgets.QMainWindow()
    trainC=MainDisplay.Ui_LoginWindow()
    
    trainApp=QtWidgets.QApplication(sys.argv)
    trainWindow=QtWidgets.QMainWindow()
    train=trainModel.Ui_MainWindow()
    track.setTrainModel(train)
    train.trackModelInstance(track)
    train.trainControllerInstance(trainC) 
    train.setupUi(trainWindow)
    
    trainC.setupUi1(trainCWindow)
    trainC.importTrain(train)
    
    
    ctc=t1_updated.CTCOFFICE()
    
    trackCApp=QtWidgets.QApplication(sys.argv)
    trackCWindow=QtWidgets.QMainWindow()
    trackC=SWTrackControllerNew.Ui_MainWindow()
    trackC.trackModelInput(track)
    trackC.CTCInput(ctc)
    trackC.setupUi(trackCWindow)
    ctc.getTC(trackC)
    
    trackWindow.show()
    trainWindow.show()
    trainCWindow.show()
    trackCWindow.show()
    ctc.SHOW()
    sys.exit(trackApp.exec_())
