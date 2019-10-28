import datetime
import random

from direction import Direction
from enemy import Enemy
from game_object import GameObject
from health_pack import HealthPack
from time_manager import TimeManager


class Spawner(GameObject):
    SET_SPAWN_WAIT_SECONDS = 1.5
    STAGE_2_START_SECONDS = 25

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
        self.next_spawn = datetime.datetime.now() + datetime.timedelta(seconds=Spawner.SET_SPAWN_WAIT_SECONDS)

    def draw(self, pixels):
        pass

    def update(self):
        if self.time_to_spawn():
            print("Seconds since start: " + str(TimeManager.get_instance().time_since_start().seconds))

            if TimeManager.get_instance().time_since_start().seconds >= Spawner.STAGE_2_START_SECONDS:
                print("Spawning from both sides")
                self.spawn_both_sides()
            else:
                print("Spawning from random side")
                self.spawn_random_side()

    def time_to_spawn(self):
        return datetime.datetime.now() >= self.next_spawn

    def spawn_random_side(self):
        direction = random.choice(list(Direction))
        class_to_spawn = Spawner.get_random_entity_class()
        class_to_spawn(direction)
        self.next_spawn += datetime.timedelta(seconds=Spawner.SET_SPAWN_WAIT_SECONDS)

    def spawn_both_sides(self):
        class_to_spawn = Spawner.get_random_entity_class()
        class_to_spawn(Direction.LEFT)

        class_to_spawn = Spawner.get_random_entity_class()
        class_to_spawn(Direction.RIGHT)

        self.next_spawn += datetime.timedelta(seconds=Spawner.SET_SPAWN_WAIT_SECONDS) * 2

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
