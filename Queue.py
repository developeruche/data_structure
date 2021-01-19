from collections import deque

class Queue:
    def __init__(self):
        self.main_structure = deque()
    
    def append_to_structure(self, data):
        self.main_structure.append(data)
    
    def insert_to_structure(self, data):
        self.main_structure.appendleft(data)
    
    def isEmpty(self):
        data_count = self.main_structure.count()
        if data_count <= 0:
            return True
        else:
            return False
    
    def pop__from_structure(self):
        self.main_structure.pop()