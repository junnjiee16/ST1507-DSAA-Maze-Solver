import networkx as nx

# subclass nx graph
class MapGraph(nx.Graph):
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

    