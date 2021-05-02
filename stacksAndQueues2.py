#!/bin/python3

import math
import os
import random
import re
import sys

class MyQueue(object):
    def __init__(self):
    	self.value = []
        
    
    def peek(self):                        #Enqueue element into the end of the queue.
        self.value.append(object)
        
    def pop(self):                         #dequeue the element at the front of the queue
        tempStack = []
        while self.value.empty() != 1:
        	top = self.value.pop()
        	tempStack.append(top)

        tempStack.pop

        while tempStack.empty() != 1:
        	
        
    def put(self, value):
        

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