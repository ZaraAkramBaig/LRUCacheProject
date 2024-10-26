# Node Class: This represents each item in the cache. It stores the key-value pair and pointers to the previous and next nodes.
# Explanation of the Code
# Doubly Linked List Setup: We use a dummy head and tail to manage the list, where:

# The head points to the most recently used item.
# The tail points to the least recently used item.
# Adding and Removing Nodes:

# _add_node adds a node right after the head, marking it as the most recently used.
# _remove_node detaches a node from its current position.
# _move_to_head removes a node and re-adds it after the head to update its usage.
# Evicting the Least Recently Used Item:

# _evict_from_tail removes the node just before the tail, representing the least recently used item.
class Node:
    def __init__(self, key=int, value=int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:  #least recently used cache
    def __init__(self,capacity=int):
        self.capacity = capacity
        self.size=0
        self.head=Node(0,0) #dummy head
        self.tail=Node(0,0) #dummy tail
        self.head.next=self.tail
        self.tail.prev=self.head

    def add_value(self,node):
        node.prev=self.head
        node.next=self.head.next
        self.head.next.prev=node
        self.head.next=node

    def remove_node(self,node):
        prev=node.prev
        new=node.next
        prev.next=new
        new.prev=prev    

    def move_to_head(self,node):
        self.remove_node(node)
        self.add_value(node)

    def evict_from_tail(self):
        lru=self.tail.prev #lru is least recently used
        self.remove_node(lru)
        return lru
    

    def get(self, key: int) -> int:
        # Traverse the list to find the node with the specified key
        current = self.head.next
        while current != self.tail:
            if current.key == key:
                # Move the accessed node to the head (most recently used)
                self.move_to_head(current)
                return current.value
            current = current.next
        return -1  # If key is not found
    
    def put(self, key: int, value: int) -> None:
        # First, check if the key already exists in the list
        current = self.head.next
        while current != self.tail:
            if current.key == key:
                # Key exists, update the value and move to head
                current.value = value
                self.move_to_head(current)
                return
            current = current.next
        
        # If the key does not exist, create a new node
        new_node = Node(key, value)
        self.add_value(new_node)
        self.size += 1

        # Check if we need to evict the least recently used item
        if self.size > self.capacity:
            # Evict from the tail and decrement size
            lru = self.evict_from_tail()
            self.size -= 1

# Initialize the cache with a capacity of 50
cache = LRUCache(50)

# Step 2: Fill the cache with keys 0 to 49
for i in range(50):
    cache.put(i, i)

# Step 3: Retrieve odd-numbered keys and count misses
misses = 0
total_retrievals = 0
for i in range(1, 50, 2):  # Odd numbers from 1 to 49
    result = cache.get(i)
    total_retrievals += 1
    if result == -1:
        misses += 1

# Step 4: Fill the cache with prime numbers 0-100
# List of prime numbers from 0 to 100
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
          53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

for prime in primes:
    cache.put(prime, prime)

# Step 5: Calculate and print the final miss rate
miss_rate = misses / total_retrievals if total_retrievals > 0 else 0
print(f"Final Miss Rate: {miss_rate:.2%}")
# Output: Final Miss Rate: 50.00%

