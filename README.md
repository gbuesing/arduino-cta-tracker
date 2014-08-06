#Arduino CTA Tracker

Code and instructions for making an [Arduino Yun](http://arduino.cc/en/Main/ArduinoBoardYun)-based device that shows arrival times for nearby [CTA](http://www.transitchicago.com/) train and bus stops on an LCD.

![Assembled and on](https://raw.githubusercontent.com/gbuesing/yun-cta-train-status/master/images/assembled_on.jpg)

Much easier to simply push a button, vs. pulling out my phone, unlocking, finding the Buster app, etc. I've got this device by the front door at home, so that I can time my exit.

Other keys return bus times, weather, current date & time, and a magic 8 ball. Each of the keys run a command line script on the Linux side of the Yun; the string returned on stdout is then displayed on the LCD. So, easy to expand this to return whatever data you find useful.


##Parts needed

- Arduino Yun
- micro-USB power supply for Yun
- Backlit 16x2 LCD screen, with headers soldered on
- Potentiometer (for adjusting LCD screen contrast)
- [3x4 Matrix Keypad](https://www.adafruit.com/product/419)
- Tiny breadboard
- Jumper wires
- [Adafruit Arduino Enclosure](https://www.adafruit.com/products/271)


##CTA API keys

You'll need a [CTA Train Tracker API Key](http://www.transitchicago.com/developers/traintrackerapply.aspx) and a [CTA Bus Tracker API Key](http://www.transitchicago.com/developers/bustracker.aspx). 

Approval for each of these may take a day or two.


## Uploading data scripts to the Yun

The scripts directory in this project contains python scripts for querying CTA train and bus apis, Yahoo weather, and a magic 8 ball. You'll need to upload these to the Linux side of the Yun:

1. Make sure the Yun is connected to Wifi, and that the time zone is set to "America/Chicago" in the configuration.

2. In the scripts directory, copy ```config.py.sample``` to ```config.py``` and add your CTA bus and train API keys.

3. Upload scripts directory to Linux side of Yun via SCP: 

    ```scp -r scripts/ root@arduino.local:/root``` 

4. SSH into Yun: 

    ```ssh root@arduino.local``` 

    and install the python-expat library:

    ```
    opkg update
    opkg install python-expat
    ```

5. While still SSH'd in, test the scripts to make sure they're working:

  ```
  # return times for Southbound Brown line at Irving Park
  python /root/scripts/cta_el.py '30282' 
  ```

  ```
  # return times for Southbound 50 bus at Irving Park
  python /root/scripts/cta_bus.py '50' '8827'
  ```

  To return times for different stops, you'll need the corresponding stop ids; check the comments inside ```cta_el.py``` and ```cta_bus.py``` for instructions.

  If the numbers returned seem excessively large, run ``date`` and confirm that it's returning the correct time in CST. Sometimes after booting up, it takes a minute for the clock to sync.


## Wiring it up

![Wiring diagram](https://raw.githubusercontent.com/gbuesing/yun-cta-train-status/master/images/wiring.png)


## Preparing the sketch and testing

1. Copy constants.h.sample file in this repo to constants.h.

2. In ```constants.h```, change the labels and commands for each key as desired. You'll want to replace stop ids used for ```cta_el.py``` and ```cta_bus.py``` commands to stops near you -- see the top of these files for how to get stop ids.

3. Upload the sketch to the Yun.

4. Wait for "Starting..." message to disappear, and then press a key. The LCD backlight will turn on; the label for the key should immediately appear on the first row, and the results returned from the command on the second row, which may take a second or two.

After five seconds, the LCD backlight will turn off and the screen will be cleared. You can push the button again to query anew.


## Finishing the device

I couldn't find a protoshield that would fit the Yun, so I just wired onto a tiny breadboard that sits on top of the Yun. The small jumper wires going from the breadboard to the Yun header pins keep it in place, so I didn't bother using the sticky on the back of the breadboard.

Note that I'm bending jumper cable pins off to the side, so that everything fits in the case.

![Opened](https://raw.githubusercontent.com/gbuesing/yun-cta-train-status/master/images/opened.jpg)

![Breadboard closeup](https://raw.githubusercontent.com/gbuesing/yun-cta-train-status/master/images/breadboard_closeup.jpg)

The wiring for the keypad is threaded through the opening in the enclosure behind it. The keypad is easily attached to the enclosure via the sticky on back.

![Assembled off](https://raw.githubusercontent.com/gbuesing/yun-cta-train-status/master/images/assembled_off.jpg)

The bottom panel of the enclose doesn't quite match the bottom of the Yun, so I just left it off.


## License

MIT
