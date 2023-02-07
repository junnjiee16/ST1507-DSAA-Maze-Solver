import turtle

# program logic imports
from classes.utils import Utils
from classes.map import Map
from classes.drone import Drone
from classes.dronecontroller import DroneController

# pathfinder imports
from classes.lefthandpathfinder import LeftHandPathfinder
from classes.shortestpathfinder import ShortestPathfinder

# media imports
from classes.sprite import Sprite
from classes.renderer import Renderer

from classes.gui import GUI


# class to control the logic of the program
class Application:
    """
    This class ...

    Parameters:
        program_name (str): name of the program

    Args:
        program_name (str): name of the program
    """
    # metadata for the program
    def __init__(self, program_name, authors, class_name):
        self.program_name = program_name
        self.authors = authors
        self.class_name = class_name
        self.title = f"{self.program_name}: Done by {self.authors}, {self.class_name}"
        self.screen = turtle.Screen()
        self.renderer = Renderer()

    def handleTimer(self):
        if bool == True:
            self.renderer.render_drone(drone)
            bool = False
        self.screen.ontimer(self.handleTimer(drone, bool), 1000)

    def startProgram(self, file_name):
        render_drone = False

        ### -------------------------------------------------------
        ### READ AND SCAN MAP FILE
        ### -------------------------------------------------------
        print("Reading and scanning map file")
        map_text, start_pos, end_pos = Utils.readMapFile(file_name)
        if map_text == None:
            return


        ### -------------------------------------------------------
        ### RUN ALL PROGRAM LOGIC FIRST BEFORE RENDERING ANYTHING
        ### -------------------------------------------------------
        # instantiate map and drone objects
        map = Map(map_text, start_pos, end_pos)
        drone = Drone(map.start_pos)
        drone_controller = DroneController(drone)

        # get graph from map
        map_graph = Utils.map_to_graph(map)

        # instantiate lefthand and shortest pathfinder objects
        lefthand_pathfinder = LeftHandPathfinder()
        shortest_pathfinder = ShortestPathfinder()

        # set current pathfinder to lefthand
        pathfinder = lefthand_pathfinder
        solution = pathfinder.solve(map_graph)

        # set instructions for drone controller
        drone_controller.instructions = solution
        print(len(solution))


        ### -------------------------------------------------------
        ### RENDERING GRAPHICS
        ### -------------------------------------------------------

        # load all required graphic objects into renderer
        self.renderer.add_sprite(Sprite(name="drone", color="red", current_pos=drone.current_pos, orientation=drone.orientation))

        self.renderer.add_sprite(Sprite(name="wall", color="grey", pencolor="black", shape="square", shapesize=24/20, speed=0))
        self.renderer.add_sprite(Sprite(name="road", color="white", pencolor="black", shape="square", shapesize=24/20, speed=0))
        self.renderer.add_sprite(Sprite(name="startpoint", color="#61ff6e", pencolor="black", shape="square", shapesize=24/20, speed=0))
        self.renderer.add_sprite(Sprite(name="endpoint", color="#56defc", pencolor="black", shape="square", shapesize=24/20, speed=0))

        # create turtle screen and display title
        # window = turtle.Screen()
        self.screen.title(self.title)

        # use Renderer to render map and spawn the drone
        self.renderer.render_map(map.layout)
        self.renderer.render_drone(drone, first_spawn=True)



        ### -------------------------------------------------------
        ### CATCH KEY PRESS EVENTS
        ### -------------------------------------------------------
        self.screen.onkey(
            lambda: 
                GUI.move_drone(drone_controller, render_drone),
            "m"
        )


        self.handleTimer(drone, render_drone)
        ### this must be the last line in the turtle program
        self.screen.listen()
        self.screen.mainloop()
