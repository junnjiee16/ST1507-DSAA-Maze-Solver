# Parent class pathfinder
class Pathfinder:
    def __init__(self):
        self._solution = None
        self._algorithm_name = None

    @property
    def algorithm_name(self):
        return self._algorithm_name

    def solve(self, graph):
        raise NotImplementedError("This method must be implemented in a subclass")