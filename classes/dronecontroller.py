# execute instructions to drive the drone. Controller is unique to each drone
class DroneController:
    '''
    Controller to execute instructions (the maze solution) for the drone.

    Parameters:
        drone (Drone): drone object to be controlled
        instructions (list): list of instructions to be executed by the drone

    Attributes:
        drone (Drone): drone object to be controlled
        instructions (list): list of instructions to be executed by the drone
        current_instruction (int): index of the current instruction to be executed
    '''
    def __init__(self, drone, instructions=None):
        self.__drone = drone
        self.__instructions = instructions
        self.__current_instruction = 0

    @property
    def instructions(self):
        return self.__instructions  # return the instructions to be executed by the drone

    @instructions.setter
    def instructions(self, value):
        self.__instructions = value  # set the instructions to be executed by the drone
        self.__current_instruction = 0  # reset the current instruction to 0

    def execute_instruction(self):
        '''
        Move drone and update drone status.

        Returns:
            bool: True if there are no more instructions to be executed, False otherwise
        '''
        # check if there are still instructions to be executed
        if self.__current_instruction < len(self.__instructions):
            instruction = self.__instructions[self.__current_instruction]  # get the current instruction
            self.__current_instruction += 1  

            # check if the instruction is a turn or a move
            if type(instruction) == list:
                self.__drone.prev_turn_angle = instruction[0]  # update the last turn angle the drone made
                self.__drone.orientation = instruction[1]  # update the orientation of the drone
 
            elif type(instruction) == tuple: # tuple means its a move
                self.__drone.current_pos = instruction  # update the current position of the drone
                self.__drone.steps_taken = self.__drone.steps_taken + 1  # update the number of steps taken by the drone
        
        else:
            return True