from pyfirmata import Arduino



class ArduinoController():

    def __init__(self, port):
        #ser = serial.Serial('COM8', 9600, timeout=1);
        self.board = Arduino(port)

        # define servo output
        self.servo_1 = self.board.get_pin('d:{}:s'.format(2))
        self.servo_2 = self.board.get_pin('d:{}:s'.format(3))
        self.servo_3 = self.board.get_pin('d:{}:s'.format(4))
        self.servo_4 = self.board.get_pin('d:{}:s'.format(5))
        self.servo_5 = self.board.get_pin('d:{}:s'.format(6))

        self.pince_opened = False
        self.pince_open()

        self.write(90, 90, 90, 45)



    def __del__(self):
        self.board.exit()

    def write(self, angle1, angle2, angle3, angle4):
        self.servo_1.write(angle1)
        self.servo_2.write(angle2)
        self.servo_3.write(angle3)
        self.servo_4.write(angle4)

    def pince_open(self):
        if not self.pince_opened:
            self.servo_5.write(50)
            self.pince_opened = True

    def pince_close(self):
        if self.pince_opened:
            self.servo_5.write(180)
            self.pince_opened = False

    def pince_controller(self):
        if self.pince_opened:
            self.pince_close()
        else:
            self.pince_open()



