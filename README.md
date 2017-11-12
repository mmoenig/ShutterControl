# ShutterControl 1.0
Commandline tool written in Python to control jarolift shutters by using an 8-channel remote control via the the raspberry pi's io ports.

## Hardware requirements
Raspberry Pi board (http://www.raspberrypi.org/)

8-channel remote control for shutters 
(https://www.jalousiescout.de/Funktechnik-/-Funksteuerung/Auswahl-nach-Hersteller/Jarolift/Jarolift-Funkwandsender-TDRC-08W.html)

## Software requirements
Raspbian installed on your Raspberry Pi (http://raspbian.org/)

## Usage
You can use the ShutterControl command line tool by typing
```
python ShutterControl.py [channel] [command]
```
[channel] = Channel of the remote control you want to use
```
1-8
```
[command] = command you want to send over the selected channel
```
1 = drive up
2 = stop
3 = drive down
4 = drive to 3rd stopping position
```

## Example2
Shutter channel 3 move down
```
python ShutterControl.py 3 3
```
Shutter channel 6 move up
```
python ShutterControl.py 6 1
```
