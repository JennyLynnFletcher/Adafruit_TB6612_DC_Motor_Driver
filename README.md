# Adafruit TB6612 DC Motor Driver

A small Python library for running a DC motor using the Adafruit TB6612 motor driver with a Raspberry Pi

# Getting Started
## Requirements
Requires Rpi.GPIO 

This can be installed from repository with 

`sudo apt-get install rpi.gpio`

## Example Code
See test.py for basic usage

When initialising a motor, three BCM pin values are required as such

`Motor(pwm_pin, in1_pin, in2_pin)`
