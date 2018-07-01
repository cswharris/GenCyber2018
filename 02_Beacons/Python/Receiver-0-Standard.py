from microbit import *
import radio

strength_1 = Image("00000:"
                   "00000:"
				   "00900:"
				   "00000:"
				   "00000")

strength_2 = Image("00000:"
                   "00900:"
				   "09990:"
				   "00900:"
				   "00000")

strength_3 = Image("00900:"
                   "09990:"
				   "99999:"
				   "09990:"
				   "00900")
	
strength_4 = Image("09990:"
                   "99999:"
				   "99999:"
				   "99999:"
				   "09990")

display.show(Image.DIAMOND)
radio.on()
radio.config(group = 1)

while True:
    details = radio.receive_full()
    if details is not None:
        x, rssi, y = details
        if (rssi>-50):
            display.show(Image.YES)
        elif (rssi>-60):
            display.show(strength_4)
        elif (rssi>-80):
            display.show(strength_3)
        elif (rssi>-120):
            display.show(strength_2)
        else:
            display.show(strength_1)