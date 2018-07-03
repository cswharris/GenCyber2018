let position = 0
let state = 0
radio.onDataPacketReceived( ({ receivedString }) =>  {
    if (receivedString == "100110") {
        if (position == 160) {
            position = 20
        } else {
            position = 160
        }
        pins.servoWritePin(AnalogPin.P16, position)
        basic.showIcon(IconNames.Heart)
    } else {
        state = 0
        basic.showIcon(IconNames.Sad)
    }
})
state = 1
radio.setGroup(1)
position = 20
pins.digitalWritePin(DigitalPin.P16, position)
basic.showIcon(IconNames.No)
basic.forever(() => {
    basic.pause(15000)
    if (state == 99) {
        radio.setGroup(1)
    } else {
        state = state + 1
        radio.setGroup(state)
    }
})
