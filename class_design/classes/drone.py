# Drone object to keep track of the drone's current position and number of steps taken, as well as take in instructions to move itself
class Drone:
    def __init__(self):
        self.__current_position = None
        self.__steps_taken = 0 # track the number of steps taken by the drone: only +1 when it moves. +0 when it turns

    @property
    def current_position(self):
        return self.__current_position

    @property
    def steps_taken(self):
        return self.__steps_taken

    @current_position.setter
    def current_position(self, coordinates):
        self.__current_position = coordinates

    @steps_taken.setter
    def steps_taken(self, steps):
        self.__steps_taken = steps
