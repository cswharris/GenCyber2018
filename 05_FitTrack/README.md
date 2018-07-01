# Project Fitness Tracker
## Files
* Javascript/fitTrack.js, Python/fitrack.py - acts as the fitness tracker and receiver of data
* serial_reader.py - run this script to capture the data from the microbit and write out to a file

### How To Run The Fitness Tracker
0) Helpful tools: https://makecode.microbit.org/device/serial

1) Designate 1 microbit as the receiver and 1 as the fitness tracker, both will have the same program written to them. However, one must be plugged into the computer to receive the data.

2) A checkmark will appear to show the microbits are ready.

3) Double click on serial_reader.py or use the following chrome extension: https://chrome.google.com/webstore/detail/serial-monitor/ohncdkkhephpakbbecnkclhjkmbjnmlo?hl=en

If you are using the chrome extension, launch the app and select the appropriate COM port (if you only have one device plugged in there will only be one option). Select a Baud Rate of 115200 and click on connect.

4) To start gathering data, hit the A button on the fitness tracker and a heart will appear.

5) To stop gathering data, hit the B button on the fitness tracker and the checkmark will reappear. 

6) When you are done sending data, hit the A and B buttons at the same time to finish and a happy face will appear. 

7) If you used serial_reader.py, a graph of the data will automatically plot. If you used the chrome extension, continue to step 8. 

8) Copy and paste the data from chrome to Excel or Google Spreadsheets (select comma-separated when you paste the numbers). 

9) Obtain the total acceleration for each row. This is calculated by squaring each value and taking the square root of the sum. In other words, in cell D1, paste this:

```
=SQRT((A1)^2+(B1)^2+(C1)^2)
```

Then, click on the bottom right corner of D1 and drag down to the bottom of your data. This will make this calculation for each row.

10) To graph the data, highlight the D column and click on the graph button. Some adjustments can be made to make the data easier to read, but the data should be self-explanatory. 