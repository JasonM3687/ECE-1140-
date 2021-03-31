from PyQt5 import QtWidgets

import MainDisplay
import SWTrackControllerNew
import t1_1
import trackModel
import trainModel

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
    train.trackModelInstance(track)
    train.trainControllerInstance(trainC) 
    train.setupUi(trainWindow)
    
    trainC.setupUi1(trainCWindow)
    trainC.importTrain(train)
    
    ctc=t1_1.CTCOFFICE()
    
    trackCApp=QtWidgets.QApplication(sys.argv)
    trackCWindow=QtWidgets.QMainWindow()
    trackC=SWTrackControllerNew.Ui_MainWindow()
    trackC.trackModelInput(track)
    trackC.CTCInput(ctc)
    trackC.setupUi(trackCWindow)
    
    
    trackWindow.show()
    trainWindow.show()
    trainCWindow.show()
    trackCWindow.show()
    ctc.SHOW()
    sys.exit(trackApp.exec_())