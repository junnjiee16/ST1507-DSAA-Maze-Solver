import turtle
from classes.drone import Drone

# object to guide the arrow through the maze with algorithm of choice
class Pathfinder:
    def __init__(self):
        self.__leftHandAlgoSolution = None
        self.__shortestPathSolution = None

    # getters and setter functions
    @property
    def leftHandAlgoSolution(self):
        return self.__leftHandAlgoSolution
    
    @leftHandAlgoSolution.setter
    def leftHandAlgoSolution(self, value):
        self.__leftHandAlgoSolution = value

    @property
    def shortestPathSolution(self):
        return self.__shortestPathSolution

    @shortestPathSolution.setter
    def shortestPathSolution(self, value):
        self.__shortestPathSolution = value


    # solve the maze using preferred algorithm
    def solve_maze(self, graph, start_position, end_position, algorithm_choice):
        if algorithm_choice == 0:
            return self.__LeftHandAlgorithm(graph, start_position, end_position)


    # helper functions for the left hand algorithm
    def go_north(self, current_node):
        return (current_node[0], current_node[1] + 1)

    def go_east(self, current_node):
        return (current_node[0] + 1, current_node[1])

    def go_south(self, current_node):
        return (current_node[0], current_node[1] - 1)

    def go_west(self, current_node):
        return (current_node[0] - 1, current_node[1])


    def __LeftHandAlgorithm(self, graph, start_pos, end_pos):
        x, y = start_pos

        # array to store steps
        coordinate_steps = []

        # keep track of orientation
        north = 90
        east = 0
        south = 270
        west = 180
        direction = ["N", "E", "S", "W"]

        direction_index = 0
        current_orientation = direction[direction_index]
        
        while (x, y) != end_pos:
            print(current_orientation)
            print(x, y)
            ### call different functions based on orientation
            # check if can go left
            if current_orientation == "N":
                next_node = self.go_west((x, y))
                new_orientation = west

            elif current_orientation == "E":
                next_node = self.go_north((x, y))
                new_orientation = north

            elif current_orientation == "S":
                next_node = self.go_east((x, y))
                new_orientation = east

            else:
                next_node = self.go_south((x, y))
                new_orientation = south

            if next_node in graph:
                x, y = next_node
                coordinate_steps.append(new_orientation)
                coordinate_steps.append((x, y))
                direction_index -=1
                current_orientation = direction[direction_index]
                continue

            # check if can go forward   
            if current_orientation == "N":
                next_node = self.go_north((x, y))

            elif current_orientation == "E":
                next_node = self.go_east((x, y))

            elif current_orientation == "S":
                next_node = self.go_south((x, y))

            else:
                next_node = self.go_west((x, y))

            if next_node in graph:
                x, y = next_node
                coordinate_steps.append((x, y))
                continue

            # check if can go right
            if current_orientation == "N":
                next_node = self.go_east((x, y))
                new_orientation = east
            
            elif current_orientation == "E":
                next_node = self.go_south((x, y))
                new_orientation = south

            elif current_orientation == "S":
                next_node = self.go_west((x, y))
                new_orientation = west

            else:
                next_node = self.go_north((x, y))
                new_orientation = north

            if next_node in graph:
                x, y = next_node
                coordinate_steps.append(new_orientation)
                coordinate_steps.append((x, y))
                direction_index += 1
                current_orientation = direction[direction_index]
                continue

            # if all fails, go opposite direction
            if current_orientation == "N":
                next_node = self.go_south((x, y))
                new_orientation = south

            elif current_orientation == "E":
                next_node = self.go_west((x, y))
                new_orientation = west
            
            elif current_orientation == "S":
                next_node = self.go_north((x, y))
                new_orientation = north

            else:
                next_node = self.go_east((x, y))
                new_orientation = east

            x, y = next_node
            coordinate_steps.append(new_orientation)
            coordinate_steps.append((x, y))
            direction_index += 2
            current_orientation = direction[direction_index]

        return coordinate_steps





    def __ShortestPathAlgorithm(self, map_graph, start_position, end_position):
        pass