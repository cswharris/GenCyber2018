# Fitness Tracker
## Lab Description

### Estimated Time: 1 Hour

### Description
You will have the opportunity to mimic data interception from a fitness tracker using radio signals. After gathering data from your partner, you will be able to interpret and graph the results using simple techniques. From the interpreted data, you will be able to tell what kind of activities your partner is doing. 

### Prerequisite Skills
* Radio Signal Basics
	* [Click here for information on radio signals](https://www.infoplease.com/encyclopedia/science-and-technology/computers-and-electrical-engineering/electrical-engineering/radio/transmission-and-reception-of-radio-waves)
	* [Click here for Micro::Bit radio basics](https://makecode.microbit.org/reference/radio)
* Serial Basics
	* [Click here for Micro::Bit serial basics](https://makecode.microbit.org/device/serial)
* Basic Math Skills 
	* We will be finding the acceleration in 3 different directions: x, y, and z.
	* To find the total acceleration, you need the following equation: $\sqrt{x^2+y^2+z^2}$ 

### Learned Skills
* Radio signal basics
* Data-interception topics
* Encryption ideas

### Materials
* Micro::Bit (1 per person / 2 per team)
* Micro-USB Cable
* Battery Pack (Equivalent to two AA batteries);

### Potential Issues
* Python must be downloaded on your computer to run serial_reader.py. You can still complete this lab without serial_reader.py with a chrome extension [here](https://chrome.google.com/webstore/detail/serial-monitor/ohncdkkhephpakbbecnkclhjkmbjnmlo?hl=en).
* It is ideal to have teams of 2, however teams of 3 work well too. 

## Instructions

### Lab Instructions
1) Read through the links under the prerequisite skills section. This will enable you to understand the basics of the lab. You want to be able to answer the following questions ([answers here]()):

    * If someone sends a message over radio waves, who can access that message?
    * What method do you use to send data over radio on a Micro::Bit?
    * What method do you use to run a block of code every time data is received?
    * How do you find the total acceleration from the x-acceleration, y-acceleration, and z-acceleration?

2) Read the **running instructions** below to get an idea of how the final program should work. Program your Micro::Bit by following the **programming instructions**. 

3) Find a partner that programmed their Micro::Bit in the same language as you (so if you used JavaScript, find someone who also used JavaScript). 

4) Begin by choosing who will be the tracker and who will be the hacker. The tracker will be the user of a fitness tracker. They will use their Micro::Bit to collect data about their movements. The other partner, the hacker, will obtain their data. See the **running instructions** for how to run the experiment. 

5) Continuing in the **running instructions**, analyze the data. These instructions will explain how to graph the data. From the graph, the hacker should make a guess about the activities that the tracker was doing (walking, running, jumping, and so on). 

6) Switch hacker and tracker roles and run again. After analyzing the data, have the new hacker make a guess about the activities of the new tracker.

7) Chat with your partner about the issues with wireless data transmission. What are some potential solutions to these problems? Can you think of a simple encryption solution that allows you to mask the data being sent? Can you reverse the encryption to use the data? 

8) With your partner, employ a solution in your code. Run the experiment one last time and to see if your solution worked. What worked well in your solution? How could your solution be improved? 

### Running Instructions
1) Designate 1 Micro::Bit as the receiver and 1 as the fitness tracker, both will have the same program written to them. However, one must be plugged into the computer to receive the data.

2) A check mark will appear to show the Micro::Bits are ready.

3) Double click on serial_reader.py or use the chrome extension: [here](https://chrome.google.com/webstore/detail/serial-monitor/ohncdkkhephpakbbecnkclhjkmbjnmlo?hl=en).

4) If you are using the chrome extension, launch the application and select the appropriate COM port (if you only have one device plugged in there will only be one option). Select a Baud Rate of 115200 and click on connect.

5) To start gathering data, hit the A button on the fitness tracker and a heart will appear.

6) To stop gathering data, hit the B button on the fitness tracker and the check mark will reappear. 

7) When you are done sending data, hit the A and B buttons at the same time to finish and a happy face will appear. 

8) If you used serial_reader.py, a graph of the data will automatically plot. If you used the chrome extension, continue to step 8. 

9) Copy and paste the data from chrome to Excel or Google Spreadsheets (select comma-separated when you paste the numbers). 

10) Obtain the total acceleration for each row. This is calculated by squaring each value and taking the square root of the sum. In other words, in cell D1, paste this:

```
=SQRT((A1)^2+(B1)^2+(C1)^2)
```

11) Click on the bottom right corner of D1 and drag down to the bottom of your data. This will make the same calculation for each row.

12) To graph the data, highlight the D column and click on the graph button. Some adjustments can be made to make the data easier to read, but the default is simply the total acceleration, ideal for showing different activities. 

### Programming Instructions
1) Start coding by pulling up the base code. There are two languages to choose from, Javascript and Python and they both work the same. To pull up the base code, [click here](). 



## JavaScript Code
Below is a copy of the base code as well as the completed code for JavaScript programmers. The answers are available as a reference, but you should attempt to complete the code without looking at the answers. There are multiple correct answers and the code below is simply a suggestion. 

### Base Code
```
let X_Accel = 0
let Y_Accel = 0
let Z_Accel = 0
let measuring = false
radio.onDataPacketReceived(({ receivedString: name, receivedNumber: value }) => {
    if (name == "x") {
        X_Accel = value
    } else if (name == "y") {
        // Set the y acceleration to value

    } else if (name == "z") {
        // set the z acceleration to value

        write_data()
    } else if (name == "done") {
        serial.writeLine("done")
    }
})
input.onButtonPressed(Button.AB, () => {
    radio.sendValue("done", 0)
    // Set measuring to false

    // Show a happy face on the display

})
input.onButtonPressed(Button.A, () => {
    // Set measuring to true

    // Show a heart on the display

})
input.onButtonPressed(Button.B, () => {
    // Set measuring to false

    // Show check mark (yes icon) on the display
})
function capture_data() {
    X_Accel = input.acceleration(Dimension.X)
    // Set the y and z accelerations to the y and z dimensions

    radio.sendValue("x", X_Accel)
    // Send y and z values over radio

}
function write_data()  {
    serial.writeLine("" + X_Accel + "," + Y_Accel + "," + Z_Accel)
}
radio.setGroup(1)
radio.setTransmitPower(7)
basic.showIcon(IconNames.Yes)
basic.forever(() => {
    if (measuring) {
        capture_data()
        basic.pause(200)
    }
})

```

### Completed Code
```
let Z_Accel = 0
let Y_Accel = 0
let X_Accel = 0
let measuring = false
radio.onDataPacketReceived( ({ receivedString: name, receivedNumber: value }) =>  {
    if (name == "x") {
        X_Accel = value
    } else if (name == "y") {
        Y_Accel = value
    } else if (name == "z") {
        Z_Accel = value
        write_data()
    } else if (name == "done") {
        serial.writeLine("done")
        basic.showIcon(IconNames.Happy)
    }
})
input.onButtonPressed(Button.AB, () => {
    measuring = false
    radio.sendValue("done", 0)
    basic.showIcon(IconNames.Happy)
})
input.onButtonPressed(Button.A, () => {
    measuring = true
    basic.showIcon(IconNames.Heart)
})
input.onButtonPressed(Button.B, () => {
    measuring = false
    basic.showIcon(IconNames.Yes)
})
function capture_data()  {
    X_Accel = input.acceleration(Dimension.X)
    Y_Accel = input.acceleration(Dimension.Y)
    Z_Accel = input.acceleration(Dimension.Z)
    radio.sendValue("x", X_Accel)
    radio.sendValue("y", Y_Accel)
    radio.sendValue("z", Z_Accel)
}
function write_data()  {
    serial.writeLine("" + X_Accel + "," + Y_Accel + "," + Z_Accel)
}
radio.setGroup(1)
radio.setTransmitPower(7)
basic.showIcon(IconNames.Yes)
basic.forever(() => {
    if (measuring) {
        capture_data()
        basic.pause(200)
    }
})
```

## Python Code
Below is a copy of the base code as well as the completed code for Python programmers. The answers are available as a reference, but you should attempt to complete the code without looking at the answers. There are multiple correct answers and the code below is simply a suggestion. 

### Base Code
```
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
```

### Completed Code
```
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
    radio.send()
    radio.send("y"+str(y_Accel))
    radio.send("z"+str(z_Accel))
    #x_Accel = accelerometer.get_x()
    #y_Accel = accelerometer.get_y()
    #z_Accel = accelerometer.get_z()
    #radio.send(str(x_Accel) + ',' + str(y_Accel) + ',' + str(z_Accel))
    
        
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
```







