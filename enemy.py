import datetime
import Adafruit_WS2801

from pixels_manager import PixelsManager
from direction import Direction
from game_object import GameObject
from player import Player


class Enemy(GameObject):
    DAMAGE = 5
    RUN_WAIT = 200000

    def __init__(self, direction):
        starting_position = 0

        if direction == Direction.LEFT:
            starting_position = PixelsManager.PIXEL_COUNT - 1

        super().__init__(current_pos=starting_position)

        self.direction = direction
        self.last_run = datetime.datetime.now()
        self.damage = self.DAMAGE

    def update(self):
        delta_since_run = datetime.datetime.now() - self.last_run

        if delta_since_run.microseconds >= self.RUN_WAIT:
            if self.direction == Direction.LEFT:
                self.move_left()
            elif self.direction == Direction.RIGHT:
                self.move_right()

            self.last_run = datetime.datetime.now()

    def draw(self, pixels):
        pixels.set_pixel(self.get_current_position(), Adafruit_WS2801.RGB_to_color(220, 50, 50))

    def on_collision(self, other_object):
        if isinstance(other_object, Player):
            other_object.damage(self.damage)
