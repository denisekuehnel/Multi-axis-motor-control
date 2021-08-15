from PyQt5 import QtGui, QtCore, QtWidgets

from ui.mainWindowLayout import Ui_MainWindow
import mainAreaWidget
import stepperMotorWidgetModelController

class mainWindow(QtWidgets.QMainWindow):
    def __init__(self, communication):
        super(mainWindow, self).__init__()
        
        self.controller = stepperMotorWidgetModelController.stepperMotorWidgetModelController(communication)

        # Set up the user interface from QtDesigner.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Multi-axis motor control")
        
        self.main_area_widget = mainAreaWidget.mainAreaWidget(self.controller)
        self.setCentralWidget(self.main_area_widget) 

        

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    mw = mainWindow()
    mw.show()
    app.exec_()