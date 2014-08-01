#CTA L-Train Arrival Time Display Device (Powered by Arduino Yun)

Code and instructions for making an [Arduino Yun](http://arduino.cc/en/Main/ArduinoBoardYun)-based device that shows train arrival times for your favorite [CTA](http://www.transitchicago.com/) train stop.  Push the button, and live train arrival times are displayed on the LCD.

A Python script uploaded to the Linux side of the Yun queries the [CTA Train Tracker API](http://www.transitchicago.com/developers/traintracker.aspx) and returns results to the Arduino sketch in a ready-to-display format.

Here's what this looks like wired to a breadboard:

![Breadboarded prototype](https://raw.githubusercontent.com/gbuesing/yun-cta-train-status/master/images/prototype.jpg)

To finish the project, I plan to solder the circuit to a protoshield and place in an enclosure which I can mount next to the front door.


##Parts Needed

- Arduino Yun
- micro-USB power supply for Yun
- Backlit 16x2 LCD screen, with headers soldered on for breadboarding
- Potentiometer (for adjusting LCD screen contrast)
- [3x4 Matrix Keypad](https://www.adafruit.com/product/419)
- Tiny breadboard
- [Enclosure](https://www.adafruit.com/products/271)


##Assembly Steps

1. [Apply for a CTA Train Tracker API Developer Key](http://www.transitchicago.com/developers/traintrackerapply.aspx). Approval may take a day or two.

2. Ensure Yun is set up so that it can reach Wifi, and that the time zone is set to "America/Chicago" in the configuration.

3. Upload cta.py script to Linux side of Yun via SCP: 

    ```scp cta.py root@arduino.local:/root``` 

4. SSH into Yun: 

    ```ssh root@arduino.local``` 

    and install the python-expat library:

    ```
    opkg update
    opkg install python-expat
    ```

5. Copy constants.h.sample file in this repo to constants.h, and set ```CTA_API_KEY``` constant to your developer key.

6. Find your stop in the [Stop List Quick Reference Zipfile](http://www.transitchicago.com/developers/ttdocs/#_Toc296199909). Unzip and look in cta_L_stops.csv for the stop id (in the leftmost column) that corresponds to your station, train line and direction of travel.  Set ```CTA_STOP_ID``` in constants.h to this ID.

7. Set ```CTA_STOP_NAME``` in constants.h to a short (16 chars or less) description of your stop for display on the LCD, e.g. "Brown Ln to Loop"

8. Add parts to the breadboard and wire up -- see the Breadboard Wiring Diagram below. If you wish to use different pins on the Arduino, just change the default pins specified in constants.h.

9. Upload the sketch to the Yun. The LCD should light up and display the message "Starting..." for a second or two.

10. Once the start message disappears, push the button. The LCD will light up, the train station name will appear in the first row, and after a second, the train times on the second row. 

After five seconds, the LCD backlight will turn off and the screen will be cleared. You can push the button again to query anew.


##Wiring Diagram

![Wiring diagram](https://raw.githubusercontent.com/gbuesing/yun-cta-train-status/master/images/wiring.png)


## License

MIT
