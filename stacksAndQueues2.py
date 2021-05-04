#!/bin/python3

import math
import os
import random
import re
import sys
from queue import Queue

class MyQueue(object):
    def __init__(self):
    	self.value = Queue()
        
    
    def peek(self):                        #Enqueue element into the end of the queue.
        self.value.append(object)
        
    def pop(self):                         #dequeue the element at the front of the queue
        tempStack = []
        while self.value.isEmpty() != 1:
        	top = self.value.pop()
        	tempStack.append(top)

        tempStack.pop

        while tempStack.isEmpty() != 1:
        	top = tempStack.value.pop()
        	self.value.append(top)
        
    def put(self, value):                  #Print the element at the front of the queue.
        tempStack = []
        while self.value.isEmpty() != 1:
        	top = self.value.pop()
        	tempStack.append(top)

        frontElement = tempStack.pop()     #pop the element to be printed out
        print(frontElement)                #print the first element from the queue
        self.value.append(frontElement)    #put the element back into the 'queue'

        while tempStack.isEmpty() != 1:
        	top = tempStack.value.pop()
        	self.value.append(top)


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