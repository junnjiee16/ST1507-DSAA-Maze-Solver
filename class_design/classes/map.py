import turtle


# map object, stores necessary metadata for the map
class Map:
    def __init__(self, map_layout, start_position, end_position):
        self.__layout = map_layout
        self.__start_position = start_position
        self.__end_position = end_position


    # getter functions
    @property
    def layout(self):
        return self.__layout

    @property
    def start_position(self):
        return self.__start_position
    
    @property
    def end_position(self):
        return self.__end_position


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
        for y_pos in range(len(self.__layout)): # y axis of map, starting from top (according to map layout in text file)
            for x_pos in range(len(self.__layout[y_pos])): # x axis of map starting from left
                
                # reverse y_pos to start from bottom
                y_reversed = len(self.__layout) - y_pos - 1

                # calculate position of grid
                grid_x_pos = 24 * x_pos
                grid_y_pos = 24 * y_reversed

                # check if it is a wall
                if self.__layout[y_pos][x_pos] == "X":
                    color = "grey"
                # check if it is start point
                elif self.__layout[y_pos][x_pos] == "s":
                    color = "#61ff6e"
                # check if it is end point
                elif self.__layout[y_pos][x_pos] == "e":
                    color = "#56defc"
                # if not anything else, it is normal road
                else:
                    color = "white"

                # configure the tile drawing
                tile_drawing.fillcolor(color)
                tile_drawing.goto((grid_x_pos, grid_y_pos))

                # place down tile on the screen
                tile_drawing.stamp()
