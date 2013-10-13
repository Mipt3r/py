#!/usr/bin/python
#--------------------------------------   
# This script reads data from a 
# MCP3008 ADC device using the SPI bus.
#
# Author : Matt Hawkins
# Date   : 13/10/2013
#
# http://www.raspberrypi-spy.co.uk/
#
#--------------------------------------

import spidev
import time
import os

# Open SPI bus
spi = spidev.SpiDev()
spi.open(0,0)

# Function to read SPI data from MCP3008 chip
# Channel must be an integer 0-7
def ReadChannel(channel):
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data

# Function to convert data to voltage level,
# rounded to specified number of decimal places. 
def ConvertVolts(data,places):
  volts = (data * 3.3) / 1023
  volts = round(volts,places)  
  return volts
  
# Function to calculate temperature from
# TMP36 data, rounded to specified
# number of decimal places.
def ConvertTemp(data,places):
  temp = ((data * 330)/1023)-50
  temp = round(temp,places)
  return temp
  
# Define sensor channels
light_channel = 0
temp_channel  = 1

# Define delay between readings
delay = 5

while True:

  # Read the light sensor data
  light_level = ReadChannel(light_channel)
  light_volts = ConvertVolts(light_level,2)

  # Read the temperature sensor data
  temp_level = ReadChannel(temp_channel)
  temp_volts = ConvertVolts(temp_level,2)
  temp       = ConvertTemp(temp_level,2)

  # Print out results
  print "--------------------------------------------"  
  print("Light : {} ({}V)".format(light_level, light_volts))  
  print("Temp  : {} ({}V) {} deg C".format(temp_level, temp_volts, temp))    
  #print "Light : " + str(light_level) + " (" + str(light_volts) + "V)"
  #print "Temp  : " + str(temp_level) + " (" + str(temp_volts) + "V) " + str(temp) + " degrees C" 

  # Wait before repeating loop
  time.sleep(delay)
 