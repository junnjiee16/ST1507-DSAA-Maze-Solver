# renderer class to render graphics object on the screen
class Renderer:
    def __init__(self):
        self.graphical_objects = dict()

    # store the graphical representation of the sprite in the dictionary
    def add_sprite(self, sprite):
        self.graphical_objects[sprite.name] = sprite

    def render_map(self, map_layout):
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
        # get all the sprites
        wall = self.graphical_objects["wall"]
        road = self.graphical_objects["road"]
        start = self.graphical_objects["startpoint"]
        end = self.graphical_objects["endpoint"]
        
        ### draw the map by placing tiles according to map layout
        for y_pos in range(len(map_layout)): # y axis of map, starting from top (according to map layout in text file)
            for x_pos in range(len(map_layout[y_pos])): # x axis of map starting from left
                
                # reverse y_pos to start from bottom
                y_reversed = len(map_layout) - y_pos - 1

                # calculate position of grid
                grid_x_pos = 24 * x_pos
                grid_y_pos = 24 * y_reversed

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


    def render_drone(self, drone, first_spawn=False):
        '''
            Updates the location and orientation given DroneSprite object on the screen. 
        '''
        ### Update its location and orientation
        drone_sprite = self.graphical_objects["drone"]

        # check if orientation changed
        if drone.orientation != drone_sprite.orientation:
            drone_sprite.right(drone.prev_turn_angle)
            # update the new orientation of the drone
            drone_sprite.orientation = drone.orientation

        # if orientation did not change, means the position changed
        elif drone.current_pos != drone_sprite.current_pos:
            drone_sprite.goto(drone.current_pos[0] * 24, drone.current_pos[1] * 24)
            # update the current position of the drone
            drone_sprite.current_pos = drone.current_pos

        # if it is the first spawn, place the drone on the screen
        elif first_spawn: 
            drone_sprite.goto(drone_sprite.current_pos[0] * 24, drone_sprite.current_pos[1] * 24)
            drone_sprite.showturtle()
