import turtle
import os

# create moving arrow
class Arrow(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.hideturtle()  
        self.penup() # so that arrow does not draw
        self.color("red")
        self.goto(-288, 288)
        self.showturtle()

# create tiles of different colors across the map
class Tile(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)

        self.hideturtle() # hide the object
        self.shape("square") # set the shape to square
        self.shapesize(24/20) # set size to be equal to the pixels we move
        self.pencolor('black') # color of the square border
        self.penup() # no drawing when moving 
        self.speed(0) # fastest speed


# function to create map
def create_map(map_layout):
    tile = Tile()

    window = turtle.Screen()
    window.title("PIZZA RUNNERS: Done by Lim Jun Jie, Timothy Chia, DAAA/FT/2B/02") # create the titlebar
    window.setup(700,700)

    for y_pos in range(len(map_layout)):
        for x_pos in range(len(map_layout[y_pos])):
            # calculate position of grid
            grid_x_pos = -288 + (24 * x_pos)
            grid_y_pos = 288 - (24 * y_pos)

            # check if it is a wall
            if map_layout[y_pos][x_pos] == "X":
                tile.fillcolor('grey')

            # check if it is start/end point
            elif map_layout[y_pos][x_pos] == "s":
                tile.fillcolor('green')
            elif map_layout[y_pos][x_pos] == "e":
                tile.fillcolor('blue')

            # if not anything else, it is normal road
            else:
                tile.fillcolor('white') 

            # go to the position and place the tile down
            tile.goto(grid_x_pos, grid_y_pos)
            tile.stamp()

    arrow = Arrow()

    # exit application when any part of turtle screen display is clicked (except for top bar)
    window.exitonclick()


# open and read map file
script_dir = os.path.dirname(os.path.abspath(__file__)) # get absolute path of current device leading to this script, then get directory
filename = ".\\test_files\\map2.txt" # specify test file folder and file
abs_file_path = os.path.join(script_dir, filename)

with open(abs_file_path) as f:
    map_layout = f.readlines()
map_layout = [x.strip() for x in map_layout]

create_map(map_layout)
