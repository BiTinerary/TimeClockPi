# TimeClockPi
A Google Sheets punching time clock. Made from an OrangePi Zero and MFRC522 module, running on Armbian.

![blinky2](https://user-images.githubusercontent.com/8212296/33339935-3d6bed48-d440-11e7-80fb-850be5dc8113.gif)
![sideby](https://user-images.githubusercontent.com/8212296/33340459-bd7858d6-d441-11e7-9e00-3e7ec3b27a79.jpg)

## Installation
`git clone https://github.com/BiTinerary/TimeClockPi && bash ./TimeClockPi/requirements.sh`

Installation assumes you're installing from a fresh Armbian installation. ie: the requirements script will prompt to set current time zone, installs basics like python-pip, etc...

## Requirements
* [OPi.GPIO](https://github.com/rm-hull/OPi.GPIO): A RPi.GPIO drop-in replacement library for OrangePi Zero
* [SPI-Py](https://github.com/lthiery/SPI-Py) Hardware SPI as a C Extension for Python
* [gspread](https://github.com/burnash/gspread): Google Spreadsheets Python API
* [oauth2client](https://github.com/google/oauth2client): ... for accessing resources protected by OAuth 2.0. (Google Sheets)
* [MFRC522-python](https://github.com/mxgxw/MFRC522-python) A small class to interface with the NFC reader Module MFRC522
  * Requires source code alteration if using original repository

All requirements are included in this repo with exception to `gspread` and `oauth2client`. You can get both using basic pip install. Some dependencies have been modified for this projects intented purpose. While others have remained untouched. Namely, the MFRC522 files have been altered to utilize `OPi.GPIO` for Orangepi Zero **instead** of default `RPi.GPIO` module for Raspi devices. As well as a change to the assigned spidev interface.
