import turtle

# map object, stores necessary metadata for the map
class Map:
    def __init__(self, map_layout, start_pos, end_pos):
        self.__layout = map_layout
        self.__start_pos = start_pos
        self.__end_pos = end_pos

    # getter functions
    @property
    def layout(self):
        return self.__layout

    @property
    def start_pos(self):
        return self.__start_pos
    
    @property
    def end_pos(self):
        return self.__end_pos

