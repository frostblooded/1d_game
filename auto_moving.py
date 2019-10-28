import datetime

import Adafruit_WS2801

from direction import Direction
from game_object import GameObject
from pixels_manager import PixelsManager


class AutoMoving(GameObject):
    def __init__(self, direction, current_pos=None):
        if not current_pos:
            current_pos = 0

            if direction == Direction.LEFT:
                current_pos = PixelsManager.PIXEL_COUNT - 1

        super().__init__(current_pos)

        self.direction = direction

        self.last_run = datetime.datetime.now()

    def update(self):
        delta_since_run = datetime.datetime.now() - self.last_run

        if delta_since_run.microseconds >= self.get_run_wait():
            self.on_run_timer()
            self.last_run = datetime.datetime.now()

    def on_run_timer(self):
        self.move()

    def move(self):
        if self.direction == Direction.LEFT:
            self.move_left()
        elif self.direction == Direction.RIGHT:
            self.move_right()

    def draw(self, pixels):
        pixels.set_pixel(self.get_current_position(), self.get_color())

    def get_color(self):
        return Adafruit_WS2801.color_to_RGB(255, 255, 255)

    def get_run_wait(self):
        return 200000

    def on_boundary_leave(self):
        self.destroy()
