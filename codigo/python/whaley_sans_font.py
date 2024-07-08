# makecode WhaleySans Font Package.
# From microbit/micropython Chinese community.
# http://www.micropython.org.cn
# from https://github.com/makecode-extensions/WhaleySansFont/blob/master/WhaleySansFont.ts

from microbit import display, Image

v = '0.1'

print('WhaleySansFont v'+v)

FONT = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 1, 0, 1, 1, 1, 1, 0, 1, 1],
        [1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
        [1, 1, 1, 0, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
        [1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 1, 1, 1, 0, 0, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 0, 1, 1, 1]
    ]

def show_number(number,bright = 9,leading_cero=True):
    display.clear()
    if number < 0 or number > 99:
        display.show(Image.CONFUSED)
    else:
        digit_10 = number // 10
        digit_1 = number % 10
        for i in range(5):
            if leading_cero or digit_10>0:
                display.set_pixel(0,i,bright*FONT[digit_10][2*i])
                display.set_pixel(1,i,bright*FONT[digit_10][2*i+1])
            display.set_pixel(3,i,bright*FONT[digit_1][2*i])
            display.set_pixel(4,i,bright*FONT[digit_1][2*i+1])    
