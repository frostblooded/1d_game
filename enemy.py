import Adafruit_WS2801

from pixels_manager import PixelsManager
from direction import Direction
from auto_moving_object import AutoMovingObject
from player import Player


class Enemy(AutoMovingObject):
    DAMAGE = 3
    RUN_WAIT = 200000

    def __init__(self, direction):
        self.damage = self.DAMAGE
        starting_position = 0

        if direction == Direction.LEFT:
            starting_position = PixelsManager.PIXEL_COUNT - 1

        super().__init__(current_pos=starting_position, direction=direction)

    def on_collision(self, other_object):
        if isinstance(other_object, Player):
            other_object.damage(self.damage)
            self.destroy()

    def get_color(self):
        return Adafruit_WS2801.RGB_to_color(220, 50, 50)

    def get_run_wait(self):
        return Enemy.RUN_WAIT
