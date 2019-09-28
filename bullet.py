from auto_moving_object import AutoMovingObject
from enemy import Enemy
import Adafruit_WS2801


class Bullet(AutoMovingObject):
    RUN_WAIT = 25000

    def on_collision(self, other_object):
        if isinstance(other_object, Enemy):
            other_object.destroy()
            self.destroy()

    def get_color(self):
        return Adafruit_WS2801.RGB_to_color(150, 150, 0)

    def get_run_wait(self):
        return Bullet.RUN_WAIT