let list: number[] = []
let found = false
let pauseRadio = false
let group = 0
radio.onDataPacketReceived(({ signal, receivedNumber }) => {
    if (!pauseRadio) {
        if (signal > -50) {
            basic.showIcon(IconNames.Yes)
            found = false
            for (let value of list) {
                if (value == receivedNumber) {
                    found = true
                }
            }
            if (!(found)) {
                list.push(receivedNumber)
                basic.showNumber(list.length)
            }
        } else if (signal > -60) {
            basic.showLeds(`
            . # # # .
            # # # # #
            # # # # #
            # # # # #
            . # # # .
            `)
        } else if (signal > -80) {
            basic.showLeds(`
            . . # . .
            . # # # .
            # # # # #
            . # # # .
            . . # . .
            `)
            basic.pause(300)
        } else if (signal > -120) {
            basic.showLeds(`
            . . . . .
            . . # . .
            . # # # .
            . . # . .
            . . . . .
            `)
        } else {
            basic.showLeds(`
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            `)
        }
    }

})
input.onButtonPressed(Button.A, () => {
    pauseRadio = true
    if (group > 0) {
        group = group - 1
    }
    radio.setGroup(group)
    basic.showNumber(group)
    basic.pause(1000)
    pauseRadio = false
})
input.onButtonPressed(Button.B, () => {
    pauseRadio = true
    if (group < 9) {
        group = group + 1
    }
    radio.setGroup(group)
    basic.showNumber(group)
    basic.pause(1000)
    pauseRadio = false
})
input.onPinPressed(TouchPin.P0, () => {
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
})
radio.setGroup(1)
basic.showIcon(IconNames.Diamond)
group = 1
