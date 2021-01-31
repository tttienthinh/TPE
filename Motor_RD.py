import math


class RoboticArmRD:
    _rangement_position = (0, 5, 6)
    _initialPosition = (90, 12, 10)
    _brasA = 9.7
    _brasB = 10.7
    _deg = 180/math.pi

    def __init__(self, arduino, position=(90, 12, 10)):
        self.arduino = arduino
        self.r, self.d, self.z = position
        self.gamma = 0
        self.alpha = 0
        self.beta = 0
        self.delta = 0
        self.j = 0
        self.new_data = False
        self.axe = None


    def calcul_move(self, target_position):
        self.new_data = True
        target_r, target_d, target_z = target_position
        #gamma
        try:
            self.gamma = 180 - target_r
            print("aaa")
            print(self.gamma)
        except:
            self.new_data = False


        try:
            d = target_d
        except:
            self.new_data = False

        #alpha
        try:
            self.alpha = math.acos((d**2 + target_z**2 - self._brasA**2 - self._brasB**2)/(-2 * self._brasA * self._brasB))
        except:
            self.new_data = False
        #beta
        try:
            B1 = math.asin(((math.sin(self.alpha)) / (math.sqrt(d**2 + target_z**2))) * self._brasB)
        except:
            self.new_data = False
        try:
            B2 = math.atan(target_z/d)
        except:
            self.new_data = False
        try:
            self.beta = ((B1 + B2) * self._deg)
        except:
            self.new_data = False
        try:
            self.alpha = 180 -( math.acos((d ** 2 + target_z ** 2 - self._brasA ** 2 - self._brasB ** 2) / (-2 * self._brasA * self._brasB)) * self._deg)
        except:
            self.new_data = False


        try:
            self.delta=270 - (self.beta+180-self.alpha)
           # self.delta =( self.j -(self.alpha+180 + self.beta))
            print(self.delta)

        except:
            self.new_data = False



        print("{} {} {}".format (self.alpha , self.beta , self.gamma ))

    def move_to_axe(self, axe, move):
        target_position = self.change_coordonnes(axe, move)
        self.move_to(target_position)

    def change_coordonnes(self, axe, move):
        self.axe = axe
        r, d, z = self.r, self.d, self.z

        if axe[0] == "-":
            move = 0 - move

        if axe[1] == "R":
            r += move * 5
        elif axe[1] == "D":
            d += move
        elif axe[1] == "Z":
            z += move
        #print("coordonnees changed {}".format(move))
        return(r, d, z)

    def move_to(self, target_position):

        self.calcul_move(target_position)

        if self.new_data == True:
            self.arduino.write(round(self.gamma, 2), round(self.beta, 2), round(self.alpha, 2), round(self.delta, 2))
            self.r, self.d, self.z = target_position
            self.new_data = False
        else:
            print("Math Error {}".format(self.axe))





