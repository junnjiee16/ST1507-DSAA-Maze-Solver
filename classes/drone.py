class Drone:
    '''
    Drone object to keep track of steps taken and execute instructions (the maze solution)
    
    Parameters: 
        name (str): name of the drone
        current_pos (tuple): current position of the drone (x, y)

    Attributes:
        name (str): name of the drone
        current_pos (tuple): current position of the drone (x, y)
        orientation (int): orientation of the drone (90 = North, 0 = East, 270 = South, 180 = West)
        steps_taken (int): number of steps taken by the drone
        prev_turn_angle (int): angle of the last turn the drone made
    '''
    def __init__(self, name, current_pos):
        self.__name = name
        self.__start_pos = current_pos
        self.__current_pos = current_pos
        self.__orientation = 0 # Legend for orientation: 90 = North, 0 = East, 270 = South, 180 = West (turtle orientations)
        self.__prev_turn_angle = 0 # track the last turn angle the drone made.
        self.__steps_taken = 0 # track the number of steps taken by the drone: only +1 when it moves. +0 when it turns

    @property
    def name(self):
        return self.__name  # return the name of the drone

    @property
    def current_pos(self):
        return self.__current_pos  # return the current position of the drone

    @property
    def orientation(self):
        return self.__orientation  # return the orientation of the drone

    @property
    def steps_taken(self):
        return self.__steps_taken  # return the number of steps taken by the drone

    @property
    def prev_turn_angle(self):
        return self.__prev_turn_angle  # return the angle of the last turn the drone made

    @name.setter
    def name(self, value):
        self.__name = value  # set the name of the drone

    @current_pos.setter
    def current_pos(self, value):
        self.__current_pos = value  # set the current position of the drone

    @orientation.setter
    def orientation(self, value):
        self.__orientation = value  # set the orientation of the drone

    @steps_taken.setter
    def steps_taken(self, value):
        self.__steps_taken = value  # set the number of steps taken by the drone

    @prev_turn_angle.setter
    def prev_turn_angle(self, value):
        self.__prev_turn_angle = value  # set the angle of the last turn the drone made

    def reset(self):
        '''Reset the drone to its starting position and orientation'''

        self.__current_pos = self.__start_pos
        self.__orientation = 0
        self.__prev_turn_angle = 0
        self.__steps_taken = 0