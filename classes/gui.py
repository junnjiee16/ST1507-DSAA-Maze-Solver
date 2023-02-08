import turtle
from classes.utils import Utils
from classes.mazegenerator import MazeGenerator
from classes.map import Map

class GUI:
    '''
    Handles all GUI related events
    Parameters:
        screen (turtle.Screen): the screen that the GUI is connected to
    Attributes:
        __moveDrone (bool): whether or not the drone should move
        __changeAlgo (bool): whether or not the algorithm should change
        screen (turtle.Screen): the screen that the GUI is connected to
    '''
    def __init__(self, screen):
        self.__moveDrone = False
        self.__changeAlgo = False
        self.__activate_random_obstacles = False
        self.__generate_maze = False
        self.__activate_tsp = False
        self.__screen = screen # gui NEEDS to know what screen it is connected to so that it can call the screen's ontimer method to capture events

    def command_move_drone(self):
        self.__moveDrone = True

    def command_change_algorithm(self):
        self.__changeAlgo = True

    def command_activate_random_maze(self):
        self.__generate_maze = True

    def command_activate_random_obstacles(self):
        if self.__activate_random_obstacles == False:
            self.__activate_random_obstacles = True
        else:
            self.__activate_random_obstacles = False

    def command_activate_tsp(self):
        if self.__activate_tsp == False:
            self.__activate_tsp = True

    # extra feature
    def tsp_event_listener(self, drone_controller, renderer, drone, tsp_pathfinder):
        if self.__activate_tsp == True:
            # read the map graph and create a new map just for TSP
            # this is because the map graph will have multiple end points
            # create new Map just for TSP

            map_layout, start, ends = Utils.readMapFile("map_files/tsp.txt", multiple_end_points=True)

            tsp_map = Map(map_layout, start, ends)

            # map to graph
            map_graph = Utils.mapToGraph(tsp_map)

            # change the start pos of map graph to the current position of the drone
            solution = tsp_pathfinder.solve(map_graph, update_solution=True, drone_orientation=drone.orientation)
            drone_controller.instructions = solution

            # reset drone
            drone.reset()

            # rendering stuff
            renderer.render_map(tsp_map)
            renderer.clear_guidelight() # clear guidelight if any
            renderer.render_drone(drone, spawn=True) # spawn drone

            # rendering stuff
            renderer.clear_guidelight()


    def move_drone_event_listener(self, drone_controller, renderer, drone, pathfinders, terrain_changer, map_graph):
        '''
        Event listener for the move drone command
        
        Parameters:
            drone_controller (DroneController): controller to execute instructions for the drone
            render_drone (function): function to render the drone
            drone (Drone): drone object to be controlled
            pathfinders (Pathfinder): Pathfinder object that contains all the algorithms
        Returns:
            None
        '''
        if self.__moveDrone == True and drone.current_pos != map_graph.end_pos:
            if self.__changeAlgo == False:
                # tell drone controller to execute the next instruction
                drone_controller.execute_instruction()
                renderer.render_drone(drone)

                # extra feature to add random obstacles
                if self.__activate_random_obstacles == True and drone.current_pos != map_graph.end_pos:
                    # change road to wall and remove the node from graph
                    node_info = terrain_changer.road_to_wall(drone.current_pos)
                    map_graph.remove_node(node_info[0])
                    solution = pathfinders.current.solution

                    # check if node removed exists in the solution
                    if node_info[0] in solution:
                        # change the start pos of map graph to the current position of the drone
                        map_graph.start_pos = drone.current_pos
                        solution = pathfinders.current.solve(map_graph, update_solution=True, drone_orientation=drone.orientation)
                        drone_controller.instructions = solution
                    
                    # rendering stuff
                    renderer.clear_guidelight() # clear guidelight if any
                    # check if there is guidelight to be rendered
                    if pathfinders.current.id == 1 and solution != []:
                        renderer.render_guidelight(solution)

                    # if drone not at end
                    if drone.current_pos != map_graph.end_pos:
                        renderer.render_no_solution(solution)

                    # render the updated block
                    renderer.render_map_block(node_info[0][0], node_info[0][1], node_info[1])

                # update the title bar
                self.__screen.title(f"{pathfinders.current.algorithm_name}, Steps Taken: {drone.steps_taken}")

            self.__moveDrone = False # set to false

        self.__screen.ontimer(lambda: self.move_drone_event_listener(drone_controller, renderer, drone, pathfinders, terrain_changer, map_graph), 10)


    def change_algorithm_event_listener(self, drone_controller, renderer, drone, pathfinders, map_graph):
        '''
        Event listener for the change algorithm command
        
        Parameters:
            drone_controller (DroneController): controller to execute instructions for the drone
            render_drone (function): function to render the drone
            drone (Drone): drone object to be controlled
            pathfinders (Pathfinder): Pathfinder object that contains all the algorithms
            map_graph (Graph): Graph object that contains the map
        
        Returns:
            None
        '''
        if self.__changeAlgo == True:
            # change current algorithm
            pathfinders.next()

            # reset drone
            drone.reset()

            map_graph.start_pos = drone.current_pos
            solution = pathfinders.current.solve(map_graph, update_solution=True)

            drone_controller.instructions = solution # reset drone controller with new instructions

            renderer.render_no_solution(solution)

            # display the guidelight for shortest path algorithm
            if pathfinders.current.id == 1:
                # render guidelight for solution if shortest path is being used
                renderer.clear_dronetrail(drone.name)
                renderer.render_guidelight(solution)
                # respawn drone sprite at start
                renderer.render_drone(drone, spawn=True)
            
            else:
                renderer.clear_guidelight()
                # respawn drone sprite at start
                renderer.render_drone(drone, spawn=True)
                if solution != []:
                    renderer.render_dronetrail(drone.name)

            # reset title bar and boolean
            self.__screen.title(f"{pathfinders.current.algorithm_name}, Steps Taken: {drone.steps_taken}")
            self.__changeAlgo = False

        self.__screen.ontimer(lambda: self.change_algorithm_event_listener(drone_controller, renderer, drone, pathfinders, map_graph), 10)

    def random_maze_event_listener(self):
        if self.__generate_maze == True:
            size = self.get_input("Generate Maze", "Enter the size of the maze (e.g. 10): ")
            size = int(size)

            maze = MazeGenerator(size, size)
            maze.__generate_maze(0, 0)
            maze.write_to_file()

            self.__generate_maze = False
            
        self.__screen.ontimer(lambda: self.random_maze_event_listener(), 10)


    
    def get_input(self, title, prompt):
        result = turtle.textinput(title, prompt)
        return result