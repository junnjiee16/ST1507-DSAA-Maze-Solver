class GUI:
    def __init__(self, screen):
        self.movedrone = False
        self.screen = screen # gui NEEDS to know what screen it is connected to so that it can call the screen's ontimer method to capture events

    def command_move_drone(self):
        self.movedrone = True

    def move_drone_event_listener(self, drone_controller, render_drone, drone, algorithm_name):
        if self.movedrone == True:
            # tell drone controller to execute the next instruction
            drone_controller.execute_instruction()
            render_drone(drone)

            # update the title bar
            self.screen.title(f"{algorithm_name}, Steps Taken: {drone.steps_taken}")

            self.movedrone = False

        self.screen.ontimer(lambda: self.move_drone_event_listener(drone_controller, render_drone, drone, algorithm_name), 10)