from classes.pathfinder import Pathfinder

# inherit pathfinder class
class ShortestPathfinder(Pathfinder):
    def __init__(self):
        super().__init__()
        self._algorithm_name = "Shortest Path Algorithm"

    def solve(self, graph):
        pass