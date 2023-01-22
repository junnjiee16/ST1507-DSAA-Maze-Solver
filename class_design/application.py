import turtle
from classes.utils import Utils
from classes.map import Map
from classes.pathfinder import Pathfinder
from classes.drone import Drone
from classes.dronecontroller import DroneController


# class to control the logic of the program
class Application:
    # metadata for the program
    def __init__(self, program_name, authors, class_name):
        self.program_name = program_name
        self.authors = authors
        self.class_name = class_name
        self.title = f"{self.program_name}: Done by {self.authors}, {self.class_name}"

    def startProgram(self, file_name=None):
        if file_name == None:
            print("Error: No file selected")
            return

        # open file
        print("Reading and scanning map file")
        map_text, start_coords, end_coords = Utils.readMapFile(file_name)
        if map_text == None:
            return

        # create the turtle screen
        window = turtle.Screen()
        window.title(self.title) # create the titlebar
        # window.setup(width=1.0, height=1.0)

        # instantiate map
        map_object = Map(map_text, start_coords, end_coords)

        # create graph from map layout
        print("Generating graph from map")
        graph = Utils.map_to_graph(map_object.map_layout)

        # instantiate pathfinder object
        print("Instantiating pathfinder object")
        pathfinder = Pathfinder()

        # draw map on screen
        print("Drawing map")
        map_object.draw() # this uses turtle's Turtle object to place down tiles on the map

        # solve maze
        print("Solving the maze")
        solution = pathfinder.solve_maze(graph, map_object.start_position, map_object.end_position, 0) # 0 = Left Hand Algorithm, 1 = Shortest Path Algorithm
        print(solution)

        # show the solution
        print("Animating solution")
        # instantiate Drone object
        # drone = Drone()
        # drone_control = DroneController(drone, solution)
        # drone_control.placeDrone(map_object.start_position)
        drone = turtle.Turtle()
        drone.goto((2, 1))

        # this must be the last line in the turtle program
        window.mainloop()