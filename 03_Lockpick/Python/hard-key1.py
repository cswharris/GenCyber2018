#hard-key1.py
from microbit import *
import radio 

radio_group = 2 #number of radio frequency to use
radio.on()
radio.config(power=7,channel=radio_group)

display.show(Image.HEART)
send_string = ""

while True:# do forever
    if button_a.was_pressed():
        radio.send("0101")
        radio.config(channel=5)
        display.show(Image.YES)
    elif button_b.was_pressed():
        radio.send("1001")
        radio.config(channel=2)
        display.show(Image.CHESSBOARD)
