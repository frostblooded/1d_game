from player import Player

from select import select
from evdev import InputDevice, ecodes


class InputManager:
    RIGHT_ARROW_KEY_CODE = 547
    LEFT_ARROW_KEY_CODE = 546

    def __init__(self):
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

    def draw(self, pixels):
        pass

