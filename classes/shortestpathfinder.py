import networkx as nx
from classes.pathfinder import Pathfinder

# inherit pathfinder class
class ShortestPathfinder(Pathfinder):
    '''
    This class implements the shortest path algorithm.

    Attributes:
        algorithm_name (str): name of the algorithm
    '''
    def __init__(self):
        super().__init__()
        self._algorithm_name = "Shortest Path Algorithm"

    def solve(self, map_graph):
        '''
        This method finds the shortest path from the start node to the end node.

        Parameters:
            map_graph (Graph): graph object

        Returns:
            None
        '''

        # if solution already exists, return it
        if self._solution != None:  
            return self._solution

        # else if there is a path from start to end
        elif nx.has_path(map_graph, map_graph.start_pos, map_graph.end_pos):
            # find the shortest path from start to end
            path = nx.shortest_path(map_graph, map_graph.start_pos, map_graph.end_pos)
            # convert the path to a list of tuples
            route_instructions = []
            facingNorth = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            facingEast = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            facingSouth = [(1, 0), (0, -1), (-1, 0), (0, 1)]
            facingWest = [(0, -1), (-1, 0), (0, 1), (1, 0)]

            # North, East, South, West. according to turtle orientations
            turn_angle = [-90, 0, 90, 180]
            turn = [-1, 0, 1, 2]

            # North, East, South, West. according to turtle orientations
            orientation = [90, 0, 270, 180]
            compass = [facingNorth, facingEast, facingSouth, facingWest]

            index = 1 # default orientation is east

            for i in range(len(path) - 1): # -1 as we don't need to check the last node
                current_direction = compass[index] # default orientation is east for turtle

                # get the x and y difference between 2 nodes
                x_diff = path[i + 1][0] - path[i][0]
                y_diff = path[i + 1][1] - path[i][1]

                # find new orientation
                next_direction_index = current_direction.index((x_diff, y_diff)) # Worst case O(4)

                if next_direction_index != 1: # if not forward, get turn angle

                    if next_direction_index == 3: # if back turn 90 degree 2 times
                        index = (index + turn[2]) % 4
                        route_instructions.append([turn_angle[2], orientation[index]])  # add the turn angle to the list

                        index = (index + turn[2]) % 4
                        route_instructions.append([turn_angle[2], orientation[index]])  # add the turn angle to the list

                    else:
                        index = (index + turn[next_direction_index]) % 4
                        route_instructions.append([turn_angle[next_direction_index], orientation[index]])  # add the turn angle to the list

                route_instructions.append(path[i + 1])  # add the next node to the list

            # set solution to route instructions
            self._solution = route_instructions

            print(route_instructions)
            print("Calculated Shortest Path Algo")
            return route_instructions                

        else:
            return None