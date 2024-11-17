import heapq

class PriorityQueue:
    def __init__(self):
        self.queue = []
    
    def add(self, product, priority):
        heapq.heappush(self.queue, (-priority, product))
    
    def pop(self):
        if self.queue:
            return heapq.heappop(self.queue)[1]
        return None
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def _hash(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))
    
    def lookup(self, key):
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

