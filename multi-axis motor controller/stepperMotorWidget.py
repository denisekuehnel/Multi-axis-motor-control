from PyQt5 import QtGui, QtCore, QtWidgets

from ui.stepperMotorWidgetLayout import Ui_Form

import TMCM6110
import stepperMotorSettingsWidget

class stepperMotorWidget(QtWidgets.QWidget):
    '''View class for a single stepper motor.'''

    def __init__(self, parent_widget, port_num, config):
        super(stepperMotorWidget, self).__init__()

        # Set up the user interface from QtDesigner.
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        # self.ui.btn_stop.setStyleSheet("background-color: red")
        
        self.parent_widget = parent_widget

        # set up buttons
        self.ui.radio_btn_relative.setChecked(True)

        self.checkBoxConnected()
        self.ui.checkBox_connected.stateChanged.connect(self.checkBoxConnected)

        self.ui.btn_home.clicked.connect(self.referenceSearch)
        self.ui.btn_move.clicked.connect(self.moveToPosition)
        self.ui.btn_settings.clicked.connect(self.btnSettings)
        self.ui.btn_stop.clicked.connect(self.motorStop)
        self.ui.btn_save.clicked.connect(self.saveRequest)
        self.ui.btn_remove.clicked.connect(self.removeRequest)

        self.ui.doubleSpinBox_move_to.setMaximum(2147483648)
        self.ui.doubleSpinBox_move_to.setMinimum(-2147483648)
        self.ui.doubleSpinBox_move_to.setDecimals(4)
        self.ui.doubleSpinBox_move_to.setSuffix(' mm')

        # set up vars
        self.port_num = port_num
        self.config = config
        
        # fill interface
        self.label_motor_text = "Motor " + str(self.port_num)
        self.ui.label_motor.setText(self.label_motor_text)

        # Settings
        self.settings = stepperMotorSettingsWidget.stepperMotorSettingsWidget()
        # stepperMotorSettingsWidget
        self.settings.ui.buttonBox.accepted.connect(self.btnSettingsAccepted)
        self.settings.ui.buttonBox.rejected.connect(self.btnSettingsRejected)

        self.setupSettings(self.config)

    def setupSettings(self, json_data):
        '''Sets up values for the interface of the settings widget to be displayed correctly.'''
        self.settings.ui.doubleSpinBox_conv_fact.setValue(json_data['conversion_factor'])
        self.settings.ui.spinBox_abs_max_current_scale.setValue(json_data['absolute_maximum_current_scale'])
        self.settings.ui.spinBox_microstep_resolution.setValue(json_data['microstep_resolution'])
        self.settings.ui.spinBox_max_acc.setValue(json_data['maximum_acceleration'])
        self.settings.ui.spinBox_max_pos_speed.setValue(json_data['maximum_positioning_speed'])
        self.settings.ui.spinBox_standby_current.setValue(json_data['standby_current'])
        search_modes = {'SearchLeftStopSwitch' : TMCM6110.ReferenceSearchModeValue.SearchLeftStopSwitch, 
                        'SearchRightStopSwitch' : TMCM6110.ReferenceSearchModeValue.SearchRightStopSwitch,
                        'SearchRightStopSwitchBothSides' : TMCM6110.ReferenceSearchModeValue.SearchRightStopSwitchBothSides,
                        'SearchLeftStopSwitchBothSides' : TMCM6110.ReferenceSearchModeValue.SearchLeftStopSwitchBothSides,
                        'SearchHomeSwitchNegativeDirection' : TMCM6110.ReferenceSearchModeValue.SearchHomeSwitchNegativeDirection,
                        'SearchHomeSwitchPositiveDirection' : TMCM6110.ReferenceSearchModeValue.SearchHomeSwitchPositiveDirection,
                        'SearchHomeSwitchPositiveDirection2' : TMCM6110.ReferenceSearchModeValue.SearchHomeSwitchPositiveDirection2,
                        'SearchHomeSwitchNegativeDirection2' : TMCM6110.ReferenceSearchModeValue.SearchHomeSwitchNegativeDirection2}        
        self.settings.ui.comboBox_reference_search_mode.setCurrentIndex(search_modes[json_data['reference_search_mode']]-1) 
        # -1 because of differing indices betweend search modes in comboBox (0-7) and search modes TMCM6110 (1-8)

    def checkBoxConnected(self):
        '''Enables/ disables home and move button after a state change of the connected checkbox.'''
        if self.ui.checkBox_connected.isChecked() == True:
            self.ui.btn_home.setEnabled(True)
            self.ui.btn_move.setEnabled(True)
        elif self.ui.checkBox_connected.isChecked() == False:
            self.ui.btn_home.setEnabled(False)
            self.ui.btn_move.setEnabled(False)
        
    def saveRequest(self):
        print("save request implementation in progress")
    
    def saveFileDialog(self):
        ''' Opens save file dialog. Only proceeds when a file is created.'''
        fd = QtWidgets.QFileDialog()
        fd.setNameFilter("*.json")
        file_name = fd.getSaveFileName(self, 'Save file', 'c:\\',"JSON files (*.json)")
        self.controller.model.saveJsonCheck(file_name)
    
    def removeRequest(self):
        print("remove request implementation in progress")
        self.parent_widget.requestStepperMotorWidgetRemoval(self.port_num)

    def removeSelf(self, motor_port):
        if motor_port == self.port_num:
            self.parent_widget.removeStepperMotorWidgetFromMainArea(self) 
            self.deleteLater()
        else:
            pass                             

### StepperMotor Commands        

    def motorStop(self):
        self.parent_widget.controller.motorStop(self.port_num)

    def moveToPosition(self):
        type = ''
        if self.ui.radio_btn_relative.isChecked:
            type = 'relative'
        else: 
            type = 'absolute'
        self.parent_widget.controller.moveToPosition(self.port_num, self.ui.doubleSpinBox_move_to.value(), type)


    def referenceSearch(self):
        self.parent_widget.controller.referenceSearch(self.port_num)

### Settings 

    def btnSettings(self):
        '''Displays the settings window.'''
        self.settings.show()

    def btnSettingsRejected(self):
        '''Closes the settings window disregarding whether values have been changed. The current values will not be changed.'''
        self.settings.close()

    def btnSettingsAccepted(self):
        '''Currently sets all values to the ones that are displayed in the settings when accepted, disregarding whether certain values have actually been changed.'''
        self.parent_widget.controller.setStandbyCurrent(self.port_num, self.settings.ui.spinBox_standby_current.value())
        self.parent_widget.controller.setAbsoluteMaximumCurrentScale(self.port_num, self.settings.ui.spinBox_abs_max_current_scale.value())
        self.parent_widget.controller.setMaximumPositioningSpeed(self.port_num, self.settings.ui.spinBox_max_pos_speed.value())
        self.parent_widget.controller.setMaximumAcceleration(self.port_num, self.settings.ui.spinBox_max_acc.value())
        self.parent_widget.controller.setMicrostepResolution(self.port_num, self.settings.ui.spinBox_microstep_resolution.value())
        self.parent_widget.controller.setReferenceSearchMode(self.port_num, self.settings.ui.comboBox_reference_search_mode.currentText())
        self.parent_widget.controller.setConversionFactor(self.port_num, self.settings.ui.doubleSpinBox_conv_fact.value())
        self.settings.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    mw = stepperMotorWidget(2)
    mw.show()
    app.exec_()