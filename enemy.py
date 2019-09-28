import Adafruit_WS2801

from pixels_manager import PixelsManager
from direction import Direction
from auto_moving_object import AutoMovingObject
from player import Player


class Enemy(AutoMovingObject):
    DAMAGE = 3
    RUN_WAIT = 500000

    def __init__(self, direction):
        self.damage = self.DAMAGE
        starting_position = 0

        if direction == Direction.LEFT:
            starting_position = PixelsManager.PIXEL_COUNT - 1

        super().__init__(current_pos=starting_position, direction=direction)
        self.active = True

    def draw(self, pixels):
        if self.active:
            super().draw(pixels)

    def on_run_timer(self):
        if self.active:
            self.deactivate()
        else:
            self.activate()

        super().on_run_timer()

    def on_collision(self, other_object):
        if isinstance(other_object, Player):
            other_object.damage(self.damage)
            self.destroy()

    def get_color(self):
        return Adafruit_WS2801.RGB_to_color(220, 50, 50)

    def get_run_wait(self):
        return Enemy.RUN_WAIT

    def deactivate(self):
        self.active = False
        self.collision_enabled = False

    def activate(self):
        self.active = True
        self.collision_enabled = True
