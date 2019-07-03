import asyncio
import time
import datetime
from select import select
import RPi.GPIO as GPIO
 
import Adafruit_WS2801
import Adafruit_GPIO.SPI as SPI

from evdev import InputDevice, categorize, ecodes

gamepad = InputDevice('/dev/input/event1')
 
PIXEL_COUNT = 32
 
SPI_PORT   = 0
SPI_DEVICE = 0
pixels = Adafruit_WS2801.WS2801Pixels(PIXEL_COUNT, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE), gpio=GPIO)
print(pixels)

current_pos = 0
    
RIGHT_ARROW_KEY_CODE=547
LEFT_ARROW_KEY_CODE=546

RUN_WAIT = 50000

last_run_left = datetime.datetime.now()
running_left = False
last_run_right = datetime.datetime.now()
running_right = False

def update():
    global current_pos
    global running_left
    global last_run_left
    global running_right
    global last_run_right

    has_to_read, _, _ = select([gamepad.fd], [], [], 0.01)

    if has_to_read:
        for event in gamepad.read():
            if event.type == ecodes.EV_KEY:
                if event.code == LEFT_ARROW_KEY_CODE and event.value == 1:
                    print("Go left")
                    running_left = True
                if event.code == LEFT_ARROW_KEY_CODE and event.value == 0:
                    print("Stop go left")
                    running_left = False
                if event.code == RIGHT_ARROW_KEY_CODE and event.value == 1:
                    print("Go right")
                    running_right = True
                if event.code == RIGHT_ARROW_KEY_CODE and event.value == 0:
                    print("Stop go right")
                    running_right = False

    delta_since_run_left = datetime.datetime.now() - last_run_left
    delta_since_run_right = datetime.datetime.now() - last_run_right

    if running_left and delta_since_run_left.microseconds >= RUN_WAIT and current_pos > 0:
        last_run_left = datetime.datetime.now()
        current_pos -= 1
        
    if running_right and delta_since_run_right.microseconds >= RUN_WAIT and current_pos < PIXEL_COUNT - 1:
        last_run_right = datetime.datetime.now()
        current_pos += 1

def draw():
    pixels.clear()
    pixels.set_pixel(current_pos, Adafruit_WS2801.RGB_to_color(50, 100, 150))
    pixels.show()

if __name__ == "__main__":
    while True:
        update()
        draw()


