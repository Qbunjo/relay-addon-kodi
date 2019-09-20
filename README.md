This is a simple RPi Libreelec addon to control the relay and turn on the amplifier when needed. Now the amplifier turns on when the screensaver goes off. 
To get this script working you have to install rpi-tools plugin from libreelec repo. Also, it is necessary to add this script to the autoexec.py to allow automatic startup.

Forked from gabrielmdc (thanks!)
The script was slightly changed to meet my requirements.
Below you can find information from the author.

Relay kodi addon
===================
__This repository is obsolete in favor of this [script.service.relay](https://github.com/nearlg/script.service.relay)__

This addon allow you to switch a relay status, (turn on or turn off)

----------


Installation
-------------

Just download the [ZIP](https://github.com/nearlg/relay-addon-kodi/archive/master.zip) , and install it using Kodi plugin installer.

Configuration
-------------
It use by default the GPIO port 18, where the relay is connected, but you can change it in the file *relay.sh* 
	
	GPIOPORT=18
