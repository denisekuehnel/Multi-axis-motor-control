
from PyQt5 import QtWidgets
import serialPortCommunication

import mainWindow

class hub(): # eine art controller
    def __init__(self):
        self.motor_list = []
        self.spc = serialPortCommunication.serialPortCommunication()
        app = QtWidgets.QApplication([])
        self.mw = mainWindow.mainWindow(self.spc)
        self.mw.show()
        app.exec_()

