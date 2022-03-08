# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 14:37:36 2022

@author: naomi
"""

import numpy as np
import math

def area_y1(a, b, c):
    area = 0
    for d in range(a, b, c):
        x = d + (c / 2)
        y = -0.5 * x + 4.0
        area += abs(c * y)
    return area


def area_y2(a, b, c):
    area = 0
    for d in range(a, b, c):
        x = d + (c / 2)
        y = -0.29 * (x ** 2) - x + 12.5
        area += abs(c * y)
    return area


def area_y3(a, b, c):
    area = 0
    for d in range(a, b, c):
        x = d + (c / 2)
        y = 1.0 + 10 * (x + 1.0) * math.exp(-x ** 2)
        area += abs(c * y)
    return area


print("      Δx   |   area   |true area|   %x")
for d in range(1, 11):
    y1_integration = (abs(40 - area_y1(-5, 5, d)) / 40)
    print(" y1    " + str(d) + "   |   " + str(round(area_y1(-5, 5, d), 2)) + "   |  40.0   |",
          y1_integration)

print("")
print("      Δx   |   area   |true area|   %x")
for d in range(1, 11):
    y2_integration = (abs(40 - area_y2(-5, 5, d)) / 40)
    print(" y2    " + str(d) + "   |   " + str(round(area_y2(-5, 5, d), 2)) + "   |  100.83 |",
          y2_integration)

print("")
print("      Δx   |   area   |true area|   %x")
for d in range(1, 11):
    y3_integration = (abs(40 - area_y3(-5, 5, d)) / 40)
    print(" y3    " + str(d) + "   |   " + str(round(area_y3(-5, 5, d), 2)) + "   |  27.72  |",
          y3_integration)