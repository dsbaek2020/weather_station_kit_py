#code by : daeseong, baek
# 2023.07.19
# scd-30 sensor interface
# Product information: https://www.adafruit.com/product/4867
# python library repository:  https://github.com/adafruit/Adafruit_CircuitPython_SCD30/tree/main

'''
SCD-30 Specifications:

NDIR CO2 sensor technology
Integrated temperature and humidity sensor
Dual-channel detection for superior stability
Measurement range: 400 ppm – 10,000 ppm
Accuracy: ±(30 ppm + 3%)
Current consumption: 19 mA @ 1 meas. per 2 s.
Fully calibrated and linearized
'''

#I2C digital interface address 0x61

import time
import board
import busio
import adafruit_scd30

# SCD-30 has tempremental I2C with clock stretching, datasheet recommends
# starting at 50KHz
i2c = busio.I2C(board.SCL, board.SDA, frequency=50000)
scd = adafruit_scd30.SCD30(i2c)


def read_all():
  return round(scd.CO2,1), round(scd.temperature,1), round(scd.relative_humidity,1)

'''
while True:
    # since the measurement interval is long (2+ seconds) we check for new data before reading
    # the values, to ensure current readings.
    if scd.data_available:
        print("Data Available!")
        print("CO2: %d PPM" % scd.CO2)
        print("Temperature: %0.2f degrees C" % scd.temperature)
        print("Humidity: %0.2f %% rH" % scd.relative_humidity)
        print("")
        print("Waiting for new data...")
        print("")

    time.sleep(0.5)
'''
