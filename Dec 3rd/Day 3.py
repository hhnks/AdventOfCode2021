# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 22:59:08 2021

@author: hanna

Advent of Code 2021

https://adventofcode.com/2021/day/3

--- Day 3: Binary Diagnostic ---

"""
import pandas as pd

#Part 1
dane = pd.read_csv("input3.csv", header=None, dtype='str')

dane.columns = ["numb"]
print(type(dane.numb))

dane = dane["numb"].apply(lambda x: pd.Series(list(x)))

for c in dane:
    print(dane[c].value_counts())
    
gamma = []
epsilon = []

for c in dane:
    if sum(dane[c] == "1") > sum(dane[c] == "0"):
        gamma.append("1") , epsilon.append("0")
    else:
        gamma.append("0") , epsilon.append("1")

gamma = ''.join(map(str, gamma))
epsilon = ''.join(map(str, epsilon))

print("Gamma rate is: ", int(gamma, 2))
print("Epsilon rate is: ", int(epsilon, 2))
print("Gamma*Epsilon is: ", int(gamma, 2)*int(epsilon, 2))

#Part 2
ox_gen_rating = dane.copy()
co2_sc_rating = dane.copy()

for c in ox_gen_rating:
    if sum(ox_gen_rating[c] == "1") >= sum(ox_gen_rating[c] == "0"):
        ox_gen_rating=ox_gen_rating[ox_gen_rating[c] == "1"]
    else:
        ox_gen_rating=ox_gen_rating[ox_gen_rating[c] == "0"]
    if len(ox_gen_rating)==1:
        break

for c in co2_sc_rating:
    if sum(co2_sc_rating[c] == "1") < sum(co2_sc_rating[c] == "0"):
        co2_sc_rating=co2_sc_rating[co2_sc_rating[c] == "1"]
    else:
        co2_sc_rating=co2_sc_rating[co2_sc_rating[c] == "0"]
    if len(co2_sc_rating)==1:
        break

print(ox_gen_rating.index)
print(co2_sc_rating.index)

dane = pd.read_csv("input3.csv", header=None, dtype='str')
dane.columns = ["numb"]

#hardcoding :(
ox_gen_decimal = int(dane.iloc[879]['numb'], 2)
co2_sc_decimal = int(dane.iloc[51]['numb'], 2)
                     
print("Oxygen generator rating is: ", ox_gen_decimal)
print("CO2 scrubber rating is: ", co2_sc_decimal)
print("Oxygen generator rating*CO2 scrubber rating is: ", ox_gen_decimal*co2_sc_decimal)