radio.onDataPacketReceived( ({ signal, receivedNumber }) =>  {
    if (signal > -50) {
        basic.showIcon(IconNames.Yes)
    } else if (signal > -60) {
        
    } else if (signal > -80) {
        
    } else if (signal > -120) {
        
    } else {
        
    }
})
radio.setGroup(1)
basic.showIcon(IconNames.Diamond)
