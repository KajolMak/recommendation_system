class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_edge(self, user, product):
        if user not in self.graph:
            self.graph[user] = []
        self.graph[user].append(product)
    
    def get_neighbors(self, user):
        return self.graph.get(user, [])
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
