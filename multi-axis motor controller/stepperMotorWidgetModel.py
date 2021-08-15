
import io, json, os
import stepperMotor

class stepperMotorWidgetModel():
    def __init__(self, communication):
        self.communication = communication

        self.motor_dict = {} # {motor_port : stepperMotor}
        self.stepper_motor_default_values = {"conversion_factor" : 1, 
                                             "maximum_positioning_speed" : 1500, 
                                             "maximum_acceleration" : 1500, 
                                             "absolute_maximum_current_scale" : 100, 
                                             "standby_current" : 8, 
                                             "microstep_resolution" : 8, 
                                             "reference_search_mode" : "SearchHomeSwitchPositiveDirection2"}

### stepperMotor related

    def addMotor(self, motor_port, json_data):
        """Instantiates stepper motor and adds it to a dictionary by motor_port \n
        motor_dict = {motor_port : stepperMotor}"""
        sm = stepperMotor.stepperMotor(self.communication, motor_port, json_data['conversion_factor'], json_data['maximum_positioning_speed'], json_data['maximum_acceleration'], json_data['absolute_maximum_current_scale'], json_data['standby_current'], json_data['microstep_resolution'], json_data['reference_search_mode'])
        self.motor_dict[motor_port] = sm

    def removeStepperMotor(self, motor_port):
        '''Removes data of a stepper motor that is to be deleted from the dict.'''
        try:
            self.motor_dict.pop(motor_port)
        except KeyError:
            print("Error in ", self.__name__, ".py: ", KeyError)
    
    def saveJsonCheck(self, file_name):
        '''Checks whether the input file_name already exists. If it does not exist it will be created.'''
        if os.path.isfile(file_name[0]) and os.access(file_name[0], os.R_OK):
            print("File exists and is readable")

        else:
            print ("Either file is missing or is not readable, creating file...")
            name = os.path.basename(file_name[0])
            path = os.path.dirname(file_name[0])
            try:
                with io.open(os.path.join(path, name), 'w') as db_file:
                    db_file.write(json.dumps({}))
            except FileNotFoundError:
                return False
        return True

### stepperMotor movement

    def moveToPosition(self, motor_port, value, type):
        self.motor_dict[motor_port].moveToPosition(value, type)

    def referenceSearch(self, motor_port):
        self.motor_dict[motor_port].referenceSearch()

### stepperMotor setter

    def motorStop(self, motor_port):
        self.motor_dict[motor_port].motorStop()

    def setConversionFactor(self, motor_port, conversion_factor):
        self.motor_dict[motor_port].setConversionFactor(conversion_factor)

    def setAbsoluteMaximumCurrentScale(self, motor_port, value):
        self.motor_dict[motor_port].setAbsoluteMaximumCurrentScale(value)

    def setMaximumPositioningSpeed(self, motor_port, value):
        self.motor_dict[motor_port].setMaximumPositioningSpeed(value)

    def setMaximumAcceleration(self, motor_port, value):
        self.motor_dict[motor_port].setMaximumAcceleration(value)

    def setMicrostepResolution(self, motor_port, value):
        self.motor_dict[motor_port].setMicrostepResolution(value)

    def setStandbyCurrent(self, motor_port, value):
        self.motor_dict[motor_port].setStandbyCurrent(value)

    def setReferenceSearchMode(self, motor_port, value):
        self.motor_dict[motor_port].setReferenceSearchMode(value)

    def setSmartEnergyActualCurrent(self, motor_port, value):
        self.motor_dict[motor_port].setSmartEnergyActualCurrent(value)

    def setReferencingSearchSpeed(self, motor_port, value):
        self.motor_dict[motor_port].setReferencingSearchSpeed(value)

    def setSoftStopFlag(self, motor_port, value):
        self.motor_dict[motor_port].setSoftStopFlag(value)

### stepperMotor getter

    def getAbsoluteMaximumCurrentScale(self, motor_port):
        self.motor_dict[motor_port].getAbsoluteMaximumCurrentScale()

    def getStandbyCurrent(self, motor_port):
        self.motor_dict[motor_port].getStandbyCurrent()

    def getMaximumPositioningSpeed(self, motor_port):
        self.motor_dict[motor_port].getMaximumPositioningSpeed()

    def getMaximumAcceleration(self, motor_port):
        self.motor_dict[motor_port].getMaximumAcceleration()

    def getReferenceSearchMode(self, motor_port):
        self.motor_dict[motor_port].getReferenceSearchMode()

    def getMicrostepResolution(self, motor_port):
        self.motor_dict[motor_port].getMicrostepResolution()

    def getSmartEnergyActualCurrent(self, motor_port):
        self.motor_dict[motor_port].getSmartEnergyActualCurrent()