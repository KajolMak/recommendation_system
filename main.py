from hash_table import HashTable
from graph import Graph
from priority_queue import PriorityQueue

# Initialize structures
user_preferences = HashTable(size=10)
recommendation_graph = Graph()
recommendation_queue = PriorityQueue()

# Example data
user_preferences.insert("user1", {"productA": 5, "productB": 3})
user_preferences.insert("user2", {"productA": 2, "productC": 4})

recommendation_graph.add_edge("user1", "productA")
recommendation_graph.add_edge("user1", "productB")
recommendation_graph.add_edge("user2", "productC")

# Generate recommendations for user1
neighbors = recommendation_graph.get_neighbors("user1")
for product in neighbors:
    priority = user_preferences.lookup("user1").get(product, 0)
    recommendation_queue.add(product, priority)

# Top recommendation
print(f"Top recommendation for user1: {recommendation_queue.pop()}")
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

