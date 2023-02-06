class GUI:
    def __init__(self, screen):
        self.moveDrone = False
        self.changeAlgo = False
        self.screen = screen # gui NEEDS to know what screen it is connected to so that it can call the screen's ontimer method to capture events

    def command_move_drone(self):
        self.moveDrone = True

    def command_change_algorithm(self):
        self.changeAlgo = True


    def move_drone_event_listener(self, drone_controller, render_drone, drone, pathfinders):
        if self.moveDrone == True:
            # tell drone controller to execute the next instruction
            drone_controller.execute_instruction()
            render_drone(drone)

            # update the title bar
            self.screen.title(f"{pathfinders.current.algorithm_name}, Steps Taken: {drone.steps_taken}")

            self.moveDrone = False

        self.screen.ontimer(lambda: self.move_drone_event_listener(drone_controller, render_drone, drone, pathfinders), 10)


    def change_algorithm_event_listener(self, drone_controller, render_drone, drone, pathfinders, map_graph):
        if self.changeAlgo == True:
            # change current algorithm
            pathfinders.next()

            # reset drone controller with new instructions
            drone_controller.instructions = pathfinders.current.solve(map_graph)

            # reset drone
            drone.reset()

            # respawn drone sprite at start
            render_drone(drone, spawn=True)

            # reset title bar
            self.screen.title(f"{pathfinders.current.algorithm_name}, Steps Taken: {drone.steps_taken}")

            self.changeAlgo = False

        self.screen.ontimer(lambda: self.change_algorithm_event_listener(drone_controller, render_drone, drone, pathfinders, map_graph), 10)