import networkx as nx
from classes.pathfinder import Pathfinder

# inherit pathfinder class
class LeftHandPathfinder(Pathfinder):
    def __init__(self):
        super().__init__()
        self._algorithm_name = "Left Hand Algorithm"
        self._id = 0


    def solve(self, map_graph, update_solution=False, drone_orientation=None):
        if self._solution != None and update_solution == False:
            return self._solution

        elif nx.has_path(map_graph, map_graph.start_pos, map_graph.end_pos) == False:
            return []

        else:
            # keep track of how many times we visited start node. if more than 4 times means we stuck in infinite loop
            start_pos = map_graph.start_pos
            visited_start_counter = 0

            x, y = map_graph.start_pos

            # array to store steps
            route_instructions = []

            # tuples are in order of left, forward, right, back according to current orientation
            facingNorth = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            facingEast = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            facingSouth = [(1, 0), (0, -1), (-1, 0), (0, 1)]
            facingWest = [(0, -1), (-1, 0), (0, 1), (1, 0)]

            # keep track of orientation when moving through maze
            # North, East, South, West. according to turtle orientations
            orientation = [90, 0, 270, 180]
            compass = [facingNorth, facingEast, facingSouth, facingWest]

            check_diagonals = [(-1,-1), (-1, 1), (1, 1), (1, -1)]

            # keep track of how to turn the compass and the direction
            # ordered by left, forward, right, back
            turn = [-1, 0, 1, 2]
            turn_angle = [-90, 0, 90, 180]

            # if not speified, set starting orientation to east (index of 1), this is default orientation the pen will face in turtle when it first starts
            # keep track of index in compass array, so that we can get index in O(1) time instead of using .index() which is O(n)
            # when changing index, always mod by 4 to keep it within range
            if drone_orientation == None:
                index = 1
            else:
                index = orientation.index(drone_orientation)
            
            # keep finding the next node to go to until we reach the end
            while (x, y) != map_graph.end_pos:
                # get current orientation
                current_orientation = compass[index]

                # step 1: check if left can, if can, check if infinite loop exists
                # index 0 means left side, 2nd indexing is to get the tuple x and y values
                left_x, left_y = x + current_orientation[0][0], y + current_orientation[0][1]

                if map_graph.has_node((left_x, left_y)):

                    # to check if infinite loop: check the diagonal and left and bottom
                    # if it is a infinite loop, check if there is a wall in front
                    # if wall in front, turn right so the left hand touches the wall
                    # else walk forward to escape the loop
                    bottom_x, bottom_y = x + current_orientation[3][0], y + current_orientation[3][1]
                    diagonal_x, diagonal_y = x + check_diagonals[index][0], y + check_diagonals[index][1]
                    if map_graph.has_node((bottom_x, bottom_y)) and map_graph.has_node((diagonal_x, diagonal_y)):

                        # if its not a wall, go forward, else go to the right
                        front_x, front_y = x + current_orientation[1][0], y + current_orientation[1][1]
                        if map_graph.has_node((front_x, front_y)):
                            x, y = front_x, front_y
                            route_instructions.append((x, y))
                        else:
                            # update the new orientation, turn right
                            index = (index + turn[2]) % 4
                            # store the new orientation of the drone, as well as its turn angle
                            route_instructions.append([turn_angle[2], orientation[index]])

                    # no infinite loop, drone can go to the left safely
                    else:
                        # update the new orientation, turn left means index 0
                        index = (index + turn[0]) % 4
                        # store the new orientation of the drone, as well as its turn angle
                        route_instructions.append([turn_angle[0], orientation[index]])
                        # update current position and add new position to route instructions
                        x, y = left_x, left_y
                        route_instructions.append((x, y))


                # we need to check every direction, starting from forward > right > back
                else:
                    for direction in range(1, 4):
                        # check if the next node in the direction exists
                        x_next, y_next = x + current_orientation[direction][0], y + current_orientation[direction][1]

                        if map_graph.has_node((x_next, y_next)):
                            if direction == 3: # if we turned back, we need to turn twice, so turn right 2 times
                                # update the new orientation according to the direction we turned
                                index = (index + turn[2]) % 4
                                route_instructions.append([turn_angle[2], orientation[index]])

                                index = (index + turn[2]) % 4
                                route_instructions.append([turn_angle[2], orientation[index]])
                            else:
                                # update the new orientation according to the direction we turned
                                index = (index + turn[direction]) % 4

                                if direction != 1: # if not forward, add turning to route instructions
                                    route_instructions.append([turn_angle[direction], orientation[index]])

                            # update position and add to route instructions
                            x, y = x_next, y_next
                            route_instructions.append((x, y))

                            # break out of loop as we found the next node
                            break

                # check if we visited the start node
                if (x, y) == start_pos:
                    visited_start_counter += 1
                    if visited_start_counter == 4:
                        # impossible to escape, exit program
                        return []
                 

            # set solution to route instructions
            self._solution = route_instructions

            print(route_instructions)
            print("Calculated Left Hand Algo")
            return route_instructions
