# -*- coding: utf-8 -*-
"""
Game of life script with animated evolution

"""
import conway
from os import system, name
from html import parser
from sys import stdin
N = 64

#create the game of life object
life = conway.GameOfLife(N)
##life.insertBlinker((0,0))
##life.insertGlider((0,0))
##life.insertGliderGun((0,0))

f = open("input.txt")
input = f.read().splitlines()
inputArray = []
for line in input:
    inputArray.append(list(list(line)))

life.nextGen(inputArray[2:])    
cells = life.getStates() #initial state

#-------------------------------
#plot cells
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()

plt.gray()

img = plt.imshow(cells, animated=True)


def animate(i):
    """perform animation step"""
    global life
    
    life.evolve()
    cellsUpdated = life.getStates()
    
    img.set_array(cellsUpdated)
    
    return img,

interval = 10 #ms

#animate 24 frames with interval between them calling animate function at each frame
ani = animation.FuncAnimation(fig, animate, frames=24, interval=interval, blit=True)

plt.show()
