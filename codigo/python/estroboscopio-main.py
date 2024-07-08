# Imports go at the top
from microbit import *
from time import *

# Code in a 'while True:' loop repeats forever
while True:
    retardo = pin1.read_analog()*50
    print(retardo)
    pin0.write_digital(1)
    sleep_us(retardo)
    pin0.write_digital(0)
    sleep_us(retardo)