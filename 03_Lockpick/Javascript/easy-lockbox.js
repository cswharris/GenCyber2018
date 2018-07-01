let position = 0
input.onButtonPressed(Button.A, () => {
    basic.showString("A")
    position = 160
    pins.servoWritePin(AnalogPin.P16, position)
    basic.pause(100)
})
input.onButtonPressed(Button.B, () => {
    basic.showString("B")
    position = 20
    pins.servoWritePin(AnalogPin.P16, position)
    basic.pause(100)
})
radio.onDataPacketReceived(({ receivedString }) => {
    if (receivedString == "0101") {
        if (position == 95) {
            position = 5
        } else {
            position = 95
        }
        pins.servoWritePin(AnalogPin.P16, position)
    }
})
radio.setGroup(1)
position = 5
pins.digitalWritePin(DigitalPin.P16, position)
basic.showIcon(IconNames.No)