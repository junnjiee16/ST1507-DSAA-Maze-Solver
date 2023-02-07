import turtle

class GUI:
    def __init__(self, screen):
        self.moveDrone = False
        self.changeAlgo = False
        self.activate_random_obstacles = False
        self.screen = screen # gui NEEDS to know what screen it is connected to so that it can call the screen's ontimer method to capture events

    def command_move_drone(self):
        self.moveDrone = True

    def command_change_algorithm(self):
        self.changeAlgo = True

    def command_activate_random_obstacles(self):
        self.activate_random_obstacles = True


    def move_drone_event_listener(self, drone_controller, render_drone, drone, pathfinders):
        if self.changeAlgo == True:
            self.moveDrone = False

        elif self.moveDrone == True:
            # tell drone controller to execute the next instruction
            drone_controller.execute_instruction()
            render_drone(drone)

            # update the title bar
            self.screen.title(f"{pathfinders.current.algorithm_name}, Steps Taken: {drone.steps_taken}")

            self.moveDrone = False

        self.screen.ontimer(lambda: self.move_drone_event_listener(drone_controller, render_drone, drone, pathfinders), 10)


    def change_algorithm_event_listener(self, drone_controller, renderer, drone, pathfinders, map_graph):
        if self.changeAlgo == True:
            # change current algorithm
            pathfinders.next()

            # reset drone controller with new instructions
            solution = pathfinders.current.solve(map_graph)
            drone_controller.instructions = pathfinders.current.solve(map_graph)
            renderer.render_no_solution(solution)

            # reset drone
            drone.reset()

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
                renderer.render_dronetrail(drone.name)


            # reset title bar
            self.screen.title(f"{pathfinders.current.algorithm_name}, Steps Taken: {drone.steps_taken}")

            self.changeAlgo = False

        self.screen.ontimer(lambda: self.change_algorithm_event_listener(drone_controller, renderer, drone, pathfinders, map_graph), 10)


    def random_obstacles_event_listener(self):
        pass

    
    def get_input(self, title, prompt):
        result = turtle.textinput(title, prompt)
        return result