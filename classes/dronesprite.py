import turtle 

class DroneSprite(turtle.Turtle):
    def __init__(self, orientation):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("red")
        self.orientation = orientation

