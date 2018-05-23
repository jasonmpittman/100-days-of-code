#!/usr/bin/env python3

# Created on 05/20/2018
# @author: Jason M. Pittman
# @license: MIT-license
# Purpose: visual example of pareto distribution
# Explanation: 
import random
import time
import numpy as np
import matplotlib.pyplot as plot
from matplotlib import colors
from matplotlib.ticker import PercentFormatter

class player:
    def __init__(self, money):
        self.wins = 0
        self.losses = 0
        self.money = money
    
    def give_money(self, amount):
        self.losses += 1
        self.money = self.money - 1
    
    def take_money(self, amount):
        self.wins = 0
        self.money = self.money + 1
    
    def check_balance(self):
        print("My balance is: {0}".format(self.money))


def flip_coin():
    result = random.randint(0,1)
    return result

def is_distributed(players):
    distributed = False
    return distributed

def elect_players(players):
    elected = []

    for i in range(2):
        index = random.randint(0, len(players) - 1)
        if index not in elected:
            elected.append(index)
        else:
            elected.append(index + 1)
    
    return elected

def main():
    players = []
    num_players = 5
    max_pay = 10
    elected = []

    for i in range(num_players):
        players.append(player(max_pay))
    
    distributed = is_distributed

    while distributed:
        coin = flip_coin()
        
        elected.clear()
        elected = elect_players(players)
        amount = random.randint(1, max_pay)

        if coin == 0:
            players[elected[0]].take_money(amount)
            players[elected[1]].give_money(amount)
        
        if coin == 1:
            players[elected[0]].give_money(amount)
            players[elected[1]].take_money(amount)
        
        #plot histogram here
        

        time.sleep(3)

    
main()