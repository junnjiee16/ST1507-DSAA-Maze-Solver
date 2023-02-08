import networkx as nx
from classes.pathfinder import Pathfinder

# inherit pathfinder class
class TravellingSalesmanPathfinder(Pathfinder):
    def __init__(self):
        super().__init__()
        self._algorithm_name = "Travelling Salesman Problem Pathfinder"
        self._id = 2


    def solve(self, map_graph):
        if self._solution != None:
            return self._solution
        else:
            tsp = nx.approximation.traveling_salesman_problem
            map_graph.end_pos.insert(0, map_graph.start_pos)
            path = tsp(map_graph, nodes=map_graph.end_pos)
            
            return path
    