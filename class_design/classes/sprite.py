import turtle

# class to manipulate turtle drawings
class Sprite(turtle.Turtle): # create Sprite class to define the turtle and its characteristics
    def __init__(self, type):
        super().__init__(shape=shape) # inherit from Turtle (parent class)
        if type == "wall":
            self.shapesize((TILE_SIZE / CURSOR_SIZE)-0.4) # define the size of the square
            self.color('orange') #  define the color that we are going to plot the turtle
            self.penup() # to prevent the pen from leaving a trace while shifting to the starting point
            self.goto(start_x, start_y) # move the turtle to the position
            self.speed('fastest') # set speed to slowest to observe the sprite movement

    def drawTile(self, x, y, color):
        self.goto(x, y)
        self.fillcolor(color)
        self.stamp()