from map import Map
from pixels_manager import PixelsManager
from objects_holder import ObjectsHolder


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

        old_pos = self.__current_pos
        self.__current_pos = position
        Map.move_object_to(self, position, old_pos)

    def move_left(self):
        self.set_current_position(self.get_current_position() - 1)

    def move_right(self):
        self.set_current_position(self.get_current_position() + 1)

    def on_collision(self, other_object):
        pass

    def destroy(self):
        ObjectsHolder.objects.remove(self)
        Map.remove_from(self, self.get_current_position())
