//NEED TO UPDATE
let forward = 0
let groupSet = 0
let radioGroup = 0
input.onButtonPressed(Button.A, () => {
    if (groupSet == 0 && radioGroup > 0) {
        // Decrement radioGroup by 1 (radioGroup-1)

    } else {
        // Send "left" over radio (radio.sendString(...))

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
        // Set grouopSet to 1

        radio.setGroup(radioGroup)
        // Show a happy face on the display (IconNames.Happy)

        // Set forward to zero
    } else {
        if (forward == 0) {
            // Send "forward" over radio

            // Set forward to one

            basic.showLeds(`
                . . # . .
                . # # # .
                # . # . #
                . . # . .
                . . # . .
                `)
        } else {
            // Send "stop" over radio


            // Set forward to zero

            basic.showLeds(`
                . # # # .
                # . . # #
                # . # . #
                # # . . #
                . # # # .
                `)
        }
    }
})
input.onButtonPressed(Button.B, () => {
    if (groupSet == 0 && radioGroup < 255) {
        // Increment radioGroup by 1 (radioGroup+1)

    } else {
        // Send "right" over radio

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
