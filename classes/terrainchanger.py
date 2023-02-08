import random

# class to change the map terrain
class TerrainChanger:
    def __init__(self, map, map_graph): # takes in map and map_graph object
        self.__map = map
        self.__map_graph = map_graph

    def road_to_wall(self, drone_current_pos):
        # get random node
        if len(self.__map_graph.nodes()) > 3:
            # get random node but not the start or end node, or the current position of the drone
            node = random.choice([node for node in self.__map_graph.nodes() if node != self.__map.start_pos and node != self.__map.end_pos and node != drone_current_pos])
            x, y = node

            # remove node from graph as it is now a wall
            # self.__map_graph.remove_node(node)

            # change map layout
            # reverse y_pos to start from bottom
            y_reversed = self.__map.y_length - y - 1
            self.__map.layout[y_reversed][x] = "X"
            
            # return the node that was changed
            return [node, "wall"]