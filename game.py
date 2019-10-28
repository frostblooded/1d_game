from spawner import Spawner
from game_manager import GameManager
from game_ender import GameEnder
from input_manager import InputManager
from map import Map
from pixels_manager import PixelsManager
from objects_holder import ObjectsHolder
from player import Player


class Game:
    @staticmethod
    def start():
        PixelsManager.setup()
        Map.setup()
        GameEnder.setup()
        InputManager()
        Player.get_instance()
        Spawner()

        GameManager.get_instance().run()

        Player.destroy_instance()
        ObjectsHolder.objects.clear()
