# Parent class pathfinder
class Pathfinder:
    '''
    This is the parent class for all pathfinding algorithms.
    Attributes:
        solution (list): list of tuples representing the path from start to end
        algorithm_name (str): name of the algorithm
    '''
    def __init__(self):
        self._solution = None
        self._algorithm_name = None
        self._id = None

    @property
    def algorithm_name(self):
        return self._algorithm_name

    @property
    def solution(self):
        return self._solution

    @property
    def id(self):
        return self._id

    def solve(self, graph, update_solution=False):
        '''
        This method must be implemented in a subclass.
        Parameters:
            graph (Graph): graph object
        Returns:
            None
        '''
        raise NotImplementedError("This method must be implemented in a subclass")
