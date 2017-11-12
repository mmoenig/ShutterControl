# ShutterControl 1.0
Commandline tool written in Python to control jarolift shutters by using an 8-channel remote control via the the raspberry pi's io ports.

## Hardware requirements
Raspberry Pi board (http://www.raspberrypi.org/)

8-channel remote control for shutters 
(https://www.jalousiescout.de/Funktechnik-/-Funksteuerung/Auswahl-nach-Hersteller/Jarolift/Jarolift-Funkwandsender-TDRC-08W.html)

## Software requirements
**Raspbian installed on your Raspberry Pi** (http://raspbian.org/)

**Updating the apt Repo to have the latest versions**
```
sudo apt-get update
```
**Update the apt Repo to have the latest versions**
```
sudo apt-get update
```
**Install the latest git client**
```
sudo apt-get install git
```
**Install the latest python gpio modules**
```
sudo apt-get install python-rpi.gpio python3-rpi.gpio
```
**Load the ShutterControl Script**
```
git clone https://github.com/mmoenig/ShutterControl.git
```
## Usage
**You can use the ShutterControl command line tool by typing**
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

## Examples
Shutter channel 3 move down
```
python ShutterControl.py 3 3
```
Shutter channel 6 move up
```
python ShutterControl.py 6 1
```
