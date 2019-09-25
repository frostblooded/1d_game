import datetime
import Adafruit_WS2801

from game_manager import GameManager
from direction import Direction


class Enemy:
    RUN_WAIT = 200000

    def __init__(self, direction):
        self.direction = direction
        self.current_pos = 0

        if direction == Direction.LEFT:
            self.current_pos = GameManager.PIXEL_COUNT - 1

        self.last_run = datetime.datetime.now()

    def update(self):
        delta_since_run = datetime.datetime.now() - self.last_run

        if delta_since_run.microseconds >= self.RUN_WAIT:
            if self.direction == Direction.LEFT and self.current_pos > 0:
                self.current_pos -= 1
            elif self.direction == Direction.RIGHT and self.current_pos < GameManager.PIXEL_COUNT - 1:
                self.current_pos += 1

            self.last_run = datetime.datetime.now()

    def draw(self, pixels):
        pixels.set_pixel(self.current_pos, Adafruit_WS2801.RGB_to_color(220, 50, 50))
