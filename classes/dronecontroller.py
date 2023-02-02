import turtle
from classes.drone import Drone

# execute instructions to drive the drone. Controller is unique to each drone
class DroneController:
    def __init__(self, drone, instructions=None):
        self.__drone = drone
        self.__instructions = instructions
        self.__current_instruction = 0

    @property
    def instructions(self):
        return self.__instructions

    @instructions.setter
    def instructions(self, value):
        self.__instructions = value

    # move drone and update drone status
    def move_drone(self):
        # check if there are still instructions to be executed
        if self.__current_instruction < len(self.__instructions):
            # get the next instruction
            instruction = self.__instructions[self.__current_instruction]
            self.__current_instruction += 1

            # check if the instruction is a turn or a move
            if type(instruction) == int:
                self.__drone.orientation = self.__drone.orientation + instruction

            elif type(instruction) == tuple: # tuple means its a move
                self.droneDrawing.goto(instruction)
                self.__drone.steps_taken = self.__drone.steps_taken + 1 # update the number of steps taken by the drone