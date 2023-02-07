import os
import random

class MazeGenerator:
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

    def write_to_file(self, filename='map_files/random_maze.txt'):
        # write to file
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