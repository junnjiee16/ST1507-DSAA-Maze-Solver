import turtle

# map object, stores necessary metadata for the map
class Map:
    def __init__(self, map_layout, start_pos, end_pos):
        self.__layout = map_layout
        self.__start_pos = start_pos
        self.__end_pos = end_pos

        # horizontal_length (x_length) and vertical_length (y_length) of the map in terms of number of cells
        self.__x_length = len(map_layout[0])
        self.__y_length = len(map_layout)


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

    @property
    def x_length(self):
        return self.__x_length

    @property
    def y_length(self):
        return self.__y_length

