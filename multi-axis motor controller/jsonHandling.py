import json

class jsonHandling():
    def __init__(self):
        pass
    
    def openJson(self, json_file):
        '''Opens a json file and returns data as dict.'''
        with open(json_file) as jf:
            jfdata = json.load(jf)
        return jfdata

    def verifyJson(self, json_file):
        '''Unfinished function. Can be used to verify whether a selected json file is actually meant for the project.'''
        jf_data = self.openJson(json_file)
        if jf_data['json_type'] == 'stepperMotorController':
            return True
        else:
            return False

