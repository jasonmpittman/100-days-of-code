#!/usr/bin/env python3

# Created on 05/20/2018
# @author: Jason M. Pittman
# @license: MIT-license
# Purpose: visual example of pareto distribution
# Explanation: 
import random
import time

players = []
num_players = 2

class player:
    def __init__(self, money):
        self.wins = 0
        self.losses = 0
        self.money = money
    
    def give_money(self):
        self.losses += 1
        self.money = self.money - 1
    
    def take_money(self):
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

    for i in range(len(players)):
        coin = flip_coin()
        
        if coin == 1:
            elected.append(player)


def main():
    for i in range(num_players):
        players.append(player(10))
    
    distributed = is_distributed

    while distributed:
        coin = flip_coin()
        
        if coin == 0:
            players[0].take_money()
            players[1].give_money()
        
        if coin == 1:
            players[0].give_money()
            players[1].take_money()
        
        players[0].check_balance()
        players[1].check_balance()

        time.sleep(3)

main()