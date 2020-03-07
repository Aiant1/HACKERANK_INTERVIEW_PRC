# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 12:10:34 2020

@author: ASUS
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    valley=0

    steps=0;

    for i in s:
        if (i=="U"):
            steps=steps+1
        else:
            steps=steps-1
            
        if (steps==0 and i=="U"):
            valley=valley+1
    return valley
        

            
            
    
    

if __name__ == '__main__':

    n = int(input())

    s = input()

    result = countingValleys(n, s)


