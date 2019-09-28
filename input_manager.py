from direction import Direction
from player import Player
from pixels_manager import PixelsManager
from objects_holder import ObjectsHolder
from bullet import Bullet
from game_object import GameObject

from select import select
from evdev import InputDevice, ecodes


class InputManager(GameObject):
    RIGHT_ARROW_KEY_CODE = 547
    LEFT_ARROW_KEY_CODE = 546
    SQUARE_KEY_CODE = 308
    CIRCLE_KEY_CODE = 305

    def __init__(self):
        super().__init__()
        self.gamepad = InputDevice('/dev/input/event1')

    def update(self):
        has_to_read, _, _ = select([self.gamepad.fd], [], [], 0.01)

        if has_to_read:
            for event in self.gamepad.read():
                if event.type == ecodes.EV_KEY:
                    if event.code == self.LEFT_ARROW_KEY_CODE and event.value == 1:
                        print('Start running left')
                        Player.get_instance().running_left = True
                    if event.code == self.LEFT_ARROW_KEY_CODE and event.value == 0:
                        print('Stop running left')
                        Player.get_instance().running_left = False
                    if event.code == self.RIGHT_ARROW_KEY_CODE and event.value == 1:
                        print('Start running right')
                        Player.get_instance().running_right = True
                    if event.code == self.RIGHT_ARROW_KEY_CODE and event.value == 0:
                        print('Stop running right')
                        Player.get_instance().running_right = False
                    if event.code == self.CIRCLE_KEY_CODE and event.value == 1:
                        self.spawn_bullet(Direction.RIGHT)
                    if event.code == self.SQUARE_KEY_CODE and event.value == 1:
                        self.spawn_bullet(Direction.LEFT)

    def draw(self, pixels):
        pass

    def can_spawn_bullet(self, direction):
        return direction == direction.LEFT and Player.get_instance().get_current_position() > 0 \
               or direction == direction.RIGHT and Player.get_instance().get_current_position() < PixelsManager.PIXEL_COUNT - 1

    def get_bullet_spawn_pos(self, direction):
        switcher = {
            direction.LEFT: Player.get_instance().get_current_position() - 1,
            direction.RIGHT: Player.get_instance().get_current_position() + 1
        }

        return switcher[direction]

    def spawn_bullet(self, direction):
        if self.can_spawn_bullet(direction):
            Bullet(self.get_bullet_spawn_pos(direction), direction)
