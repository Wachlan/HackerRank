#!/bin/python3

import math
import os
import random
import re
import sys
from queue import Queue

class MyQueue(object):
    def __init__(self):
    	self.firstStack = []
    	self.secondStack = []
        
    
    def peek(self):                        #Enqueue element into the end of the queue.
        firstStack.append()
        
    def pop(self):                         #dequeue the element at the front of the queue
        
        
    def put(self, value):                  #Print the element at the front of the queue.
        


queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())