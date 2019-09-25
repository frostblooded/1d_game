from pixels_manager import PixelsManager


class Map:
    map = None

    @staticmethod
    def setup():
        Map.map = [[] for _ in range(PixelsManager.PIXEL_COUNT)]

    @staticmethod
    def move_object_to(game_object, new_pos, prev_pos=None):
        if prev_pos is not None:
            # Remove if the element is in the map. Otherwise do nothing.
            try:
                Map.map[prev_pos].remove(game_object)
            except: pass

        Map.map[new_pos].append(game_object)
