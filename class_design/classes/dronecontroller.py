import turtle

# drives the drone
class DroneController:
    def __init__(self, drone, instructions):
        self.drone = drone
        self.instructions = instructions
        self.current_instruction = 0
        self.droneDrawing = None

    # place down drone on the map as a turtle object
    def placeDrone(self, start_coordinates):
        self.drone.current_position = start_coordinates # update drone's current position
        print(start_coordinates)

        # create turtle object to represent the drone
        self.droneDrawing = turtle.Turtle()
        self.droneDrawing.hideturtle()
        self.droneDrawing.goto(start_coordinates)
        self.droneDrawing.color("red")
        self.droneDrawing.penup()
        self.droneDrawing.speed(0)
        self.droneDrawing.showturtle()

    def moveDrone(self):
        # check if there are still instructions to be executed
        if self.current_instruction < len(self.instructions):
            # get the next instruction
            instruction = self.instructions[self.current_instruction]
            self.current_instruction += 1

            # check if the instruction is a turn or a move
            if type(instruction) == int:
                self.droneDrawing.right(instruction)

            elif type(instruction) == tuple: # tuple means its a move
                self.droneDrawing.goto(instruction)
                self.drone.steps_taken += 1 # update the number of steps taken by the drone