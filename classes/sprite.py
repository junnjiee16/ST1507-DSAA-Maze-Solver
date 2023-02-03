import turtle

class Sprite:
    def __init__(self, color, current_pos=None, orientation=None):
        self.__color = color
        self.__orientation = orientation
        self.__current_pos = current_pos

    @property
    def orientation(self):
        return self.__orientation

    @property
    def current_pos(self):
        return self.__current_pos

    @orientation.setter
    def orientation(self, value):
        self.__orientation = value

    @current_pos.setter
    def current_pos(self, value):
        self.__current_pos = value