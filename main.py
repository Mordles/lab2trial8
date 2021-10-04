import RPi.GPIO as gpio
from time import sleep

gpio.setmode(gpio.BOARD)
gpio.setup(26, gpio.IN, pull_up_down=gpio.PUD_DOWN)

def on_pushdown(channel):
    print ("Button Pushed.")

# only add the detection call once!
gpio.add_event_detect(5, gpio.RISING, callback=on_pushdown, bouncetime=200)

while(True):
    try:
        # do any other processing, while waiting for the edge detection
        sleep(1) # sleep 1 sec
    finally:
        gpio.cleanup()