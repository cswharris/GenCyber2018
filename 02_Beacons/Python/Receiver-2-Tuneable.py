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
radio.config(group=1)
group = 1
recordedIds = []

while True:
   
    if button_a.was_pressed():
        if group > 0:
            group = group - 1
            radio.config(group=group)
        display.show(str(group))
        sleep(500)
    
    if button_b.was_pressed():
        if group < 9:
            group = group + 1
            radio.config(group=group)
        display.show(str(group))
        sleep(500)
        
    details = radio.receive_full()
    if details is not None:
		id, rssi, y = details
		if (rssi > -50):
		 	display.show(Image.YES)
			sleep(100)
			if id[-4:] not in recordedIds:
				recordedIds.append(id[-4:])
				display.show(str(len(recordedIds)))
				sleep(500)
		elif (rssi>-60):
			display.show(strength_4)
		elif (rssi>-80):
			display.show(strength_3)
		elif (rssi>-120):
			display.show(strength_2)
		else:
			display.show(strength_1)