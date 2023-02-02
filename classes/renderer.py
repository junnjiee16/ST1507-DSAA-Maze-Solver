from dronesprite import DroneSprite
from blocksprite import BlockSprite

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


    def spawn_drone(current_pos, orientation):
        '''
            Spawns a drone object on the screen. The following properties
            of the Drone object must be given:
            - current_pos: The current position of the drone
            - orientation: The orientation of the drone (0, 90, 180, 270)
        '''



    def render_drone(drone, current_pos, orientation):
        '''
            Renders the given drone object on the screen. The following
            properties of the Drone object must be given:
            - current_pos: The current position of the drone
            - orientation: The orientation of the drone (0, 90, 180, 270)
        '''
