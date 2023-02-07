

class GUI:
    '''
    Handles all GUI related events

    Parameters:
        screen (turtle.Screen): the screen that the GUI is connected to

    Attributes:
        moveDrone (bool): whether or not the drone should move
        changeAlgo (bool): whether or not the algorithm should change
        screen (turtle.Screen): the screen that the GUI is connected to
    '''
    def __init__(self, screen):
        self.moveDrone = False
        self.changeAlgo = False
        self.generateMaze = False
        # gui NEEDS to know what screen it is connected to so that it can 
        # call the screen's ontimer method to capture events
        self.screen = screen 

    def command_move_drone(self):
        self.moveDrone = True  # set moveDrone to True so that the drone will move

    def command_change_algorithm(self):
        self.changeAlgo = True  # set changeAlgo to True so that the algorithm will change

    def move_drone_event_listener(self, drone_controller, render_drone, drone, pathfinders):
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
        if self.moveDrone == True:
            drone_controller.execute_instruction()  # execute the next instruction
            render_drone(drone)

            # update the title bar
            self.screen.title(f"{pathfinders.current.algorithm_name}, Steps Taken: {drone.steps_taken}")
            self.moveDrone = False  # reset moveDrone to False, drone wont move

        # call this function again after 10 milliseconds
        self.screen.ontimer(lambda: self.move_drone_event_listener(drone_controller, render_drone, drone, pathfinders), 10)


    def change_algorithm_event_listener(self, drone_controller, render_drone, drone, pathfinders, map_graph):
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
        if self.changeAlgo == True:
            pathfinders.next()  # change algorithm
            drone_controller.instructions = pathfinders.current.solve(map_graph)  # get new instructions
            drone.reset()  # reset drone

            render_drone(drone, spawn=True)  # respawn drone sprite at start

            # reset title bar
            self.screen.title(f"{pathfinders.current.algorithm_name}, Steps Taken: {drone.steps_taken}")

            self.changeAlgo = False  # reset changeAlgo to False, algorithm wont change

        # call this function again after 10 milliseconds
        self.screen.ontimer(lambda: self.change_algorithm_event_listener(drone_controller, render_drone, drone, pathfinders, map_graph), 10)