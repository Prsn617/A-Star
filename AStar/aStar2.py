import pygame, sys
import math as mt
from pygame import *
from pygame.draw import *
import numpy as np
import spot

pygame.init()

clock = pygame.time.Clock()
pygame.display.set_caption('A* Algorithm Visualizer')
WINDOW_SIZE = (800, 800)
screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)

#Colors variables
red = (240, 50, 50)
green = (50, 240, 50)
blue = (50, 50, 240)
black = (50, 50, 50)
white = (240, 240, 240)

#Global variables
cols = 80
rows = 80
grid = [None] * cols
wdt = (int)(WINDOW_SIZE[0] / cols)
hgt = (int)(WINDOW_SIZE[1] / rows)
openSet = []
closeSet = []
path = []

#Making list inside of grid list
for i in range(cols):
    grid[i] = [None] * rows

#Assigning object to each grid
for i in range(cols):
    for j in range(rows):
        grid[i][j] = spot.Spot(i, j)

start = grid[0][0]

#Adding neighbours to each grid
for i in range(cols):
    for j in range(rows):
        grid[i][j].addNeighbour(grid, cols, rows)

openSet.append(start)

#Removes specific element from a list
def removefromList(arr, element):
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == element:
            arr.pop(i)

#Returns the distance between any two points
def heuristic(x1, y1, x2, y2):
    xSq = (x2 - x1)**2
    ySq = (y2 - y1)**2
    dist = mt.sqrt(xSq + ySq)
    return dist

def renderGrids():
    for i in range(cols):
        for j in range(rows):
            grid[i][j].draw(wdt, hgt, screen, white)

    for i in range(len(closeSet)):
        closeSet[i].draw(wdt, hgt, screen, red)

    for i in range(len(openSet)):
        openSet[i].draw(wdt, hgt, screen, green)

    for i in range(len(path)):
        path[i].draw(wdt, hgt, screen, blue)

def drawWalls():
    mosX, mosY = pygame.mouse.get_pos()
    posX = mt.floor(mosX / wdt)
    posY = mt.floor(mosY/ hgt)
    grid[posX][posY].wall = True

def findPath():
    mosX, mosY = pygame.mouse.get_pos()

    posX = mt.floor(mosX / wdt)
    posY = mt.floor(mosY/ hgt)

    end = grid[posX][posY]
    if len(openSet) > 0:
        lowIndex = 0
        for i in range(len(openSet)):
            if openSet[i].f < openSet[lowIndex].f:
                lowIndex = i

        current = openSet[lowIndex]
        if current == end:
            temp = current
            path.append(temp)
            while temp.previous:
                path.append(temp.previous)
                temp = temp.previous
            else:
                print("No Solutions")
                pass
            print("Done")
        else:
            removefromList(openSet, current)
            closeSet.append(current)

            neighbours = current.neighbour
            for i in range(len(neighbours)):
                neighbour = neighbours[i]

                if not neighbour in closeSet and not neighbour.wall:
                    tempG = current.g + 1

                    newPath = False
                    if neighbour in openSet:
                        if tempG < neighbour.g:
                            neighbour.g = tempG
                            newPath = True

                    else:
                        neighbour.g = tempG
                        newPath = True
                        openSet.append(neighbour)

                    if newPath:
                        neighbour.h = heuristic(neighbour.i, neighbour.j, end.i, end.j)
                        neighbour.f = neighbour.g + neighbour.h
                        neighbour.previous = current


#Infinite Loop
while True:
    click = pygame.mouse.get_pressed()

    #Draws walls when Right Button is pressed or hold
    if click[2] == True:
        drawWalls()

    #Algorithm starts when Left Button is pressed or hold
    if click[0] == True:
        findPath()

    screen.fill((20, 20, 20))

    renderGrids()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()


    pygame.display.update()
    clock.tick(60)

