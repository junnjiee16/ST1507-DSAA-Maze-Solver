import turtle
import os

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
        self.showturtle()


# create file manager class
class FileManager:
    def __init__(self, filename):
        self.path = os.path.dirname(os.path.abspath(__file__)) # get the directory of the absolute path leading to this specific script
        self.abs_file_path = os.path.join(self.path, filename)

    def readFile(self):
        with open(self.abs_file_path) as f:
            map_layout = f.readlines()
        map_layout = [x.strip() for x in map_layout]

        return map_layout


# arrow class
class Arrow:
    def __init__(self):
        pass


# create map class
class Map:
    def __init__(self):
        pass


starting_x = -288
starting_y = 288

# function to create map
def create_map(map_layout):
    window = turtle.Screen()
    window.title("PIZZA RUNNERS: Done by Lim Jun Jie, Timothy Chia, DAAA/FT/2B/02") # create the titlebar
    window.setup(700,700)

    for y_pos in range(len(map_layout)):
        for x_pos in range(len(map_layout[y_pos])):
            # calculate position of grid
            grid_x_pos = starting_x + (24 * x_pos)
            grid_y_pos = starting_y - (24 * y_pos)

            # check if it is a wall
            if map_layout[y_pos][x_pos] == "X":
                tile.fillcolor('grey')

            # check if it is start/end point
            elif map_layout[y_pos][x_pos] == "s":
                tile.fillcolor('#61ff6e')
            elif map_layout[y_pos][x_pos] == "e":
                tile.fillcolor('#56defc')

            # if not anything else, it is normal road
            else:
                tile.fillcolor('white') 

            # go to the position and place the tile down
            tile.goto(grid_x_pos, grid_y_pos)
            tile.stamp()

    # exit application when any part of turtle screen display is clicked (except for top bar)
    window.mainloop()



#####################################
# main program
#####################################
# create map
tile = Tile()

# open and read map file
script_dir = os.path.dirname(os.path.abspath(__file__)) # get absolute path of current device leading to this script, then get directory
filename = ".\\test_files\\map2.txt" # specify test file folder and file
abs_file_path = os.path.join(script_dir, filename)

with open(abs_file_path) as f:
    map_layout = f.readlines()
map_layout = [x.strip() for x in map_layout]


# create map using function
create_map(map_layout)