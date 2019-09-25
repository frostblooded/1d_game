from game_manager import *
from player import *
from enemy import *


if __name__ == "__main__":
    GameManager.objects.append(Player())
    GameManager.objects.append(Enemy(Direction.LEFT))
    GameManager.run()
