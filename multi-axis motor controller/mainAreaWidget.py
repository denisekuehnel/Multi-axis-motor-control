from PyQt5 import QtGui, QtCore, QtWidgets
import os

from ui.mainAreaWidgetLayout import Ui_Form
import stepperMotorWidget

import jsonHandling


class mainAreaWidget(QtWidgets.QWidget):
    def __init__(self, controller):
        super(mainAreaWidget, self).__init__()

        # Set up the user interface from QtDesigner.
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.controller = controller

        self.jh = jsonHandling.jsonHandling()

        self.ui.btn_select_config.clicked.connect(self.openFileDialog)
        self.ui.btn_add_motor.clicked.connect(self.addMotor)
        self.ui.btn_add_motor.setToolTip('Select a config before adding motor')
        self.ui.radio_btn_default.setChecked(True)
        self.ui.spin_box_port_number.setValue(0)

        self.motor_list = [] # list of objects
        self.stepper_motor_default_values = {"conversion_factor" : 1, 
                                             "maximum_positioning_speed" : 1500, 
                                             "maximum_acceleration" : 1500, 
                                             "absolute_maximum_current_scale" : 100, 
                                             "standby_current" : 8, 
                                             "microstep_resolution" : 8, 
                                             "reference_search_mode" : "SearchHomeSwitchPositiveDirection2"}

        self.controller.sigRemoveStepperMotor.connect(self.checkStepperMotorWidgetRemoval)

    def addMotor(self):
        '''Adds a stepper motor widget to the layout with the parameters according to those of the selected config file or default values.'''
        if self.ui.radio_btn_config.isChecked():
            config = self.ui.label_config_name.text()
            json_data = self.jh.openJson(config)
        else:
            json_data = self.stepper_motor_default_values
        motor_port = self.ui.spin_box_port_number.value()
        smw = stepperMotorWidget.stepperMotorWidget(self,
                                                    motor_port, 
                                                    json_data)
        self.motor_list.append(smw)
        self.ui.frame_stepper_motors.layout().addWidget(smw)
        self.controller.addMotor(motor_port, json_data)

    def requestStepperMotorWidgetRemoval(self, motor_port):
        '''Forwards request to delete stepper motor data from the model.'''
        self.controller.removeStepperMotorData(motor_port)

    def checkStepperMotorWidgetRemoval(self, motor_port):
        '''Initiates actual removal of the stepper motor widget.'''
        for stepper_motor_widget in self.motor_list:
            stepper_motor_widget.removeSelf(motor_port)

    def removeStepperMotorWidgetFromMainArea(self, widget):
        self.ui.frame_stepper_motors.layout().removeWidget(widget)
        self.motor_list.remove(widget)

    def openFileDialog(self):
        ''' Opens file dialog. Only proceeds when a file is selected. '''
        fd = QtWidgets.QFileDialog()
        fd.setNameFilter("*.json")
        file_name = fd.getOpenFileName(self, 'Open file', 
         'c:\\',"JSON files (*.json)")
        if os.path.isfile(file_name[0]):
            self.updateConfigName(file_name[0])
            print("Open File: ", file_name[0])
        else:
            pass

    def updateConfigName(self, file_name):
        '''Changes the name of the label on the GUI to the path of the selected json file.'''
        self.ui.label_config_name.setText(file_name) 

 
if __name__ == '__main__':
    import stepperMotorWidgetModelController
    import serialPortCommunication
    spc = serialPortCommunication.serialPortCommunication()
    app = QtWidgets.QApplication([])
    controller = stepperMotorWidgetModelController.stepperMotorWidgetModelController(spc)
    mw = mainAreaWidget(controller)
    mw.show()
    app.exec_()