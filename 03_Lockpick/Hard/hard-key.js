let state = 0
state = 50
radio.setGroup(state)
basic.showIcon(IconNames.Heart)
basic.forever(() => {
    basic.pause(100)
    radio.sendString("100110")
    if (state == 1) {
        radio.setGroup(99)
    } else {
        state = state - 1
        radio.setGroup(state)
    }
})
