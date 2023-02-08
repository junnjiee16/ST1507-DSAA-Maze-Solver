import turtle

# program logic imports
from classes.utils import Utils
from classes.map import Map
from classes.drone import Drone
from classes.dronecontroller import DroneController
from classes.objectstatemanager import ObjectStateManager

from classes.terrainchanger import TerrainChanger

# pathfinder imports
from classes.lefthandpathfinder import LeftHandPathfinder
from classes.shortestpathfinder import ShortestPathfinder
from classes.travellingsalesmanpathfinder import TravellingSalesmanPathfinder

# graphics related imports
from classes.sprite import Sprite
from classes.renderer import Renderer

# user interaction imports
from classes.gui import GUI


# class to control the logic of the program
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
    # metadata for the program
    def __init__(self, program_name, authors, class_name):
        self.program_name = program_name
        self.authors = authors
        self.class_name = class_name
        self.title = f"{self.program_name}: Done by {self.authors} {self.class_name}"


    def startProgram(self):
        """
        This the main method of the main program and runs the program logic.
        Parameters:
            file_name (str): name of the map file to be read
        Returns:
            None
        """
        # create turtle screen and display title
        window = turtle.Screen()

        ### -------------------------------------------------------
        ### GUI CLASS: CAPTURES KEY PRESS EVENTS
        ### -------------------------------------------------------
        gui = GUI(window)
        filename = gui.get_input("Map File Input", "Please enter file name:")

        ### -------------------------------------------------------
        ### READ AND SCAN MAP FILE
        ### -------------------------------------------------------
        print("Reading and scanning map file")
        map_text, start_pos, end_pos = Utils.readMapFile("map_files/" + filename)
        if map_text == None:
            return

        ### -------------------------------------------------------
        ### RUN ALL PROGRAM LOGIC FIRST BEFORE RENDERING ANYTHING
        ### -------------------------------------------------------
        # instantiate map and drone objects
        map = Map(map_text, start_pos, end_pos)
        drone_name = "drone1"
        drone = Drone(drone_name, map.start_pos)
        drone_controller = DroneController(drone)

        # get graph from map
        map_graph = Utils.map_to_graph(map)

        # instantiate terrain changer object
        terrain_changer = TerrainChanger(map, map_graph)

        # instantiate lefthand and shortest pathfinder objects
        pathfinders = ObjectStateManager([LeftHandPathfinder(), ShortestPathfinder()])

        # tsp pathfinder is initialized outside the object state manager, as it is not required to be cycled through
        tsp_pathfinder = TravellingSalesmanPathfinder()

        solution = pathfinders.current.solve(map_graph)

        # set instructions for drone controller
        drone_controller.instructions = solution


        ### -------------------------------------------------------
        ### LOADING NECCESSARY GRAPHICS ASSETS
        ### -------------------------------------------------------
        renderer = Renderer(pixel_size=25)
        pixel_ratio = renderer.pixel_size / 20 # 20 pixels is 1 unit for shapesize()

        # load all required graphic objects into renderer
        renderer.add_sprite(Sprite(name=drone_name, color="red", current_pos=drone.current_pos, orientation=drone.orientation))
        renderer.add_sprite(Sprite(name="writer", color="black", pencolor="black", speed=0))

        renderer.add_sprite(Sprite(name="wall", color="grey", pencolor="black", shape="square", shapesize=pixel_ratio, speed=0))
        renderer.add_sprite(Sprite(name="road", color="white", pencolor="black", shape="square", shapesize=pixel_ratio, speed=0))
        renderer.add_sprite(Sprite(name="startpoint", color="#61ff6e", pencolor="black", shape="square", shapesize=pixel_ratio, speed=0))
        renderer.add_sprite(Sprite(name="endpoint", color="#56defc", pencolor="black", shape="square", shapesize=pixel_ratio, speed=0))
        
        renderer.add_sprite(Sprite(name="guidelight", color="yellow", pencolor="black", shape="circle", shapesize=pixel_ratio, speed=0))


        ### -------------------------------------------------------
        ### RENDERING GRAPHICS
        ### -------------------------------------------------------
        title_bar = f"{pathfinders.current.algorithm_name}, Steps Taken: {drone.steps_taken}"
        window.title(title_bar)

        # use Renderer to render map, title and spawn the drone
        renderer.render_map(map)
        renderer.render_title(self.title)
        renderer.render_drone(drone, spawn=True)
        renderer.render_dronetrail(drone.name)
        renderer.render_no_solution(solution)


        ### -------------------------------------------------------
        ### CATCH KEY PRESS EVENTS, THIS IS THE "MAIN LOOP" OF THE PROGRAM
        ### -------------------------------------------------------

        ### series of commands to be executed on key press

        # this activates on "m" key press, it moves the drone, renders new position and updates the title bar
        gui.move_drone_event_listener(drone_controller, renderer, drone, pathfinders, terrain_changer, map_graph)

        # this activates on "Tab" key press, it changes the pathfinder algorithm and updates the title bar
        gui.change_algorithm_event_listener(drone_controller, renderer, drone, pathfinders, map_graph)

        # this activates the TSP algorithm, once this is activated, Tab out is disabled
        gui.tsp_event_listener(drone_controller, renderer, drone, tsp_pathfinder)


        # listen for key presses
        window.onkey(
            gui.command_move_drone, "m"
        )

        window.onkeypress(
            gui.command_move_drone, "n"
        )

        window.onkey(
            gui.command_change_algorithm, "Tab"
        )

        # Extra feature activation keys (Jun Jie)
        window.onkey(
            gui.command_activate_tsp, "1"
        )

        window.onkey(
            gui.command_activate_random_obstacles, "2"
        )

        # Extra feature activation keys (Tim)
        window.onkey(
            gui.command_activate_random_maze, "3"
        )

        # window.onkey(
        #     gui.2nd_feature, "4"
        # )

        window.listen()

        ### this must be the last line in the turtle program
        window.mainloop()
