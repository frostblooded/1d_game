import Adafruit_WS2801

from pixels_manager import PixelsManager
from map import Map
from player import Player
from enemy import Enemy
from direction import Direction
from game_ender import GameEnder
from input_manager import InputManager
from objects_holder import ObjectsHolder
from enemy_spawner import EnemySpawner


class GameManager:
    @staticmethod
    def setup():
        PixelsManager.setup()
        Map.setup()

        InputManager()
        Player.get_instance()
        EnemySpawner()

    @staticmethod
    def run():
        GameManager.setup()

        while True:
            if GameEnder.has_ended:
                GameManager.draw_ended_game()
            else:
                GameManager.update()
                GameManager.draw()

    @staticmethod
    def update():
        for obj in ObjectsHolder.objects:
            obj.update()

    @staticmethod
    def draw():
        PixelsManager.pixels.clear()

        for obj in ObjectsHolder.objects:
            obj.draw(PixelsManager.pixels)

        PixelsManager.pixels.show()

    @staticmethod
    def draw_ended_game():
        PixelsManager.pixels.clear()

        for i in range(0, PixelsManager.PIXEL_COUNT):
            PixelsManager.pixels.set_pixel(i, Adafruit_WS2801.RGB_to_color(50, 0, 0))

        PixelsManager.pixels.show()

