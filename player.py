import datetime
from select import select

import Adafruit_WS2801

from evdev import InputDevice, ecodes
from game_manager import GameManager


class Player:
    RIGHT_ARROW_KEY_CODE = 547
    LEFT_ARROW_KEY_CODE = 546

    RUN_WAIT = 50000

    def __init__(self):
        self.gamepad = InputDevice('/dev/input/event1')

        self.current_pos = 0

        self.last_run_left = datetime.datetime.now()
        self.running_left = False
        self.last_run_right = datetime.datetime.now()
        self.running_right = False

    def update(self):
        has_to_read, _, _ = select([self.gamepad.fd], [], [], 0.01)

        if has_to_read:
            for event in self.gamepad.read():
                if event.type == ecodes.EV_KEY:
                    if event.code == self.LEFT_ARROW_KEY_CODE and event.value == 1:
                        print("Go left")
                        self.running_left = True
                    if event.code == self.LEFT_ARROW_KEY_CODE and event.value == 0:
                        print("Stop go left")
                        self.running_left = False
                    if event.code == self.RIGHT_ARROW_KEY_CODE and event.value == 1:
                        print("Go right")
                        self.running_right = True
                    if event.code == self.RIGHT_ARROW_KEY_CODE and event.value == 0:
                        print("Stop go right")
                        self.running_right = False

        delta_since_run_left = datetime.datetime.now() - self.last_run_left
        delta_since_run_right = datetime.datetime.now() - self.last_run_right

        if self.running_left and delta_since_run_left.microseconds >= self.RUN_WAIT and self.current_pos > 0:
            self.last_run_left = datetime.datetime.now()
            self.current_pos -= 1

        if self.running_right and delta_since_run_right.microseconds >= self.RUN_WAIT and self.current_pos < GameManager.PIXEL_COUNT - 1:
            self.last_run_right = datetime.datetime.now()
            self.current_pos += 1

    def draw(self, pixels):
        pixels.clear()
        pixels.set_pixel(self.current_pos, Adafruit_WS2801.RGB_to_color(50, 100, 150))
        pixels.show()
