let radioGroup = 0
let groupSet = 0
input.onButtonPressed(Button.AB, () => {
    if (groupSet != 1) {
        groupSet = 1
        radio.setGroup(radioGroup)
    }
})
radio.onDataPacketReceived( ({ receivedString: remoteString }) =>  {
    if (remoteString == "forward") {
        motobit.setMotorSpeed(Motor.Left, MotorDirection.Forward, 100)
        motobit.setMotorSpeed(Motor.Right, MotorDirection.Forward, 100)
        basic.showLeds(`
            . . # . .
            . # # # .
            # . # . #
            . . # . .
            . . # . .
            `)
        basic.pause(200)
        motobit.setMotorSpeed(Motor.Left, MotorDirection.Forward, 0)
        motobit.setMotorSpeed(Motor.Right, MotorDirection.Forward, 0)
    } else if (remoteString == "left") {
        motobit.setMotorSpeed(Motor.Left, MotorDirection.Reverse, 50)
        motobit.setMotorSpeed(Motor.Right, MotorDirection.Forward, 50)
        basic.showLeds(`
            . . # . .
            . # . . .
            # # # # #
            . # . . .
            . . # . .
            `)
        basic.pause(200)
        motobit.setMotorSpeed(Motor.Left, MotorDirection.Forward, 0)
        motobit.setMotorSpeed(Motor.Right, MotorDirection.Forward, 0)
    } else if (remoteString == "right") {
        motobit.setMotorSpeed(Motor.Left, MotorDirection.Forward, 50)
        motobit.setMotorSpeed(Motor.Right, MotorDirection.Reverse, 50)
        basic.showLeds(`
            . . # . .
            . . . # .
            # # # # #
            . . . # .
            . . # . .
            `)
        basic.pause(200)
        motobit.setMotorSpeed(Motor.Left, MotorDirection.Forward, 0)
        motobit.setMotorSpeed(Motor.Right, MotorDirection.Forward, 0)
    } else {

    }
})
input.onButtonPressed(Button.A, () => {
    if (groupSet != 1 && radioGroup > 0) {
        radioGroup = radioGroup - 1
    }
})
input.onButtonPressed(Button.B, () => {
    if (groupSet != 1 && radioGroup < 255) {
        radioGroup = radioGroup + 1
    }
})
while (groupSet != 1) {
    basic.showNumber(radioGroup)
}
basic.showIcon(IconNames.Happy)
basic.pause(100)
basic.showNumber(radioGroup)
motobit.enable(MotorPower.On)
