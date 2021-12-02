# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 17:07:24 2021

@author: hhnks

Advent of Code 2021

https://adventofcode.com/2021/day/1

--- Day 1: Sonar Sweep ---

"""
import pandas as pd

#Part 1
dane = pd.read_csv("C:/Users/hanna/OneDrive/Dokumenty/Projects/AdventOfCode2021/Dec 1st/input1.csv", header=None)
dane.columns = ['depth']

result = []
for i in range(1,len(dane)):
    if dane.depth.loc[i] > dane.depth.loc[i-1]:
        result.append('increased')
    else:
        result.append('decreased')

result.insert(0, 'N/A')

dane["result"] = result

print('Numer of measurements larger than the previous measurement is: ',
      sum(dane.result == 'increased'))


#Part 2
result2=[]
for i in range(0, len(dane)-3):

    if dane.depth.loc[i]+dane.depth.loc[i+1]+dane.depth.loc[i+2] < dane.depth.loc[i+1]+dane.depth.loc[i+2]+dane.depth.loc[i+3]:
        result2.append('increased')
    else:
        result2.append('decreased')

result2.insert(0, 'N/A')
result2.append('N/A')
result2.append('N/A')

dane["sum_result"] = result2

print('Numer of measurements larger sum than the previous sum is: ',
      sum(dane["sum_result"] == 'increased'))
