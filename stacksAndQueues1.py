#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):

    cycleTimes = len(s)
    
    for x in range(cycleTimes):
        s = s.replace("[]","")
        s = s.replace("()","")
        s = s.replace("{}","")

    if not s:
        answer = "YES"
    else:
        answer = "NO"

    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()

