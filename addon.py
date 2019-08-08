import xbmcgui
import xbmc
import sys
sys.path.append('/storage/.kodi/addons/virtual.rpi-tools/lib')

import RPi.GPIO as GPIO

# Set pin number once
RELAY_PIN = 18

GPIO.setmode(GPIO.BCM)

GPIO.setup(RELAY_PIN, GPIO.OUT)

# read the current state of the pin
current_state = GPIO.input(RELAY_PIN)

if current_state == GPIO.HIGH:

    # Pin is on so we should turn off
    GPIO.output(RELAY_PIN, GPIO.LOW)
    state = "off"

else:

    # Pin is off so we should turn on
    GPIO.output(RELAY_PIN, GPIO.HIGH)
    state = "on"

# Send notification
xbmcgui.Dialog().notification("Relay", "Relay is now {0}!".format(state))
