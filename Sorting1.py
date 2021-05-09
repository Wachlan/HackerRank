#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    swaps = 0

    for i in range(len(a)):
    	for j in range(len(a)-1):
    		if a[j] > a[j+1]:
    			a[j], a[j+1] = a[j+1], a[j]
    			swaps = swaps + 1

    first = a[0]
    last = a[-1]

    print("Array is sorted in", swaps, "swaps.")
    print("First Element:", first)
    print("Last Element:", last)

    return

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
