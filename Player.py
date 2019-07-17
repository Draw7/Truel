#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 16:10:03 2019

@author: andreascazzosi
"""


# =============================================================================
# Class
# =============================================================================

class Player:
    
    players_list = []
    change_probability = True
    
    def checkopinion():
        for player in Player.players_list:
            if player.getopinion() != Player.players_list[0].getopinion():
                return False
        return True
    
    def countforopinion(opinion):
        count = 0
        for player in Player.players_list:
            if player.getopinion() == opinion:
                count += 1
        return count
    
    def __init__(self, probability = 0, opinion = 0):      
        self.probability = probability
        self.opinion = opinion
        Player.players_list.append(self)
        
    def delete(self):
        Player.players_list.remove(self)
        
    def findopponent(self, opponents):
        possible_opponent = []
        positions = []
        for i in range(len(opponents)):
            if self.opinion != opponents[i].opinion:
                possible_opponent.append(opponents[i].probability)
                positions.append(i)
        position = positions[possible_opponent.index(max(possible_opponent))]                
        return position
    
    def shooting(self, opponent):
        import random
        if self.probability >= random.random():
            opponent.setopinion(self.opinion)
            if Player.getchange_probability():
                opponent.setprobability(self.probability)

    def setchange_probability(new_value):
        Player.change_probability = new_value
    
    def getchange_probability():
        return Player.change_probability
                
    def delete_list(list_):
        for item in list_:
            item.delete()
    
    def delete_matrix(matrix):
        for list_ in matrix:
            for item in list_:
                item.delete()
    
    def setprobability (self, probability):
        self.probability = probability
            
    def setopinion(self, opinion):
        self.opinion = opinion
    
    def getopinion(self):
        return self.opinion
    
    def getprobability(self):
        return self.probability
                    