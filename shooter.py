from bullet import Bullet
from pixels_manager import PixelsManager
from player import Player


class Shooter:
    @staticmethod
    def can_spawn_bullet(direction):
        return direction == direction.LEFT and Player.get_instance().get_current_position() > 0 \
               or direction == direction.RIGHT and Player.get_instance().get_current_position() < PixelsManager.PIXEL_COUNT - 1

    @staticmethod
    def get_bullet_spawn_pos(direction):
        switcher = {
            direction.LEFT: Player.get_instance().get_current_position() - 1,
            direction.RIGHT: Player.get_instance().get_current_position() + 1
        }

        return switcher[direction]

    @staticmethod
    def spawn_bullet(direction):
        if Shooter.can_spawn_bullet(direction):
            Bullet(Shooter.get_bullet_spawn_pos(direction), direction)
            Player.get_instance().damage(Player.HEALTH_LOST_ON_SHOT)
