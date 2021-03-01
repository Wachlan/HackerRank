#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the candies function below.
def candies(n, arr):
    candyTotal = 0
    previousRating = 0
    currentGift = 1
    
    for x in arr:
        if x > previousRating:
            currentGift = currentGift + 1
            if currentGift < 1:
                currentGift = 1
            candyTotal = candyTotal + currentGift
        elif x < previousRating:
            currentGift = currentGift - 1
            if currentGift < 1:
                currentGift = 1
            candyTotal = candyTotal + currentGift
            
        previousRating = x
        
    return candyTotal

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
