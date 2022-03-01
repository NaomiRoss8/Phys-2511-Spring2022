# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 14:17:40 2022

@author: naomi
"""
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as pltfile

Tornadoes = []
Year = []

in_file = open("CO tornadoes.txt","r")

for line in in_file:
    lines = [i for i in line.split()]
    Tornadoes.append(lines[0])
    Year.append(lines[1])
    
pltfile.show()
print(Tornadoes)
print(Year)
pltfile.scatter(Year,Tornadoes)