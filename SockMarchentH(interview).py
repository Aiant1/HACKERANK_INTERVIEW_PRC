# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 21:27:45 2020

@author: Antika
"""


import math
import os
import random
import re
import sys
l=[]
# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    unique_number=set(ar)
    for i in unique_number:
        C=ar.count(i)
        l.append(C//2)
    return sum(l) 

if __name__ == '__main__':

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)


