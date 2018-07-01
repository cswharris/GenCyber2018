let list: number[] = []
let found = false
let group = 0
radio.onDataPacketReceived( ({ signal, receivedNumber }) =>  {
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
})
input.onButtonPressed(Button.A, () => {
    if (group > 0) {
        group = group - 1
        radio.setGroup(group)
    }
    basic.showNumber(group)
})
input.onButtonPressed(Button.B, () => {
    if (group < 9) {
        group = group + 1
        radio.setGroup(group)
    }
    basic.showNumber(group)
})
radio.setGroup(1)
basic.showIcon(IconNames.Diamond)
group = 1
