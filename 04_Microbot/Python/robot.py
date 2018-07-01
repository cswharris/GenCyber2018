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

while True:# do forever
    if not group_set:
        display.show(str(radio_group))
        if button_a.is_pressed() and button_b.is_pressed():
            group_set = True
            radio.config(channel = radio_group)
            display.show(Image.HAPPY)
            
        elif button_a.is_pressed():
            if radio_group > 0:
                radio_group = radio_group - 1
                
        elif button_b.is_pressed():
            if radio_group < 255:
                radio_group = radio_group + 1 
        sleep(150)

    else:# radio group has been set
        incoming = radio.receive()
        
        if incoming is "forward":
            motobit.drive(127, 127)
            display.show(Image.ARROW_N)
        elif incoming is "stop":
            motobit.drive(0,0)
            display.show(stop_sign)
        elif incoming is "right":
            motobit.drive(127,0)
            display.show(Image.ARROW_E)
        elif incoming is "left":
            motobit.drive(0, 127)
            display.show(Image.ARROW_W)
        sleep(100)
        
        
