#hard-key2.py
from microbit import *
import radio 

state = 50
radio_group = state #number of radio frequency to use
radio.on()
radio.config(power=7,channel=radio_group)

display.show(Image.HEART)
while True:# do forever
    if state == 1:
        state = 99
    else:
        state = state-1
    radio.config(channel=state)
    radio.send("100110")
    sleep(100)
