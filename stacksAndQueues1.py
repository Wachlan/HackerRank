#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    halfwayFlag = 0

    for i in range(len(s)):
        if s[i] == ')' or ']' or '}':
            halfwayFlag = 1
            break
        elif s[i] == '(' or '[' or '{':
            continue
    
    while i < len(s):
        if s[i] == '(' or '[' or '{':
            answer = "NO"
            break
        elif s[i] == ')' or ']' or '}':
            continue

    answer = "YES"

    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
