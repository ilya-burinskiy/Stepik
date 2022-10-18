class HashTable:
    
    p = 1000000007
    x = 263

    def __init__(self, size: int):
        self.size = size
        self.T = [[] for _ in range(self.size)]

    def h(self, string: str):
        def power_mod(b, p, m):
            if p == 1: 
                return b
            if p == 0:
                return 1
            return (power_mod(b, p-1, m) % m * b % m) % m
        
        X = [power_mod(self.x, i, self.p) for i in range(len(string))]
        hash_ = 0
        for i, char in enumerate(string):
            hash_ = hash_ + ord(char) * X[i]
        hash_ = (hash_ % self.p) % self.size
        
        return hash_


    def insert(self, key: str):
        self.T[self.h(key)].insert(0, key)

    def search(self, key: str):
        chain = self.T[self.h(key)]
        result = True 

        try:
            chain.index(key)
        except ValueError:
            result = False	

        return result
        
    def delete(self, key: str):
        chain = self.T[self.h(key)]
        try:
            idx = chain.index(key)
        except ValueError:
            return
        else:
            del chain[idx]

    def check(self, idx: int):
        return self.T[idx].copy()