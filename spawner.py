import datetime
import random

from direction import Direction
from enemy import Enemy
from game_object import GameObject
from health_pack import HealthPack


class Spawner(GameObject):
    SPAWN_WAIT = 900000

    SPAWN_PROBABILITIES = [
        {
            'class': Enemy,
            'probability': 90
        },
        {
            'class': HealthPack,
            'probability': 10
        }
    ]

    def __init__(self):
        super().__init__()
        self.last_spawn = datetime.datetime.now()

    def draw(self, pixels):
        pass

    def update(self):
        delta_since_spawn = datetime.datetime.now() - self.last_spawn

        if delta_since_spawn.microseconds >= Spawner.SPAWN_WAIT:
            direction = random.choice(list(Direction))
            class_to_spawn = Spawner.get_random_entity_class()
            class_to_spawn(direction)

            self.last_spawn = datetime.datetime.now()

    @staticmethod
    def get_random_entity_class():
        rand = random.random() * 100

        for entity_prob in Spawner.SPAWN_PROBABILITIES:
            probability = entity_prob.get('probability')

            if rand < probability:
                return entity_prob.get('class')
            else:
                rand -= probability

        return Enemy
