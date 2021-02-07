from grovepi import *
from grove_rgb_lcd import *
from time import sleep
from math import isnan

dht_sensor_port = 7 # connect the DHt sensor to port 7
dht_sensor_type = 1 # use 0 for the blue-colored sensor and 1 for the white-colored sensor

# set green as backlight color
# we need to do it just once
# setting the backlight color once reduces the amount of data transfer over the I2C line
setRGB(0,255,0)

while True:
	try:
        # get the temperature and Humidity from the DHT sensor
		[ temp,hum ] = dht(dht_sensor_port,dht_sensor_type)		
		print("temp =", temp, "C\thumidity =", hum,"%")

		# check if we have nans
		# if so, then raise a type error exception
		if isnan(temp) is True or isnan(hum) is True:
			raise TypeError('nan error')