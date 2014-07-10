#Yun CTA Train Status

Code and instructions for making an [Arduino Yun](http://arduino.cc/en/Main/ArduinoBoardYun)-based device that shows train arrival times for your favorite [CTA](http://www.transitchicago.com/) train stop.  Push the button, and live train arrival times are displayed on the LCD.

A Python script uploaded to the Linux side of the Yun queries the [CTA Train Tracker API](http://www.transitchicago.com/developers/traintracker.aspx) and returns results to the Arduino sketch in a ready-to-display format.


##Parts Needed

- Arduino Yun
- micro-USB power supply for Yun
- Backlit 16x2 LCD screen, with headers soldered on for breadboarding
- Potentiometer (for adjusting LCD screen contrast)
- Button
- Breadboard and wires


##Assembly Steps

1. [Apply for a CTA Train Tracker API Developer Key](http://www.transitchicago.com/developers/traintrackerapply.aspx). Approval may take a day or two.

2. Ensure Yun is set up so that it can reach Wifi, and that the time zone is set to "America/Chicago" in the configuration.

3. Upload cta.py script to Linux side of Yun via SCP: ```scp cta.py root@yun.local:/root``` (use whatever local name you set your Yun up with).

4. Copy constants.h.sample to constants.h, and set CTA_API_KEY to your developer key.

5. Find your stop in the (Stop List Quick Reference Zipfile)[http://www.transitchicago.com/developers/ttdocs/#_Toc296199909]. Unzip and look in cta_L_stops.csv for the stop id (in the leftmost column) that corresponds to your station, train line and direction of travel.  Set CTA_STOP_ID in constants.h to this ID.

6. Set CTA_STOP_NAME in constants.h to a good, short (16 chars or less) description of your stop.

7. Add parts to the breadboard and wire up -- see the Breadboard Wiring Diagram below.

8. Upload the sketch to the Yun.

9. Once the "Starting..." message disappears, push the button. The LCD will light up, the train station name will appear in the first row, and after a second, the train times on the second row. After five seconds, the LCD backlight will turn off. You can push the button again to query anew.



##Breadboard Wiring Diagram

![Breadboard wiring diagram](https://raw.githubusercontent.com/gbuesing/yun-cta-train-status/master/breadboard-wiring.png)