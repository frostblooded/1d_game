from pixels_manager import PixelsManager


class Map:
    map = None

    @staticmethod
    def setup():
        Map.map = [[] for _ in range(PixelsManager.PIXEL_COUNT)]

    @staticmethod
    def move_object_to(game_object, new_pos, prev_pos=None):
        if prev_pos is not None:
            Map.map[prev_pos].remove(game_object)

        Map.map[new_pos].append(game_object)
        Map.collide_objects_with(Map.map[new_pos], game_object)

    @staticmethod
    def collide_objects_with(objects, colliding_object):
        for obj in objects:
            if obj.collision_enabled and colliding_object.collision_enabled:
                obj.on_collision(colliding_object)
                colliding_object.on_collision(obj)

    @staticmethod
    def remove_from(game_object, position):
        Map.map[position].remove(game_object)
