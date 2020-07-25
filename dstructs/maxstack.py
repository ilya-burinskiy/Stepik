class MaxSupportStack:
   
    def __init__(self):
        self.mstack = []
        self.mstack_len = 0
        
    def push(self, value):
        max_val = value if self.is_empty() else max(value, self.top()[1])
        self.mstack.append((value, max_val))
        self.mstack_len += 1
        
    def top(self):
        return self.mstack[self.mstack_len - 1]
    
    def pop(self):
        popped = self.mstack.pop()
        self.mstack_len -= 1

        return popped
        
    def max(self):
        return self.mstack[self.mstack_len - 1][1]
    
    def is_empty(self):
        return self.mstack_len == 0