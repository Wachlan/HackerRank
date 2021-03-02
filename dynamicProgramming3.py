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
    currentGift = 0
    
    for i in range(len(arr)):
        if arr[i] > previousRating:
            currentGift = currentGift + 1
            if currentGift < 1:
                currentGift = 1
            candyTotal = candyTotal + currentGift
        elif arr[i] <= previousRating:
            currentGift = currentGift - 1
            lesserGift = len(arr) - i;
            
            if lesserGift < currentGift:
                currentGift = lesserGift
                
            if currentGift < 1:
                currentGift = 1
            candyTotal = candyTotal + currentGift
            
        previousRating = arr[i]
        
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
