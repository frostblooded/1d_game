import datetime
import random

from direction import Direction
from enemy import Enemy
from game_object import GameObject


class EnemySpawner(GameObject):
    SPAWN_WAIT = 900000

    def __init__(self):
        super().__init__()
        self.last_spawn = datetime.datetime.now()

    def draw(self, pixels):
        pass

    def update(self):
        delta_since_spawn = datetime.datetime.now() - self.last_spawn

        if delta_since_spawn.microseconds >= EnemySpawner.SPAWN_WAIT:
            direction = random.choice(list(Direction))
            Enemy(direction)

            self.last_spawn = datetime.datetime.now()
