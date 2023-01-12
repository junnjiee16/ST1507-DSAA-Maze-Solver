import turtle
from classes.filemanager import FileManager
from classes.arrow import Arrow
from classes.map import Map
from classes.pathfinder import Pathfinder


# class to control the logic of the program
class LogicController:
    def startProgram(self):
        window = turtle.Screen()
        window.title("PIZZA RUNNERS: Done by Lim Jun Jie, Timothy Chia, DAAA/FT/2B/02") # create the titlebar
        window.setup(700,700)

        # open file
        map_text = FileManager.readFile("test_files/map1.txt")

        # create map
        map_object = Map(map_text)

        # draw map
        map_object.draw()

        # create arrow
        arrow = turtle.Turtle()
        arrow.hideturtle()
        arrow.penup()
        arrow.speed(0)
        arrow.color('red')
        arrow.goto(-288, 288)
        arrow.showturtle()


        # this must be the last line in the turtle program
        window.exitonclick()