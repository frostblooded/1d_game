import datetime
import random

from direction import Direction
from objects_holder import ObjectsHolder
from enemy import Enemy


class EnemySpawner:
    SPAWN_WAIT = 500000

    def __init__(self):
        self.last_spawn = datetime.datetime.now()

    def draw(self, pixels):
        pass

    def update(self):
        delta_since_spawn = datetime.datetime.now() - self.last_spawn

        if delta_since_spawn.microseconds >= EnemySpawner.SPAWN_WAIT:
            direction = random.choice(list(Direction))
            ObjectsHolder.objects.append(Enemy(direction))

            self.last_spawn = datetime.datetime.now()
