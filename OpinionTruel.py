#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 16:47:52 2019

@author: andreascazzosi
"""
from Player import Player
import random

# =============================================================================
# Function
# =============================================================================

def opinionspreading(players):
    while Player.checkopinion()!=True:
        random_player = random.randint(0, len(players)-1)
        player_of_turn = players[random_player]
        position = player_of_turn.findopponent(players)
        player_of_turn.shooting(players[position])        
    return players[0].getopinion()

# =============================================================================
# Main
# =============================================================================

Player.setchange_probability = True    
probabilities = [0.9, 0.7, 0.5]
players = []
winners = []
for i in range(len(probabilities)):
    winners.append(0)

for k in range(1000000):
    for i in range(len(probabilities)): 
        players.append(Player(probabilities[i],i,i))
    winner = opinionspreading(players)
    winners[winner]+=1
    Player.delete_list(players)
    players.clear()
print(winners)