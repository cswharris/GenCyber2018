from microbit import *
import radio

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
            
        elif (rssi>-80):
            
        elif (rssi>-120):
            
        else:
            