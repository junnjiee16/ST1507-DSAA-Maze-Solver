import networkx as nx

# subclass nx graph
class MapGraph(nx.Graph):
    '''
    A graph representing the map of the game.
    
    Parameters:
        map_layout (list): 2D array of 0s and 1s, 0s represent walls, 1s represent open spaces
        start_pos (tuple): tuple of x and y coordinates of the start position
        end_pos (tuple): tuple of x and y coordinates of the end position
    Attributes:
        layout (list): 2D array of 0s and 1s, 0s represent walls, 1s represent open spaces
        start_pos (tuple): tuple of x and y coordinates of the start position
        end_pos (tuple): tuple of x and y coordinates of the end position
    '''
    def __init__(self, start_pos, end_pos):
        super().__init__()
        self.__start_pos = start_pos
        self.__end_pos = end_pos

    @property
    def start_pos(self):
        return self.__start_pos

    @property
    def end_pos(self):
        return self.__end_pos

    @start_pos.setter
    def start_pos(self, value):
        self.__start_pos = value

    @end_pos.setter
    def end_pos(self, value):
        self.__end_pos = value

    