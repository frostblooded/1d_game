import datetime

import Adafruit_WS2801

from direction import Direction
from game_object import GameObject


class AutoMovingObject(GameObject):
    def __init__(self, current_pos, direction):
        super().__init__(current_pos)

        self.direction = direction

        self.last_run = datetime.datetime.now()

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