let send_string = ""
input.onButtonPressed(Button.B, () => {
    send_string = "" + send_string + "0"
})
input.onButtonPressed(Button.A, () => {
    send_string = "" + send_string + "1"
})
input.onButtonPressed(Button.AB, () => {
    radio.sendString(send_string)
    send_string = ""
    basic.showIcon(IconNames.StickFigure)
})
radio.setGroup(1)
basic.showIcon(IconNames.Happy)
basic.forever(() => {
    basic.showString(send_string)
})
