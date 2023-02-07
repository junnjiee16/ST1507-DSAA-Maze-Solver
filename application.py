import turtle

# program logic imports
from classes.utils import Utils
from classes.map import Map
from classes.drone import Drone
from classes.dronecontroller import DroneController
from classes.objectstatemanager import ObjectStateManager

# pathfinder imports
from classes.lefthandpathfinder import LeftHandPathfinder
from classes.shortestpathfinder import ShortestPathfinder

# graphics related imports
from classes.sprite import Sprite
from classes.renderer import Renderer

# user interaction imports
from classes.gui import GUI

class Application:
    """
    This class contols the logic of the program

    Parameters:
        program_name (str):
        authors (str):
        class_name (str):

    Attributes:
        program_name (str):
        authors (str):
        class_name (str):
        title (str):
    """
    def __init__(self, program_name, authors, class_name):
        self.program_name = program_name  # name of the program
        self.authors = authors  # authors of the program
        self.class_name = class_name  # class name of the program
        self.title = f"{self.program_name}: Done by {self.authors} {self.class_name}"  # title of the program


    def startProgram(self, file_name):
        """
        This the main method of the main program and runs the program logic.

        Parameters:
            file_name (str): name of the map file to be read

        Returns:
            None
        """
        print("Reading and scanning map file")
        map_text, start_pos, end_pos = Utils.readMapFile(file_name)  # read map file
        if map_text == None:
            return  # if map file is not found, exit program


        # -------------------------------------------------------
        # RUN ALL PROGRAM LOGIC FIRST BEFORE RENDERING ANYTHING
        # -------------------------------------------------------
        # instantiate map and drone objects
        map = Map(map_text, start_pos, end_pos)  # instantiate map object with map text
        drone_name = "drone1"  # name of the drone
        drone = Drone(drone_name, map.start_pos)  # instantiate drone object
        drone_controller = DroneController(drone)  # instantiate drone controller object

        map_graph = Utils.map_to_graph(map)  # get graph from map
        # instantiate lefthand and shortest pathfinder objects
        pathfinders = ObjectStateManager([LeftHandPathfinder(), ShortestPathfinder()])  
        solution = pathfinders.current.solve(map_graph)  # solve map with current pathfinder algorithm

        drone_controller.instructions = solution  # set instructions for drone controller
        print(len(solution))

        # -------------------------------------------------------
        # LOADING NECCESSARY GRAPHICS ASSETS
        # -------------------------------------------------------
        renderer = Renderer(pixel_size=25)
        pixel_ratio = renderer.pixel_size / 20 # 20 pixels is 1 unit for shapesize()

        # load all required graphic objects into renderer
        renderer.add_sprite(Sprite(name=drone_name, color="red", current_pos=drone.current_pos, orientation=drone.orientation))
        renderer.add_sprite(Sprite(name="wall", color="grey", pencolor="black", shape="square", shapesize=pixel_ratio, speed=0))
        renderer.add_sprite(Sprite(name="road", color="white", pencolor="black", shape="square", shapesize=pixel_ratio, speed=0))
        renderer.add_sprite(Sprite(name="startpoint", color="#61ff6e", pencolor="black", shape="square", shapesize=pixel_ratio, speed=0))
        renderer.add_sprite(Sprite(name="endpoint", color="#56defc", pencolor="black", shape="square", shapesize=pixel_ratio, speed=0))

        # -------------------------------------------------------
        # RENDERING GRAPHICS
        # -------------------------------------------------------
        # create turtle screen and display title
        window = turtle.Screen()

        title_bar = f"{pathfinders.current.algorithm_name}, Steps Taken: {drone.steps_taken}"
        window.title(title_bar)

        # use Renderer to render map, title and spawn the drone
        renderer.render_map(map)
        renderer.render_title(self.title, map.y_length)
        renderer.render_drone(drone, spawn=True)

        gui = GUI(window)  # instantiate GUI object


        ### -------------------------------------------------------
        ### CATCH KEY PRESS EVENTS, THIS IS THE "MAIN LOOP" OF THE PROGRAM
        ### -------------------------------------------------------

        ### series of commands to be executed on key press

        # this activates on "m" key press, it moves the drone, renders new position and updates the title bar
        gui.move_drone_event_listener(drone_controller, renderer.render_drone, drone, pathfinders)

        # this activates on "Tab" key press, it changes the pathfinder algorithm and updates the title bar
        gui.change_algorithm_event_listener(drone_controller, renderer.render_drone, drone, pathfinders, map_graph)

        # listen for key presses
        window.onkey(gui.command_move_drone, "m")  # move drone 
        window.onkey(gui.command_change_algorithm, "Tab")  # change algorithm

        # # Extra feature activation keys (Jun Jie)
        # window.onkey(
        #     gui.command_activate_multiple_endpoints_problem, "1"
        # )

        # window.onkey(
        #     gui.command_activate_random_obstacles_problem, "2"
        # )

        window.listen()

        ### this must be the last line in the turtle program
        window.mainloop()
