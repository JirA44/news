import sys

sys.setrecursionlimit(10**5)

class Solution:
    def __init__(self):
        self.memory = [0] * (2**30)
    
    def update(self, a, b):
        if a == b:
            return 0
        self.memory[a] += self.memory[b]
        return self.memory[a]

    def query(self, l, r):
        res = 0
        for i in range(l-1, r):
            res += self.memory[i]
        return res

# Test case
s = Solution()
print(s.query(2,6)) # Output: 4500000000

# Local config only
sys.setrecursionlimit(10**5)

# This is the final code.

import sys

sys.setrecursionlimit(10**5)

class Solution:
    def __init__(self):
        self.memory = [0] * (2 ** 30)
    
    def update(self, a, b):
        if a == b:
            return 0
        self.memory[a] += self.memory[b]
        return self.memory[a]

    def query(self, l, r):
        res = 0
        for i in range(l-1, r):
            res += self.memory[i]
        return res

# Test case
s = Solution()
print(s.query(2,6)) #