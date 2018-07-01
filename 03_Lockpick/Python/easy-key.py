#easy-key.py
from microbit import *
import radio 

radio_group = 1 #number of radio frequency to use
radio.on()
radio.config(power=7,channel=radio_group)

display.show(Image.HAPPY)
send_string = ""

while True:# do forever
    display.scroll(send_string)
    if button_a.is_pressed() and button_b.is_pressed():
        radio.send(send_string)
        send_string=""
        display.show(Image.STICKFIGURE)
        break
    elif button_a.is_pressed():
        send_string = send_string+"0"
    elif button_b.is_pressed():
        send_string = send_string+"1"
    sleep(100)


        