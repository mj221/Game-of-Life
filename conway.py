# -*- coding: utf-8 -*-
"""
The Game of Life (GoL) module named in honour of John Conway

This module defines the classes required for the GoL simulation.

Created on Tue Jan 15 12:21:17 2019

@author: shakes
"""
import numpy as np
from scipy import signal

class GameOfLife:
    '''
    Object for computing Conway's Game of Life (GoL) cellular machine/automata
    '''
    def __init__(self, N=256, finite=False, fastMode=False):
        self.grid = np.zeros((N,N), np.uint)
        self.neighborhood = np.ones((3,3), np.uint) # 8 connected kernel
        self.neighborhood[1,1] = 0 #do not count centre pixel
        self.finite = finite
        self.fastMode = fastMode
        self.aliveValue = 1
        self.deadValue = 0
        self.place_holder_alive = 2
        self.place_holder_dead = 3
        self.N = N
        self.inputArray = []
        
    def getStates(self):
        '''
        Returns the current states of the cells
        '''
        return self.grid
    
    def getGrid(self):
        '''
        Same as getStates()
        '''
        return self.getStates()
               
    def evolve(self):
        '''
        Given the current states of the cells, apply the GoL rules:
        - Any live cell with fewer than two live neighbors dies, as if by underpopulation.
        - Any live cell with two or three live neighbors lives on to the next generation.
        - Any live cell with more than three live neighbors dies, as if by overpopulation.
        - Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction
        '''
        N = self.N
        grid = self.grid.copy()
    
        #get weighted sum of neighbors
        #PART A & E CODE HERE

        for j in range(N):
            for i in range(N):
                try:
                    self.neighborhood[0,0] = self.grid[i-1,j-1]
                except:
                    self.neighborhood[0,0] = 0

                try:
                    self.neighborhood[0,1] =self.grid[i-1,j]
                except:
                    self.neighborhood[0,1] = 0

                try:
                    self.neighborhood[0,2] = self.grid[i-1,j+1]
                except:
                    self.neighborhood[0,2] = 0

                try:
                    self.neighborhood[1,0] = self.grid[i,j-1]
                except:
                    self.neighborhood[1,0] = 0

                try:
                    self.neighborhood[1,2] = self.grid[i,j+1]
                except:
                    self.neighborhood[1,2] = 0
                try:
                    self.neighborhood[2,0] = self.grid[i+1,j-1]
                except:
                    self.neighborhood[2,0] = 0
                try:
                    self.neighborhood[2,1] = self.grid[i+1,j]
                except:
                    self.neighborhood[2,1] = 0
                try:
                    self.neighborhood[2,2] = self.grid[i+1,j+1]
                except:
                    self.neighborhood[2,2] = 0

##                print(self.neighborhood)
##                print(sum(self.neighborhood))
##                print(sum(sum(self.neighborhood)))
                if int(grid[i,j]) == self.aliveValue:
                    if (sum(sum(self.neighborhood))<2) or (sum(sum(self.neighborhood))>3):
                        grid[i,j] = self.place_holder_dead
                    elif (sum(sum(self.neighborhood))==2) or (sum(sum(self.neighborhood))==3):
                        grid[i,j] = self.aliveValue
                else:
                    if (sum(sum(self.neighborhood))==3):
                        grid[i,j] = self.place_holder_alive

        for i in range(N):
            for j in range(N):
                if grid[i,j] == self.place_holder_alive:
                    grid[i,j] = self.aliveValue
                
                if grid[i,j] == self.place_holder_dead:
                    grid[i,j] = self.deadValue   
        
        #implement the GoL rules by thresholding the weights
        #PART A CODE HERE
        
        
        #update the grid
#        self.grid = #UNCOMMENT THIS WITH YOUR UPDATED GRID
        self.grid = grid
    
    def insertBlinker(self, index=(0,0)):
        '''
        Insert a blinker oscillator construct at the index position
        '''
        self.grid[index[0], index[1]+1] = self.aliveValue
        self.grid[index[0]+1, index[1]+1] = self.aliveValue
        self.grid[index[0]+2, index[1]+1] = self.aliveValue
        
    def insertGlider(self, index=(0,0)):
        '''
        Insert a glider construct at the index position
        '''
        self.grid[index[0], index[1]+1] = self.aliveValue
        self.grid[index[0]+1, index[1]+2] = self.aliveValue
        self.grid[index[0]+2, index[1]] = self.aliveValue
        self.grid[index[0]+2, index[1]+1] = self.aliveValue
        self.grid[index[0]+2, index[1]+2] = self.aliveValue
        
    def insertGliderGun(self, index=(0,0)):
        '''
        Insert a glider construct at the index position
        '''
        self.grid[index[0]+1, index[1]+26] = self.aliveValue
        
        self.grid[index[0]+2, index[1]+24] = self.aliveValue
        self.grid[index[0]+2, index[1]+26] = self.aliveValue
        
        self.grid[index[0]+3, index[1]+14] = self.aliveValue
        self.grid[index[0]+3, index[1]+15] = self.aliveValue
        self.grid[index[0]+3, index[1]+22] = self.aliveValue
        self.grid[index[0]+3, index[1]+23] = self.aliveValue
        self.grid[index[0]+3, index[1]+36] = self.aliveValue
        self.grid[index[0]+3, index[1]+37] = self.aliveValue
        
        self.grid[index[0]+4, index[1]+13] = self.aliveValue
        self.grid[index[0]+4, index[1]+17] = self.aliveValue
        self.grid[index[0]+4, index[1]+22] = self.aliveValue
        self.grid[index[0]+4, index[1]+23] = self.aliveValue
        self.grid[index[0]+4, index[1]+36] = self.aliveValue
        self.grid[index[0]+4, index[1]+37] = self.aliveValue

##        Shift the first cube by a unit of 1 to the right
        self.grid[index[0]+5, index[1]+2] = self.aliveValue
        self.grid[index[0]+5, index[1]+3] = self.aliveValue
        self.grid[index[0]+5, index[1]+12] = self.aliveValue
        self.grid[index[0]+5, index[1]+18] = self.aliveValue
        self.grid[index[0]+5, index[1]+22] = self.aliveValue
        self.grid[index[0]+5, index[1]+23] = self.aliveValue
        
        self.grid[index[0]+6, index[1]+2] = self.aliveValue
        self.grid[index[0]+6, index[1]+3] = self.aliveValue
        self.grid[index[0]+6, index[1]+12] = self.aliveValue
        self.grid[index[0]+6, index[1]+16] = self.aliveValue
        self.grid[index[0]+6, index[1]+18] = self.aliveValue
        self.grid[index[0]+6, index[1]+19] = self.aliveValue
        self.grid[index[0]+6, index[1]+24] = self.aliveValue
        self.grid[index[0]+6, index[1]+26] = self.aliveValue
        
        self.grid[index[0]+7, index[1]+12] = self.aliveValue
        self.grid[index[0]+7, index[1]+18] = self.aliveValue
        self.grid[index[0]+7, index[1]+26] = self.aliveValue
        
        self.grid[index[0]+8, index[1]+13] = self.aliveValue
        self.grid[index[0]+8, index[1]+17] = self.aliveValue
        
        self.grid[index[0]+9, index[1]+14] = self.aliveValue
        self.grid[index[0]+9, index[1]+15] = self.aliveValue

    def nextGen(self, inputArray):
        newArray = inputArray.copy()
        index=(0,0)
        for lineKey, line in enumerate(inputArray):
            for charKey, char in enumerate(line):
                if inputArray[lineKey][charKey] == "O":
                    self.grid[index[0]+lineKey, index[1]+charKey] = self.aliveValue
