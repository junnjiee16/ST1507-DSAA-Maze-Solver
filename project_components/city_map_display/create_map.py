import turtle
import os

# create wall class
class Block(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color('grey')
        self.penup()
        self.speed(0)

# open and read map file
script_dir = os.path.dirname(os.path.abspath(__file__)) # get absolute path of current device (relative to this script)
filename = ".\\test_files\\map1.txt"
abs_file_path = os.path.join(script_dir, filename)

with open(abs_file_path) as f:
    content = f.readlines()
content = [x.strip() for x in content] 

print(script_dir)

# create map
pen = Block()

window = turtle.Screen()
window.title("PIZZA RUNNERS") # create the titlebar
window.setup(700,700)
for arr in content:
    for block in arr:
        if block == "X":
            pen.stamp()



# exit application when any part of turtle screen display is clicked (except for top bar)
window.exitonclick()