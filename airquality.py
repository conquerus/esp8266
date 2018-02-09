import network
import urequests
from machine import Pin, I2C
import ssd1306
import time

i2c = I2C(sda=Pin(4), scl=Pin(5),freq=400000)
display = ssd1306.SSD1306_I2C(128, 32, i2c)    
wifi = network.WLAN(network.STA_IF)
wifi.connect('***network-name***','***password***')
display.contrast(0)

while True:
    air = urequests.get("https://api.waqi.info/feed/here/?token=*********")
    air = air.json()
    tempr = air['data']['iaqi']['t']['v']
    pm25 = air['data']['iaqi']['pm25']['v']
    updated = air['data']['time']['s']
    display.fill(0)
    display.text(str(updated),1,1)
    display.text('PM 2.5:',1,12)
    display.text('Temperature:',1,23)
    display.text(str(pm25),100,12)
    display.text(str(tempr),100,23)
    display.show()
    time.sleep(60)
