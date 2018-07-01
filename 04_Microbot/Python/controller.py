#robot-ctrl.py
#Robot controller

from microbit import *
import radio

radio_group = 0 #number of radio frequency to use
forward = False
group_set = False #has the radio group been set?
radio.on()
radio.config(power=7)

stop_sign = Image(  "09990:"
                    "90099:"
                    "90909:"
                    "99009:"
                    "09990")

while True:# do forever
        if group_set is False:
            display.show(str(radio_group))

        if button_a.is_pressed() and button_b.is_pressed():
            if group_set is False:
                group_set = True
                radio.config(channel = radio_group)
                display.show(Image.HAPPY)
                forward = False
            else:
                if forward == False:
                    radio.send("forward")
                    forward = True
                    display.show(Image.ARROW_N)
                else:
                    radio.send("stop")
                    forward = False
                    display.show(stop_sign)
            
        elif button_a.is_pressed():
            if group_set == False and radio_group > 0 :
                radio_group = radio_group - 1
            else:
                radio.send("left")
                display.show(Image.ARROW_W)
                
        elif button_b.is_pressed():
            if group_set is False and radio_group < 255:
                radio_group = radio_group + 1 
            else:
                radio.send("right")
                display.show(Image.ARROW_E)
        sleep(200)
