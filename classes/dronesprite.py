import turtle 

class DroneSprite(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.shapesize(0.5, 0.5)
        self.penup()
        self.speed(0)
        self.color("red")

