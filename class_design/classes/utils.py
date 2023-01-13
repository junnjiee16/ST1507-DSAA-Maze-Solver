import os
import sys
from classes.mazegraph import MazeGraph

class Utils:
    # takes in the processed map text and converts it to a graph
    def map_to_graph(processed_map):

        # Create an empty graph
        graph = MazeGraph()

        # Add the nodes to the graph
        # nodes are the coordinates of each road tile in the map
        for y in range(len(processed_map)): # go from bottom up
            for x in range(len(processed_map[0])):
                if processed_map[y][x] != 'X': #1 is used to represent walls
                    
                    # reverse y axis order before adding node
                    y_reverse = len(processed_map) - 1 - y
                    graph.addNode((x, y_reverse))

        # Add the edges (connections) to the graph
        for node in graph.nodes:
            x, y = node

            # Check the top cell (y + 1)
            if (x, y + 1) in graph.nodes:
                graph.addEdge(node, (x, y + 1))

            # Check the bottom cell (y - 1)
            if (x, y - 1) in graph.nodes:
                graph.addEdge(node, (x, y - 1))

            # Check the left cell (x - 1)
            if (x - 1, y) in graph.nodes:
                graph.addEdge(node, (x - 1, y))

            # Check the right cell (x + 1)
            if (x + 1, y) in graph.nodes:
                graph.addEdge(node, (x + 1, y))

        return graph


    def readFile(filename):
        # get the directory of the absolute path leading to the script it is running on (so it will be correct when another script imports this)
        path = os.path.dirname(os.path.abspath(sys.argv[0]))
        print(path)

        # join the directory path with the filename
        abs_file_path = os.path.join(path, filename)

        # check if file exists
        if os.path.exists(abs_file_path):
            with open(abs_file_path) as f:
                content = f.read()

                print(content)        
                return content

        else:
            print("Error: File does not exist")
            return None