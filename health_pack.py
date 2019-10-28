import Adafruit_WS2801

from auto_moving_blinking import AutoMovingBlinking
from player import Player


class HealthPack(AutoMovingBlinking):
    HEAL = 1

    def get_color(self):
        return Adafruit_WS2801.RGB_to_color(0, 255, 0)

    def on_collision(self, other_object):
        if isinstance(other_object, Player):
            other_object.heal(HealthPack.HEAL)
            self.destroy()

