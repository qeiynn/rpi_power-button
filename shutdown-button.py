#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import subprocess

gpio_pin_number=3
def Shutdown():
    print("Cowabunga!")
    time.sleep(1)
    subprocess.call(['shutdown', '-h', 'now'], shell=False)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(gpio_pin_number, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    GPIO.wait_for_edge(gpio_pin_number, GPIO.FALLING)
    #sleep and check button again (in case of accidental button press)
    time.sleep(2)
    if GPIO.input(gpio_pin_number) == 0:
        break
Shutdown()
