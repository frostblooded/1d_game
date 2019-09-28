import datetime
from select import select

import Adafruit_WS2801

from evdev import InputDevice, ecodes
from game_object import GameObject
from game_ender import GameEnder


class Player(GameObject):
    HEALTH = 5

    RIGHT_ARROW_KEY_CODE = 547
    LEFT_ARROW_KEY_CODE = 546

    RUN_WAIT = 50000

    def __init__(self):
        super().__init__(current_pos=0)
        self.gamepad = InputDevice('/dev/input/event1')

        self.last_run_left = datetime.datetime.now()
        self.running_left = False
        self.last_run_right = datetime.datetime.now()
        self.running_right = False

        self.__health = self.HEALTH
        self.__is_alive = True

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

        if self.running_left and delta_since_run_left.microseconds >= self.RUN_WAIT:
            self.last_run_left = datetime.datetime.now()
            self.move_left()

        if self.running_right and delta_since_run_right.microseconds >= self.RUN_WAIT:
            self.last_run_right = datetime.datetime.now()
            self.move_right()

    def draw(self, pixels):
        pixels.set_pixel(self.get_current_position(), Adafruit_WS2801.RGB_to_color(50, 100, 150))

    def die(self):
        self.__is_alive = False
        GameEnder.has_ended = True
        print('Ded')

    def damage(self, amount):
        self.__health -= amount

        if self.__health <= 0:
            self.die()
