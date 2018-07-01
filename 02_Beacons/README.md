# Project Beacon Locators
## Files
* JavaScript/Beacon.js - The only beacon needed to run all of the receivers. Even the Python receivers use this beacon.
* JavaScript/Receiver-0-Standard.js, Python/Receiver-0-Standard.py - The basic receiver which scans for a single beacon on a single group.
* JavaScript/Receiver-1-Counter.js, Python/Receiver-1-Counter.py - A receiver built from the standard receiver, however it counts the number of beacons found on a single group.
* JavaScript/Receiver-2-Tuneable.js, JavaScript/Receiver-2-Tunable.py - A receiver built from the counter receiver, however it counts the number of beacons found on multiple groups.

### How To Run Beacon
1) The beacon displays the id (1-10) on the two left-most columns. If 3 LEDs are lit, the id for that beacon is 3. You can set the id using the A button. *Each beacon must have a unique id.*

2) The beacon displays the group (1-10) on the two right-most columns. If 3 LEDs are lit, the group for that beacon is 3. You can set the group using the B button.

3) The beacon outputs it's id repeatedly and must be connected to a constant power source.
