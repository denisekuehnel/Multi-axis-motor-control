from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        
        self.widget = QtWidgets.QWidget()
        self.layout = QtWidgets.QGridLayout(self.widget)
        self.sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        self.sizePolicy.setHorizontalStretch(0)
        self.sizePolicy.setVerticalStretch(0)
        # label
        self.label_motors = QtWidgets.QLabel()
        self.label_motors.setObjectName("label_motors")
        self.layout.addWidget(self.label_motors, 0,0,1,1)
        # btn
        self.btn = QtWidgets.QPushButton()
        self.btn.setObjectName("btn")
        self.layout.addWidget(self.btn, 0,1,1,1)
        # current_value

        # self.layout = QtWidgets.QVBoxLayout()
        # self.widget = QtWidgets.QWidget()
        # self.widget.setLayout(self.layout)
    

        # # self.frame_motors = QtWidgets.QFrame(self.widget)
        # # self.frame_motors.setGeometry(QtCore.QRect(20, 100, 238, 32))
        # # self.frame_motors.setMaximumSize(QtCore.QSize(16777215, 32))
        # # self.frame_motors.setFrameShadow(QtWidgets.QFrame.Raised)
        # self.btn = QtWidgets.QPushButton(self.widget)


        # # self.layout_stepper_motors = QtWidgets.QFrame(self.widget)
        # # self.verticalLayout = QtWidgets.QVBoxLayout(self.layout_stepper_motors)
        # # self.frame_stepper_motors = QtWidgets.QFrame(self.layout_stepper_motors)
        # # self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_stepper_motors)
        # self.label_stepper_motor = QtWidgets.QLabel(self.widget)
        # self.label_stepper_motor.setObjectName("label_stepper_motor")
        # self.layout.addWidget(self.label_stepper_motor)


        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.centralWidget = self.widget

        MainWindow.setCentralWidget(self.centralWidget)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_motors.setText(_translate("MainWindow", "Stepper Motors"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
