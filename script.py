import serial, json
import pyautogui, time
import os

s = serial.Serial('/dev/cu.usbmodem14101')
lights_status = "ON"

def toggleLights():
	global lights_status

	if lights_status == "OFF":
		turnOnLights()
	else:
		turnOffLights()

def turnOnLights():
	global lights_status

	lights_status = "ON"
	os.system("curl https://maker.ifttt.com/trigger/desk_on/with/key/cZaYjDiLwVyUerel-sdsmSuzIVK5naHuLP3NJC6jMME")

def turnOffLights():
	global lights_status

	lights_status = "OFF"
	os.system("curl https://maker.ifttt.com/trigger/desk_off/with/key/cZaYjDiLwVyUerel-sdsmSuzIVK5naHuLP3NJC6jMME")

while True:
	try:
		data = json.loads(s.readline())
		proximity = (data["detail"]["proximity"])

		print(proximity)

		if proximity > 0:
			toggleLights()
			print("\n\n\n\n" + lights_status + "\n\n\n\n")
			time.sleep(3)

		s.flushInput()
	except Exception:
		continue
