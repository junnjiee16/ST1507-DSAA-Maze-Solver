# Parent class pathfinder
class Pathfinder:
    def __init__(self):
        self._solution = None
        self._algorithm_name = None
        self._id = None

    @property
    def algorithm_name(self):
        return self._algorithm_name

    @property
    def id(self):
        return self._id

    def solve(self, graph):
        raise NotImplementedError("This method must be implemented in a subclass")

# # object to guide the arrow through the maze with algorithm of choice
# class Pathfinder:
#     def __init__(self, graph, start_position, end_position):
#         self.__graph = graph
#         self.__start_position = start_position
#         self.__end_position = end_position

#         self.__leftHandAlgoSolution = None
#         self.__shortestPathSolution = None
#         self.__useAlgo = 0 # 0 = Left Hand Algorithm, 1 = Shortest Path Algorithm

#     # getters and setter functions
#     @property
#     def leftHandAlgoSolution(self):
#         return self.__leftHandAlgoSolution
    
#     @leftHandAlgoSolution.setter
#     def leftHandAlgoSolution(self, value):
#         self.__leftHandAlgoSolution = value

#     @property
#     def shortestPathSolution(self):
#         return self.__shortestPathSolution

#     @shortestPathSolution.setter
#     def shortestPathSolution(self, value):
#         self.__shortestPathSolution = value

#     # getter to get name of algorithm, setter to switch between algorithms
#     def algo_name(self):
#         if self.__useAlgo == 0:
#             return "Left Hand Algorithm"
#         elif self.__useAlgo == 1:
#             return "Shortest Path Algorithm"

#     def change_algo(self):
#         if self.__useAlgo == 0:
#             print("Changing to shortest path")
#             self.__useAlgo = 1
#         else:
#             print("Changing to left hand")
#             self.__useAlgo = 0


#     # solve the maze using preferred algorithm
#     def maze_solution(self):
#         if self.__useAlgo == 0:
#             if self.__leftHandAlgoSolution == None:
#                 print("First time solving left hand")
#                 self.__leftHandAlgoSolution = self.__LeftHandAlgorithm()
#             return self.__leftHandAlgoSolution

#         elif self.__useAlgo == 1:
#             if self.__shortestPathSolution == None:
#                 print("First time solving shortest path")
#                 self.__shortestPathSolution = self.__ShortestPathAlgorithm()
#             return self.__shortestPathSolution


#     def __LeftHandAlgorithm(self):
#         x, y = self.__start_position

#         # array to store steps
#         route_instructions = []

#         # tuples are in order of left, forward, right, back according to current orientation
#         facingNorth = [(-1, 0), (0, 1), (1, 0), (0, -1)]
#         facingEast = [(0, 1), (1, 0), (0, -1), (-1, 0)]
#         facingSouth = [(1, 0), (0, -1), (-1, 0), (0, 1)]
#         facingWest = [(0, -1), (-1, 0), (0, 1), (1, 0)]

#         # keep track of orientation when moving through maze
#         # compass = ["N", "E", "S", "W"]
#         compass = [facingNorth, facingEast, facingSouth, facingWest]

#         # keep track of how to turn the compass and the direction
#         # ordered by left, forward, right, back
#         turn = [-1, 0, 1, 2]
#         turn_angle = [-90, 0, 90, 180]

#         # set starting orientation to east (index of 1), this is default orientation the pen will face in turtle when it first starts
#         # keep track of index in compass array, so that we can get index in O(1) time instead of using .index() which is O(n)
#         # when changing index, always mod by 4 to keep it within range
#         index = 1
        
#         # keep finding the next node to go to until we reach the end
#         while (x, y) != self.__end_position:
#             # get current orientation
#             current_orientation = compass[index]

#             # find all neighbors of current node, convert to list as function returns a iterator
#             neighbors = list(self.__graph.neighbors((x, y)))

#             # if neighbors is 4, means all 4 directions are available, always turn left
#             if len(neighbors) == 4:
#                 # update current position and add to route instructions
#                 x, y = x + current_orientation[0][0], y + current_orientation[0][1]
#                 route_instructions.append(turn_angle[0]) # turn left first
#                 route_instructions.append((x, y))

#                 # update the new orientation, turn left means index 0
#                 index = (index + turn[0]) % 4

#             # else if 1, 2 or 3 neighbours, we need to check every direction, starting from left > forward > right > back
#             else:
#                 # direction is in order of left, forward, right, back
#                 for direction in range(len(current_orientation)):
#                     # check if the next node in the direction exists
#                     x_next, y_next = x + current_orientation[direction][0], y + current_orientation[direction][1]

#                     if self.__graph.has_node((x_next, y_next)):
#                         # update position and add to route instructions
#                         x, y = x_next, y_next
#                         route_instructions.append(turn_angle[direction]) # keep track of turn angle
#                         route_instructions.append((x, y))

#                         # update the new orientation
#                         index = (index + turn[direction]) % 4

#                         # break out of loop as we found the next node
#                         break

#         print(route_instructions)
#         return route_instructions


#     def __ShortestPathAlgorithm(self):
#         if nx.has_path(self.__graph, self.__start_position, self.__end_position):
#             path = nx.shortest_path(self.__graph, self.__start_position, self.__end_position)

#             # convert path to route instructions
#             route_instructions = []
            
#             facingNorth = [(-1, 0), (0, 1), (1, 0), (0, -1)]
#             facingEast = [(0, 1), (1, 0), (0, -1), (-1, 0)]
#             facingSouth = [(1, 0), (0, -1), (-1, 0), (0, 1)]
#             facingWest = [(0, -1), (-1, 0), (0, 1), (1, 0)]

#             turn_angle = [-90, 0, 90, 180]
#             turn = [-1, 0, 1, 2]

#             compass = [facingNorth, facingEast, facingSouth, facingWest]

#             index = 1 # default orientation is east

#             for i in range(len(path) - 1): # -1 as we don't need to check the last node
#                 current_direction = compass[index] # default orientation is east for turtle

#                 # get the x and y difference between 2 nodes
#                 x_diff = path[i + 1][0] - path[i][0]
#                 y_diff = path[i + 1][1] - path[i][1]

#                 # find new orientation
#                 next_direction_index = current_direction.index((x_diff, y_diff)) # Worst case O(4)

#                 if next_direction_index != 1: # if not forward, get turn angle
#                     route_instructions.append(turn_angle[next_direction_index])
#                     index = (index + turn[next_direction_index]) % 4

#                 route_instructions.append(path[i + 1])

#             print(route_instructions)
#             return route_instructions                

#         else:
#             return None