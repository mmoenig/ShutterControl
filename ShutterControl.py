import time
import RPi.GPIO as GPIO
import sys

# RPi.GPIO Layout (use PIN numbers)
GPIO.setmode(GPIO.BOARD)

position = int(sys.argv[1])
function = int(sys.argv[2])

print("Shutter Channel [" + str(position) + "], Function [" + str(function) + "]")

##################################################################
##################### CUSTOMIZEABLE SETTINGS #####################
##################################################################
UP      = 37    #PIN 37
STOP    = 33    #PIN 33
DOWN    = 35    #PIN 35
CHANNEL = 31    #PIN 31
BLOCK   = 40    #PIN 40
PULSE   = 0.1   #Wait time between channel switch
PUSH    = 1.4   #transmission time for radio command 
CHANNELS= 8     #number of available remote channels (could be changed to 4 or 16 channels)
##################################################################
##################### CUSTOMIZEABLE SETTINGS #####################
##################################################################

# Setup Raspberry PINs ----------------------------------------
GPIO.setup(UP,      GPIO.OUT)
GPIO.setup(STOP,    GPIO.OUT)
GPIO.setup(DOWN,    GPIO.OUT)
GPIO.setup(CHANNEL, GPIO.OUT)
GPIO.setup(BLOCK,   GPIO.OUT)

# Send command to raspberry  ----------------------------------
def executeCommand(cmd):
    GPIO.output(cmd, GPIO.LOW)
    time.sleep(PULSE)
    GPIO.output(cmd, GPIO.HIGH)
    time.sleep(PUSH)
    GPIO.output(cmd, GPIO.LOW)

# CHECK if GPIOs are currently blocked  -----------------------
while GPIO.input(BLOCK) == GPIO.HIGH:
    time.sleep(0.5)
    print("GPIOs are currently blocked, wait.....")

# Block GPIOs for command execution ---------------------------
GPIO.output(BLOCK, GPIO.HIGH) 

# Switch to target channel starting from 1  ---------------------
for i in range(1, position):
    GPIO.output(CHANNEL, GPIO.HIGH)
    time.sleep(PULSE)
    GPIO.output(CHANNEL, GPIO.LOW)
    time.sleep(PULSE)

# Execute Shutter function  -------------------------------------
if function == 1:           # Drive up
    executeCommand(UP)
elif function == 2:         # Stop
    executeCommand(STOP)
elif function == 3:         # Drive down
    executeCommand(DOWN)
elif function == 4:         # Drive to 3rd stopping point
    GPIO.output(STOP, GPIO.LOW)
    time.sleep(PULSE)
    GPIO.output(STOP, GPIO.HIGH)
    time.sleep(3)
    GPIO.output(STOP, GPIO.LOW)
    
# Back to start position  (channel 1) ----------------------------
for i in range(position, CHANNELS + 1):
    GPIO.output(CHANNEL, GPIO.HIGH)
    time.sleep(PULSE)
    GPIO.output(CHANNEL, GPIO.LOW)
    time.sleep(PULSE)

# Remove GPIO Blocking -------------------------------------------
GPIO.output(BLOCK, GPIO.LOW)
GPIO.cleanup()