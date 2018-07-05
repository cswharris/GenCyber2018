let send_string = ""
input.onButtonPressed(Button.B, () => {
    led.plotBrightness(send_string.length % 5,  send_string.length / 5, 5)
    send_string = "" + send_string + "0"
})
input.onButtonPressed(Button.A, () => {
    led.plotBrightness(send_string.length % 5,  send_string.length / 5, 255)
    send_string = "" + send_string + "1"
})
input.onButtonPressed(Button.AB, () => {
    led.setBrightness(led.brightness())
    radio.sendString(send_string)
    send_string = ""
    basic.showIcon(IconNames.StickFigure)
    basic.pause(200)
    basic.clearScreen()
})
radio.setGroup(1)
basic.showIcon(IconNames.Happy)
basic.pause(200)
basic.clearScreen()
basic.forever(() => {

})
