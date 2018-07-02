let found = 0
let list: number[] = []
let strongest = 0
let beacon_id = 0
let already_found = false
let scanned = false
let index = 0
let id = 0
radio.onDataPacketReceived( ({ signal, receivedNumber: received_number }) =>  {
    if (!(scanned)) {
        if (strongest < signal) {
            already_found = false
            for (let index = 0; index <= list.length; index++) {
                if (list[index] == received_number + 1) {
                    already_found = true
                }
            }
            if (!(already_found)) {
                strongest = signal
                beacon_id = received_number
            }
        }
    } else {
        if (signal > -60) {
            basic.showIcon(IconNames.Yes)
            beacon_id = 999
            list.insertAt(found, received_number + 1)
            found = found + 1
            strongest = -128
            scanned = false
        } else if (signal > -65) {
            basic.showLeds(`
                . # # # .
                # # # # #
                # # # # #
                # # # # #
                . # # # .
                `)
        } else if (signal > -75) {
            basic.showLeds(`
                . . # . .
                . # # # .
                # # # # #
                . # # # .
                . . # . .
                `)
        } else if (signal > -95) {
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
function set_id()  {
    if (!(scanned)) {
        for (let id = 0; id <= 9; id++) {
            already_found = false
            for (let index = 0; index <= list.length; index++) {
                if (list[index] == id + 1) {
                    already_found = true
                }
            }
            if (!(already_found)) {
                radio.setGroup(id)
                basic.showNumber(id)
                basic.pause(200)
                basic.clearScreen()
            }
        }
        if (beacon_id != 999) {
            scanned = true
        }
    } else {
        radio.setGroup(beacon_id)
    }
}
index = 0
radio.setGroup(0)
scanned = false
id = 0
strongest = -128
found = 0
beacon_id = 999
basic.forever(() => {
    set_id()
})