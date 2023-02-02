from classes.pathfinder import Pathfinder

# inherit pathfinder class
class LeftHandPathfinder(Pathfinder):
    def __init__(self):
        super().__init__()
        self.__algorithm_name = "Left Hand Algorithm"


    def solve(self, map_graph):
        if self.__solution != None:
            return self.__solution

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
            # compass = ["N", "E", "S", "W"]
            compass = [facingNorth, facingEast, facingSouth, facingWest]
            headings = [90, 0, 270, 180]

            # keep track of how to turn the compass and the direction
            # ordered by left, forward, right, back
            turn = [-1, 0, 1, 2]
            turn_angle = [-90, 0, 90, 180]

            # set starting orientation to east (index of 1), this is default orientation the pen will face in turtle when it first starts
            # keep track of index in compass array, so that we can get index in O(1) time instead of using .index() which is O(n)
            # when changing index, always mod by 4 to keep it within range
            index = 1
            
            # keep finding the next node to go to until we reach the end
            while (x, y) != map_graph.end_pos:
                # get current orientation
                current_orientation = compass[index]

                # find all neighbors of current node, convert to list as function returns a iterator
                neighbors = list(map_graph.neighbors((x, y)))

                # if neighbors is 4, means all 4 directions are available, always turn left
                if len(neighbors) == 4:
                    # update current position and add to route instructions
                    x, y = x + current_orientation[0][0], y + current_orientation[0][1]
                    route_instructions.append(turn_angle[0]) # turn left first
                    route_instructions.append((x, y))

                    # update the new orientation, turn left means index 0
                    index = (index + turn[0]) % 4

                # else if 1, 2 or 3 neighbours, we need to check every direction, starting from left > forward > right > back
                else:
                    # direction is in order of left, forward, right, back
                    for direction in range(len(current_orientation)):
                        # check if the next node in the direction exists
                        x_next, y_next = x + current_orientation[direction][0], y + current_orientation[direction][1]

                        if map_graph.has_node((x_next, y_next)):
                            # update position and add to route instructions
                            x, y = x_next, y_next
                            route_instructions.append(turn_angle[direction]) # keep track of turn angle
                            route_instructions.append((x, y))

                            # update the new orientation
                            index = (index + turn[direction]) % 4

                            # break out of loop as we found the next node
                            break

            print(route_instructions)
            print("Calculated Left Hand Algo")
            return route_instructions
