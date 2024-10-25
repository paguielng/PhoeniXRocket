########################################
#### BerryRocket ####
# On-board code for BR Micro-Avionic
# Louis Barbier
# MIT License
########################################

import time
from machine import Pin, I2C, PWM

from lib.buzzer import Buzzer
from lib.bmp180 import BMP180
from lib.mpu6050 import *
from lib.lps22hb import LPS22HB
from lib.lsm6dsx import LSM6DSx

#### Initialisation
# Buzzer
buzzer = Buzzer(0)
# I2C connection
i2c = I2C(0, sda=Pin(4), scl=Pin(5), freq=400000)

### /!\ Select your version of the board (comment baro/imu accordingly) /!\
## Version BR Micro-Sensor (black sensor board)
# baro = LPS22HB(i2c) # Barometer
# imu = LSM6DSx(i2c, 0x6B) # IMU 
## Version GY87/HW290
baro = BMP180(i2c) # Barometer
imu = MPU6050(bus=0, sda=Pin(4), scl=Pin(5), freq=400000, gyro=GYRO_FS_2000, accel=ACCEL_FS_16) # IMU

# Variables
launch_detected = False

# 3 bip buzzer to indicate end of initialisation
buzzer.set(freq=800, period=0.2)
time.sleep(0.6)
buzzer.unset()

# Set repeating buzzer to 2 seconds
buzzer.set(freq=1000, period=2)

# Infinite loop
while True:
    # Get time in second
    timetag = time.ticks_ms()/1000.0

    # Read sensor values
    pressure = baro.pressure
    temperature = baro.temperature
    ax, ay, az, gx, gy, gz = imu.data

    # Create one line with revelant values from sensors
    relevant_data = "Time: {:.2f} s | AccY: {:.2f} g | Baro: {:.2f} mBar | Temperature: {:.2f} dC".format(timetag, ay, pressure, temperature)

    # Detection of take-off if acceleration of Y axis is greater than 2 g
    if ay > 2 and launch_detected is False:
          launch_detected = True
          buzzer.set(freq=1500, period=0.5)
          relevant_data = "Takeoff detected, start recording...\n" + relevant_data
    
    # Write data to file after take-off
    if launch_detected == True:
        with open('data.txt', 'a') as fp:
            fp.write(relevant_data + "\r\n")

    # Print data in terminal (optional, can be ommited to speed up the program)
    print(relevant_data + "\r\n")

    # Slow down the program to have 0.1s between each cycle
    while ((time.ticks_ms()/1000.0 - timetag) < 0.1):
        next
