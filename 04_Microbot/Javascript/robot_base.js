//NEED TO UPDATE
let radioGroup = 0
let groupSet = 0
input.onButtonPressed(Button.AB, () => {
    // If groupSet is not equal to 1

        // Set groupSet to 1

        // Set the radio group to radioGroup (radio.setGroup(radioGroup))
})
input.onButtonPressed(Button.A, () => {
    // If groupSet is not equal to 1 AND radioGroup is greater than 0

        // Decrement radioGroup by 1 (radioGroup-1)
})
radio.onDataPacketReceived( ({ receivedString: remoteString }) =>  {
    if (remoteString == "forward") {
        // NOTE - The code below sets the motor speed of the left motor to forward 100%
        motobit.setMotorSpeed(Motor.Left, MotorDirection.Forward, 100)
        // Set the motor speed of the right motor to forward 100%

        // Show an up arrow on the display (see the code for stop sign below)

        basic.pause(200)
    } else if (remoteString == "stop") {
        // Set the motor speed of the left motor to forward 0%

        // Set the motor speed of the right motor to forward 0%

        basic.showLeds(`
            . # # # .
            # . . # #
            # . # . #
            # # . . #
            . # # # .
            `)
        basic.pause(200)
    } else if (remoteString == "left") {
        // Set the motor speed of the left motor to reverse 100%

        // Set the motor speed of the right motor to forward 100%

        // Show a left arrow on the display

        basic.pause(200)
    } else if (remoteString == "right") {
        // Set the motor speed of the left motor forward 100%

        // Set the motor speed of the right motor to reverse 100%

        // Show a right arrow on the display

        basic.pause(200)
    }
})
input.onButtonPressed(Button.B, () => {
    // If groupSet is not equal to 1 AND radioGroup is less than 255

        // Increment radioGroup by 1 (radioGroup+!)

})
while (groupSet != 1) {
    basic.showNumber(radioGroup)
}
basic.showIcon(IconNames.Happy)
basic.pause(100)
basic.showNumber(radioGroup)
motobit.enable(MotorPower.On)
