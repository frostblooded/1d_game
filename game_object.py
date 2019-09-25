from map import Map
from pixels_manager import PixelsManager


class GameObject:
    def __init__(self, current_pos):
        self.__current_pos = None
        self.set_current_position(current_pos)

    def get_current_position(self):
        return self.__current_pos

    @staticmethod
    def validate_position(position):
        return 0 <= position < PixelsManager.PIXEL_COUNT

    def set_current_position(self, position):
        if not GameObject.validate_position(position):
            return

        Map.move_object_to(self, position, self.get_current_position())
        self.__current_pos = position

    def move_left(self):
        self.set_current_position(self.get_current_position() - 1)

    def move_right(self):
        self.set_current_position(self.get_current_position() + 1)
