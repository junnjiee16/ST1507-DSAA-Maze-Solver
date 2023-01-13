import turtle
from classes.drone import Drone
from classes.doublyCircularLinkedList import DoublyCircularLinkedList

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
            self.__leftHandAlgoSolution = self.__LeftHandAlgorithm(graph, start_position, end_position)
            return self.__leftHandAlgoSolution


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
        route_instructions = []

        # keep track of orientation when moving through maze
        compass = DoublyCircularLinkedList()
        compass.add("E") # east
        compass.add("S") # south
        compass.add("W") # west
        compass.add("N") # north

        # set starting orientation to east, this is default orientation the pen will face in turtle when it first starts
        current_orientation = compass.head
        
        while (x, y) != end_pos:
            print(x, y)
            ### call different functions based on orientation
            # check if can go left
            if current_orientation.data == "N":
                next_node = self.go_west((x, y))

            elif current_orientation.data == "E":
                next_node = self.go_north((x, y))

            elif current_orientation.data == "S":
                next_node = self.go_east((x, y))

            elif current_orientation.data == "W":
                next_node = self.go_south((x, y))

            if next_node in graph:
                x, y = next_node # update current position
                current_orientation = current_orientation.prev # turn compass to left
                route_instructions.append("L") # append the side to turn the drone to
                route_instructions.append(next_node) # append the next coordinates to go to
                continue

            # check if can go forward   
            if current_orientation.data == "N":
                next_node = self.go_north((x, y))

            elif current_orientation.data == "E":
                next_node = self.go_east((x, y))

            elif current_orientation.data == "S":
                next_node = self.go_south((x, y))

            elif current_orientation.data == "W":
                next_node = self.go_west((x, y))

            if next_node in graph:
                x, y = next_node # update current position
                # no need to change orientation as drone is going straight
                route_instructions.append(next_node) # append the next coordinates to go to
                continue

            # check if can go right
            if current_orientation.data == "N":
                next_node = self.go_east((x, y))
            
            elif current_orientation.data == "E":
                next_node = self.go_south((x, y))

            elif current_orientation.data == "S":
                next_node = self.go_west((x, y))

            elif current_orientation.data == "W":
                next_node = self.go_north((x, y))

            if next_node in graph:
                x, y = next_node # update current position
                current_orientation = current_orientation.next # turn compass to right
                route_instructions.append("R") # append the side to turn the drone to
                route_instructions.append(next_node)
                continue

            # if all fails, go opposite direction
            if current_orientation.data == "N":
                next_node = self.go_south((x, y))

            elif current_orientation.data == "E":
                next_node = self.go_west((x, y))
            
            elif current_orientation.data == "S":
                next_node = self.go_north((x, y))

            elif current_orientation.data == "W":
                next_node = self.go_east((x, y))

            x, y = next_node # update current position
            current_orientation = current_orientation.next.next # turn compass to opposite
            route_instructions.append("B") # append the side to turn the drone to
            route_instructions.append(next_node) # append the next coordinates to go to

        return route_instructions


    def __ShortestPathAlgorithm(self, map_graph, start_position, end_position):
        pass