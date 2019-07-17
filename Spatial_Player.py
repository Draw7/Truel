#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 16:11:28 2019

@author: andreascazzosi
"""

import Player as p

class Spatial_Player (p.Player):
      
    def __init__(self, probability = 0, opinion = 0, positioning =[] , position = 0):      
        super().__init__(probability, opinion, position)
        self.positioning = positioning
        
    def setpositioning (self, new_positioning):
        self.positioning = new_positioning
       
    def getpositioning(self):
        return self.positioning
    
    def getx(self):
        return int(self.positioning[1])
    
    def gety(self):
        return int(self.positioning[0])
    
    def same_type(self, list_):
        for player in list_:
            if self.getopinion() != player.getopinion():
                return False
        return True