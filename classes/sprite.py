import turtle

class Sprite(turtle.Turtle):
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
        self.shapesize(shapesize)
        self.speed(speed)

        self.__name = name
        self.__current_pos = current_pos
        self.__orientation = orientation

    @property
    def name(self):
        return self.__name

    @property
    def orientation(self):
        return self.__orientation

    @property
    def current_pos(self):
        return self.__current_pos

    @name.setter
    def name(self, value):
        self.__name = value

    @orientation.setter
    def orientation(self, value):
        self.__orientation = value

    @current_pos.setter
    def current_pos(self, value):
        self.__current_pos = value