from PyQt5 import QtCore, QtWidgets

import stepperMotorWidgetModel

class stepperMotorWidgetModelController(QtCore.QObject):
    
    ## Stepper Motor Signals
    sigRemoveStepperMotor = QtCore.pyqtSignal(int)

    def __init__(self, communication):
        QtCore.QObject.__init__(self)

        self.communication = communication
        self.model = stepperMotorWidgetModel.stepperMotorWidgetModel(self.communication)

### StepperMotorWidget

    def addMotor(self, motor_port, json_data):
        self.model.addMotor(motor_port, json_data)
    
### remove StepperMotor
    def removeStepperMotorData(self, motor_port):
        self.model.removeStepperMotor(motor_port)
        self.sigRemoveStepperMotor.emit(motor_port)
    
### StepperMotor Movement

    def moveToPosition(self, motor_port, value, type):
        # self.sigMoveToPosition.emit(motor_port, value, type)
        self.model.moveToPosition(motor_port, value, type)

    def referenceSearch(self, motor_port):
        self.model.referenceSearch(motor_port)

### stepperMotor setter

    def motorStop(self, motor_port):
        self.model.motorStop(motor_port)

    def setConversionFactor(self, motor_port, conversion_factor):
        self.model.setConversionFactor(motor_port, conversion_factor)

    def setAbsoluteMaximumCurrentScale(self, motor_port, value):
        self.model.setAbsoluteMaximumCurrentScale(motor_port, value)

    def setMaximumPositioningSpeed(self, motor_port, value):
        self.model.setMaximumPositioningSpeed(motor_port, value)

    def setMaximumAcceleration(self, motor_port, value):
        self.model.setMaximumAcceleration(motor_port, value)

    def setMicrostepResolution(self, motor_port, value):
        self.model.setMicrostepResolution(motor_port, value)

    def setStandbyCurrent(self, motor_port, value):
        self.model.setStandbyCurrent(motor_port, value)

    def setReferenceSearchMode(self, motor_port, value):
        self.model.setReferenceSearchMode(motor_port, value)

    def setSmartEnergyActualCurrent(self, motor_port, value):
        self.model.setSmartEnergyActualCurrent(motor_port, value)

    def setReferencingSearchSpeed(self, motor_port, value):
        self.model.setReferencingSearchSpeed(motor_port, value)

    def setSoftStopFlag(self, motor_port, value):
        self.model.setSoftStopFlag(motor_port, value)

### stepperMotor getter

    def getAbsoluteMaximumCurrentScale(self, motor_port):
        self.model.getAbsoluteMaximumCurrentScale(motor_port)

    def getStandbyCurrent(self, motor_port):
        self.model.getStandbyCurrent(motor_port)

    def getMaximumPositioningSpeed(self, motor_port):
        self.model.getMaximumPositioningSpeed(motor_port)

    def getMaximumAcceleration(self, motor_port):
        self.model.getMaximumAcceleration(motor_port)

    def getReferenceSearchMode(self, motor_port):
        self.model.getReferenceSearchMode(motor_port)

    def getMicrostepResolution(self, motor_port):
        self.model.getMicrostepResolution(motor_port)

    def getSmartEnergyActualCurrent(self, motor_port):
        self.model.getSmartEnergyActualCurrent(motor_port)






        