""" This data structure works with the order of Last in First out """

from collections import deque

class Stack:
    def __init__(self):
        self.state = deque()

    def push(self, data):
        self.state.append(data)

    def pop(self):
        self.state.pop()
    
    def peek(self):
        return self.state[-1]

    def is_empty(self):
        return len(self.state) == 0

    def size(self):
        return len(self.state)