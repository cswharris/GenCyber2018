#hard-lockbox1.py
from microbit import *
import radio

class Servo:

    """
    A simple class for controlling hobby servos.
    Args:
        pin (pin0 .. pin3): The pin where servo is connected.
        freq (int): The frequency of the signal, in hertz.
        min_us (int): The minimum signal length supported by the servo.
        max_us (int): The maximum signal length supported by the servo.
        angle (int): The angle between minimum and maximum positions.
    Usage:
        SG90 @ 3.3v servo connected to pin0
        = Servo(pin0).write_angle(90)
    """

    def __init__(self, pin, freq=50, min_us=600, max_us=2400, angle=180):
        self.min_us = min_us
        self.max_us = max_us
        self.us = 0
        self.freq = freq
        self.angle = angle
        self.analog_period = 0
        self.pin = pin
        analog_period = round((1/self.freq) * 1000)  # hertz to miliseconds
        self.pin.set_analog_period(analog_period)

    def write_us(self, us):
        us = min(self.max_us, max(self.min_us, us))
        duty = round(us * 1024 * self.freq // 1000000)
        self.pin.write_analog(duty)
        self.pin.write_digital(0)  # turn the pin off

    def write_angle(self, degrees=None):
        degrees = degrees % 360
        total_range = self.max_us - self.min_us
        us = self.min_us + total_range * degrees // self.angle
        self.write_us(us)

state = 0
radio_group = 2 #number of radio frequency to use
radio.on()
radio.config(power=7,channel=radio_group)
position = 20

def getMessage():
    while True:
        display.show(Image.DIAMOND)
        incoming = radio.receive()
        #display.show(incoming)
        if len(incoming)>3:
            break
    return incoming

while True:# do forever
    msg = radio.receive()
    #if state == 0:
    if msg == "0101" and state ==0:
        state = 1
        radio_group = 5
        radio.config(channel = radio_group)
        display.show(Image.YES)
    elif msg == "1001" and state ==1:
        state = 0
        radio_group = 2
        radio.config(channel = radio_group)
        if position == 160:
            position = 20
        else:
            position = 160
        Servo(pin16).write_angle(position)
        display.show(Image.HEART)
