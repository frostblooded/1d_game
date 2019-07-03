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
    
RIGHT_ARROW_KEY_CODE=546
LEFT_ARROW_KEY_CODE=547

last_run = datetime.datetime.now()
RUN_WAIT = 30000
running = False

def update():
    global current_pos
    global running
    global last_run

    has_to_read, _, _ = select([gamepad.fd], [], [], 0.01)

    if has_to_read:
        for event in gamepad.read():
            if event.type == ecodes.EV_KEY:
                if event.code == LEFT_ARROW_KEY_CODE and event.value == 1 and current_pos < PIXEL_COUNT - 1:
                    print("Go left")
                    running = True
                if event.code == LEFT_ARROW_KEY_CODE and event.value == 0 and current_pos < PIXEL_COUNT - 1:
                    print("Stop go left")
                    running = False
                if event.code == RIGHT_ARROW_KEY_CODE and event.value == 1 and current_pos > 0:
                    print("Go right")

    delta_since_run = datetime.datetime.now() - last_run

    if running and delta_since_run.microseconds >= RUN_WAIT:
        last_run = datetime.datetime.now()
        current_pos += 1

def draw():
    pixels.clear()
    pixels.set_pixel(current_pos, Adafruit_WS2801.RGB_to_color(50, 100, 150))
    pixels.show()

if __name__ == "__main__":
    while True:
        update()
        draw()


