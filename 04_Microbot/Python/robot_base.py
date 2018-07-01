#robot-johno.py
#perform robot actions from received commands

from microbit import *
import radio

class MotoBit:
    moto_l = 0x21
    moto_r = 0x20
    moto_on = 0x70
    
    def __init__(self, address = 0x59):
        self.ADDR = address
          
    def write16(self,a,b):
        i2c.write(self.ADDR, bytes([a,b]), repeat=False)
    
    # True or False
    def enable(self, pwr):
        if pwr:
            self.write16(0x70,1)
        else:
            self.write16(0x70,0)
            
    # 0 for right, 1 for left, speed -127 to 127    
    def set_speed(self, motor, speed):
        motor = motor + 32
        if speed>=0:
            self.write16(motor,128 + speed)
        else:
            speed = speed + 127
            self.write16(motor, speed)
    # left and right speeds
    def drive(self,left,right):
        self.set_speed(0,right)
        self.set_speed(1,left)



radio_group = 0 #number of radio frequency to use
group_set = False #has the radio group been set?
motobit = MotoBit()
motobit.enable(True) # Enable motor driver
radio.on()
radio.config(power=7)

stop_sign = Image(  "09990:"
                    "90099:"
                    "90909:"
                    "99009:"
                    "09990")

while True:
    if not group_set:
        display.show(str(radio_group))
        if button_a.is_pressed() and button_b.is_pressed():
            # Set group_set to True
            
            radio.config(channel = radio_group)
            # Show a happy face on the display (Image.HAPPY)
            
        elif button_a.is_pressed():
            # If radio_group is greater than 0:

                # Decrement radio_group by 1 (radio_group-1)
                
        elif button_b.is_pressed():
            # If radio_group is less than 255:
            
                # Increment radio_group by 1 (radio_group+1) 
        sleep(150)

    else:
        incoming = radio.receive()
        # NOTE - Drive the motobit using motobit.drive(left, right)
       
        # If incoming is "forward":

            # Drive the motobit forward (127 for left wheel and 127 for right wheel)
            
            # Show a forward arrow on the display (Image.ARROW_N)

        # Else, if incoming is "stop":

            # Stop the motobit (drive with 0 for left and 0 for right)

            # Show a stop_sign on the display

        # Else, if incoming is "right":

            # Drive the motobit right (127 for left and 0 for right)

            # Show a right arrow on the display (Image.ARROW_E)

        # Else, if incoming is "left":
        
            # Drive the motobit left (0 for left and 127 for right)

            # Show a left arrow on the display (Image.ARROW_W)

        sleep(100)
        
        
