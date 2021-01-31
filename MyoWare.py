import serial
from threading import Thread


class Myoware(Thread):
    def __init__(self, port):
        self.ser = None
        self.port = port

        self.mw1 = -1
        self.mw2 = -1

        self.mw1_value = -1
        self.mw2_value = -1

        self.newdata = False
        self.thread = True
        Thread.__init__(self)
        self.start()


    def run(self):
        self.ser = serial.Serial()
        self.ser.baudrate = 9600
        self.ser.port = self.port
        self.ser.open()
        while self.thread:
            self.mw1 = self.ser.readline()
            try:
                self.mw1_value = int(self.mw1)
            except:
                print("MyoWare1 was {}".format(self.mw1))

            self.mw2 = self.ser.readline()
            try:
                self.mw2_value = int(self.mw2)
            except:
                print("MyoWare2 was {}".format(self.mw2))

            self.newdata = True

    def __del__(self):
        self.thread = False
        self.join()


if __name__ == "__main__":
    MW = Myoware("COM6")
    print("hello")
    from time import sleep
    sleep(5)
    MW.__del__()

