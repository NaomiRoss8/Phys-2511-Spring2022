# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 13:13:04 2022

@author: naomi
"""

import numpy as np
import math
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation as animation
 
v = float(input("Enter inital speed: ")) 
theta = float(input("Enter initial angle: "))
theta = np.deg2rad(theta)

a_x = 0
a_y = -9.8
v_x = v * np.cos(theta)
t = 2 * v * np.sin(theta) / (-a_y)
t = np.linspace(0, t, 100)
x = v * np.cos(theta) * t
v_y = v * np.sin(theta) + (a_y*t)
y = v * np.sin(theta) * t + (0.5 * a_y * t * t)

xaxis = np.array(x)
yaxis = np.array(y) 
plt.plot(xaxis, yaxis)
plt.xlabel("Horizontal distance of arrow")
plt.ylabel("Vertical height of arrow")
plt.title("Archer and Arrow")
plt.show()

xmax = max(x)
if xmax >= 8 or xmax <= 10:
   print("Target hit!")
if xmax < 8:
    low = xmax
    distance = 8 - low
    print("You missed by " + str(round(distance,2)) + " feet. Try again")
if xmax > 10:
    high = xmax
    distance = high - 10
    print("You missed by " + str(round(distance,2)) + " feet. Try again")
