import xbmcgui
import xbmc
import sys
import time
sys.path.append('/storage/.kodi/addons/virtual.rpi-tools/lib')

import RPi.GPIO as GPIO

# Set pin number once
RELAY_PIN = 18

GPIO.setmode(GPIO.BCM)

GPIO.setup(RELAY_PIN, GPIO.OUT)


while True:
# sleep for some time to reduce CPU usage
    time.sleep(1)
# read the current state of the pin
    current_state = GPIO.input(RELAY_PIN)
    ssaver_state = xbmc.getCondVisibility("System.ScreenSaverActive")
    if ssaver_state == True:
        # Screensaver is on so we should turn off the relay
        GPIO.output(RELAY_PIN, GPIO.HIGH)
        state = "off"
    else:
        # Screensaver is off so we should turn on the relay
        GPIO.output(RELAY_PIN, GPIO.LOW)
        state = "on"
        # Send notification
        # xbmcgui.Dialog().notification("Relay", "Amplifier is now {0}!".format(state))
