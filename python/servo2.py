#!/usr/bin/python
#--------------------------------------
#    ___  ___  _ ____
#   / _ \/ _ \(_) __/__  __ __
#  / , _/ ___/ /\ \/ _ \/ // /
# /_/|_/_/  /_/___/ .__/\_, /
#                /_/   /___/
#
#           servo2.py
# Basic example script to control a servo
# connected to GPIO17 using the Gpiozero library.
# Allows tweaking of pulse widths to get the full
# range of movement.
#
# Use CTRL-C to break out of While loop.
#
# Author : Matt Hawkins
# Date   : 19/12/2017
#
# http://www.raspberrypi-spy.co.uk/tag/dht11/
#
#--------------------------------------
from gpiozero import Servo
from time import sleep

myGPIO=17

# Min and Max pulse widths converted into milliseconds
# To increase range of movement:
#   increase maxPW from default of 2
#   decrease minPW from default of 1
# Use increments of 0.05 and check values work with
# your servo.
maxPW=2.45/1000
minPW=0.55/1000

servo = Servo(myGPIO,min_pulse_width=minPW,max_pulse_width=maxPW)

while True:
    servo.mid()
    print("mid")
    sleep(0.5)
    servo.min()
    print("min")
    sleep(1)
    servo.mid()
    print("mid")
    sleep(0.5)
    servo.max()
    print("max")
    sleep(1)