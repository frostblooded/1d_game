from pixels_manager import PixelsManager
from map import Map
from player import Player
from enemy import Enemy
from direction import Direction


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
