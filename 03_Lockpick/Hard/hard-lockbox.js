let position = 0
let state = 1
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
        basic.showIcon(IconNames.Sad)
    }
})
radio.setGroup(state)
position = 20
pins.digitalWritePin(DigitalPin.P16, position)
basic.showIcon(IconNames.No)
basic.forever(() => {
    basic.pause(10000)
    if (state == 99) {
        state=0
    } else {
        state = state + 1
    }
    radio.setGroup(state)
})
