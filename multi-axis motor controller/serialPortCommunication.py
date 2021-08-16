import serial

class serialPortCommunication():
    def __init__(self):
        self.address = 1
        self.baudrate = 4000
        self.port_name = 'COM4'

        self.status_codes = {100 : 'Successfully executed, no error', 101 : 'Command loaded into TMCL program EEPROM', 1 : 'Wrong checksum', 2 : 'Invalid command', 3 : 'Wrong type', 4 : 'Invalid value', 5 : 'Configuration EEPROM locked', 6 : 'Command not available'}
        self.motor_list = []

        # open serial port
        self.ser = serial.Serial(self.port_name, self.baudrate)  # open serial port, timeout inkludieren

### Command related     

    def checksum(self, command): #motor
        '''Edit command array to be the desired command. \n
        Bytes Meaning \n
        1    1 Module address \n
        2    1 Command number \n
        3    1 Type number \n
        4    1 Motor or Bank number \n
        5-8  4 Value (MSB first!) \n 
        9    1 Checksum \n '''
        checksum = command[0]
        for i in range(1,8):
            checksum += command[i]
        checksum = str(self.padHex(hex(checksum)))[-2::]
        command[8] = int(checksum, 16) # insert checksum as last byte of command

        return command   

    def sendCommand(self, command_num, type, motor_num, value):
        '''Sends command and value to respective functions to turn it into the correct syntax and executes the command. \n
        Command : Bytearray syntax: [host address : int, command_number : int, type : int, motor_port : int, value : int, value : int, value : int, value : int, checksum : int]'''
        if type is None:
            type = 0
        command = [self.address, command_num, type, motor_num, 0,0,0,0,0]
        self.ser.read_all() 
        if value is None:
            array = bytearray(command)
        else:
            array = bytearray(self.setupCommand(command, value))
        self.ser.read_all()
        self.ser.write(self.checksum(array))
        self.ser.in_waiting
        return self.ser.read_all()        

    def padHex(self, hex_value): # motor
        '''Fills a hex with zeros to wanted length of 8 bytes and removes the '0x' that is not needed.\n'
        Example: \n
            hex(303) == '0x12f' \n
            padHex(hex(303)) == '0000012f' \n
        '''
        return hex_value[2:].zfill(8)

    def addHexValueToCommand(self, value): # motor RENAME addHexValueToList
        '''Prepares value so it can easily be added to the command list. Currently already adds the value.
        \n Command syntax: [host address, command_number, type, motor_port, value, value, value, value, checksum]'''
        hex_value = self.padHex(hex((value + (1 << 32)) % (1 << 32)))
        value_list = [hex_value[i:i+2] for i in range(0, len(hex_value), 2)]
        return value_list

    def setupCommand(self, command, value):
        '''Adds value in right syntax to the command
        Command syntax: [host address, command_number, type, motor_port, value, value, value, value, checksum]'''
        value_list = self.addHexValueToCommand(value)
        command[4] = 0
        for i in range(len(value_list)):
            command[i + 4] = int(value_list[i], 16)
        return command

### Reply related

    def evaluateReply(self, reply): 
        '''Currently only prints reply and status_code.'''
        print(reply, 'Status: ', reply[2], self.status_codes[reply[2]])
        print("Value", self.replyValueToInt(reply))

    def replyValueToInt(self, reply):
        '''Turns the reply hex values into interpretable int values.'''
        value_list = []
        for i in range(4,8):
            value_list.append(reply[i])

        hex_list = []
        for e in value_list:
            hex_v = hex(e)
            hex_list.append(hex_v)
        
        string = ''.join([str(item) for item in hex_list])

        res = string.replace('0x', '')
        hex_i = int(res, 16)
        hex_h = hex_i + 0x0
        if hex_h >= 1<<31: hex_h -= 1<<32
        return hex_h

if __name__ == '__main__':
    serialPortCommunication.__init__(serialPortCommunication)


    
