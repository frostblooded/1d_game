import datetime
import math

from game_object import GameObject
from game_ender import GameEnder
from pixels_manager import PixelsManager

import Adafruit_WS2801


class Player(GameObject):
    HEALTH = 5

    RUN_WAIT = 50000

    __instance = None

    def __init__(self):
        super().__init__(current_pos=math.ceil(PixelsManager.PIXEL_COUNT / 2))

        self.last_run_left = datetime.datetime.now()
        self.running_left = False
        self.last_run_right = datetime.datetime.now()
        self.running_right = False

        self.__health = self.HEALTH
        self.__is_alive = True

    def update(self):
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

    @staticmethod
    def get_instance():
        if Player.__instance is None:
            Player.__instance = Player()

        return Player.__instance
