from machine import Pin, I2C
import time
import utime
import ntptime
import ssd1306
import network

i2c = I2C(sda=Pin(4), scl=Pin(5),freq=400000)
display = ssd1306.SSD1306_I2C(128, 32, i2c)    
wifi = network.WLAN(network.STA_IF)
wifi.connect('***network-name***','***password***')

while True:
    try:
        current_time = ntptime.time()
        old_time = current_time
    except OSError:
        current_time=old_time

    #china
    china_time = utime.localtime(current_time+(8*3600))
    time_string=(str(china_time[3])+":"+str(china_time[4])+":"+str(china_time[5]))
    display.fill(0)
    display.text('China:',1,1)
    display.text(time_string,62,1)

    #toronto
    toronto_time = utime.localtime(current_time-(4*3600))
    time_string=(str(toronto_time[3])+":"+str(toronto_time[4])+":"+str(toronto_time[5]))
    display.text('Toronto:',1,12)
    display.text(time_string,70,12)

    #london
    london_time = utime.localtime(current_time)
    time_string=(str(london_time[3])+":"+str(london_time[4])+":"+str(london_time[5]))
    display.text('London:',1,23)
    display.text(time_string,70,23)

    display.show()
    time.sleep(0.3)
