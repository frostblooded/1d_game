import Adafruit_WS2801

from auto_moving_blinking import AutoMovingBlinking
from player import Player


class Enemy(AutoMovingBlinking):
    DAMAGE = 1
    RUN_WAIT = 500000

    def __init__(self, direction):
        self.damage = self.DAMAGE
        super().__init__(direction=direction)

    def on_collision(self, other_object):
        if isinstance(other_object, Player):
            other_object.damage(self.damage)
            self.destroy()

    def get_color(self):
        return Adafruit_WS2801.RGB_to_color(50, 50, 255)

    def get_run_wait(self):
        return Enemy.RUN_WAIT

