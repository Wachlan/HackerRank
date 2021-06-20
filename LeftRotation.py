#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'rotateLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#

def rotateLeft(d, arr):
    rotatedArray = []

    #start at position d in array arr and copy the array to rotatedArray until the end of array arr
    for cnt in range(d, len(arr)):
        rotatedArray.append(arr[cnt])


    #go back to the beginning of arr and copy until position d into rotatedArray
    for cnt in range(0, d):
        rotatedArray.append(arr[cnt])

    return rotatedArray

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = rotateLeft(d, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
