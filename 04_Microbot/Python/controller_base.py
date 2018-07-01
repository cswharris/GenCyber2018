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
            # Show radio_group on the display (use str(radio_group))
            

        if button_a.is_pressed() and button_b.is_pressed():
            if group_set is False:
                # Set group_set to True
                
                radio.config(channel = radio_group)
                # Show a happy face on the display (Image.HAPPY)
                
                # Set forward to False
            else:
                if forward == False:
                    # Send "forward" over radio (radio.send(...))
                    
                    # Set forward to True

                    # Show a forward arrow on the display (Image.ARROW_N)
                    
                else:
                    # Send "stop" over radio (radio.send(...))
                    
                    # Set forward to False

                    # Show a stop sign on the display (stop_sign)
            
        elif button_a.is_pressed():
            if group_set == False and radio_group > 0 :
                # Decrement radio_group by one (radio_group-1)
                
            else:
                # Send "left" over radio

                # Show a left arrow on the display (Image.ARROW_W)
                
        elif button_b.is_pressed():
            if group_set is False and radio_group < 255:
                # Increment radio_group by one (radio_group+1)

            else:
                # Send "right" over radio

                # Show a right arrow on the display (Image.ARROW_E)
        sleep(200)
