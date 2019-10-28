import Adafruit_WS2801

from auto_moving_blinking import AutoMovingBlinking
from player import Player
from time_manager import TimeManager


class Enemy(AutoMovingBlinking):
    DAMAGE = 1
    BASE_RUN_WAIT = 700000

    RUN_WAIT_DECREASE_DELAY_SECONDS = 10
    RUN_WAIT_DECREASE_STEP = 50000
    RUN_WAIT_DECREASE_MIN = 200000
    SECONDS_TO_REACH_MIN_WAIT = (BASE_RUN_WAIT - RUN_WAIT_DECREASE_MIN) / RUN_WAIT_DECREASE_STEP * RUN_WAIT_DECREASE_DELAY_SECONDS

    def __init__(self, direction):
        self.damage = self.DAMAGE
        self.run_wait = self.calculate_run_wait()
        super().__init__(direction=direction)

    def on_collision(self, other_object):
        if isinstance(other_object, Player):
            other_object.damage(self.damage)
            self.destroy()

    def get_color(self):
        if self.active:
            return Adafruit_WS2801.RGB_to_color(50, 50, 255)
        else:
            return Adafruit_WS2801.RGB_to_color(0, 0, 5)

    def get_run_wait(self):
        return self.run_wait

    @staticmethod
    def calculate_run_wait():
        difficulty_modifier = TimeManager.get_instance().time_since_start().seconds // Enemy.RUN_WAIT_DECREASE_DELAY_SECONDS\
                              * Enemy.RUN_WAIT_DECREASE_STEP
        res = Enemy.BASE_RUN_WAIT - difficulty_modifier
        res = max(res, Enemy.RUN_WAIT_DECREASE_MIN)
        print("Current enemy run wait: " + str(res))
        return res

