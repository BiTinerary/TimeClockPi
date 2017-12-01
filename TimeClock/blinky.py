import OPi.GPIO as GPIO
import time, os

def blink(color, times):
        def onboardLEDs(color):
                ledOn = os.system('echo 1 >/sys/class/leds/%s_led/brightness' % color)
                time.sleep(.1)
                ledOff = os.system('echo 0 >/sys/class/leds/%s_led/brightness' % color)
                time.sleep(.1)
        
        def gpioMultiLED(color):
                color = int(color)
                GPIO.setmode(GPIO.BOARD)
                GPIO.setup(color, GPIO.OUT)
                time.sleep(.2)
                GPIO.output(color, GPIO.HIGH)
                time.sleep(.2)
                GPIO.output(color, GPIO.LOW)
                GPIO.cleanup()

        for x in range(times):
                try:
                        if len(color) == 2:
                                for redGreen in color:
                                        onboardLEDs(redGreen)
                except:
                        gpioMultiLED(color)
