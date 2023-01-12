import turtle
from classes.tile import Tile


# map object, stores required data for the map
class Map:
    def __init__(self, map_layout, start_position=None, end_position=None):
        self.map_layout = map_layout
        self.__start_position = start_position
        self.__end_position = end_position

        # process map for drawing on turtle
        self.processed_map = self.map_layout.split("\n") # split the map into a list of strings


    def draw(self): # draw the map
        ### use turtle to place the tile on the screen
        tile_drawing = turtle.Turtle()
        tile_drawing.hideturtle()
        tile_drawing.penup()
        tile_drawing.speed(0)
        tile_drawing.shape("square")
        tile_drawing.shapesize(24/20)
        tile_drawing.pencolor('black')

        ### draw the map by placing tiles according to map layout
        # also find the start and end coordinates of the map while drawing it
        for y_pos in range(len(self.processed_map)): # y axis of map, starting from top (according to map layout in text file)
            for x_pos in range(len(self.processed_map[y_pos])): # x axis of map starting from left
                # calculate position of grid
                grid_x_pos = -288 + (24 * x_pos)
                grid_y_pos = 288 - (24 * y_pos)

                # check if it is a wall
                if self.processed_map[y_pos][x_pos] == "X":
                    tile = Tile((grid_x_pos, grid_y_pos), "wall")

                # check if it is start/end point
                elif self.processed_map[y_pos][x_pos] == "s":
                    tile = Tile((grid_x_pos, grid_y_pos), "start")

                elif self.processed_map[y_pos][x_pos] == "e":
                    tile = Tile((grid_x_pos, grid_y_pos), "end")

                # if not anything else, it is normal road
                else:
                    tile = Tile((grid_x_pos, grid_y_pos), "road")

                # configure the tile drawing
                tile_drawing.fillcolor(tile.color)
                tile_drawing.goto(tile.coordinates)

                # place down tile on the screen
                tile_drawing.stamp()