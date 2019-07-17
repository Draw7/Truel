#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 16:46:47 2019

@author: andreascazzosi
"""

from Spatial_Player import Spatial_Player as Player
from Space import Space 

# =============================================================================
# Main
# =============================================================================

Player.setchange_probability(False)
dimension = 20
prova = Space(dimension)
winners = [0,0,0]
simulations = 2000
means = [0.9, 0.7, 0.5]
sigma = 0.2

for i in range(simulations):
    prova.matrix_setting(means, sigma)  
    prova.start_validpositions()
    while Player.checkopinion() == False:
        prova.player_pick()
        prova.turnplayers()
        prova.opinion_spreading()
        prova.update()
    winners[prova.output[0][0]] += 1
for i in range(len(winners)):
    print("Opinion "+str(i)+": "+str(winners[i]))
