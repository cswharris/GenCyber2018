from microbit import *
import radio

radio.on()
radio.config(group=1)
radio.config(power=7)
z_Accel = 0
y_Accel = 0
x_Accel = 0
measuring = False
display.show(Image.YES)

def capture_data():
    vals = {'x':0, 'y':0, 'z':0}
    vals['x'] = accelerometer.get_x()
    vals['y'] = accelerometer.get_y()
    vals['z'] = accelerometer.get_z()
    radio.send("x"+str(x_Accel))
    radio.send("y"+str(y_Accel))
    radio.send("z"+str(z_Accel))
    
        
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
        elif incoming.startswith('x'):
        elif incoming.startswith('y'):
        elif incoming.startswith('z'):
            
            write_data()
        else:
            #x_Accel, y_Accel, z_Accel = incoming.split(",")
            #write_data()
    if measuring:
        capture_data()
    sleep(200)