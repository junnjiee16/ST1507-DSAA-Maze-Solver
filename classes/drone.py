import turtle

# Drone object to keep track of steps taken and execute instructions (the maze solution)
class Drone:
    def __init__(self, current_pos):
        self.__current_pos = current_pos
        self.__orientation = "E"
        self.__prev_turn_angle = 0 # track the last turn angle the drone made.
        self.__steps_taken = 0 # track the number of steps taken by the drone: only +1 when it moves. +0 when it turns

    @property
    def current_pos(self):
        return self.__current_pos

    @property
    def orientation(self):
        return self.__orientation

    @property
    def steps_taken(self):
        return self.__steps_taken

    @property
    def prev_turn_angle(self):
        return self.__prev_turn_angle

    @current_pos.setter
    def current_pos(self, value):
        self.__current_pos = value

    @orientation.setter
    def orientation(self, value):
        self.__orientation = value

    @steps_taken.setter
    def steps_taken(self, value):
        self.__steps_taken = value

    @prev_turn_angle.setter
    def prev_turn_angle(self, value):
        self.__prev_turn_angle = value