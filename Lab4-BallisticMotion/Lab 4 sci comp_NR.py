# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 13:13:04 2022

@author: naomi
"""

import numpy as np

x0 = 0
x_final = 23
y0 = 0
y = 0
v_x0 = 0
v_y0 = 0
a_x0 = 0
a_y0 = -9.8
t = 0
while x0 != x_final:
    t = float(input("Guess seconds elapsed: "))
    v_x0 = v_x0 + (a_x0*t)
    v_y0 = v_y0 + (a_y0*t)
    a_y0 = a_y0 - v_y0
    a_x0 = -v_x0
    x0 = x0 + (v_x0 * t)
    y = y0 + (v_y0 * t) 
    print("Target missed! Try again")
print("Target hit!")