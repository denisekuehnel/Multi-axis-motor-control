import json
import time

import TMCM6110

class stepperMotor():
    '''Class for a single stepper motor that sends commands to the controller.'''

    def __init__(self, parent, motor_port, conversion_factor, maximum_positioning_speed, maximum_acceleration, absolute_maximum_current_scale, standby_current, microstep_resolution, reference_search_mode): # parent -> host
        self.parent = parent

        self.motor_port = motor_port
        self.conversion_factor = conversion_factor
        self.maximum_positioning_speed = maximum_positioning_speed
        self.maximum_acceleration = maximum_acceleration
        self.absolute_maximum_current_scale = absolute_maximum_current_scale
        self.standby_current = standby_current
        self.microstep_resolution = microstep_resolution
        self.reference_search_mode = reference_search_mode

        # set initial parameters
        self.setInitialParameters()

### init
    def setInitialParameters(self):
        self.setMaximumPositioningSpeed(self.maximum_positioning_speed)
        self.setAbsoluteMaximumCurrentScale(self.absolute_maximum_current_scale)
        self.setMaximumAcceleration(self.maximum_acceleration)
        self.setReferenceSearchMode(self.reference_search_mode)
        self.setAbsoluteMaximumCurrentScale(self.absolute_maximum_current_scale)
        self.setStandbyCurrent(self.standby_current)

### Conversion

    def setConversionFactor(self, value):
        self.conversion_factor = value

    def mmToSteps(self, value): # to motor
        '''Calculates how many steps the input mm equals using the conversion factor.'''
        return int(value / self.conversion_factor) 
        
### Movement Commands

    def moveToPosition(self, value, command_type):
        ''''''
        mvp_type = {'relative' : TMCM6110.MoveToPositionType.relative, 'absolute' : TMCM6110.MoveToPositionType.absolute}
        print("command_type", mvp_type[command_type])
        x = self.parent.sendCommand(TMCM6110.MoveToPosition, mvp_type[command_type], self.motor_port, self.mmToSteps(value))
        print(x)

    def motorStop(self):
        self.parent.sendCommand(TMCM6110.MotorStop, None, self.motor_port, None)

    def referenceSearch(self):
        print('Reference Search mode:')
        print(self.getReferenceSearchMode())
        self.parent.sendCommand(TMCM6110.ReferenceSearch, TMCM6110.ReferenceSearchType.START, self.motor_port, None)

### neccessary Axis Parameter (set when initializing) # says so in documentation

    def setAbsoluteMaximumCurrentScale(self, value):
        print("set absolute maximum current scale")
        self.parent.sendCommand(TMCM6110.StoreAxisParameter, TMCM6110.AxisParameterType.AbsoluteMaximumCurrentScale, self.motor_port, value)
        return value

    def setMaximumPositioningSpeed(self, value):
        '''Value between 0..2047'''
        print("set maximum positioning speed")
        self.parent.sendCommand(TMCM6110.SetAxisParameter, TMCM6110.AxisParameterType.MaximumPositioningSpeed, self.motor_port, value)
        return value 

    def setMaximumAcceleration(self, value):
        '''Value between 0… 2047'''
        print("set maximum acceleration")
        self.parent.sendCommand(TMCM6110.SetAxisParameter, TMCM6110.AxisParameterType.MaximumAcceleration, self.motor_port, value)
        return value

    def setMicrostepResolution(self, value):
        '''0 full step \n
            1 half step \n
            2 4 microsteps \n
            3 8 microsteps \n
            4 16 microsteps \n
            5 32 microsteps \n
            6 64 microsteps \n
            7 128 microsteps \n
            8 256 microsteps'''
        self.parent.sendCommand(TMCM6110.SetAxisParameter, TMCM6110.AxisParameterType.MicrostepResolution, self.motor_port, value)

    def setStandbyCurrent(self, value):
        self.parent.sendCommand(TMCM6110.SetAxisParameter, TMCM6110.AxisParameterType.StandbyCurrent, self.motor_port, value)
        return value

### set Axis Parameter

    def setReferenceSearchMode(self, value):
        print('set reference search mode')
        search_modes = {'SearchLeftStopSwitch' : TMCM6110.ReferenceSearchModeValue.SearchLeftStopSwitch, 
                        'SearchRightStopSwitch' : TMCM6110.ReferenceSearchModeValue.SearchRightStopSwitch,
                        'SearchRightStopSwitchBothSides' : TMCM6110.ReferenceSearchModeValue.SearchRightStopSwitchBothSides,
                        'SearchLeftStopSwitchBothSides' : TMCM6110.ReferenceSearchModeValue.SearchLeftStopSwitchBothSides,
                        'SearchHomeSwitchNegativeDirection' : TMCM6110.ReferenceSearchModeValue.SearchHomeSwitchNegativeDirection,
                        'SearchHomeSwitchPositiveDirection' : TMCM6110.ReferenceSearchModeValue.SearchHomeSwitchPositiveDirection,
                        'SearchHomeSwitchPositiveDirection2' : TMCM6110.ReferenceSearchModeValue.SearchHomeSwitchPositiveDirection2,
                        'SearchHomeSwitchNegativeDirection2' : TMCM6110.ReferenceSearchModeValue.SearchHomeSwitchNegativeDirection2}
        self.parent.sendCommand(TMCM6110.SetAxisParameter, TMCM6110.AxisParameterType.ReferenceSearchMode, self.motor_port, search_modes[value])
        return value

    def setSmartEnergyActualCurrent(self, value):
        self.parent.sendCommand(TMCM6110.SetAxisParameter, TMCM6110.AxisParameterType.SmartEnergyActualCurrent, self.motor_port, value)
        return value

    def setReferencingSearchSpeed(self, value):
        self.parent.sendCommand(TMCM6110.SetAxisParameter, TMCM6110.AxisParameterType.ReferencingSearchSpeed, self.motor_port, value)

    def setSoftStopFlag(self):
        '''Value 0/1'''
        self.parent.sendCommand(TMCM6110.SetAxisParameter, TMCM6110.AxisParameterType.SoftStopFlag, self.motor_port, 0)

### getter

    def getAbsoluteMaximumCurrentScale(self):
        print("get absolute maximum current scale")
        reply = self.parent.sendCommand(TMCM6110.GetAxisParameter, TMCM6110.AxisParameterType.AbsoluteMaximumCurrentScale, self.motor_port, None)
        self.parent.evaluateReply(reply)

    def getStandbyCurrent(self):
        print("get standby current")
        reply = self.parent.sendCommand(TMCM6110.GetAxisParameter, TMCM6110.AxisParameterType.StandbyCurrent, self.motor_port, None)
        self.parent.evaluateReply(reply)

    def getMaximumPositioningSpeed(self):
        print("get maximum positioning speed")
        reply = self.parent.sendCommand(TMCM6110.GetAxisParameter, TMCM6110.AxisParameterType.MaximumPositioningSpeed, self.motor_port, None)
        self.parent.evaluateReply(reply)

    def getMaximumAcceleration(self):
        print("get maximum acceleration")
        reply = self.parent.sendCommand(TMCM6110.GetAxisParameter, TMCM6110.AxisParameterType.MaximumAcceleration, self.motor_port, None)
        self.parent.evaluateReply(reply)

    def getReferenceSearchMode(self):
        print('get reference search mode')
        search_modes = {1 : 'SearchLeftStopSwitch',
                        2 : 'SearchRightStopSwitch',
                        3 : 'SearchRightStopSwitchBothSides',
                        4 : 'SearchLeftStopSwitchBothSides',
                        5 : 'SearchHomeSwitchNegativeDirection',
                        6 : 'SearchHomeSwitchPositiveDirection',
                        7 : 'SearchHomeSwitchPositiveDirection2',
                        8 : 'SearchHomeSwitchNegativeDirection2'}
        reply = self.parent.sendCommand(TMCM6110.GetAxisParameter, TMCM6110.AxisParameterType.ReferenceSearchMode, self.motor_port, None)
        return self.parent.evaluateReply(reply)

    def getMicrostepResolution(self):
        print('get microstep resolution')
        reply = self.parent.sendCommand(TMCM6110.GetAxisParameter, TMCM6110.AxisParameterType.MicrostepResolution, self.motor_port, None)
        self.parent.evaluateReply(reply)

    def getSmartEnergyActualCurrent(self):
        print('get SmartEnergyActualCurrent')
        reply = self.parent.sendCommand(TMCM6110.GetAxisParameter, TMCM6110.AxisParameterType.SmartEnergyActualCurrent, self.motor_port, None)
        self.parent.evaluateReply(reply)