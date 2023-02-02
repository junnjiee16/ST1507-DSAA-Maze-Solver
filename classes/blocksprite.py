import turtle

# block sprite graphics object
class BlockSprite(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(0.5, 0.5)
        self.penup()
        self.speed(0)
        self.color("black")