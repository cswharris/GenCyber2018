let channel = 0
let id = 0
let index = 0
input.onButtonPressed(Button.A, () => {
    if (id < 10) {
        id = id + 1
    } else {
        id = 1
    }
    showLights()
})
input.onButtonPressed(Button.B, () => {
    if (channel < 10) {
        channel = channel + 1
    } else {
        channel = 1
    }
    radio.setGroup(channel)
    showLights()
})
function showLights()  {
    basic.clearScreen()
    for (let index = 0; index <= 9; index++) {
        if (id > index) {
            led.plot(index / 5, index % 5)
        }
    }
    for (let index = 0; index <= 9; index++) {
        if (channel > index) {
            led.plot(4 - index / 5, index % 5)
        }
    }
}
id = 1
channel = 1
radio.setGroup(channel)
showLights()
basic.forever(() => {
    radio.sendNumber(id)
    basic.pause(250)
})
