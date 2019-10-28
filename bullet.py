from auto_moving import AutoMoving
from enemy import Enemy
import Adafruit_WS2801

from health_pack import HealthPack
from player import Player


class Bullet(AutoMoving):
    RUN_WAIT = 25000

    def __init__(self, direction, current_pos):
        super().__init__(direction, current_pos)

    def on_collision(self, other_object):
        if isinstance(other_object, Enemy)\
                or isinstance(other_object, HealthPack):
            other_object.destroy()
            self.destroy()
            Player.get_instance().heal(Player.HEALTH_GAINED_ON_KILL)

    def get_color(self):
        return Adafruit_WS2801.RGB_to_color(150, 150, 0)

    def get_run_wait(self):
        return Bullet.RUN_WAIT
