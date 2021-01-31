import time
from Arduino import *
from Mindwave import *
from Motor_3D import *
from Motor_RD import *
from Interface import *
from MyoWare import *

"""
Programme Main connectant les 5 objets du projets TPE de Moncef, Jeffrey, 4T
"""

tkinter = interface()

Arduino = ArduinoController("COM8")
Mindwave = MindwaveController('localhost', 13854)
Bras3D = RoboticArm3D(Arduino)
BrasRD = RoboticArmRD(Arduino)
Myoware = Myoware("COM6")

Axe = ["+X", "-X", "+Y", "-Y", "+Z", "-Z"]
index_axe = 0
blink_starter_clock = time.perf_counter()  # int time from the start of the program
mw_1_starter_clock = time.perf_counter()  # int time from the start of the program
mw_2_starter_clock = time.perf_counter()  # int time from the start of the program


def change_axe():
	global index_axe, Axe
	index_axe = (index_axe + 1) % 6

while True:
	# Myoware
	if Myoware.newdata and tkinter.running:
		# Myoware 1
		if time.perf_counter() - mw_1_starter_clock >= 2:
			if Myoware.mw1_value >= 150 and tkinter.myoware_1_change_bool:
				change_axe()
				mw_1_starter_clock = time.perf_counter()
			if Myoware.mw1_value >= 500 and tkinter.myoware_1_pince_bool:
				Arduino.pince_controller()
				mw_1_starter_clock = time.perf_counter()
		# Myoware 2
		if time.perf_counter() - mw_2_starter_clock >= 2:
			if Myoware.mw2_value >=150 and tkinter.myoware_2_change_bool:
				change_axe()
				mw_2_starter_clock = time.perf_counter()
			if Myoware.mw2_value >= 500 and tkinter.myoware_2_pince_bool:
				Arduino.pince_controller()
				mw_2_starter_clock = time.perf_counter()

		Myoware.newdata = False


	# Mindwave
	if Mindwave.newdata and tkinter.running:
		signalQualityInt = Mindwave.signal
		attentionInt = Mindwave.eSenseDict['attention']
		meditationInt = Mindwave.eSenseDict['meditation']
		blinkStrengthInt = Mindwave.blinkStrength

		if blinkStrengthInt >= 70 and time.perf_counter() - blink_starter_clock >= 2.0 and tkinter.yeux_change_bool:
			change_axe()
			blink_starter_clock = time.perf_counter()

		if attentionInt >= 80:
			if tkinter.mode_3D:
				Bras3D.move_to_axe(Axe[index_axe], float(tkinter.value_incrementation.get()))
			if tkinter.mode_RD:
				BrasRD.move_to_axe(Axe[index_axe], float(tkinter.value_incrementation.get()))

		Mindwave.newdata = False

	#Interface
	if tkinter.thread:
		if tkinter.mode_changed:
			Arduino.write(90, 90, 90, 45)
			Bras3D.x, Bras3D.y, Bras3D.z = 12, 0, 9
			BrasRD.r, BrasRD.d, BrasRD.z = 90, 12, 10
			tkinter.mode_changed = False

		if tkinter.newdata_coordonnees:
			x = int(tkinter.x)
			y = int(tkinter.y)
			z = int(tkinter.z)
			print("{} {} {}".format(x, y, z))
			if tkinter.mode_3D:
				Bras3D.move_to((x, y, z))
				tkinter.newdata_coordonnees = False
			if tkinter.mode_RD:
				BrasRD.move_to((x, y, z))
				tkinter.newdata_coordonnees = False

		if tkinter.newdata_pince:
			Arduino.pince_controller()
			tkinter.newdata_pince = False

		if tkinter.running:
			tkinter.eeg_attention_value.set(Mindwave.attention)
			tkinter.eeg_meditation_value.set(Mindwave.meditation)
			tkinter.eeg_yeux_value.set(Mindwave.blink)
			tkinter.eeg_signal_value.set(Mindwave.signal)

			tkinter.emg_myoware_1_value.set(Myoware.mw1_value)
			tkinter.emg_myoware_2_value.set(Myoware.mw2_value)

		tkinter.arm_Axe_value.set(Axe[index_axe])
		if tkinter.mode_3D:
			tkinter.pos_X_value.set(Bras3D.x)
			tkinter.pos_Y_value.set(Bras3D.y)
			tkinter.pos_Z_value.set(Bras3D.z)
		if tkinter.mode_RD:
			tkinter.pos_X_value.set(BrasRD.x)
			tkinter.pos_Y_value.set(BrasRD.y)
			tkinter.pos_Z_value.set(BrasRD.z)
	else:
		print("out")
		Myoware.__del__()
		Mindwave.__del__()
		tkinter.__del__()
		break




print("end")