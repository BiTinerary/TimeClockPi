#!/usr/bin/env python
# -*- coding: utf8 -*-

import OPi.GPIO as GPIO
from OPiZ.MFRC522 import MFRC522
import threading, signal, time, os

continue_reading = True

def osThread(hashie, uidFull):
	os.system('%s' % hashie[uidFull])

# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    print "\nCtrl+C captured, ending read."
    continue_reading = False
    GPIO.cleanup()

# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()

# Welcome message
print "\nWelcome to the MFRC522 data read example"

# This loop keeps checking for chips. If one is near it will get the UID and authenticate
while continue_reading:
    
    # Scan for cards    
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # If a card is found
    if status == MIFAREReader.MI_OK:
        print "Card detected"
    
    # Get the UID of the card
    (status,uid) = MIFAREReader.MFRC522_Anticoll()

    # If we have the UID, continue
    if status == MIFAREReader.MI_OK:

        # Print UID
	uidFull = "%s-%s-%s-%s" % (uid[0], uid[1], uid[2], uid[3])
        #print "Card read UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3])
	
	hashie = {}
	with open('hashFile.txt') as file:
		for line in file:
			key, value = line.split(',')
			print key, value,
			hashie[key] = value
	
	if uidFull in hashie:
		print uidFull
		
		osCommand = threading.thread(target=osThread, args=[hashie, uidFull])
		osCommand.start()
		#osThread(hashie, uidFull)
		#os.system('%s' % hashie[uidFull])
	else:
		print "UID: %s is not associated with a trigger" % uidFull
	
	os.system('echo "heartbeat" > /sys/class/leds/red_led/trigger')
	
        # This is the default key for authentication
        key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
        
        # Select the scanned tag
        MIFAREReader.MFRC522_SelectTag(uid)

        # Authenticate
        status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, 8, key, uid)

        # Check if authenticated
        if status == MIFAREReader.MI_OK:
            MIFAREReader.MFRC522_Read(8)
            MIFAREReader.MFRC522_StopCrypto1()
	    time.sleep(2)
	    os.system('echo 0 > /sys/class/leds/red_led/brightness')
	else:
            print "Authentication error"
