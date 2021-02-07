""" EE 250L Lab 02: GrovePi Sensors

List team members here.

Insert Github repository link here.
"""

"""python3 interpreters in Ubuntu (and other linux distros) will look in a 
default set of directories for modules when a program tries to `import` one. 
Examples of some default directories are (but not limited to):
  /usr/lib/python3.5
  /usr/local/lib/python3.5/dist-packages

The `sys` module, however, is a builtin that is written in and compiled in C for
performance. Because of this, you will not find this in the default directories.
"""
import sys
import time
# By appending the folder of all the GrovePi libraries to the system path here,
# we are successfully `import grovepi`
sys.path.append('/home/ee250/Desktop/lab02-mabdulwa/Software/Python/')
# This append is to support importing the LCD library.
sys.path.append('/home/ee250/Desktop/lab02-mabdulwa/Software/Python/grove_rgb_lcd')

import grovepi
from grove_rgb_lcd import *


"""This if-statement checks if you are running this python file directly. That 
is, if you run `python3 grovepi_sensors.py` in terminal, this if-statement will 
be true"""
if __name__ == '__main__':
    ultrasonicPort = 4    # ultrasonic is connected to port D4.
    potentiometer = 0     # Rotary Angle Sensor connected to A0.

    grovepi.pinMode(ultrasonicPort,"INPUT")
    grovepi.pinMode(potentiometer,"INPUT")
    time.sleep(1)


    while True:
        #So we do not poll the sensors too quickly which may introduce noise,
        #sleep for a reasonable time of 200ms between each iteration.
        time.sleep(0.5)

        print(grovepi.ultrasonicRead(ultrasonicPort))

        # Read sensor value from potentiometer
        sensor_value = str(grovepi.analogRead(potentiometer))
        setText(sensor_value)

        
        ultrasonicValue = str(grovepi.ultrasonicRead(ultrasonicPort))
        setText("\n" + ultrasonicValue)
