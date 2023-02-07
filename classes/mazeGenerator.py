import random

class MazeGenerator:
    '''
    Class to generate a maze with DFS algorithm.

    Parameters:
        width (int): width of the maze
        height (int): height of the maze

    Attributes:
        width (int): width of the maze
        height (int): height of the maze
        maze (list): 2D array of 0s and 1s, 0s represent walls, 1s represent open spaces
        visited (list): 2D array of booleans, True if the cell has been visited, False otherwise
        directions (list): list of directions to move in
        dx (list): list of x coordinates of the directions
        dy (list): list of y coordinates of the directions
        start (tuple): tuple of x and y coordinates of the start position
        end (tuple): tuple of x and y coordinates of the end position
    '''
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.maze = [[1 for _ in range(width)] for _ in range(height)]
        self.visited = [[False for _ in range(width)] for _ in range(height)]
        self.directions = ["N", "S", "E", "W"]
        self.dx = [0, 0, 1, -1]
        self.dy = [-1, 1, 0, 0]
        # random start and end
        self.start = None
        self.end = None

    def generate_maze(self, x, y):
        '''
        Maze is stored in self.maze attribute.

        Parameters:
            x (int): x coordinate of the current cell
            y (int): y coordinate of the current cell

        Returns:
            None
        '''
        self.visited[y][x] = True
        random.shuffle(self.directions)
        for direction in self.directions:
            if direction == "N":
                if y > 1 and not self.visited[y-2][x]:
                    self.maze[y-1][x] = 0
                    self.maze[y-2][x] = 0
                    self.generate_maze(x, y-2)
            elif direction == "S":
                if y < self.height-2 and not self.visited[y+2][x]:
                    self.maze[y+1][x] = 0
                    self.maze[y+2][x] = 0
                    self.generate_maze(x, y+2)
            elif direction == "E":
                if x < self.width-2 and not self.visited[y][x+2]:
                    self.maze[y][x+1] = 0
                    self.maze[y][x+2] = 0
                    self.generate_maze(x+2, y)
            elif direction == "W":
                if x > 1 and not self.visited[y][x-2]:
                    self.maze[y][x-1] = 0
                    self.maze[y][x-2] = 0
                    self.generate_maze(x-2, y)
                    
        if not self.start:
            self.start = (x, y)
        else:
            self.end = (x, y)

    def write_to_file(self, filename):
        with open(filename, "w") as f:
            for y, row in enumerate(self.maze):
                for x, cell in enumerate(row):
                    if (x, y) == self.start:
                        f.write("s")
                    elif (x, y) == self.end:
                        f.write("e")
                    elif cell == 1:
                        f.write("X")
                    else:
                        f.write(".")
                f.write("\n")