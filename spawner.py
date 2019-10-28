import datetime
import random

from direction import Direction
from enemy import Enemy
from game_object import GameObject
from health_pack import HealthPack
from time_manager import TimeManager


class Spawner(GameObject):
    BASE_SPAWN_WAIT_SECONDS = 1.5
    SPAWN_WAIT_STEP_SECONDS = 0.2
    SPAWN_WAIT_DECREASE_DELAY_SECONDS = 10
    MIN_SPAWN_WAIT_SECONDS = 0.5
    SPAWN_WAIT_DECREASE_START_SECONDS = Enemy.SECONDS_TO_REACH_MIN_WAIT

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
        self.next_spawn = datetime.datetime.now() + datetime.timedelta(seconds=Spawner.BASE_SPAWN_WAIT_SECONDS)

    def draw(self, pixels):
        pass

    def update(self):
        if self.is_time_to_spawn():
            print("Seconds since start: " + str(TimeManager.get_instance().time_since_start().seconds))

            if TimeManager.get_instance().time_since_start().seconds >= Spawner.STAGE_2_START_SECONDS:
                print("Spawning from both sides")
                self.spawn_both_sides()
            else:
                print("Spawning from random side")
                self.spawn_random_side()

    def is_time_to_spawn(self):
        return datetime.datetime.now() >= self.next_spawn

    def calculate_spawn_wait_seconds(self):
        seconds_past_start = TimeManager.get_instance().time_since_start().seconds - Spawner.SPAWN_WAIT_DECREASE_START_SECONDS

        if seconds_past_start < 0:
            return self.BASE_SPAWN_WAIT_SECONDS

        difficulty_modifier = seconds_past_start / Spawner.SPAWN_WAIT_DECREASE_DELAY_SECONDS * Spawner.SPAWN_WAIT_STEP_SECONDS
        res = Spawner.BASE_SPAWN_WAIT_SECONDS - difficulty_modifier
        res = max(res, Spawner.MIN_SPAWN_WAIT_SECONDS)
        print("Current spawn wait: " + str(res))
        return res

    def spawn_random_side(self):
        direction = random.choice(list(Direction))
        class_to_spawn = Spawner.get_random_entity_class()
        class_to_spawn(direction)
        self.next_spawn += datetime.timedelta(seconds=self.calculate_spawn_wait_seconds())

    def spawn_both_sides(self):
        class_to_spawn = Spawner.get_random_entity_class()
        class_to_spawn(Direction.LEFT)

        class_to_spawn = Spawner.get_random_entity_class()
        class_to_spawn(Direction.RIGHT)

        self.next_spawn += datetime.timedelta(seconds=self.calculate_spawn_wait_seconds()) * 2

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
