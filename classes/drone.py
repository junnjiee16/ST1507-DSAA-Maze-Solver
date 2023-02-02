import turtle

# Drone object to keep track of steps taken and execute instructions (the maze solution)
class Drone:
    def __init__(self, instructions, start_position, current_position=None):
        self.__start_position = start_position
        self.__curr_position = current_position
        self.__instructions = instructions

        self.__steps_taken = 0 # track the number of steps taken by the drone: only +1 when it moves. +0 when it turns
        self.__current_instruction = 0 # track the current instruction the drone is executing

        self.__droneDrawing = turtle.Turtle() # turtle object to represent the drone
        self.__droneDrawing.hideturtle()
        self.__droneDrawing.penup()
        self.__droneDrawing.goto(start_position[0] * 24, start_position[1] * 24)
        self.__droneDrawing.color("red")
        self.__droneDrawing.showturtle()

    @property
    def steps_taken(self):
        return self.__steps_taken

    def set_instructions(self, instructions):
        self.__instructions = instructions

    def reset(self):
        self.__steps_taken = 0
        self.__current_instruction = 0

        self.__droneDrawing.goto(self.__start_position[0] * 24, self.__start_position[1] * 24)
        self.__droneDrawing.setheading(0)

    # execute 1 instruction
    def move(self):
        # check if all instructions have been executed
        if self.__current_instruction < len(self.__instructions):
            # get the current instruction
            instruction = self.__instructions[self.__current_instruction]
            self.__current_instruction += 1

            # check if the instruction is to turn
            if type(instruction) == int:
                self.__droneDrawing.right(instruction)

            # move the drone
            else:
                self.__droneDrawing.goto(instruction[0] * 24, instruction[1] * 24)
                self.__steps_taken += 1
