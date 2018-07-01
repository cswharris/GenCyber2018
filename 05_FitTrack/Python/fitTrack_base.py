from microbit import *
import radio

radio.on()
radio.config(channel=1)
radio.config(power=7)
x_Accel = 0
# Initialize y and z acceleration

measuring = False
display.show(Image.YES)

def capture_data():
    x_Accel = accelerometer.get_x()
    # Get y and z acceleration

    radio.send(str(x_Accel) + ',' + str(y_Accel) + ',' + str(z_Accel))
    
        
def write_data():
    print(x_Accel, y_Accel, z_Accel, sep=',', end='\n')

while True:
    if button_a.is_pressed() and button_b.is_pressed():
        # Set measuring to False
        
        # Send "done" over radio
        
        # Show a Happy face on the display (display.show(Image.HAPPY))
        
    elif button_a.is_pressed():
        # Set measuring to True

        # Show a heart on the display (Image.HEART)
        
    elif button_b.is_pressed():
        # Set measuring to False

        # Show a checkmark on the display (Image.YES)
        
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