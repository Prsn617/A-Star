import pygame
from pygame import *
from pygame.draw import *

class Spot():
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.f = 0
        self.g = 0
        self.h = 0
        self.neighbour = []
        self.previous = None
        self.wall = False

    def draw(self, width, height, screen, color):
        if self.wall:
            color = (20, 20, 20)
        pygame.draw.rect(screen, color, (self.i * width, self.j * height, width-1, height-1), width=0)
        


    def addNeighbour(self, grid, cols, rows):
        i = self.i
        j = self.j

        if i < cols - 1:
            self.neighbour.append(grid[i+1][j])
        if i > 0:
            self.neighbour.append(grid[i-1][j])
        if j < rows - 1:
            self.neighbour.append(grid[i][j+1])
        if j > 0:
            self.neighbour.append(grid[i][j-1])

        if i < cols - 1 and j < rows - 1:
            self.neighbour.append(grid[i+1][j+1])
        if i > 0 and j < rows - 1:
            self.neighbour.append(grid[i-1][j+1])
        if i < cols - 1 and j > 0:
            self.neighbour.append(grid[i+1][j-1])
        if i > 0 and j > 0:
            self.neighbour.append(grid[i-1][j-1])

