# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 15:19:08 2022

@author: naomi
"""

nvictor = 0
ncreature = 0
nagatha = 0
ncaroline = 0
nlacey = 0
neliz = 0
nernest = 0
nfelix = 0
nhenry = 0
njustine = 0
nwill = 0
cc = 0
print("Number of Occurances of Character Names by Chapter in Frankenstein")
print("Column Titles:")
print("Chapter#  Victor  Creature  Agatha  Caroline  Lacey  Elizabeth  Ernest  Felix  Henry  Justine  Will")
my_file = open("pg42324.txt", "r")
for line in my_file:
    if "CHAPTER" in line:
            print(cc, nvictor, ncreature, nagatha, ncaroline, nlacey, neliz,
                  nernest, nfelix, nhenry, njustine, nwill)
            cc = cc + 1
            nvictor = 0
            ncreature = 0
            nagatha = 0
            ncaroline = 0
            nlacey = 0
            neliz = 0
            nernest = 0
            nfelix = 0
            nhenry = 0
            njustine = 0
            nwill = 0
    nvictor = nvictor + line.count("Victor")
    ncreature = ncreature + line.count("creature")
    nagatha = nagatha + line.count("Agatha")
    ncaroline = ncaroline + line.count("Caroline")
    nlacey = nlacey + line.count("De Lacey")
    neliz = neliz + line.count("Elizabeth")
    nernest = nernest + line.count("Ernest")
    nfelix = nfelix + line.count("Felix")
    nhenry = nhenry + line.count("Henry")
    njustine = njustine + line.count("Justine")
    nwill = nwill + line.count("William")
print(cc, nvictor, ncreature, nagatha, ncaroline, nlacey, neliz,
          nernest, nfelix, nhenry, njustine, nwill) 
my_file.close()

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
xcc = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 
       20, 21, 22, 23, 24]
yvictor = [0, 1, 1, 0, 0, 1, 3, 8, 1, 3, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 
           6, 1, 1]
ycreature = [7, 2, 0, 0, 1, 3, 3, 1, 3, 3, 8, 3, 2, 1, 0, 8, 2, 5, 1, 1, 5, 1,
             2, 3, 7]
yagatha = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 8, 4, 4, 1, 0, 0, 0, 0, 0, 0,
           0, 0]
ycaroline = [0, 2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0]
ylacey = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 2, 3, 0, 0, 0, 0, 0, 0,
          0, 0,]
yeliz = [0, 4, 2, 7, 0, 4, 2, 8, 17, 3, 0, 0, 0, 0, 0, 0, 0, 0, 8, 1, 2, 2, 
         18, 6, 6,]
yernest = [0, 0, 0, 0, 0, 0, 2, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
          2, 0, 2, 0]
yfelix = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 13, 18, 4, 6, 0, 0, 0, 0, 
          0, 0, 0, 2]
yhenry = [0, 0, 1, 1, 0, 5, 5, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 0, 
          4, 1, 0, 0]
yjustine = [0, 0, 0, 0, 0, 0, 12, 9, 21, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 
            2, 3, 1, 1]
ywill = [0, 0, 0, 0, 0, 0, 1, 13, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 
         1, 1, 2]
plt.plot(xcc, yvictor) 
plt.plot(xcc, ycreature)
plt.plot(xcc, yagatha)
plt.plot(xcc, ycaroline)
plt.plot(xcc, ylacey)
plt.plot(xcc, yeliz)
plt.plot(xcc, yernest)
plt.plot(xcc, yfelix)
plt.plot(xcc, yhenry)
plt.plot(xcc, yjustine)
plt.plot(xcc, ywill)
plt.title("Name occurances by chapter")
plt.xlabel("Chapter")
plt.ylabel("Number of Occurances of Name")
plt.show()