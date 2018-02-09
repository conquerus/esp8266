from machine import Pin, I2C
import time
import utime
import ntptime
import ssd1306
import network

i2c = I2C(sda=Pin(4), scl=Pin(5),freq=400000)
display = ssd1306.SSD1306_I2C(128, 32, i2c)
display.contrast(0)
wifi = network.WLAN(network.STA_IF)
wifi.connect('***network-name***','***password***')

christmas_time =  utime.mktime((2017,12,25,0,0,1,0,359))

while True:
    try:
        current_time = ntptime.time()
        old_time = current_time
    except OSError:
        current_time=old_time

    #china
    remaining = utime.localtime(christmas_time-(current_time+8*3600))
    
    time_string_1=(str(remaining[7]-1)+" days, "+str(remaining[3])+" hrs,")
    time_string_2=(str(remaining[4])+" mins,")
    time_string_3=("and "+str(remaining[5])+" secs.")
    display.fill(0)
    display.text(time_string_1,1,1)
    display.text(time_string_2,1,12)
    display.text(time_string_3,1,23)
    display.show()
    time.sleep(0.3)
