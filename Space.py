#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 21:18:39 2019

@author: andreascazzosi
"""

# =============================================================================
# Class 
# =============================================================================

from Spatial_Player import Spatial_Player as Player 
import random


class Space:
        
    def __init__(self, dimension):
        self.dimension = dimension
        self.matrix = []
        self.output = []
        for i in range(self.dimension):
            self.matrix.append([])
            self.output.append([])
            for k in range(self.dimension):
                self.matrix[i].append(Player())
                self.output[i].append(0)
        
        self.valid_positions = []
        
    def initialization(self):
        Player.delete_matrix(self.matrix)
        self.matrix = []
        for i in range(self.dimension):
            self.matrix.append([])
            self.output.append([])
            for k in range(self.dimension):
                self.matrix[i].append(Player())
                self.output.append(0)
                
    def matrix_setting(self, means, sigma):
        for i in range(self.dimension):
            for k in range(self.dimension):
                self.matrix[i][k].setopinion(random.randint(0,len(means)-1))
                self.matrix[i][k].setprobability(probability_distribution(means[self.matrix[i][k].getopinion()], sigma))
                self.matrix[i][k].setpositioning([i,k])
                self.output[i][k] = self.matrix[i][k].getopinion()
                
    def check_position(self, player):
        x = player.getx() 
        y = player.gety()
        boundaries_x = boundaries(x, self.matrix)
        boundaries_y = boundaries(y, self.matrix)
        array_check = []
        array_check.append(self.matrix[y][x].getopinion())
        for i in range(boundaries_y[0], boundaries_y[1]+1):
            for k in range(boundaries_x[0], boundaries_x[1]+1):
                if abs(i)!=abs(k):
                    array_check.append(self.matrix[y+i][x+k].getopinion())
        if array_check.count(array_check[0]) != len(array_check):
            return True
        else:
            return False
    
    def start_validpositions(self):
        self.valid_positions = []
        for y in range(self.dimension):
            for x in range(self.dimension):
                if self.check_position(self.matrix[y][x]):
                    self.valid_positions.append([y,x])
    
    def player_pick(self):
        self.turnposition = random.choice(self.valid_positions)
        self.turnplayer = self.matrix[self.turnposition[0]][self.turnposition[1]]
        
    def turnplayers(self):
        boundaries_x = boundaries(self.turnposition[0],self.matrix)
        boundaries_y = boundaries(self.turnposition[1],self.matrix)
        self.list_turn = []
        self.list_turn.append(self.turnplayer)
        while len(self.list_turn) != 3:
            i = random.randint(boundaries_x[0],boundaries_x[1])
            k = random.randint(boundaries_y[0],boundaries_y[1])
            if abs(i)!=abs(k) & self.list_turn.count(self.matrix[self.turnplayer.gety()+i][self.turnplayer.getx()+k]) == 0:
                self.list_turn.append(self.matrix[self.turnplayer.gety()+i][self.turnplayer.getx()+k])
        for i in range(len(self.list_turn)):
            self.list_turn[i].setposition(i)
            
    def opinion_spreading(self):
        while self.list_turn[0].same_type(self.list_turn) == False:
            random_player = random.randint(0, len(self.list_turn)-1)
            player_of_turn = self.list_turn[random_player]
            position = player_of_turn.findopponent(self.list_turn)
            player_of_turn.shooting(self.list_turn[position]) 
        return self.list_turn[0].getopinion()
    
    def update(self):
        for player in self.list_turn:
            self.output[player.gety()][player.getx()] = player.getopinion()
            if self.check_position(player):
                if self.valid_positions.count(player.getpositioning())==0:
                    self.valid_positions.append([player.gety(),player.getx()])
            else:
                if self.valid_positions.count(player.getpositioning())!=0:
                    self.valid_positions.remove([player.gety(),player.getx()])   
        
# =============================================================================
# Functions
# =============================================================================

def boundaries(position, matrix):
    start_position = -1
    end_position = 1
    #change of boundaries where to find opponents
    if position == 0:
        start_position = 0
    elif position == len(matrix)-1:
        end_position = 0   
    return [start_position, end_position]                

def probability_distribution(mu, sigma):
    import numpy as np
    probability = np.random.normal(mu, sigma)
    if probability > 1:
        probability = 1
    if probability < 0:
        probability = 0.1
    return probability

