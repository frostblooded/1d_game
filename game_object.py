from map import Map


class GameObject:
    def __init__(self, current_pos):
        self.__current_pos = None
        self.set_current_position(current_pos)

    def get_current_position(self):
        return self.__current_pos

    def set_current_position(self, position):
        Map.move_object_to(self, position, self.get_current_position())
        self.__current_pos = position

    def move_left(self):
        self.set_current_position(self.get_current_position() - 1)

    def move_right(self):
        self.set_current_position(self.get_current_position() + 1)
