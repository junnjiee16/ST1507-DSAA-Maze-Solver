# screen class is a subclass of turtle.Screen
# to have custom function to update title bar as well as capture key presses
import turtle
import tkinter as tk

class MapScreen(turtle._Screen):
    def __init__(self, title):
        super().__init__()
        turtle.TurtleScreen.__init__(self, MapScreen._canvas)
        if turtle.Turtle._screen is None:
            turtle.Turtle._screen = self

        self.title(title + " Steps Taken = 0")
        self.setup(width=1.0, height=1.0) 
        self.listen()

    def update_title(self, steps):
        self.title(steps)

