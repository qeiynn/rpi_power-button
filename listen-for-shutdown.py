#!/usr/bin/env python

import RPi.GPIO as GPIO
import subprocess
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.wait_for_edge(3, GPIO.FALLING)

#wait for 2 seconds to see if this was deliberate
sleep(2)
# check the button level again
if GPIO.input(3) == 0:
    subprocess.call(['shutdown', '-h', 'now'], shell=False)
