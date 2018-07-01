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
