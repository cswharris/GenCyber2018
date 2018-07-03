let groupSet = 0
let radioGroup = 0
input.onButtonPressed(Button.A, () => {
    if (groupSet == 0 && radioGroup > 0) {
        radioGroup = radioGroup - 1
    } else {
        radio.sendString("left")
        basic.showLeds(`
            . . # . .
            . # . . .
            # # # # #
            . # . . .
            . . # . .
            `)
    }
})
input.onButtonPressed(Button.AB, () => {
    if (groupSet == 0) {
        groupSet = 1
        radio.setGroup(radioGroup)
        basic.showIcon(IconNames.Happy)
    } else {
        radio.sendString("forward")
        basic.showLeds(`
            . . # . .
            . # # # .
            # . # . #
            . . # . .
            . . # . .
            `)
    }
})
input.onButtonPressed(Button.B, () => {
    if (groupSet == 0 && radioGroup < 255) {
        radioGroup = radioGroup + 1
    } else {
        radio.sendString("right")
        basic.showLeds(`
            . . # . .
            . . . # .
            # # # # #
            . . . # .
            . . # . .
            `)
    }
})
radioGroup = 0
while (groupSet != 1) {
    basic.showNumber(radioGroup)
}
basic.showIcon(IconNames.Happy)
basic.pause(100)
basic.showNumber(radioGroup)
