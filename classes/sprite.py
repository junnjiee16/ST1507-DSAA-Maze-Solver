import turtle


class Sprite(turtle.Turtle):
    '''
    Sprite class that inherits from Turtle class.

    Parameters:
        name (str): name of the sprite
        color (str): color of the sprite
        pencolor (str): color of the pen
        shape (str): shape of the sprite
        shapesize (int): size of the sprite
        speed (int): speed of the sprite
        current_pos (tuple): current position of the sprite
        orientation (str): orientation of the sprite

    Attributes:
        name (str): name of the sprite
        current_pos (tuple): current position of the sprite
        orientation (str): orientation of the sprite
    '''
    def __init__(self, name, color, pencolor=None, shape=None, shapesize=None, speed=None, current_pos=None, orientation=None):
        super().__init__()
        self.hideturtle()
        self.penup()

        # cannot set None when setting colors
        if color != None:
            self.color(color)
        if pencolor != None: 
            self.pencolor(pencolor)

        self.shape(shape)
        self.shapesize(shapesize) # 1 unit = 20 pixels for shapesize()
        self.speed(speed)

        self.__name = name
        self.__current_pos = current_pos
        self.__orientation = orientation

    @property
    def name(self):
        return self.__name  # returns the name of the sprite

    @property
    def orientation(self):
        return self.__orientation  # returns the orientation of the sprite

    @property
    def current_pos(self):
        return self.__current_pos  # returns the current position of the sprite

    @name.setter
    def name(self, value):
        self.__name = value  # sets the name of the sprite

    @orientation.setter
    def orientation(self, value):
        self.__orientation = value  # sets the orientation of the sprite

    @current_pos.setter
    def current_pos(self, value):
        self.__current_pos = value  # sets the current position of the sprite