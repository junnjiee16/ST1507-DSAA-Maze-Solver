class GUI:

    def move_drone(drone_controller, render_drone):
        # tell drone controller to execute the next instruction
        drone_controller.execute_instruction()
        render_drone = True