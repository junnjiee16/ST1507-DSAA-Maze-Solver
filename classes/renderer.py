import turtle

# renderer class to render graphics object on the screen
class Renderer:
    '''
    pixel_size: size of each unit space on the map in pixels

    '''
    def __init__(self, pixel_size):
        self.graphics_assets = dict()
        self.__pixel_size = pixel_size # pixel size of each unit space on the map

        # calculate how much to offset the map so that it will be centered on the screen
        self.__offset_x = None
        self.__offset_y = None
  
    @property
    def pixel_size(self):
        return self.__pixel_size

    # store the graphic representation of the sprite in the dictionary
    def add_sprite(self, sprite):
        self.graphics_assets[sprite.name] = sprite

    def render_title(self, title, map_y_length):
        max_height = map_y_length * self.__pixel_size - self.__offset_y

        # create a new turtle object to draw the title
        title_turtle = turtle.Turtle()
        title_turtle.hideturtle()
        title_turtle.penup()
        title_turtle.color("black")
        title_turtle.goto(-self.__offset_x - (self.__pixel_size / 2), max_height + 5)
        title_turtle.write(title, font=("Arial", 12, "normal"))

    def render_map(self, map):
        '''
            Renders the given map input on the screen. The map
            must be an array of strings, with each string representing
            a row of the map. Each character in the string represents
            a block in the map. The following characters are used:
            - X: Wall
            - s: Start point
            - e: End point
            - .: Normal road
        '''
        # calculate offset
        self.__calculate_offset(map.x_length, map.y_length)

        # get all the sprites
        wall = self.graphics_assets["wall"]
        road = self.graphics_assets["road"]
        start = self.graphics_assets["startpoint"]
        end = self.graphics_assets["endpoint"]

        # get map layout
        map_layout = map.layout

        
        ### draw the map by placing tiles according to map layout
        for y_pos in range(len(map_layout)): # y axis of map, starting from top (according to map layout in text file)
            for x_pos in range(len(map_layout[y_pos])): # x axis of map starting from left
                
                # reverse y_pos to start from bottom
                y_reversed = len(map_layout) - y_pos - 1

                # calculate position of grid
                grid_x_pos = self.__pixel_size * x_pos - self.__offset_x
                grid_y_pos = self.__pixel_size * y_reversed - self.__offset_y

                # check if it is a wall
                if map_layout[y_pos][x_pos] == "X":
                    block = wall
                # check if it is a road
                elif map_layout[y_pos][x_pos] == ".":
                    block = road
                # check if it is start point
                elif map_layout[y_pos][x_pos] == "s":
                    block = start
                # it is a end point
                else:
                    block = end

                # configure the tile drawing``
                block.goto((grid_x_pos, grid_y_pos))

                # place down tile on the screen
                block.stamp()


    def render_drone(self, drone, spawn=False):
        '''
            Updates the location and orientation given DroneSprite object on the screen. 
        '''
        ### Update its location and orientation
        drone_sprite = self.graphics_assets[drone.name]

        # if spawn is true, renders drone sprite immediately at the current position of drone
        if spawn:
            drone_sprite.hideturtle()

            # move the drone to the starting position
            drone_sprite.goto(drone.current_pos[0] * self.__pixel_size - self.__offset_x, drone.current_pos[1] * self.__pixel_size - self.__offset_y)
            # change the orientation of the drone
            drone_sprite.setheading(0)

            # update the current position of the drone
            drone_sprite.current_pos = drone.current_pos
            # update the orientation of the drone
            drone_sprite.orientation = drone.orientation

            # show the drone
            drone_sprite.showturtle()


        # check if orientation changed
        elif drone.orientation != drone_sprite.orientation:
            drone_sprite.right(drone.prev_turn_angle)
            # update the new orientation of the drone
            drone_sprite.orientation = drone.orientation

        # if orientation did not change, means the position changed
        elif drone.current_pos != drone_sprite.current_pos:
            drone_sprite.goto(drone.current_pos[0] * self.__pixel_size - self.__offset_x, drone.current_pos[1] * self.__pixel_size - self.__offset_y)
            # update the current position of the drone
            drone_sprite.current_pos = drone.current_pos


    def __calculate_offset(self, map_x_length, map_y_length):
        '''
            Calculates the offset of the map so that it will be centered on the screen.
        '''
        # calculate the offset
        self.__offset_x = (map_x_length * self.__pixel_size) / 2
        self.__offset_y = (map_y_length * self.__pixel_size) / 2