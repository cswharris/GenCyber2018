# Lockpick Activity Descriptions

## microbit-easy-lockbox.hex
The simplest of all activities. The A and B buttons on the lock will un/lock the door. You can also unlock wirelessly by sending the bit string "0101" over radio group one from a remote key. Opens with microbit-easy-key.hex

## microbit-hard-lockbox1.hex
Requires two wireless keys. First key("0101") must be sent over radio group 2, and then the second key("1001") must be sent over radio group 5. Should open with microbit-hard-key1.hex when you hit btnA then btnB

## microbit-hard-lockbox2.hex
This lockbox expects the key("100110") but advances its radio group by 1 every 15 seconds. Good luck catching it. Should open with microbit-hard-key2.hex, after a few seconds the code is sent to the correct group after broadcasting to every channel.
