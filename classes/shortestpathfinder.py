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
        self._id = 1

        # use manhattan distance as heuristic
        self.__heuristic = lambda u, v: abs(u[0] - v[0]) + abs(u[1] - v[1])

    def solve(self, map_graph, update_solution=False, drone_orientation=None):
        '''
        This method finds the shortest path from the start node to the end node.
        Parameters:
            map_graph (Graph): graph object
        Returns:
            None
        '''
        if self._solution != None and update_solution == False:
            return self._solution

        elif nx.has_path(map_graph, map_graph.start_pos, map_graph.end_pos):

            if map_graph.number_of_nodes() < 50:
                print("Using Dijkstra's algorithm")
                path = nx.shortest_path(map_graph, map_graph.start_pos, map_graph.end_pos) # djiksra's algorithm
            else:
                print("Using A* algorithm")
                path = nx.astar_path(map_graph, map_graph.start_pos, map_graph.end_pos, heuristic=self.__heuristic)

            # convert path to route instructions
            route_instructions = []
            
            facingNorth = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            facingEast = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            facingSouth = [(1, 0), (0, -1), (-1, 0), (0, 1)]
            facingWest = [(0, -1), (-1, 0), (0, 1), (1, 0)]

            turn_angle = [-90, 0, 90, 180]
            turn = [-1, 0, 1, 2]

            # North, East, South, West. according to turtle orientations
            orientation = [90, 0, 270, 180]

            compass = [facingNorth, facingEast, facingSouth, facingWest]

            if drone_orientation == None:
                index = 1 # default orientation is east
            else:
                index = orientation.index(drone_orientation)

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
                        route_instructions.append([turn_angle[2], orientation[index]])

                        index = (index + turn[2]) % 4
                        route_instructions.append([turn_angle[2], orientation[index]])

                    else:
                        index = (index + turn[next_direction_index]) % 4
                        route_instructions.append([turn_angle[next_direction_index], orientation[index]])

                route_instructions.append(path[i + 1])

            # set solution to route instructions
            self._solution = route_instructions

            print(route_instructions)
            print("Calculated Shortest Path Algo")
            return route_instructions                

        else:
            return []