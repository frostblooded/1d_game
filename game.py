from spawner import Spawner
from game_manager import GameManager
from game_ender import GameEnder
from input_manager import InputManager
from map import Map
from pixels_manager import PixelsManager
from objects_holder import ObjectsHolder
from player import Player
from time_manager import TimeManager


class Game:
    @staticmethod
    def start():
        PixelsManager.setup()
        Map.setup()
        GameEnder.setup()
        TimeManager.setup()
        InputManager()
        Player.get_instance()
        Spawner()
        print("Starting game")

        GameManager.get_instance().run()

        print("Ending game")
        TimeManager.destroy()
        Player.destroy_instance()
        ObjectsHolder.objects.clear()
