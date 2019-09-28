import Adafruit_WS2801

from pixels_manager import PixelsManager
from game_ender import GameEnder
from objects_holder import ObjectsHolder
import time


class GameManager:
    __instance = None

    def __init__(self):
        self.__restart_game = False

    @staticmethod
    def get_instance():
        if GameManager.__instance is None:
            GameManager.__instance = GameManager()

        return GameManager.__instance

    def run(self):
        self.__restart_game = False

        while not self.__restart_game:
            if GameEnder.has_ended:
                self.end_game()
            else:
                self.run_frame()

    def update(self):
        for obj in ObjectsHolder.objects:
            obj.update()

    def draw(self):
        PixelsManager.pixels.clear()

        for obj in ObjectsHolder.objects:
            obj.draw(PixelsManager.pixels)

        PixelsManager.pixels.show()

    def draw_ended_game(self):
        PixelsManager.pixels.clear()

        for i in range(0, PixelsManager.PIXEL_COUNT):
            PixelsManager.pixels.set_pixel(i, Adafruit_WS2801.RGB_to_color(50, 0, 0))

        PixelsManager.pixels.show()

    def restart(self):
        self.__restart_game = True

    def end_game(self):
        self.draw_ended_game()
        time.sleep(2)
        self.restart()

    def run_frame(self):
        self.update()
        self.draw()

