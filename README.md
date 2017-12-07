# TimeClockPi
A Google Sheets punching time clock. Made from an OrangePi Zero and MFRC522 module, running on Armbian.

![blinky2](https://user-images.githubusercontent.com/8212296/33339935-3d6bed48-d440-11e7-80fb-850be5dc8113.gif)
![sideby](https://user-images.githubusercontent.com/8212296/33340459-bd7858d6-d441-11e7-9e00-3e7ec3b27a79.jpg)

## Installation and Setup
`git clone https://github.com/BiTinerary/TimeClockPi && bash ./TimeClockPi/requirements.sh`

Installation assumes you're installing from a fresh Armbian installation. ie: the requirements script will prompt to set current time zone, installs basics like python-pip, etc...

After the requirements.sh has been run, all repos and dependencies will be installed. The main script which waits for an RFID badge to be scanned is also, concurrently executed. So if you have your MFRC522 module already hooked up to the proper pins, you are basically good to go. If not, and you are wondering how to setup each MFRC522 pin, reference the following guide which will be consolidated here, at a later date: https://github.com/BiTinerary/OrangePiZeroMFRC522

From here you still need to setup your badges/Google Sheets API. Change the UID variables in the `hashFile.txt` to match UID's of your own badges. Then also change the spreadsheet name in this same file, to the exact name of the spreadsheet being hosted on Google Drive.

Setup Google API credentials. Directions on this later. Copy/Paste the Google API .json file to the OpiZero. **Share the email address** listed in this file with the Google spreadsheet you want to edit.

## Requirements
* [OPi.GPIO](https://github.com/rm-hull/OPi.GPIO): A RPi.GPIO drop-in replacement library for OrangePi Zero
* [SPI-Py](https://github.com/lthiery/SPI-Py) Hardware SPI as a C Extension for Python
* [gspread](https://github.com/burnash/gspread): Google Spreadsheets Python API
* [oauth2client](https://github.com/google/oauth2client): ... for accessing resources protected by OAuth 2.0. (Google Sheets)
* [MFRC522-python](https://github.com/mxgxw/MFRC522-python) A small class to interface with the NFC reader Module MFRC522
  * Requires source code alteration if using original repository

All requirements are included in this repo with exception to `gspread` and `oauth2client`. You can get both using basic pip install. Some dependencies have been modified for this projects intented purpose. While others have remained untouched. Namely, the MFRC522 files have been altered to utilize `OPi.GPIO` for Orangepi Zero **instead** of default `RPi.GPIO` module for Raspi devices. As well as a change to the assigned spidev interface.

### Fitting In The Case
This project needed to be as simple looking as such a device can be. At the very least, not intimidating. This is a little bit of a catch seeing as how they don't make OPiZero cases to house both the board and an arbitrary MFRC522 module. So I purchased the following, more 'modular' case since it showed more promise for hacking it all together.

[Orange Pi Acrylic Case Transparent Box](https://www.amazon.com/gp/product/B073W8XCS3/ref=oh_aui_detailpage_o03_s00?ie=UTF8&psc=1): $5.99

**MFRC522 Modifications**  
You can see the orientation I chose in the pictures. I desoldered the red LED since I planned on using several others. Most noteworthy is the fact that I desoldered the 27.120 Crystal on the MFRC522 module and flipped it to the bottom side of the board. So that the RFID scanner would be flush with the top of the acrylic case. As result, closer to the RFID tag being passed over the sensor. I also desoldered the existing GPIO pins. Resoldered the male end of some jumper wire on the bottom of the board, at a 90degree angle, to continue to save on space. (more pictures of box dissassembled to come)

**LED Modifications**  
A three prong, multi-color (Red/Green) LED, with a common ground was added with resistors to two seperate GPIO's defined in the `blinky.py` script and mounted (using a Plastic LED Holder/Clip **similar** to [this](https://www.ebay.com/itm/50pcs-5mm-Plastic-LED-Holders-Clips-Bezels-Mounts-Cases-Housings-Black-New-S5-/281745445114)) into the 3.5MM hole in the case. Which was originally intended for the audio jack an expansion board available for the OPiZero

**Board Modifications**  
I actually removed the black, plastic casing around the main GPIO pins of the board. This doesn't have to be done but by removing the GPIO 'sleeve' I could easily continue to use jumper cables for connections, rather than permanently soldering or making alterations to board. Otherwise the plastic ends of the jumper cable we simply to long to accomodate within the available height.
