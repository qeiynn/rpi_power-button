#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import subprocess

def Shutdown():
    subprocess.call(['shutdown', '-h', 'now'], shell=False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    GPIO.wait_for_edge(3, GPIO.FALLING, bouncetime=1500)
    #sleep and check button again (in case of accidental button press)
    time.sleep(2)
    if GPIO.input(3) == 0:
        break
Shutdown()
