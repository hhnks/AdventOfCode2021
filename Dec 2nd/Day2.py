# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 22:07:14 2021

@author: hanna

Advent of Code 2021

https://adventofcode.com/2021/day/2

--- Day 2: Dive! ---

"""
import pandas as pd

#Part 1
dane = pd.read_csv("C:/Users/hanna/OneDrive/Dokumenty/Projects/AdventOfCode2021/Dec 1st/Dec 2nd/input2.csv", header=None, sep=" ")

dane.columns = ['command', 'value']

forward = dane.loc[dane.command == 'forward']
up = dane.loc[dane.command == 'up']
down = dane.loc[dane.command == 'down']

depth = sum(down.value) - sum(up.value)
horiz_pos = sum(forward.value)

print('The horizontal position after the course is: ' , horiz_pos)
print('The depth after the course is: ' , depth)
print('Multiplying these together produces ', depth*horiz_pos)

#Part 2
depth2_vec = []
aim = []
for i in range(0,len(dane)):
    if dane.command[i] == 'down':
        aim.append(dane.value[i])
    elif dane.command[i] == 'up':
        aim.append(-dane.value[i])
    else:
        depth2_vec.append(dane.value[i]*sum(aim))

depth2 = sum(depth2_vec)

print('The fixed depth after the course is: ' , depth2)
print('Multiplying these together produces ', depth2*horiz_pos)