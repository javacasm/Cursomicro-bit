# test wukong
# https://www.elecfreaks.com/learn-en/microbitExtensionModule/wukong.html
# 
from microbit import *
from Wukong import *

wk = WUKONG()
# breath light
wk.set_light_breath(True)
sleep(5000)
# ligth intensity
wk.set_light(100)

# drive the motors

def test_motors():
    while True:
        wk.set_motors(1, 100)
        wk.set_motors(2, 100)
        sleep(2000)
        wk.set_motors(1, -100)
        wk.set_motors(2, -100)
        sleep(2000)

def test_servos():
    while True:
        wk.set_servo(0, 0)
        sleep(2000)
        wk.set_servo(0, 180)
        sleep(2000)
