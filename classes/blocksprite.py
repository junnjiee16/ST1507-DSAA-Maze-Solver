import turtle

# block sprite graphics object
class BlockSprite(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed(0)
        self.shape("square")
        self.shapesize(24/20)
        self.pencolor("black")