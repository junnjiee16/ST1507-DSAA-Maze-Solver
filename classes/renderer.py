from classes.dronesprite import DroneSprite
from classes.blocksprite import BlockSprite

# renderer class to render graphics object on the screen
class Renderer:
    def render_map(map_layout):
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
        block = BlockSprite()
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
                    color = "grey"
                # check if it is start point
                elif map_layout[y_pos][x_pos] == "s":
                    color = "#61ff6e"
                # check if it is end point
                elif map_layout[y_pos][x_pos] == "e":
                    color = "#56defc"
                # if not anything else, it is normal road
                else:
                    color = "white"

                # configure the tile drawing
                block.fillcolor(color)
                block.goto((grid_x_pos, grid_y_pos))

                # place down tile on the screen
                block.stamp()


    def render_drone(drone, drone_sprite=None):
        '''
            Updates the location and orientation given DroneSprite object on the screen. 
            If no DroneSprite object is given, a new DroneSprite object will be created 
            and returned.
        '''
        # if no DroneSprite object is given, create a new one and return it
        if drone_sprite == None:
            drone_sprite = DroneSprite(drone.current_pos, drone.orientation)
            drone_sprite.goto(drone.current_pos[0] * 24, drone.current_pos[1] * 24)
            drone_sprite.showturtle()
            return drone_sprite


        ### if a DroneSprite object is given, update its location and orientation
        
        # check if orientation changed
        if drone.orientation != drone_sprite.orientation:
            drone_sprite.right(drone.prev_turn_angle)
            # update the new orientation of the drone
            drone_sprite.orientation = drone.orientation

        # check if position changed
        if drone.current_pos != drone_sprite.current_pos:
            drone_sprite.goto(drone.current_pos[0] * 24, drone.current_pos[1] * 24)
            # update the current position of the drone
            drone_sprite.current_pos = drone.current_pos