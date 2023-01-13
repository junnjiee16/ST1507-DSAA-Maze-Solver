import turtle
from classes.utils import Utils
from classes.map import Map
from classes.pathfinder import Pathfinder
from classes.mazegraph import MazeGraph
from classes.drone import Drone
from classes.dronecontroller import DroneController


# class to control the logic of the program
class Application:
    # metadata for the program
    def __init__(self, program_name, authors, class_name):
        self.program_name = program_name
        self.authors = authors
        self.class_name = class_name
        self.file_name = None
    
    def useFile(self, file_name):
        self.file_name = file_name

    def startProgram(self, window_size_x, window_size_y):
        if self.file_name == None:
            print("Error: No file selected")
            return

        # open file
        map_text = Utils.readFile(self.file_name)
        if map_text == None:
            return

        # create the turtle screen
        window = turtle.Screen()
        window.title(f"{self.program_name}: Done by {self.authors}, {self.class_name}") # create the titlebar
        window.setup(window_size_x, window_size_y)

        # create map
        map_object = Map(map_text)

        # draw map
        map_object.draw()

        # create graph
        graph = Utils.map_to_graph(map_object.processed_map)

        # create pathfinder
        pathfinder = Pathfinder()
        solution = pathfinder.solve_maze(graph, map_object.start_position, map_object.end_position, 0)
        print(solution)

        # spawn drone
        drone = DroneController.spawnTurtleDrone(map_object.start_position)

        # move drone to end using solution
        DroneController.driveDrone(drone, solution)


        # this must be the last line in the turtle program
        window.mainloop()