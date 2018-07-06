let concatIndex = ""
let index = 0
let scan = false
let counter = 0
let array: string[] = []
input.onButtonPressed(Button.A, () => {
    if (scan) {
        if (index > 0) {
            index = index - 1
            radio.setGroup(index)
        }
    } else {
        scan = true
    }
    basic.showNumber(index)
})
input.onButtonPressed(Button.B, () => {
    if (scan) {
        if (index <= 255) {
            index = index + 1
            radio.setGroup(index)
        }
    } else {
        scan = true
    }
    basic.showNumber(index)
})
radio.onDataPacketReceived( ({ receivedString }) =>  {
    basic.showIcon(IconNames.Yes)
    basic.pause(50)
    basic.showNumber(index)
    if (index < 10) {
        concatIndex = "0" + index
        array.insertAt(counter, "" + concatIndex + receivedString)
        counter = counter + 1
    } else {
        array.insertAt(counter, "" + index + receivedString)
        counter = counter + 1
    }
})
input.onButtonPressed(Button.AB, () => {
    basic.clearScreen()
    if (scan) {
        scan = false
        basic.showIcon(IconNames.Skull)
        for (let i = 0; i < 5; i++) {
            for (let value of array) {
                radio.setGroup(parseInt(value.substr(0, 2)))
                radio.sendString(value.substr(2, value.length - 2))
                basic.pause(25)
            }
        }
        basic.showIcon(IconNames.Heart)
    } else {
        scan = true
        index = 0
        radio.setGroup(0)
        basic.showNumber(index)
    }
})
array = []
counter = 0
index = 0
scan = true
radio.setGroup(0)
basic.showNumber(index)
basic.forever(() => {

})
