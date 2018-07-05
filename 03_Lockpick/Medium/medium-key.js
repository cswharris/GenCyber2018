let state = 0
input.onButtonPressed(Button.A, () => {
    radio.sendString("0101")
    radio.setGroup(5)
    basic.showIcon(IconNames.Yes)
})
input.onButtonPressed(Button.B, () => {
    radio.sendString("1001")
    radio.setGroup(2)
    basic.showIcon(IconNames.Chessboard)
})
state = 2
radio.setGroup(state)
basic.showIcon(IconNames.Heart)
