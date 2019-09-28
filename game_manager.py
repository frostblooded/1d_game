import Adafruit_WS2801

from pixels_manager import PixelsManager
from map import Map
from player import Player
from enemy import Enemy
from direction import Direction
from game_ender import GameEnder


class GameManager:
    objects = []

    @staticmethod
    def setup():
        PixelsManager.setup()
        Map.setup()
        GameManager.objects.append(Player())
        GameManager.objects.append(Enemy(Direction.LEFT))

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
        for obj in GameManager.objects:
            obj.update()

    @staticmethod
    def draw():
        PixelsManager.pixels.clear()

        for obj in GameManager.objects:
            obj.draw(PixelsManager.pixels)

        PixelsManager.pixels.show()

    @staticmethod
    def draw_ended_game():
        PixelsManager.pixels.clear()

        for i in range(0, PixelsManager.PIXEL_COUNT - 1):
            PixelsManager.pixels.set_pixel(i, Adafruit_WS2801.RGB_to_color(255, 0, 0))

        PixelsManager.pixels.show()
