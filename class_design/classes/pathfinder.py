import turtle
from classes.arrow import Arrow

# object for the screen to start screen
class Pathfinder:
    def __init__(self, algorithm):
        self.algorithm = algorithm # [0 = left-hand algorithm, 1 = 2nd algorithm]

    def guideArrow(self):
        # spawn arrow at start point
        arrow = turtle.Turtle()
        arrow.color('red')
        arrow.goto(-288, 288)