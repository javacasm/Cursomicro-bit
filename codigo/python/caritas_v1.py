# Imports go at the top
from microbit import *

retardo = 250
# Code in a 'while True:' loop repeats forever
while True:
    if button_a.is_pressed():
        retardo += 50
        print(retardo)
    if button_b.is_pressed() and retardo>0:
        retardo -= 50
        print(retardo)
    display.show(Image('00000:'
                       '09090:'
                       '00000:'
                       '09990:'
                       '90009'))
    sleep(retardo)
    display.show(Image('00000:'
                       '09090:'
                       '00000:'
                       '99999:'
                       '00000'))
    sleep(retardo)
    display.show(Image('00000:'
                       '09090:'
                       '00000:'
                       '90009:'
                       '09990'))
    sleep(retardo)
    