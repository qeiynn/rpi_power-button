# Rpi_Power-Button

Original script is from ZLevine -> 'https://github.com/Howchoo/pi-power-button'.

I modified it to require the button pressed for 2 seconds in order to shutdodwn. 
The idea is to avoid accidental button presses.

## Installation

1. [Connect to your Raspberry Pi via SSH]
1. Clone this repo: git clone https://github.com/qeiynn/Rpi_Power-Button.git
1. Inside folder run the setup script: sudo bash install

## Uninstallation

If you need to uninstall the power button script in order to use GPIO3 for another project or something:

1. Inside folder run the uninstall script: sudo bash uninstall

## Hardware

A full list of what you'll need can be found [here](https://howchoo.com/g/mwnlytk3zmm/how-to-add-a-power-button-to-your-raspberry-pi#parts-list). At a minimum, you'll need a normally-open (NO) power button, some jumper wires, and a soldering iron. If you _don't_ have a soldering iron or don't feel like breaking it out, you can use [this prebuilt button](https://howchoo.com/shop/product/prebuilt-raspberry-pi-power-button) instead.

Connect the power button to Pin 5 (SCL) and Pin 6 (GND) as shown in this diagram:

![Connection Diagram](https://raw.githubusercontent.com/Howchoo/pi-power-button/master/diagrams/pinout.png)
