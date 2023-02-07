from classes.pathfinder import Pathfinder

# inherit pathfinder class
class LeftHandPathfinder(Pathfinder):
    def __init__(self):
        super().__init__()
        self._algorithm_name = "Left Hand Algorithm"


    def solve(self, map_graph):
        if self._solution != None:
            return self._solution
        else:
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

            # keep track of how to turn the compass and the direction
            # ordered by left, forward, right, back
            turn = [-1, 0, 1, 2]
            turn_angle = [-90, 0, 90, 180]

            # set starting orientation to east (index of 1), this is default orientation the pen will face in turtle when it first starts
            # keep track of index in compass array, so that we can get index in O(1) time instead of using .index() which is O(n)
            # when changing index, always mod by 4 to keep it within range
            index = 1
            
            # while current position is not the end position, keep moving
            while (x, y) != map_graph.end_pos:
                # get current orientation
                current_orientation = compass[index]

                # get all neighbors of current position
                neighbors = list(map_graph.neighbors((x, y)))

                # if neighbors is 4, means all 4 directions are available, always turn left
                if len(neighbors) == 4:
                    # update the new orientation, turn left means index 0
                    index = (index + turn[0]) % 4

                    # store the new orientation of the drone, as well as its turn angle
                    route_instructions.append([turn_angle[0], orientation[index]])

                    # update current position and add new position to route instructions
                    x, y = x + current_orientation[0][0], y + current_orientation[0][1]
                    route_instructions.append((x, y))


                # else if 1, 2 or 3 neighbours, we need to check every direction, starting from left > forward > right > back
                else:
                    # direction is in order of left, forward, right, back
                    for direction in range(len(current_orientation)):
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

                                if direction != 1: # if not forward, add to route instructions
                                    # store the new orientation of the drone as well as the angle to turn
                                    route_instructions.append([turn_angle[direction], orientation[index]])

                            # update position and add to route instructions
                            x, y = x_next, y_next
                            route_instructions.append((x, y))

                            # break out of loop as we found the next node
                            break

            # set solution to route instructions
            self._solution = route_instructions

            print(route_instructions)
            print("Calculated Left Hand Algo")
            return route_instructions
