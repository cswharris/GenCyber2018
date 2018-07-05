let state = 0
let position = 0
radio.onDataPacketReceived( ({ receivedString }) =>  {
    if (state == 0) {
        if (receivedString == "0101") {
            state = 1
            radio.setGroup(5)
            basic.showIcon(IconNames.Yes)
        } else {
            basic.showIcon(IconNames.Sad)
        }
    } else if (state == 1) {
        if (receivedString == "1001") {
            state = 0
            radio.setGroup(2)
            if (position == 160) {
                position = 20
            } else {
                position = 160
            }
            pins.servoWritePin(AnalogPin.P16, position)
            basic.showIcon(IconNames.Heart)
        } else {
            state = 0
            radio.setGroup(2)
            basic.showIcon(IconNames.Sad)
        }
    }
})
radio.setGroup(2)
position = 20
pins.digitalWritePin(DigitalPin.P16, position)
basic.showIcon(IconNames.No)
