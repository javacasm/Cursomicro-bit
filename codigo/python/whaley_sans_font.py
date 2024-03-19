# makecode WhaleySans Font Package.
# From microbit/micropython Chinese community.
# http://www.micropython.org.cn
# from https://github.com/makecode-extensions/WhaleySansFont/blob/master/WhaleySansFont.ts

from microbit import display

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

def show_number(number,bright = 9):
    display.clear()
    if number < 0 or number > 99:
        display.show(Image.CONFUSED)
    else:
        digit_10 = number // 10
        digit_1 = number % 10
        for i in range(5):
            display.set_pixel(i,0,bright*FONT[2*i][digit_10])
            display.set_pixel(i,1,bright*FONT[[2*i+1][digit_10])
            display.set_pixel(i,3,bright*FONT[2*i][digit_10])
            display.set_pixel(i,4,bright*FONT[2*i+1][digit_10])    

if __name__ == '__main__':
    from utime import sleep_ms
    for i in range(100):
        show_number(i)
        sleep_ms(500)