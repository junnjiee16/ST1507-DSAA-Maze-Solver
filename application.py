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


# class to control the logic of the program
class Application:
    # metadata for the program
    def __init__(self, program_name, authors, class_name):
        self.program_name = program_name
        self.authors = authors
        self.class_name = class_name
        self.title = f"{self.program_name}: Done by {self.authors}, {self.class_name}"

    def startProgram(self, file_name):

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
        # load all graphic objects
        wall_drawing = Sprite(color="grey")
        road_drawing = Sprite(color="white")
        start_drawing = Sprite(color="#61ff6e") # green
        end_drawing = Sprite(color="#56defc") # blue


        # create turtle screen and display title
        window = turtle.Screen()
        window.title(self.title)

        # use Renderer to render map and spawn the drone
        Renderer.render_map(map.layout)
        drone_sprite = Renderer.render_drone(drone)



        ### -------------------------------------------------------
        ### CATCH KEY PRESS EVENTS
        ### -------------------------------------------------------
        window.onkey(
            lambda: 
                drone_controller.move() or
                Renderer.render_drone(drone, drone_sprite), 
            "m"
        )


        ### this must be the last line in the turtle program
        window.listen()
        window.mainloop()

        # # create the turtle screen
        # window = Screen(self.title)

        # # instantiate map
        # map = Map(map_text, start_coords, end_coords)

        # # create graph from map layout
        # print("Generating graph from map")
        # graph = Utils.map_to_graph(map.layout)

        # # instantiate pathfinder object
        # print("Instantiating pathfinder object")
        # pathfinder = Pathfinder(graph, map.start_position, map.end_position)

        # # draw map on screen
        # print("Drawing map")
        # map.draw() # this uses turtle's Turtle object to place down tiles on the map

        # # solve maze
        # solution = pathfinder.maze_solution() # 0 = Left Hand Algorithm, 1 = Shortest Path Algorithm

        # # show the solution
        # # instantiate Drone object
        # drone = Drone(solution, map.start_position)

        # # update title bar after everything is initialized
        # window.update_title(f"{self.title}, {pathfinder.algo_name()} - Steps: {drone.steps_taken}")

        # # set key event handlers
        # # command drone to execute next step in solution and update title bar
        # window.set_key(
        #     lambda: 
        #         drone.move() or 
        #         window.update_title(f"{self.title}, {pathfinder.algo_name()} - Steps: {drone.steps_taken}"), 
        #     "m"
        # )

        # # TAB key: reset drone, change algorithm, update solution, update title bar
        # window.set_key(
        #     lambda: 
        #         drone.reset() or 
        #         pathfinder.change_algo() or 
        #         drone.set_instructions(pathfinder.maze_solution()) or
        #         window.update_title(f"{self.title}, {pathfinder.algo_name()} - Steps: {drone.steps_taken}"), 
        #     "Tab"
        # )

        # # this must be the last line in the turtle program
        # window.mainloop()
