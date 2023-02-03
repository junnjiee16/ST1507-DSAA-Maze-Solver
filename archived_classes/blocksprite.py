import turtle

# block sprite graphics object
class BlockSprite(turtle.Turtle):
    def __init__(self, name, color):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed(0)
        self.shape("square")
        self.shapesize(24/20)
        self.pencolor("black")
        self.color(color)
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def color(self, color):
        self.fillcolor(color)
