    from microbit import *
    import radio
    import time
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
    
    strength_5 = Image("99999:"
                       "99999:"
        			   "99999:"
    				   "99999:"
    				   "99999")
    
    id = 0
    display.show(Image.DIAMOND)
    radio.on()
    
    while True:
        radio.config(group=id)
        if id is 10:
            id = 0
        else:
            id = id + 1
        
        details = radio.receive_full()
        if details is not None:
            x, rssi, y = details
            if (rssi>-60):
                display.show(strength_5)
                sleep(300)
                display.show(Image.YES)
                sleep(500)
                display.clear()
            elif (rssi>-65):
                display.show(strength_4)
                sleep(300)
            elif (rssi>-75):
                display.show(strength_3)
                sleep(300)
            elif (rssi>-95):
                display.show(strength_2)
                sleep(300)
            else:
                display.show(strength_1)
                sleep(300)
        sleep(100)