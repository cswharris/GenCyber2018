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
