#!/usr/bin/env python

import RPi.GPIO as GPIO
import os
#import subprocess
from time import sleep

gpio_pin_number=3

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(gpio_pin_number, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    GPIO.wait_for_edge(gpio_pin_number, GPIO.FALLING)
    #sleep and check button again (in case of accidental button press)
    time.sleep(2)
    if GPIO.input(gpio_pin_number) == 0:
        break
        
print("ta ta")
time.sleep(1)
os.system("sudo shutdown -h now")
