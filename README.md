# Rpi_Power-Button

Python script to safely turn-off the Raspi with a use of a button. The script is waiting for an interrupt in order to trigger. This saves some cpu resources as it isn't constantly watching the Pins.

The button must pressed for 2 seconds in order to shutdown. The purpose is to avoid shutdown by accidental button presses.

## Install

1. [Connect to your Raspberry Pi via SSH]
2. Clone this repo: git clone https://github.com/qeiynn/rpi_power-button.git
3. Inside folder run the setup script: sudo bash install

## Uninstall

If you need to uninstall the power button script in order to use GPIO3 for another project or something:

1. Inside folder run the uninstall script: sudo bash uninstall
2. Go back one directory and delete the folder. rm -r rpi_power-button 

## Hardware / Wiring

A normally-open (NO) push button is required.
Connect the power button to the GPIO's Pin 5 (SCL) and Pin 6 (GND).

```
40-Pin Layout - RPI 3b(+), 4, Zero (W)
    -        
· ·|·|· · · · · · · · · · · · · · · · · 
· ·|·|· · · · · · · · · · · · · · · · · 
    -       
(microSD input)
      (HDMI input)
```
