import json
from telnetlib import Telnet
from threading import Thread


class MindwaveController(Thread):
    """
    Objet pour lire dans le Mindwave le fichier JSON.
    poorSignalLevel (int) : niveau de précision du Mindwave (0 - 200)
    blinkStrength (int) : niveau de clin d'oeil
    waveDict (dict) : {delta, theta, lowAlpha, highAlpha, lowBeta, highBeta, lowGamma, highGamma}
    eSenseDict (dict) : {attention, meditation}
    """

    def __init__(self, host, baudrate):

        self.signalLevel = -1
        self.blinkStrength = -1
        self.waveDict = {'lowGamma': -1, 'highGamma': -1,
                         'highAlpha': -1, 'lowAlpha': -1,
                         'highBeta': -1, 'lowBeta': -1,
                         'delta': -1, 'theta': -1}
        self.eSenseDict = {'attention': -1, 'meditation': -1}
        self.newdata = False

        self.host = host
        self.baudrate = baudrate

        self.thread = True
        Thread.__init__(self)
        self.start()

    def __del__(self):
        self.thread = False
        self.join()
        self.tn.close()


    def run(self):
        self.tn = Telnet(self.host, self.baudrate)
        self.tn.write('{"enableRawOutput": true, "format": "Json"}'.encode('ascii'))

        self.tn.read_until(b'\r')
        while self.thread:
            line = self.tn.read_until(b'\r')
            dict = json.loads(line.decode())

            if len(line) > 20:
                # print(line)
                self.resetData()
                if "poorSignalLevel" in dict:
                    self.signalLevel = dict['poorSignalLevel']
                if "blinkStrength" in dict:
                    self.blinkStrength = dict['blinkStrength']
                if "eegPower" in dict:
                    self.waveDict = dict['eegPower']
                    self.eSenseDict = dict['eSense']


                self.newdata = True


                """
                print("SignaLevel : {}".format(self.signal))
                print("Attention : {}".format(self.attention))
                print("Meditation : {}".format(self.meditation))
                print("Blink : {}".format(self.blink))
                print()
                """


    def resetData(self):
        self.signalLevel = -1
        self.blinkStrength = -1
        self.waveDict = {'lowGamma': -1, 'highGamma': -1,
                         'highAlpha': -1, 'lowAlpha': -1,
                         'highBeta': -1, 'lowBeta': -1,
                         'delta': -1, 'theta': -1}
        self.eSenseDict = {'attention': -1, 'meditation': -1}


    @property
    def attention(self):
        #return int
        return self.eSenseDict["attention"]

    @property
    def meditation(self):
        #return int
        return self.eSenseDict["meditation"]

    @property
    def blink(self):
        #return int
        return self.blinkStrength

    @property
    def signal(self):
        #return int
        return self.signalLevel

    @property
    def eeg(self):
        #return dict
        return self.waveDict



if __name__ == "__main__":
    Mindwave = MindwaveController('localhost', 13854)



