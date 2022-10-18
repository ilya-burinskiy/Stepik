from .maxstack import MaxSupportStack

class MaxSupportQueue:
    
    def __init__(self):
        self.lstack = MaxSupportStack()
        self.rstack = MaxSupportStack()
        
    def enqueue(self, val):
        self.lstack.push(val)
        
    def dequeue(self):
        if not self.rstack.is_empty():
            return self.rstack.pop()
        else:
            while not self.lstack.is_empty():
                self.rstack.push(self.lstack.pop()[0])
            return self.rstack.pop()
        
    def max(self):
        if self.lstack.is_empty():
            max_val = self.rstack.top()[1]
        elif self.rstack.is_empty():
            max_val = self.lstack.top()[1]
        else:
            max_val = max(self.lstack.top()[1], self.rstack.top()[1])
        
        return max_val