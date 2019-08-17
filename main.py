from game_manager import *
from player import *


if __name__ == "__main__":
    GameManager.objects.append(Player())
    GameManager.run()
