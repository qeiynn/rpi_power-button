#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import subprocess

# Define the GPIO pin for the button
BUTTON_PIN = 3

# Rpi shutdown funtion
def shutdown():
    subprocess.run(['shutdown', '-h', 'now'], shell=False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    GPIO.wait_for_edge(BUTTON_PIN, GPIO.FALLING)
    time.sleep(2)   # if button is still pressed after 2 secs, rpi will shutdown
    if GPIO.input(BUTTON_PIN) == 0:
        break

GPIO.cleanup()
shutdown()
