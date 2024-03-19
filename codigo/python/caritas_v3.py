# Imports go at the top
from microbit import *
from utime import *

images = (Image('00000:'
                       '09090:'
                       '00000:'
                       '09990:'
                       '90009'),
          Image('00000:'
                       '09090:'
                       '00000:'
                       '99999:'
                       '00000'),
          Image('00000:'
                       '09090:'
                       '00000:'
                       '90009:'
                       '09990'))

retardo = 250
n = 0 
last = ticks_ms()
last_pressed = 0
bounce_time = 10

while True:
    if button_a.is_pressed() and ticks_ms() - last_pressed > bounce_time:
        retardo += 5
        print(retardo)
        last_pressed = ticks_ms()
    if button_b.is_pressed() and retardo>0 and ticks_ms() - last_pressed > bounce_time:
        retardo -= 5
        print(retardo)
        last_pressed = ticks_ms()
    if button_a.is_pressed() and button_b.is_pressed():
        retardo = 250
        print(retardo)
    if ticks_ms()-last > retardo:
        display.show(images[n % len(images)])
        n += 1
        last =ticks_ms()
 
    

    
