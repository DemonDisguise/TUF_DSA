# LFU Cache

"""  Design and implement a data structure for a Least Frequently Used (LFU) cache.

Implement the LFUCache class with the following functions:

LFUCache(int capacity): Initialize the object with the specified capacity.

int get(int key): Retrieve the value of the key if it exists in the cache; otherwise, return -1.
void put(int key, int value): Update the value of the key if it is present in the cache, or insert the key if it is not already present. If the cache has reached its capacity, invalidate and remove the least frequently used key before inserting a new item. In case of a tie (i.e., two or more keys with the same frequency), invalidate the least recently used key.

A use counter is maintained for each key in the cache to determine the least frequently used key. The key with the smallest use counter is considered the least frequently used.

When a key is first inserted into the cache, its use counter is set to 1 due to the put operation. The use counter for a key in the cache is incremented whenever a get or put operation is called on it. Ensure that the functions get and put run in O(1) average time complexity. """

from collections import defaultdict

class Node:
    def __init__(self, key=-1, val=-1):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        self.freq = 1

class DLL:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        
        self.head.next = self.tail
        self.tail.prev = self.head
        
        self.size = 0
    
    def add_front(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        
        self.size += 1
        
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
        self.size -= 1
    
    def remove_last(self):
        if self.size == 0:
            return None
        
        node = self.tail.prev
        self.remove(node)
        
        return node          

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        
        self.cache = {}
        self.freq_map = defaultdict(DLL)

    def update_freq(self, node: Node) -> None:
        freq = node.freq
        
        self.freq_map[freq].remove(node)
        
        if freq == self.min_freq and self.freq_map[freq].size == 0:
            self.min_freq += 1
        
        node.freq += 1
        self.freq_map[node.freq].add_front(node)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        
        self.update_freq(node)
        
        return node.val
        
    def put(self, key: int, val: int) -> None:
        if self.capacity == 0:
            return
        
        if key in self.cache:
            node = self.cache[key]
            node.value = val
            
            self.update_freq(node)
            return
        
        if len(self.cache) == self.capacity:
            lfu_node = self.freq_map[self.min_freq].remove_last()
            
            del self.cache[lfu_node.key]
        
        node = Node(key, val)
        self.cache[key] = node
        self.freq_map[1].add_front(node)
        self.min_freq = 1

if __name__ == "__main__":
    lfu_cache = LFUCache(2)
    lfu_cache.put(1, 10)
    lfu_cache.put(2, 20)
    print(lfu_cache.get(1))
    lfu_cache.put(3, 30)
    print(lfu_cache.get(2))
    print(lfu_cache.get(3))
    lfu_cache.put(4, 4)
    print(lfu_cache.get(1))
    print(lfu_cache.get(3))
    print(lfu_cache.get(4))
    