import turtle

# Drone object to keep track of steps taken and execute instructions (the maze solution)
class Drone:
    def __init__(self, current_pos):
        self.__current_pos = current_pos
        self.__steps_taken = 0 # track the number of steps taken by the drone: only +1 when it moves. +0 when it turns
    