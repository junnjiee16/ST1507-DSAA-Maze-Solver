import os
import sys
from classes.mapgraph import MapGraph

# class to store general functions to support the application
class Utils:
    # takes in the processed map text and converts it to a graph
    def map_to_graph(map):

        # Create an empty graph
        graph = MapGraph(map.start_pos, map.end_pos)

        # Add the nodes to the graph
        # nodes are the coordinates of each road tile in the map
        for y in range(len(map.layout)): # go from bottom up
            for x in range(len(map.layout[0])):
                if map.layout[y][x] != 'X': #1 is used to represent walls
                    
                    # reverse y axis order before adding node
                    y_reverse = len(map.layout) - 1 - y
                    graph.add_node((x, y_reverse))

        # Add the edges (connections) to the graph
        for node in graph.nodes:
            x, y = node

            # Check the top cell (y + 1)
            if (x, y + 1) in graph.nodes:
                graph.add_edge(node, (x, y + 1))

            # Check the bottom cell (y - 1)
            if (x, y - 1) in graph.nodes:
                graph.add_edge(node, (x, y - 1))

            # Check the left cell (x - 1)
            if (x - 1, y) in graph.nodes:
                graph.add_edge(node, (x - 1, y))

            # Check the right cell (x + 1)
            if (x + 1, y) in graph.nodes:
                graph.add_edge(node, (x + 1, y))

        return graph

    # reads the text file and returns the content as a string
    def readMapFile(filename):
        # get the directory of the absolute path leading to the script it is running on (so it will be correct when another script imports this)
        path = os.path.dirname(os.path.abspath(sys.argv[0]))
        print(path)

        # join the directory path with the filename
        abs_file_path = os.path.join(path, filename)

        # check if file exists
        if os.path.exists(abs_file_path):
            with open(abs_file_path) as f:
                content = f.read()
            
            content = content.splitlines() # split the content into lines

            # array of possible characters in the map
            possible_chars = ['X', 's', 'e', '.']

            # scan through the content and check if it is a valid character
            # also checks if there is only one start and end point, and returns the coordinates of the start and end points
            start_point = None
            end_point = None
            for y in range(len(content)):
                for x in range(len(content[y])):
                    if content[y][x] not in possible_chars:
                        print("Error: Invalid character in map")
                        return None, None, None

                    elif content[y][x] == 's':
                        if start_point != None:
                            print("Error: Multiple start points in map")
                            return None, None, None
                        else:
                            reversed_y = len(content) - 1 - y
                            start_point = (x, reversed_y)

                    elif content[y][x] == 'e':
                        if end_point != None:
                            print("Error: Multiple end points in map")
                            return None, None, None
                        else:
                            reversed_y = len(content) - 1 - y
                            end_point = (x, reversed_y)

            return content, start_point, end_point

        else:
            print("Error: File does not exist")
            return None, None, None
