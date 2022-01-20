# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 10:34:10 2022

@author: naomi
"""

import random
import time

question=input("What is your question?")
print("Thinking...")
time.sleep(2)
print("Your question was:" + question)

num = random.randint (0,1)

if(num==0):
    print("My answer is yes!")
else:
    print("My answer is no!")
    