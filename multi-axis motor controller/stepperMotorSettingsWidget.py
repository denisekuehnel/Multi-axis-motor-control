from ui.stepperMotorSettingsWidget import Ui_Form
from PyQt5 import QtWidgets


class stepperMotorSettingsWidget(QtWidgets.QWidget):
    def __init__(self):
        super(stepperMotorSettingsWidget, self).__init__()

        # Set up the user interface from QtDesigner.
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.doubleSpinBox_conv_fact.setMaximum(2147483648)
        self.ui.doubleSpinBox_conv_fact.setMinimum(-2147483648)
        self.ui.doubleSpinBox_conv_fact.setDecimals(10)


        self.ui.spinBox_abs_max_current_scale.setMaximum(180)
        self.ui.spinBox_abs_max_current_scale.setMinimum(0)

        self.ui.spinBox_max_acc.setMaximum(2047)
        self.ui.spinBox_max_acc.setMinimum(0)

        self.ui.spinBox_max_pos_speed.setMaximum(2047)
        self.ui.spinBox_max_pos_speed.setMinimum(0)

        self.ui.spinBox_standby_current.setMaximum(180)
        self.ui.spinBox_standby_current.setMinimum(0)

        self.ui.spinBox_microstep_resolution.setMaximum(8)
        self.ui.spinBox_microstep_resolution.setMinimum(0)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    mw = stepperMotorSettingsWidget()
    mw.show()
    app.exec_()