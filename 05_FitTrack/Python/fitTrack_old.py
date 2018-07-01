from microbit import *
import radio


radio.on()
radio.config(channel=1)
radio.config(power=7)
z_Accel = 0
y_Accel = 0
x_Accel = 0
measuring = False
display.show(Image.YES)

def capture_data():
    x_Accel = accelerometer.get_x()
    y_Accel = accelerometer.get_y()
    z_Accel = accelerometer.get_z()
    radio.send(str(x_Accel) + ',' + str(y_Accel) + ',' + str(z_Accel))
    
        
def write_data():
    print(x_Accel, y_Accel, z_Accel, sep=',', end='\n')

while True:
    if button_a.is_pressed() and button_b.is_pressed():
        measuring = False
        radio.send("done")
        display.show(Image.HAPPY)
    elif button_a.is_pressed():
        measuring = True
        display.show(Image.HEART)
    elif button_b.is_pressed():
        measuring = False
        display.show(Image.YES)
    incoming = radio.receive()
    if incoming is not None:
        if incoming.startswith('done'):
            display.show(Image.HAPPY)
            print("done")
        else:
            x_Accel, y_Accel, z_Accel = incoming.split(",")
            write_data()
    if measuring:
        capture_data()
    sleep(200)