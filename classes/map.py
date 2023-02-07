# map object, stores necessary metadata for the map
class Map:
    '''
    Stores map layout, start position, end position, and map dimensions

    Parameters:
        map_layout (list): 2D array of 0s and 1s, 0s represent walls, 1s represent open spaces
        start_pos (tuple): tuple of x and y coordinates of the start position
        end_pos (tuple): tuple of x and y coordinates of the end position

    Attributes:
        layout (list): 2D array of 0s and 1s, 0s represent walls, 1s represent open spaces
        start_pos (tuple): tuple of x and y coordinates of the start position
        end_pos (tuple): tuple of x and y coordinates of the end position
        x_length (int): horizontal length of the map in terms of number of cells
        y_length (int): vertical length of the map in terms of number of cells
    '''
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

